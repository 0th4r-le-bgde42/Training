from pyray import *

width = 800
height = 450

init_window(width, height, "background scrolling")

background = load_texture("ldauber_test/resources/cyberpunk_street_background.png")
midground = load_texture("ldauber_test/resources/cyberpunk_street_midground.png")
foreground = load_texture("ldauber_test/resources/cyberpunk_street_foreground.png")

scrolling_back = 0.0
scrolling_mid = 0.0
scrolling_fore = 0.0

set_target_fps(60)

while not window_should_close():
	scrolling_back -= 0.1
	scrolling_mid -= 0.5
	scrolling_fore -= 1.0

	if scrolling_back <= -background.width*2:
		scrolling_back = 0
	if scrolling_mid <= -midground.width*2:
		scrolling_mid = 0
	if scrolling_fore <= -foreground.width*2:
		scrolling_fore = 0
	
	begin_drawing()
	clear_background(get_color(0x052c46ff))

	draw_texture_ex(background, Vector2(scrolling_back, 20), 0.0, 2.0, WHITE)
	draw_texture_ex(background, Vector2(background.width*2 + scrolling_back, 20), 0.0, 2.0, WHITE)

	draw_texture_ex(midground, Vector2(scrolling_mid, 20), 0.0, 2.0, WHITE)
	draw_texture_ex(midground, Vector2(midground.width*2 + scrolling_mid, 20), 0.0, 2.0, WHITE)

	draw_texture_ex(foreground, Vector2(scrolling_fore, 70), 0.0, 2.0, WHITE)
	draw_texture_ex(foreground, Vector2(foreground.width*2+scrolling_fore, 70), 0.0, 2.0, WHITE)

	end_drawing()

unload_texture(background)
unload_texture(midground)
unload_texture(foreground)

close_window()
