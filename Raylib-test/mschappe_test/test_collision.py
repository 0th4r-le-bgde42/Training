from pyray import *

width = 2500
height = 1500

init_window(width, height, "COLLISION TEST")

camera = Camera3D(Vector3(0.0, 30.0, 10.0),
                  Vector3(0.0, 0.0, 0.0),
                  Vector3(0.0, 10.0, 0.0),
                  45.0,
                  0)

player_postition = Vector3(0.0, 1.0, 2.0)
player_size = Vector3(1.0, 2.0, 1.0)
player_color = GREEN


box_position = Vector3(-4.0, 1.0, 0.0)
box_size = Vector3(2.0, 2.0, 2.0)

plane_origin = Vector3(0.0, 0.0, 0.0)
plane_size = Vector2(10.0, 10.0)


collision = False

set_target_fps(60)

while not window_should_close():

    print(player_postition.x)

    if is_key_down(KEY_D): # type: ignore
        if player_postition.x + player_size.x / 2 + 0.2 <= plane_size.x / 2:
            player_postition.x += 0.2
    elif is_key_down(KEY_A): # type: ignore
        if player_postition.x - player_size.x / 2 - 0.2 >= -(plane_size.x / 2):
            player_postition.x -= 0.2
    elif is_key_down(KEY_S): # type: ignore
        if player_postition.z + player_size.x / 2 + 0.2 <= plane_size.x / 2:
            player_postition.z += 0.2
    elif is_key_down(KEY_W): # type: ignore
        if player_postition.z - player_size.x / 2 - 0.2 >= -(plane_size.x / 2):
            player_postition.z -= 0.2
    
    collision = False

    #===== DRAW

    begin_drawing()

    clear_background(WHITE)

    begin_mode_3d(camera)

    draw_plane(plane_origin,
               plane_size,
               YELLOW)

    draw_cube(box_position, box_size.x, box_size.y, box_size.z, GRAY)
    draw_cube_wires(box_position, box_size.x, box_size.y, box_size.z, DARKGRAY)

    draw_cube_v(player_postition, player_size, player_color)

    end_mode_3d()


    end_drawing()

close_window()