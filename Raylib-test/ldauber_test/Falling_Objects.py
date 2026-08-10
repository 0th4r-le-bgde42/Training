from pyray import *
import random

#window
s_width = 800
s_height = 600
init_window(s_width, s_height, "Catch the falling objects")
set_target_fps(60)

#player
p_width = 100
p_height = 20
p_x = s_width//2 - p_width // 2
p_y = s_height - 40
p_speed = 7

#objects
o_width = 30
o_height = 30
o_x = random.randint(0, s_width - o_width)
o_y = 0
o_speed = 6

#score
score = 0

while not window_should_close():
    if is_key_down(KEY_LEFT) and p_x > 0: # type: ignore
        p_x -= p_speed
    if is_key_down(KEY_RIGHT) and p_x < s_width - p_width: # type: ignore
        p_x += p_speed
    o_y += o_speed
    if (
        o_y + o_height >= p_y and
        o_x + o_width >= p_x and
        o_x <= p_x + p_width
    ):
        score += 1
        o_y = 0
        o_x = random.randint(0, s_width - o_width)
    if o_y > s_height:
        o_y = 0
        o_x = random.randint(0, s_width - o_width)
    begin_drawing()
    clear_background(BLACK)
    draw_rectangle(p_x, p_y, p_width, p_height, BLUE)
    draw_rectangle(o_x, o_y, o_width, o_height, RED)
    draw_text(f"Score: {score}", 10, 10, 20, WHITE)
    end_drawing()
close_window()