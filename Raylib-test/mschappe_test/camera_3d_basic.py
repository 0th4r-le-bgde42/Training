from pyray import *

width = 800
height = 450

init_window(width, height, "BASIC CAMERA 3D")

camera = Camera3D()
camera.position = Vector3(0.0, 10.0, 10.0)
camera.target = Vector3(0.0, 0.0, 0.0)
camera.up = Vector3(0.0, 1.0, 0.0)
camera.fovy = 45.0
camera.projection = CAMERA_PERSPECTIVE # type: ignore

cube_position = Vector3(0.0, 0.0, 0.0)

set_target_fps(60)

while not window_should_close():
    begin_drawing()

    begin_mode_3d(camera)

    draw_cube(cube_position, 2.0, 2.0, 2.0, RED)
    draw_cube_wires(cube_position, 2.0, 2.0, 2.0, MAROON)

    draw_grid(10, 1.0)

    end_mode_3d()


    end_drawing()


close_window()