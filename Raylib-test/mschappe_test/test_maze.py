import mazegenerator as maze
from pyray import *
import random

maze_len = 15

test = maze.MazeGenerator((maze_len, maze_len), False, (0,0), (2,2), 42)
test.generate(67)
with open("maze.txt", 'w') as file:
    for ligne in test.maze:
        for cell in ligne:
            file.write(f"{cell} ")
        file.write('\n')

width = 2000
height = 1500
init_window(width, height, "TEST MAZE")
set_target_fps(60)

disable_cursor()


camera = Camera3D()
camera.position = Vector3(0.0, float(maze_len * 2 + 5), 23.0)
camera.target =Vector3(0.0, 0.0, 0.0)
camera.up = Vector3(0.0, 10.0, 0.0)
camera.fovy = 47.0
camera.projection = 0

block_list = []
block_size = Vector3(1.0, 1.0, 1.0)
block_origin = Vector3(float(-maze_len), 0, float(-maze_len))
offset_x = 0
offset_z = 0

pac_man_pos = Vector3(0.0, 0.0, 0.0)
pac_man_size = 0.5
pac_man_box = 0.8

for _ in range(maze_len * 2 + 1):
    offset_x = 0
    temp_list = []
    for _ in range(maze_len * 2 + 1):
        temp_list.append(Vector3(block_origin.x + offset_x * block_size.x, 0, block_origin.z + offset_z * block_size.z))
        offset_x += 1
    block_list.append(temp_list)
    offset_z += 1

def int_to_bin(n: int) -> str:
    res = bin(n).split('b')[1]
    if len(res) < 4:
        res = res[::-1]
        while len(res) < 4:
            res += '0'
        res = res[::-1]
    return res

def make_maze(blocks: list, maze: list) -> list:
    actual_wall_list = []
    new_block_list = []
    offset_i = 0
    offset_j = 0
    for i in range(maze_len):
        offset_i += 1
        temp_block_list = []
        for j in range(maze_len):
            offset_j += 1
            bin_pos = int_to_bin(maze[i][j])
            if bin_pos[0] == '1':
                wall_pos = (offset_i, offset_j - 1)
                wall_inter_1 = (offset_i - 1, offset_j - 1)
                wall_inter_2 = (offset_i + 1, offset_j - 1)
                if wall_pos not in actual_wall_list:
                    temp_block_list.append(blocks[offset_i][offset_j - 1])
                    actual_wall_list.append(wall_pos)
                if wall_inter_1 not in actual_wall_list:
                    temp_block_list.append(blocks[offset_i - 1][offset_j - 1])
                    actual_wall_list.append(wall_inter_1)
                if wall_inter_2 not in actual_wall_list:
                    temp_block_list.append(blocks[offset_i + 1][offset_j - 1])
                    actual_wall_list.append(wall_inter_2)
            if bin_pos[1] == '1':
                wall_pos = (offset_i + 1, offset_j)
                wall_inter_1 = (offset_i + 1, offset_j - 1)
                wall_inter_2 = (offset_i + 1, offset_j + 1)
                if wall_pos not in actual_wall_list:
                    temp_block_list.append(blocks[offset_i + 1][offset_j])
                    actual_wall_list.append(wall_pos)
                if wall_inter_1 not in actual_wall_list:
                    temp_block_list.append(blocks[offset_i + 1][offset_j - 1])
                    actual_wall_list.append(wall_inter_1)
                if wall_inter_2 not in actual_wall_list:
                    temp_block_list.append(blocks[offset_i + 1][offset_j + 1])
                    actual_wall_list.append(wall_inter_2)
            if bin_pos[2] == '1':
                wall_pos = (offset_i, offset_j + 1)
                wall_inter_1 = (offset_i - 1, offset_j + 1)
                wall_inter_2 = (offset_i + 1, offset_j + 1)
                if wall_pos not in actual_wall_list:
                    temp_block_list.append(blocks[offset_i][offset_j + 1])
                    actual_wall_list.append(wall_pos)
                if wall_inter_1 not in actual_wall_list:
                    temp_block_list.append(blocks[offset_i - 1][offset_j + 1])
                    actual_wall_list.append(wall_inter_1)
                if wall_inter_2 not in actual_wall_list:
                    temp_block_list.append(blocks[offset_i + 1][offset_j + 1])
                    actual_wall_list.append(wall_inter_2)
            if bin_pos[3] == '1':
                wall_pos = (offset_i - 1, offset_j)
                wall_inter_1 = (offset_i - 1, offset_j - 1)
                wall_inter_2 = (offset_i - 1, offset_j + 1)
                if wall_pos not in actual_wall_list:
                    temp_block_list.append(blocks[offset_i - 1][offset_j])
                    actual_wall_list.append(wall_pos)
                if wall_inter_1 not in actual_wall_list:
                    temp_block_list.append(blocks[offset_i - 1][offset_j - 1])
                    actual_wall_list.append(wall_inter_1)
                if wall_inter_2 not in actual_wall_list:
                    temp_block_list.append(blocks[offset_i - 1][offset_j + 1])
                    actual_wall_list.append(wall_inter_2)
            offset_j += 1
        new_block_list.append(temp_block_list)
        offset_j = 0
        offset_i += 1
    return new_block_list

