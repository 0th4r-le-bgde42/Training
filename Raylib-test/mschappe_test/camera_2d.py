from pyray import *
import random

MAX_BUILDINGS = 100

width = 800
height = 450

init_window(width, height, "CAMERA 2D")

player = Rectangle(400.0, 280.0, 40.0, 40.0)
player_speed = 2

buildings_list = [Rectangle(0.0, 0.0, 0.0, 0.0) for _ in range(MAX_BUILDINGS)]
buildings_color = [Color(random.randrange(200, 240, 1),
                         random.randrange(200, 240, 1),
                         random.randrange(200, 240, 1),
                         255) for _ in range(MAX_BUILDINGS)]

spacing = 0

for i in range(MAX_BUILDINGS):
    buildings_list[i].width = float(random.randrange(50, 200, 1))
    buildings_list[i].height = float(random.randrange(100, 800, 1))
    buildings_list[i].y = height - 130.0 - buildings_list[i].height
    buildings_list[i].x = -6000.0 + spacing

    spacing += int(buildings_list[i].width)

camera = Camera2D()
camera.target = Vector2(player.x + 20.0, player.y + 20.0)
camera.offset = Vector2(width / 2, height /2)
camera.rotation = 0.0
camera.zoom = 1.0

set_target_fps(60)

while not window_should_close():
    if is_key_down(KEY_D): # type: ignore
        player.x += player_speed
    elif is_key_down(KEY_A): # type: ignore
        player.x -= player_speed
    
    camera.target = Vector2(player.x + 20.0, player.y + 20.0)

    if is_key_down(KEY_LEFT): # type: ignore
        camera.rotation -= 1
    elif is_key_down(KEY_RIGHT): # type: ignore
        camera.rotation += 1
    
    if is_key_down(KEY_R): # type: ignore
        camera.zoom = 1.0
        camera.rotation = 0.0
    
    begin_drawing()
    clear_background(RAYWHITE)

    begin_mode_2d(camera)

    draw_rectangle(-6000, 320, 13000, 8000, DARKGRAY)

    for i in range(MAX_BUILDINGS):
        draw_rectangle_rec(buildings_list[i], buildings_color[i])
    
    draw_rectangle_rec(player, RED)

    end_mode_2d()


    end_drawing()

close_window()