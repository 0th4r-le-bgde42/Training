from pyray import *


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


width = 1800
height = 1800
init_window(width, height, "First Person Maze")

camera = Camera3D()
# camera.position = Vector3(0.2, 0.4, 0.2)
# camera.target = Vector3(0.185, 0.4, 8.0)
camera.up = Vector3(0.0, 1.0, 0.0)
camera.fovy = 45.0
camera.position.y = 0.44
camera.projection = CAMERA_PERSPECTIVE # type: ignore

# imMap = load_image("ldauber_test/resources/cubicmap.png")
imMap = load_image("ldauber_test/resources/cubicmaze2.png")
cubicmap = load_texture_from_image(imMap)
mesh = gen_mesh_cubicmap(imMap, Vector3(1.0, 1.0, 1.0))
model = load_model_from_mesh(mesh)

texture = load_texture("ldauber_test/resources/sherk.jpeg")
model.materials[0].maps[MATERIAL_MAP_DIFFUSE].texture = texture # type: ignore

mapPixels = load_image_colors(imMap)
unload_image(imMap)

mapPosition = Vector3(-16.0, 0.0, -8.0)
disable_cursor()
set_target_fps(60)

# --- RECHERCHE AUTOMATIQUE DE L'ENTRÉE (LIGNE DU HAUT) ---
spawn_x = 0
spawn_y = 0
entrée_trouvée = False

# On parcourt la première ligne de pixels (y = 0) de gauche à droite
for x in range(cubicmap.width):
    # Si on trouve un pixel NOIR (r == 0), c'est notre entrée !
    if mapPixels[0 * cubicmap.width + x].r == 0:
        spawn_x = x
        spawn_y = 0
        entrée_trouvée = True
        break

# Si l'entrée du haut est bouchée, on cherche une ouverture sur la ligne du bas
if not entrée_trouvée:
    for x in range(cubicmap.width):
        if mapPixels[(cubicmap.height - 1) * cubicmap.width + x].r == 0:
            spawn_x = x
            spawn_y = cubicmap.height - 1
            break

# On téléporte la caméra pile au centre de la case d'entrée trouvée
camera.position.x = mapPosition.x + spawn_x + 0.5
camera.position.z = mapPosition.z + spawn_y + 0.5

# On oriente le regard vers l'intérieur du labyrinthe
if spawn_y == 0:
    camera.target = Vector3(camera.position.x, camera.position.y, camera.position.z + 5.0) # Regarde vers le bas
else:
    camera.target = Vector3(camera.position.x, camera.position.y, camera.position.z - 5.0) # Regarde vers le haut
# --------------------------------------------------------

while not window_should_close():
    mouse_delta = get_mouse_delta()
    sens = 0.20
    rotation = Vector3(mouse_delta.x * sens, mouse_delta.y * sens, 0.0)
    update_camera_pro(camera, Vector3(0.0, 0.0, 0.0), rotation, 0.0)

    move_forward_back = 0.0
    move_strafe = 0.0
    mouvement = Vector3(0.0, 0.0, 0.0)
    speed = 0.1
    player_radius = 0.2

    if is_key_down(KEY_LEFT_SHIFT): # type: ignore
        speed = speed*2
    if is_key_down(KEY_W): # type: ignore
        move_forward_back += speed
    if is_key_down(KEY_S): # type: ignore
        move_forward_back -= speed
    if is_key_down(KEY_D): # type: ignore
        move_strafe += speed
    if is_key_down(KEY_A): # type: ignore
        move_strafe -= speed
    
    dir_x = camera.target.x - camera.position.x
    dir_z = camera.target.z - camera.position.z

    length = (dir_x * dir_x + dir_z * dir_z) ** 0.5
    if length > 0:
        dir_x /= length
        dir_z /= length

    right_x = -dir_z
    right_z = dir_x

    delta_x = (dir_x * move_forward_back) + (right_x * move_strafe)
    delta_z = (dir_z * move_forward_back) + (right_z * move_strafe)

    old_x = camera.position.x
    old_target_x = camera.target.x

    camera.position.x += delta_x
    camera.target.x += delta_x

    player_pos = Vector2(camera.position.x, camera.position.z)
    if check_wall_collision(player_pos, mapPixels, cubicmap, mapPosition, player_radius):
        camera.position.x = old_x
        camera.target.x = old_target_x

    old_z = camera.position.z
    old_target_z = camera.target.z

    camera.position.z += delta_z
    camera.target.z += delta_z

    player_pos = Vector2(camera.position.x, camera.position.z)
    if check_wall_collision(player_pos, mapPixels, cubicmap, mapPosition, player_radius):
        camera.position.z = old_z
        camera.target.z = old_target_z

    playerCellx = int(player_pos.x - mapPosition.x + 0.5)
    playerCelly = int(player_pos.y - mapPosition.z + 0.5)

    playerCellx = max(0, min(playerCellx, cubicmap.width - 1))
    playerCelly = max(0, min(playerCelly, cubicmap.height - 1))

    begin_drawing()
    clear_background(RAYWHITE)

    begin_mode_3d(camera)
    draw_model(model, mapPosition, 1.0, WHITE)
    end_mode_3d()

    mini_map_size = 150.0
    mini_map_x = get_screen_width() - mini_map_size - 20.0
    mini_map_y = 20.0

    src_rec = Rectangle(0.0, 0.0, float(cubicmap.width), float(cubicmap.height))
    dest_rec = Rectangle(mini_map_x, mini_map_y, mini_map_size, mini_map_size)
    draw_texture_pro(
        cubicmap, src_rec, dest_rec,
        Vector2(0.0, 0.0),
        0.0,
        WHITE
    )
    draw_rectangle_lines(
        int(mini_map_x),
        int(mini_map_y),
        int(mini_map_size),
        int(mini_map_size),
        GREEN
    )

    ratio_x = mini_map_size / cubicmap.width
    ratio_y = mini_map_size / cubicmap.height

    draw_rectangle(
        int(mini_map_x + playerCellx * ratio_x),
        int(mini_map_y + playerCelly * ratio_y),
        6, 6,
        RED
    )

    draw_fps(10, 10)

    end_drawing()

