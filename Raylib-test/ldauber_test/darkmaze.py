from pyray import *
import pyray as pr
import math
from src.Maze_3D import Maze_3D


class Colors:
    RED = [1.0, 0.0, 0.0]
    PINK = [1.0, 0.4, 0.7]
    CYAN = [0.0, 1.0, 1.0]
    ORANGE = [1.0, 0.5, 0.0]
    BLUE = [0.0, 0.3, 1.0]
    WHITE = [1.0, 1.0, 1.0]
    HOT_WHITE = [1.0, 0.95, 0.85]


def check_wall_collision(playerPos, mapPixels, cubicmap, mapPosition, playerRadius):
    playerCellx = int(playerPos.x - mapPosition.x)
    playerCelly = int(playerPos.y - mapPosition.z)

    playerCellx = max(0, min(playerCellx, cubicmap.width - 1))
    playerCelly = max(0, min(playerCelly, cubicmap.height - 1))

    for y in range(playerCelly - 1, playerCelly + 2):
        if 0 <= y < cubicmap.height:
            for x in range(playerCellx - 1, playerCellx + 2):
                if 0 <= x < cubicmap.width:
                   if mapPixels[y * cubicmap.width + x].r == 255:
                        wall_rec = Rectangle(
                           mapPosition.x - 0.5 + x * 1.0,
                           mapPosition.z - 0.5 + y * 1.0,
                           1.0, 1.0
                        )
                        if check_collision_circle_rec(
                            playerPos, playerRadius, wall_rec
                        ):
                            return True
    return False


