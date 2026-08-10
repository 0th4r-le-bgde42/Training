from pyray import *


start_width = 800
start_height = 450

set_config_flags(FLAG_WINDOW_RESIZABLE) # type: ignore
init_window(start_width, start_height, "button test")

def menu():
	btn_hello_pressed = False
	btn_game_pressed = False
	btn_paste_pressed = False
	btn_clear_pressed = False
	btn_reset_pressed = False
	msg = None

	hello_launch = False
	falling_launch = False

	gui_set_style(DEFAULT, TEXT_SIZE, 20) # type: ignore
	gui_set_icon_scale(2)

	set_target_fps(60)

	while not window_should_close():
		width = get_screen_width()
		height = get_screen_height()
		begin_drawing()
		clear_background(RAYWHITE)
		gui_label(Rectangle(50,20,700,36), "Select buttons:")
		draw_text("HELLO | GAME | PASTE", 50,60,20,MAROON)

		if gui_button(Rectangle(50, 180, 158, 40), "HELLO"):
			hello_launch = True
		if gui_button(Rectangle(50 + 165, 180, 158, 40), "GAME"):
			falling_launch = True

		btn_paste_pressed = gui_button(Rectangle(50 + 165*2, 180, 158, 40), "PASTE")
		btn_clear_pressed = gui_button(Rectangle(50 + 165*3, 180, 158, 40), "CLEAR")
		if falling_launch:
			falling(width, height)
			falling_launch = False
		if hello_launch:
			hello(width, height)
			hello_launch = False

		end_drawing()

	close_window()

def hello(width, height):
	while not window_should_close():
		begin_drawing()
		clear_background(GREEN)
		msg = "Hello!"
		draw_text(msg, int(width/2-80), int(height/2-30), 60, WHITE)
		draw_text("R: Return", 700, 430, 20, WHITE)
		if is_key_down(KEY_R): # type: ignore
			return False
		end_drawing()
	return False


def falling(s_width, s_height):
	import random

	# #window
	# s_width = 800
	# s_height = 600
	# init_window(s_width, s_height, "Catch the falling objects")
	# set_target_fps(60)

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

	init_window(400, 1000, "Fallint objects")

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
		if is_key_down(KEY_R): # type: ignore
			return False
		begin_drawing()
		clear_background(BLACK)
		draw_rectangle(p_x, p_y, p_width, p_height, BLUE)
		draw_rectangle(o_x, o_y, o_width, o_height, RED)
		draw_text(f"Score: {score}", 10, 10, 20, WHITE)
		draw_text("R: Return", 690, 10, 20, WHITE)
		end_drawing()
	return False


if __name__ == "__main__":
	menu()