unload_image_colors(mapPixels)

unload_texture(cubicmap)
unload_texture(texture)
unload_model(model)

close_window()



# from pyray import *
# from math import sin, cos

# width = 800
# height = 450
# init_window(width, height, "First Person Maze - Custom Movement & Collisions")

# # Caméra classique
# camera = Camera3D()
# camera.position = Vector3(2.0, 0.4, 2.5)  # Placé au centre d'une case vide
# camera.target = Vector3(3.5, 0.4, 2.5)
# camera.up = Vector3(0.0, 1.0, 0.0)
# camera.fovy = 60.0
# camera.projection = CAMERA_PERSPECTIVE # type: ignore

# # Labyrinthe de texte
# MAZE_DATA = [
#     "##################################",
#     "#                                #",
#     "#  ####   ###  #   # #    # #    #",
#     "#  #   # #   # #   # #    # #    #",
#     "#  ####  #####  ###  #    # #### #",
#     "#  #  #  #   #   #   #    # #  # #",
#     "#  #   # #   #   #   #### # #### #",
#     "#                                #",
#     "##################################"
# ]

# mapWidth = len(MAZE_DATA[0])
# mapHeight = len(MAZE_DATA)
# mapPosition = Vector3(0.0, 0.0, 0.0)

# walls_cache = []
# for y in range(mapHeight):
#     for x in range(mapWidth):
#         if MAZE_DATA[y][x] == '#':
#             walls_cache.append((x, y))

# # --- VARIABLES DE MOUVEMENT MAISON ---
# camera_angle_x = 0.0  # Rotation gauche/droite
# camera_angle_y = 0.0  # Rotation haut/bas
# player_speed = 4.0    # Vitesse de marche normale
# mouse_sensitivity = 0.003

# disable_cursor()
# set_target_fps(60)

# while not window_should_close():
#     dt = get_frame_time()
#     if dt > 0.1: dt = 0.1

#     # --- 1. GESTION DE LA SOURIS (REGARD) ---
#     mouse_delta = get_mouse_delta()
#     camera_angle_x -= mouse_delta.x * mouse_sensitivity
#     camera_angle_y -= mouse_delta.y * mouse_sensitivity

#     # On limite la vision verticale pour ne pas se tordre le cou
#     if camera_angle_y > 1.4: camera_angle_y = 1.4
#     if camera_angle_y < -1.4: camera_angle_y = -1.4

#     # Calcul des vecteurs de direction de la caméra
#     forward = Vector3(cos(camera_angle_y) * sin(camera_angle_x), sin(camera_angle_y), cos(camera_angle_y) * cos(camera_angle_x))
#     right = Vector3(cos(camera_angle_x), 0.0, -sin(camera_angle_x))