def dark_map():
    width = 2500
    height = 1500
    set_config_flags(ConfigFlags.FLAG_MSAA_4X_HINT)
    init_window(width, height, "DarkMap - Dynamic Shader Light")

    # Caméra FPS
    camera = Camera3D()
    camera.position = Vector3(0.0, 0.0, 0.0)
    camera.target = Vector3(0.185, 0.4, 8.0)
    camera.up = Vector3(0.0, 1.0, 0.0)
    camera.fovy = 50.0
    camera.position.y = 0.30
    camera.projection = CameraProjection.CAMERA_PERSPECTIVE

    camera_angle = 0.0
    angle_cible = 0.0
    rotation_speed = 0.1

    # Chargement de la map
    # imMap = load_image("ldauber_test/resources/cubicmap.png")
    # cubicmap = load_texture_from_image(imMap)
    # map_pixels = load_image_colors(imMap)
    # unload_image(imMap)

    map_maze = Maze_3D(42)
    map_maze.make_maze(42)

    # --- INITIALISATION SHADER ---
    shader = load_shader("ldauber_test/shaders/light.vs", "ldauber_test/shaders/light.fs")
    
    cam_pos_loc = get_shader_location(shader, "cameraPos")
    fog_rad_loc = get_shader_location(shader, "fogRadius")
    light_color_loc = get_shader_location(shader, "lightColor")
    light_on_loc = get_shader_location(shader, "lightOn")

    # Configuration initiale : Portée de 8.0 unités et couleur Jaune Pac-Man (R=1.0, G=0.9, B=0.0)
    fog_radius = 8.0
    set_shader_value(shader, fog_rad_loc, ffi.new("float *", fog_radius), ShaderUniformDataType.SHADER_UNIFORM_FLOAT)
    
    current_color = Colors.PINK 
    set_shader_value(shader, light_color_loc, ffi.new("float[]", current_color), ShaderUniformDataType.SHADER_UNIFORM_VEC3)
    
    is_light_on = 1
    set_shader_value(shader, light_on_loc, ffi.new("int *", is_light_on), ShaderUniformDataType.SHADER_UNIFORM_INT)

    # # Modèle du sol
    # mesh_sol = gen_mesh_plane(200.0, 200.0, 1, 1)
    # plane = load_model_from_mesh(mesh_sol)
    # plane.materials[0].shader = shader # Injection du shader sur le sol
    
    # # Modèle de cube unique pour les murs
    # mesh_cube = gen_mesh_cube(1.0, 1.0, 1.0)
    # cube_model = load_model_from_mesh(mesh_cube)
    # cube_model.materials[0].shader = shader # Injection du shader sur les murs

    map_maze.init_shader(shader)

    map_position = Vector3(-16.0, 0.0, -8.0)
    speed = 0.05

    disable_cursor()
    set_target_fps(60)

    def update_view(cam: Camera3D, angle: float):
        cam.target.x = cam.position.x + math.cos(angle)
        cam.target.z = cam.position.z + math.sin(angle)
        cam.target.y = cam.position.y

    update_view(camera, camera_angle)

    while not window_should_close():
        # --- SWITCH LAMPE (TOUCHE F) ---
        if is_key_pressed(KEY_L): # type: ignore
            is_light_on = 0 if is_light_on == 1 else 1
            set_shader_value(shader, light_on_loc, ffi.new("int *", is_light_on), ShaderUniformDataType.SHADER_UNIFORM_INT)

        # --- INPUTS ROTATION ---
        if is_key_pressed(KEY_A): # type: ignore
            angle_cible -= math.pi / 2
        if is_key_pressed(KEY_D): # type: ignore
            angle_cible += math.pi / 2

        camera_angle += (angle_cible - camera_angle) * rotation_speed

        # --- INPUTS DÉPLACEMENT ---
        mouvement = Vector3(0.0, 0.0, 0.0)
        player_radius = 0.35

        if is_key_down(KEY_W): # type: ignore
            mouvement.x = math.cos(angle_cible) * speed
            mouvement.z = math.sin(angle_cible) * speed
        if is_key_down(KeyboardKey.KEY_S):
            mouvement.x = -math.cos(angle_cible) * speed
            mouvement.z = -math.sin(angle_cible) * speed
        
        # # --- GESTION DES COLLISIONS ---
        # old_x = camera.position.x
        camera.position.x += mouvement.x
        # player_pos_2d = Vector2(camera.position.x, camera.position.z)
        # if check_wall_collision(player_pos_2d, map_pixels, cubicmap, map_position, player_radius):
        #     camera.position.x = old_x

        # old_z = camera.position.z
        camera.position.z += mouvement.z
        # player_pos_2d = Vector2(camera.position.x, camera.position.z)
        # if check_wall_collision(player_pos_2d, map_pixels, cubicmap, map_position, player_radius):
        #     camera.position.z = old_z

        update_view(camera, camera_angle)

        # --- ENVOI DE LA POSITION SOURIS/CAMÉRA MISE À JOUR ---
        cam_pos_c = ffi.new("float[]", [camera.position.x, camera.position.y, camera.position.z])
        set_shader_value(shader, cam_pos_loc, cam_pos_c, ShaderUniformDataType.SHADER_UNIFORM_VEC3)

        # --- DESSIN RENDU ---
        begin_drawing()
        clear_background(BLACK)
        begin_mode_3d(camera)
        map_maze.print_maze()

        # 1. Le sol en violet (son rendu sera atténué par la position dans le shader)
        # ground_height = Vector3(map_position.x, 0.01, map_position.z)
        # draw_model(plane, ground_height, 1.0, DARKPURPLE)

        # # 2. Les murs en bleu et leurs lignes
        # for y in range(cubicmap.height):
        #     for x in range(cubicmap.width):
        #         if map_pixels[y * cubicmap.width + x].r == 255:
        #             cube_pos = Vector3(
        #                 map_position.x + x * 1.0,
        #                 0.5,
        #                 map_position.z + y * 1.0
        #             )
        #             draw_model(cube_model, cube_pos, 1.0, DARKBLUE)
        #             # draw_cube_wires(cube_pos, 1.0, 1.0, 1.0, BLUE)

        end_mode_3d()

        # --- RADAR / MINIMAP COMPATIBLE ---
        mini_map_size = 150.0
        mini_map_x = get_screen_width() - mini_map_size - 20.0
        mini_map_y = 20.0

        # draw_texture_pro(cubicmap, Rectangle(0.0, 0.0, float(cubicmap.width), float(cubicmap.height)), Rectangle(mini_map_x, mini_map_y, mini_map_size, mini_map_size), Vector2(0.0, 0.0), 0.0, WHITE)
        # draw_rectangle_lines(int(mini_map_x), int(mini_map_y), int(mini_map_size), int(mini_map_size), GREEN)

        # playerCellx = int(camera.position.x - map_position.x)
        # playerCelly = int(camera.position.z - map_position.z)
        # playerCellx = max(0, min(playerCellx, cubicmap.width - 1))
        # playerCelly = max(0, min(playerCelly, cubicmap.height - 1))

        # ratio_x = mini_map_size / cubicmap.width
        # ratio_y = mini_map_size / cubicmap.height
        # draw_rectangle(int(mini_map_x + playerCellx * ratio_x), int(mini_map_y + playerCelly * ratio_y), 6, 6, RED)

        draw_text("Appuie sur L pour la Lampe", 20, 20, 20, PINK if is_light_on else GRAY)
        draw_fps(10, height - 30)
        end_drawing()

    # Nettoyage complet
    unload_shader(shader)
    # unload_image_colors(map_pixels)
    # unload_texture(cubicmap)
    # unload_model(plane)
    # unload_model(cube_model)
    close_window()


if __name__ == "__main__":
    dark_map()