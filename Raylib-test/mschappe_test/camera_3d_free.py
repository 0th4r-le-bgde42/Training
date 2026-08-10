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

disable_cursor()

set_target_fps(60)

while not window_should_close():
    update_camera(camera, CAMERA_FREE) # type: ignore

    if is_key_down(KEY_Z): # type: ignore
        camera.target = Vector3(0.0, 0.0, 0.0)


    begin_drawing()

    clear_background(RAYWHITE)

    begin_mode_3d(camera)

    draw_cube(cube_position, 2.0, 2.0, 2.0, RED)
    draw_cube_wires(cube_position, 2.0, 2.0, 2.0, MAROON)

    draw_grid(10, 1.0)

    end_mode_3d()


    end_drawing()


close_window()