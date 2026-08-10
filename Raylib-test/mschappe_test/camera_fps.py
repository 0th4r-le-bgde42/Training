from pyray import *
import random
import math
from time import time


MAX_COLUMNS = 10

width = 2000
height = 1000

init_window(width, height, "FPS")

camera = Camera3D()
camera.position = Vector3(0.0, 2.0, 4.0)
camera.target = Vector3(0.0, 2.0, 0.0)
camera.up = Vector3(0.0, 1.0, 0.0)
camera.fovy = 90.0
camera.projection = CAMERA_PERSPECTIVE # type: ignore
# camera_angle = 0.0
# angle_cible = 0.0
# vitesse_rotation = 0.1



heights = [random.randint(1, 12) for _ in range(MAX_COLUMNS)]
positions = [Vector3(random.randint(-15, 15),
                     heights[i]/2.0,
                     random.randint(-15, 15)) for i in range(MAX_COLUMNS)]
colors = [Color(random.randint(20, 255),
                random.randint(10, 55),
                30,
                255) for _ in range(MAX_COLUMNS)]

cube_len = 2.0

# mouvement = Vector3(0.0, 0.0, 0.0)
# speed = 0.15


disable_cursor()

set_target_fps(60)

speed = 0.15

# def update_view(cam: Camera3D, angle: float):
#     cam.target.x = cam.position.x + math.cos(angle)
#     cam.target.z = cam.position.z + math.sin(angle)
#     cam.target.y = cam.position.y

# update_view(camera, camera_angle)

ground = 2.0
jump = 5.0
is_jump = False
top = False

shader_crt = load_shader("", "crt.fs")
time_loc = get_shader_location(shader_crt, "time")
current_time = 0.0
time_data = ffi.new("float *", current_time)
target = load_render_texture(get_screen_width(), get_screen_height())
# set_texture_filter(target.texture, TEXTURE_FILTER_BILINEAR)

start = time()
timer = time()
t = 20
actual = int(str(int(timer))[-1])
last = actual
count = 0

while not window_should_close():
    timer = time()
    actual = int(str(int(timer))[-1])
    if actual != last:
        last = actual
        if count >= 1: 
            t -= 1
        count += 1
    if t == 0:
        break
    current_time += get_frame_time()
    time_data[0] = current_time
    set_shader_value(shader_crt, time_loc, time_data, SHADER_UNIFORM_FLOAT)
    mouvement = Vector3(0.0, 0.0, 0.0)
    if is_key_down(KEY_R):
        break

    if is_key_down(KEY_SPACE):
        if is_jump is False:
            is_jump = True
    
    if is_jump is True:
        s = 0.1
        d = 0.2
        if top is False:
            if camera.position.y < jump:
                camera.position.y += s
                if camera.position.y >= jump:
                    camera.position.y = jump
                    top = True
        else:
            if camera.position.y >= ground:
                camera.position.y -= d
                if camera.position.y <= ground:
                    camera.position.y = ground
                    top = False
                    is_jump = False
    # MOUSE===================================================
    mouse_speed = 0.1
    mouse_delta = get_mouse_delta()
    rotation = Vector3(mouse_delta.x * mouse_speed,
                       mouse_delta.y * mouse_speed,
                       0.0)

    update_camera_pro(camera, Vector3(0, 0, 0), rotation, 0.0)


    # KEY======================================================
    dx = camera.target.x - camera.position.x
    dz = camera.target.z - camera.position.z
    angle_regard = math.atan2(dz, dx)

    if is_key_down(KEY_W): # Avancer
        mouvement.x += math.cos(angle_regard) * speed
        mouvement.z += math.sin(angle_regard) * speed
    if is_key_down(KEY_S): # Reculer
        mouvement.x -= math.cos(angle_regard) * speed
        mouvement.z -= math.sin(angle_regard) * speed
    if is_key_down(KEY_A): # Pas de côté (Strafe gauche)
        # On ajoute 90° (pi/2) à l'angle pour aller sur le côté
        mouvement.x += math.cos(angle_regard - math.pi / 2) * speed
        mouvement.z += math.sin(angle_regard - math.pi / 2) * speed
    if is_key_down(KEY_D): # Pas de côté (Strafe droite)
        mouvement.x += math.cos(angle_regard + math.pi / 2) * speed
        mouvement.z += math.sin(angle_regard + math.pi / 2) * speed

    camera.position.x += mouvement.x
    camera.position.z += mouvement.z
    camera.target.x += mouvement.x
    camera.target.z += mouvement.z







    # if is_key_pressed(KEY_A):  # type: ignore
    #     angle_cible -= math.pi / 2
    #     #camera_angle -= math.pi / 2
    #     #update_view(camera, camera_angle)
    
    # if is_key_pressed(KEY_D): # type: ignore
    #     angle_cible += math.pi / 2
    #     #camera_angle += math.pi / 2
    #     #update_view(camera, camera_angle)

    # camera_angle += (angle_cible - camera_angle) * vitesse_rotation

    # mouvement = Vector3(0.0, 0.0, 0.0)

    # if is_key_down(KEY_W): # type: ignore
    #     mouvement.x = math.cos(angle_cible) * speed
    #     mouvement.z = math.sin(angle_cible) * speed
    
    # if is_key_down(KEY_S): # type: ignore
    #     mouvement.x = -math.cos(angle_cible) * speed
    #     mouvement.z = -math.sin(angle_cible) * speed
    
    
    # camera.position.x += mouvement.x
    # camera.position.z += mouvement.z

    # update_view(camera, camera_angle)

    #===========================DRAW SECTION
    # begin_drawing()
    begin_drawing()
    begin_texture_mode(target)
    clear_background(RAYWHITE)

    #======3D
    begin_mode_3d(camera)
    draw_plane(Vector3(0.0, 0.0, 0.0),
               Vector2(32.0, 32.0),
               LIGHTGRAY)
    draw_cube(Vector3(-16.0, 2.5, 0.0),
              1.0, 5.0, 32.0,
              BLUE)
    draw_cube(Vector3(16.0, 2.5, 0.0),
              1.0, 5.0, 32.0,
              LIME)
    draw_cube(Vector3(0.0, 2.5, 16.0),
              32.0, 5.0, 1.0,
              GOLD)
    
    for i in range(MAX_COLUMNS):
        draw_cube(positions[i], cube_len, heights[i], cube_len, colors[i])
        draw_cube_wires(positions[i], cube_len, heights[i], cube_len, MAROON)

    end_mode_3d()
    draw_text(f"X: {camera.position.x}\nY: {camera.position.y}\nZ: {camera.position.z}", 0, 0, 50, BLACK)
    end_texture_mode()

    # begin_drawing()
    clear_background(BLACK)

    begin_shader_mode(shader_crt)
    source_rect = Rectangle(0, 0, target.texture.width, -target.texture.height)
    dest_rect = Rectangle(0, 0, get_screen_width(), get_screen_height())
    draw_texture_pro(target.texture, source_rect, dest_rect, Vector2(0, 0), 0.0, WHITE)
    # draw_text(f"X: {camera.position.x}\nY: {camera.position.y}\nZ: {camera.position.z}", 0, 0, 50, BLACK)
    end_shader_mode()
    # draw_text(f"X: {camera.position.x}\nY: {camera.position.y}\nZ: {camera.position.z}", 0, 0, 50, YELLOW)
    end_drawing()

unload_render_texture(target)
unload_shader(shader_crt)
close_window()