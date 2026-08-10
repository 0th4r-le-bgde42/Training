from pyray import *

width = 800
height = 800

init_window(width, height, "KEY INPUT")

ball_position = Vector2(float(width/2), float(height/2))

set_target_fps(60)

speed = 5.0 

while not window_should_close():

    if is_key_down(KEY_A): # type: ignore
        ball_position.x -= speed
    if is_key_down(KEY_D): # type: ignore
        ball_position.x += speed
    if is_key_down(KEY_W): # type: ignore
        ball_position.y -= speed
    if is_key_down(KEY_S): # type: ignore
        ball_position.y += speed
    
    if ball_position.x < 0:
        ball_position.x = width
    
    if ball_position.x > width:
        ball_position.x = 0
    
    if ball_position.y < 0:
        ball_position.y = height
    
    if ball_position.y > height:
        ball_position.y = 0


    begin_drawing()

    clear_background(RAYWHITE)

    draw_circle_v(ball_position, 50, MAROON)

    end_drawing()

close_window()