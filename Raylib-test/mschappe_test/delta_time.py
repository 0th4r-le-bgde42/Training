from pyray import *

width = 800
height = 800

init_window(width, height, "TEST")

current_fps = 60

delta_circle = Vector2(0.0, float(height / 3.0))
frame_circle = Vector2(0.0, float(height * (2.0 / 3.0)))

speed = 10.0
circle_radius = 32.0

set_target_fps(current_fps)

while not window_should_close():
    mouse_wheel = get_mouse_wheel_move()
    if mouse_wheel != 0:
        current_fps += int(mouse_wheel)
        if current_fps < 0:
            current_fps = 0
        set_target_fps(current_fps)
    
    delta_circle.x += get_frame_time() * 6.0 * speed
    frame_circle.x += 0.1 * speed

    if delta_circle.x > width:
        delta_circle.x = 0
    
    if frame_circle.x > width:
        frame_circle.x = 0
    
    if (is_key_pressed(KEY_R)): # type: ignore
        delta_circle.x = 0
        frame_circle.x = 0
    
    begin_drawing()
    clear_background(RAYWHITE)
    
    draw_circle_v(delta_circle, circle_radius, RED)
    draw_circle_v(frame_circle, circle_radius, BLUE)

    draw_text(f"FPS: {get_fps()}", 10, 10, 20, DARKGRAY)

    end_drawing()
close_window()