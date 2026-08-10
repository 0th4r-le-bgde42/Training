import json
import os
from pyray import *

MAX_INPUT_CHARS = 10
SCORE_FILE = "highscores.json"


def save_score(player_name, score):
	scores_list = []

	if os.path.exists(SCORE_FILE):
		try:
			with open(SCORE_FILE, "r", encoding="utf-8") as f:
				scores_list = json.load(f)
				if not isinstance(scores_list, list):
					scores_list = []
		except json.JSONDecodeError:
			scores_list = []
		
	new_entry = {
		"name": player_name.strip(),
		"score": score
	}

	scores_list.append(new_entry)
	scores_list = sorted(scores_list, key=lambda x: x["score"], reverse=True)

	with open(SCORE_FILE, "w", encoding="utf-8") as f:
		json.dump(scores_list, f, indent=4, ensure_ascii=False)


def main():
	width = 2500
	height = 1500
	final_score = 999
	init_window(width, height, "input test")

	name = ""
	frames_counter = 0

	text_box = Rectangle(width / 2.0 - 200, height / 2.0, 400, 60)


	while not window_should_close():
		frames_counter += 1

		key = get_char_pressed()

		while key > 0:
			if (key >= 32) and (key <= 125) and (len(name) < MAX_INPUT_CHARS):
				name += chr(key)
			key = get_char_pressed()
		
		if is_key_pressed(KEY_BACKSPACE):
			name = name[:-1]
		
		if is_key_pressed(KEY_ENTER):
			if name.strip() != "":
				save_score(name, final_score)
				break

		begin_drawing()
		clear_background(BLACK)

		draw_text("GAME OVER", int(width / 2 - measure_text("GAME OVER", 80) / 2), int(height / 2 - 250), 80, RED)

		score_txt = f"FINAL SCORE: {final_score}"
		draw_text(score_txt, int(width / 2 - measure_text(score_txt, 30) / 2), int(height / 2 - 120), 30, WHITE)

		draw_rectangle_rec(text_box, fade(DARKBLUE, 0.2))
		draw_rectangle_lines_ex(text_box, 2, BLUE)

		if name == "":
			draw_text("TYPE YOUR NAME...", int(text_box.x) + 15, int(text_box.y) + 18, 24, DARKGREEN)
		else:
			draw_text(name, int(text_box.x) + 15, int(text_box.y) + 18, 28, YELLOW)
		
		if len(name) < MAX_INPUT_CHARS:
			if ((frames_counter // 20) % 2) == 0:
				shift = measure_text(name, 28) if name != "" else 0
				draw_text("_", int(text_box.x) + 18 + shift, int(text_box.y) + 18, 28, YELLOW)
		
		draw_text("PRESS ENTER TO VALIDATE", int(width / 2 - measure_text("PRESS ENTER TO VALIDATE", 20) / 2), int(height / 2 + 120), 20, GRAY)

		end_drawing()
	
	close_window()

if __name__ == "__main__":
	main()

