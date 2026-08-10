from pyray import *
import math

class Buttons():
    def __init__(self):
        self.game_modes = False
        self.credits = False
        self.settings = False
        self.highscore = False
        self.pm_3d = False
        self.pm_2d = False
        self.dark_mode = False
        self.exit = False
        self.ret = False


def menu(width, height):

    # ------------------- implementation des shaders global (map cam fixe)
    # shader_relief = load_shader("ldauber_test/shaders/reliefs.vs", "ldauber_test/shaders/reliefs.fs")

    # light_dir_loc = get_shader_location(shader_relief, "lightDir")
    # light_color_loc = get_shader_location(shader_relief, "lightColor")

    # light_direction = [-0.5, -1.0, -0.3]
    # set_shader_value(shader_relief, light_dir_loc, ffi.new("float[]", light_direction), ShaderUniformDataType.SHADER_UNIFORM_VEC3)

    # light_color = [1.0, 1.0, 1.0]
    # set_shader_value(shader_relief, light_color_loc, ffi.new("float[]", light_color), ShaderUniformDataType.SHADER_UNIFORM_VEC3)

    # cube_model.materials[0].shader = shader_relief
    # plane.materials[0].shader = shader_relief


    init_window(width, height, "Pac-Man menu")

    btn = Buttons()

    gui_set_style(DEFAULT, TEXT_SIZE, 20) # type:ignore
    gui_set_icon_scale(2)

    frames_count = ffi.new("int *", 0)
    anim_image = load_image_anim("ldauber_test/resources/Pacman.gif", frames_count)

    gif_texture = load_texture_from_image(anim_image)
    set_texture_filter(gif_texture, TextureFilter.TEXTURE_FILTER_POINT)

    current_frame = 0
    frame_counter = 0
    frame_speed = 4

    frame_data_offset = 0

    set_target_fps(60)
    current_screen = "MAIN_MENU"

    menu_title = "PAC-MAN"
    title_size = 122
    time = 0.0
    title_speed = 7.5
    wave_height = 15.0
    title_frequency = 0.5

    while not window_should_close():
        if frames_count[0] > 1:
            frame_counter += 1
            if frame_counter >= frame_speed:
                frame_counter = 0
                current_frame += 1
                if current_frame >= frames_count[0]:
                    current_frame = 0
                
                frame_data_offset = current_frame * (gif_texture.width * gif_texture.height * 4)
                update_texture(gif_texture, anim_image.data + frame_data_offset)

        time += get_frame_time() * title_speed

        begin_drawing()
        clear_background(BLACK)

        src_rect = Rectangle(0.0, 0.0, int(gif_texture.width), int(gif_texture.height))
        dest_rect = Rectangle(0.0, height - 110 - gif_texture.height, int(gif_texture.width*3), int(gif_texture.height*2))

        draw_texture_pro(gif_texture, src_rect, dest_rect, Vector2(0.0, 0.0), 0.0, WHITE)

        if current_screen == "MAIN_MENU":
            letter_length = int(title_size * 0.72)
            title_length = len(menu_title) * letter_length
            x_start =  int(width/2-title_length/2)
            # draw_rectangle(int(width/2 - 300), int(height/2 - 460), 600, 200, fade(DARKBLUE, 0.8))
            for i, letter in reversed(list(enumerate(menu_title))):
                x_dynamique = x_start + (i * letter_length)
                y_dynamique = int(height/2 - 415) + int(math.sin(time + (i * title_frequency)) * wave_height)
                draw_text(letter, x_dynamique - 36, y_dynamique - 36, 122, ORANGE)
                draw_text(letter, x_dynamique - 27, y_dynamique - 27, 122, BLUE)
                draw_text(letter, x_dynamique - 18, y_dynamique - 18, 122, PINK)
                draw_text(letter, x_dynamique - 9, y_dynamique - 9, 122, RED)
                draw_text(letter, x_dynamique, y_dynamique, 122, YELLOW)
                x_dynamique += letter_length
        

            if gui_button(Rectangle(width/2-145, height/2-90, 300, 60), "Game Modes"):
                current_screen = "GAME_MODES"
            if gui_button(Rectangle(width/2-145, height/2-10, 300, 60), "Highscores"):
                btn.highscore = True
            if gui_button(Rectangle(width/2-145, height/2+70, 300, 60), "Settings"):
                btn.settings = True
            if gui_button(Rectangle(width/2-145, height/2+150, 300, 60), "Credits"):
                btn.credits = True

            if gui_button(Rectangle(width - 90, height - 90, 60, 60), "EXIT"):
                btn.exit = True
            
            if btn.exit:
                break

        
        elif current_screen == "GAME_MODES":
            draw_rectangle(int(width/2 - 300), int(height/2 - 460), 600, 200, DARKGRAY)
            draw_text("Game Modes", int(width/2 - 281), int(height/2 - 415), 120, DARKPURPLE)

            if gui_button(Rectangle(width/2-145, height/2-90, 300, 60), "Pac-Man 2d"):
                btn.pm_2d = True
            if gui_button(Rectangle(width/2-145, height/2-10, 300, 60), "Pac-Man 3d"):
                btn.pm_3d = True
            if gui_button(Rectangle(width - 90, height - 90, 60, 60), "RETURN"):
                current_screen = "MAIN_MENU"

        end_drawing()
    
    unload_texture(gif_texture)
    unload_image(anim_image)
    close_window()


if __name__ == "__main__":
    width = 1800
    height = 1000
    menu(width, height)