new_block_list = make_maze(block_list, test.maze)

speed = 0.2

def check_collision(pos: Vector3, blocks: list, key: str) -> int:
    new_pos = Vector3(pos.x, pos.y, pos.z)
    if key == "W":
        new_pos.z -= speed
    elif key == "S":
        new_pos.z += speed
    elif key == "A":
        new_pos.x -= speed
    elif key == "D":
        new_pos.x += speed
    pos_bounding = BoundingBox(Vector3(new_pos.x - pac_man_box / 2,
                                       new_pos.y - pac_man_box / 2,
                                       new_pos.z - pac_man_box / 2),
                                Vector3(new_pos.x + pac_man_box / 2,
                                       new_pos.y + pac_man_box / 2,
                                       new_pos.z + pac_man_box / 2))
    for line in blocks:
        for block in line:
            block_bounding = BoundingBox(Vector3(block.x - block_size.x / 2,
                                                block.y - block_size.y / 2,
                                                block.z - block_size.z / 2),
                                        Vector3(block.x + block_size.x / 2,
                                                block.y + block_size.y / 2,
                                                block.z + block_size.z / 2))
            if check_collision_boxes(pos_bounding, block_bounding):
                return 0
    return 1


while not window_should_close():
    #update_camera(camera, CAMERA_FREE)

    if is_key_down(KEY_W): # type: ignore
        if check_collision(pac_man_pos, new_block_list, 'W'):
            pac_man_pos.z -= speed
    if is_key_down(KEY_S): # type: ignore
        if check_collision(pac_man_pos, new_block_list, 'S'):
            pac_man_pos.z += speed
    if is_key_down(KEY_A): # type: ignore
        if check_collision(pac_man_pos, new_block_list, 'A'):
            pac_man_pos.x -= speed
    if is_key_down(KEY_D): # type: ignore
        if check_collision(pac_man_pos, new_block_list, 'D'):
            pac_man_pos.x += speed


    begin_drawing()
    clear_background(BLACK)

    begin_mode_3d(camera)

    draw_sphere(pac_man_pos, pac_man_size, YELLOW)
    draw_cube_wires_v(pac_man_pos, Vector3(1.0, 1.0, 1.0), WHITE)

    for line in new_block_list:
        for pos in line:
            draw_cube_v(pos, block_size, DARKBLUE)
            #draw_cube_wires_v(pos, block_size, DARKBROWN)
    draw_plane(Vector3(0.0, -0.5, 0.0), Vector2(maze_len * 2 + 1, maze_len * 2 + 1), DARKPURPLE)

    end_mode_3d() 

    draw_text(f"x: {pac_man_pos.x}\nz: {pac_man_pos.z}", 0, 0, 50, WHITE)

    end_drawing()


close_window()