#     # --- 2. GESTION DU CLAVIER (DÉPLACEMENT PRÉVU) ---
#     move_direction = Vector3(0, 0, 0)

#     # Détection AZERTY (Z, S, Q, D)
#     if is_key_down(KEY_W) or is_key_down(KEY_Z):  # Z ou W (haut) # type: ignore
#         move_direction.x += forward.x
#         move_direction.z += forward.z
#     if is_key_down(KEY_S):                        # S (bas) # type: ignore
#         move_direction.x -= forward.x
#         move_direction.z -= forward.z
#     if is_key_down(KEY_A) or is_key_down(KEY_Q):  # Q ou A (gauche) # type: ignore
#         move_direction.x += right.x
#         move_direction.z += right.z
#     if is_key_down(KEY_D):                        # D (droite) # type: ignore
#         move_direction.x -= right.x
#         move_direction.z -= right.z

#     # Normalisation du mouvement pour ne pas avancer plus vite en diagonale
#     leng = (move_direction.x**2 + move_direction.z**2)**0.5
#     if leng > 0:
#         move_direction.x = (move_direction.x / leng) * player_speed * dt
#         move_direction.z = (move_direction.z / leng) * player_speed * dt

#     # --- 3. RECONNAISSANCE DES COLLISIONS ÉTAPE PAR ÉTAPE ---
#     # Nouvelle position potentielle du joueur
#     next_pos_x = camera.position.x + move_direction.x
#     next_pos_z = camera.position.z + move_direction.z
    
#     player_radius = 0.35  # Taille du cylindre du joueur

#     # Collision sur l'axe X
#     player_grid_x = int(next_pos_x + 0.5)
#     player_grid_z = int(camera.position.z + 0.5)
#     collision_x = False
    
#     for x, y in walls_cache:
#         if abs(x - player_grid_x) <= 1 and abs(y - player_grid_z) <= 1:
#             if check_collision_circle_rec(Vector2(next_pos_x, camera.position.z), player_radius, Rectangle(x - 0.5, y - 0.5, 1.0, 1.0)):
#                 collision_x = True
#                 break
#     if not collision_x:
#         camera.position.x = next_pos_x

#     # Collision sur l'axe Z
#     player_grid_x = int(camera.position.x + 0.5)
#     player_grid_z = int(next_pos_z + 0.5)
#     collision_z = False
    
#     for x, y in walls_cache:
#         if abs(x - player_grid_x) <= 1 and abs(y - player_grid_z) <= 1:
#             if check_collision_circle_rec(Vector2(camera.position.x, next_pos_z), player_radius, Rectangle(x - 0.5, y - 0.5, 1.0, 1.0)):
#                 collision_z = True
#                 break
#     if not collision_z:
#         camera.position.z = next_pos_z

#     # Mise à jour de la cible du regard
#     camera.target.x = camera.position.x + forward.x
#     camera.target.y = camera.position.y + forward.y
#     camera.target.z = camera.position.z + forward.z

#     # --- 4. DESSIN ---
#     begin_drawing()
#     clear_background(SKYBLUE)
    
#     begin_mode_3d(camera)
#     # Sol
#     draw_plane(Vector3(mapWidth/2, 0.0, mapHeight/2), Vector2(100.0, 100.0), LIGHTGRAY)
    
#     # Murs
#     for x, y in walls_cache:
#         posX = mapPosition.x + x * 1.0
#         posZ = mapPosition.z + y * 1.0
#         draw_cube(Vector3(posX, 1.0, posZ), 1.0, 2.0, 1.0, DARKGRAY)
#         draw_cube_wires(Vector3(posX, 1.0, posZ), 1.0, 2.0, 1.0, BLACK)
#     end_mode_3d()

#     # Radar
#     radar_scale = 6
#     radar_x = get_screen_width() - mapWidth * radar_scale - 20
#     radar_y = 20
#     draw_rectangle(radar_x, radar_y, mapWidth * radar_scale, mapHeight * radar_scale, fade(BLACK, 0.5))
#     for x, y in walls_cache:
#         draw_rectangle(radar_x + x * radar_scale, radar_y + y * radar_scale, radar_scale, radar_scale, WHITE)
    
#     p_cell_x = int(camera.position.x + 0.5)
#     p_cell_y = int(camera.position.z + 0.5)
#     draw_rectangle(radar_x + p_cell_x * radar_scale, radar_y + p_cell_y * radar_scale, radar_scale, radar_scale, RED)

#     draw_fps(10, 10)
#     end_drawing()

# close_window()