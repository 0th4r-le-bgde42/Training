import json
import os
from pyray import *
import math

SCORE_FILE = "highscores.json"

def load_highscores():
    if os.path.exists(SCORE_FILE):
        try:
            with open(SCORE_FILE, "r", encoding="utf-8") as f:
                scores = json.load(f)
                if isinstance(scores, list):
                    return sorted(scores, key=lambda x: x.get("score", 0), reverse=True)
        except (json.JSONDecodeError, KeyError):
            return []
    return []


def menu(width, height):
    init_window(width, height, "new_menu")
    set_target_fps(60)

    highscores = load_highscores()

    main_options = ["GAME MODES", "SETTINGS", "CREDITS", "EXIT"]
    game_options = ["PLAY 2D", "PLAY 3D", "BACK"]
    settings_options = ["DARK MODE: OFF", "BACK"]

    current_screen = "MAIN_MENU"
    current_choice = 0
    dark_mode_state = False # GameConfig

    background_color = BLACK
    selection_color = YELLOW
    txt_selection_color = BLACK
    default_color = DARKBLUE
    default_txt_color = WHITE

    while not window_should_close():
        disable_cursor()
        clear_background(background_color)
    
        current_option = main_options if current_screen == "MAIN_MENU" else game_options if current_screen == "GAME_MENU" else settings_options
        if is_key_pressed(KEY_DOWN): # type: ignore
            current_choice = (current_choice + 1) % len(current_option)
        
        if is_key_pressed(KEY_UP): # type: ignore
            current_choice = (current_choice - 1) % len(current_option)
        
        if is_key_pressed(KEY_ENTER): # type: ignore
            if current_screen == "MAIN_MENU":
                if current_option[current_choice] == "SETTINGS":
                    current_screen = "SETTINGS"
                    current_choice = 0
                elif current_option[current_choice] == "EXIT":
                    break
            elif current_screen == "SETTINGS":
                if "DARK MODE" in current_option[current_choice]:
                    dark_mode_state = not dark_mode_state
                    settings_options[0] = f"DARK MODE: {'ON' if dark_mode_state else 'OFF'}"
                elif current_option[current_choice] == "BACK":
                    current_screen = "MAIN_MENU"
                    current_choice = 1
        
        for i, option in enumerate(current_option):
            rect_width = 350
            rect_height = 60
            x = int(width / 2 - rect_width / 2)
            y = int(height / 2 - 150 + (i * 80))

            rect_destination = Rectangle(x, y, rect_width, rect_height)

            if i == current_choice:
                draw_rectangle_rec(rect_destination, selection_color)
                draw_rectangle_lines_ex(rect_destination, 4, ORANGE)

                txt_size = 24
                txt_width = measure_text(option, txt_size)
                draw_text(option, int(x + rect_width/2 - txt_width/2), int(y + rect_height/2 - txt_size/2), txt_size, txt_selection_color)

            else:
                draw_rectangle_rec(rect_destination, fade(default_color, 0.3))
                draw_rectangle_lines_ex(rect_destination, 1, default_color)

                txt_size = 20
                txt_width = measure_text(option, txt_size)
                draw_text(option, int(x + rect_width/2 - txt_width/2), int(y + rect_height/2 - txt_size/2), txt_size, default_txt_color)

        panel_x = width - 650
        panel_y = int(height / 2 - 250)
        panel_width = 500

        draw_text("HIGHSCORES", panel_x + int(panel_width/2 - measure_text("HIGHSCORES", 30)/2), panel_y, 30, PURPLE)
        draw_text("NAME", panel_x, panel_y + 50, 20, GRAY)
        draw_text("SCORE", panel_x + panel_width - measure_text("SCORE", 20), panel_y + 50, 20, GRAY)

        draw_line(panel_x, panel_y + 75, panel_x + panel_width, panel_y + 75, DARKGRAY)

        for idx in range(10):
            row_y = panel_y + 95 + (idx * 40)

            if idx < len(highscores):
                entry = highscores[idx]
                name = str(entry.get("name", "UNKNOWN"))
                score = str(entry.get("score", 0))

                color_row = YELLOW if idx == 0 else WHITE

                draw_text(f"{idx + 1}. {name}",panel_x, row_y, 22, color_row)
                draw_text(score, panel_x + panel_width - measure_text(score, 22), row_y, 22, color_row)
            
            else:
                empty_txt = "???.............???"
                empty_width = measure_text(empty_txt, 22)
                draw_text(empty_txt, panel_x + int(panel_width/2 - empty_width/2), row_y, 22, DARKGRAY)
    
        end_drawing()
    
    close_window()


if __name__ == "__main__":
    width = 2000
    height = 1500
    menu(width, height)