from pyray import *
import math

def main():
    screen_width = 2000
    screen_height = 1000
    init_window(screen_width, screen_height, "True 3D FPS Light - Real FPS Controls")

    # --- CAMÉRA FPS ---
    camera = Camera3D()
    camera.position = Vector3(0.0, 0.44, 0.0) 
    camera.target = Vector3(0.0, 0.44, 1.0)   
    camera.up = Vector3(0.0, 1.0, 0.0)             
    camera.fovy = 60.0
    camera.projection = CameraProjection.CAMERA_PERSPECTIVE

    # --- VARIABLES DE ROTATION MAISON ---
    camera_angle_x = 0.0  # Regard Gauche / Droite
    camera_angle_y = 0.0  # Regard Haut / Bas
    player_speed = 4.0    
    mouse_sensitivity = 0.003

    # --- CHARGEMENT DU SHADER ---
    shader = load_shader("ldauber_test/shaders/fog.vs", "ldauber_test/shaders/fog.fs")
    cam_pos_loc = get_shader_location(shader, "cameraPos")
    fog_rad_loc = get_shader_location(shader, "fogRadius")

    fog_radius = 7.0
    fog_radius_c = ffi.new("float *", fog_radius)
    set_shader_value(shader, fog_rad_loc, fog_radius_c, ShaderUniformDataType.SHADER_UNIFORM_FLOAT)

    # --- GÉOMÉTRIE ---
    mesh_cube = gen_mesh_cube(1.0, 1.0, 1.0)
    cube_model = load_model_from_mesh(mesh_cube)
    cube_model.materials[0].shader = shader

    mesh_sol = gen_mesh_plane(100.0, 100.0, 1, 1)
    plane_model = load_model_from_mesh(mesh_sol)
    plane_model.materials[0].shader = shader

    cube_positions = [
        Vector3(2.0, 0.5, 3.0),
        Vector3(-2.0, 0.5, 4.0),
        Vector3(0.0, 0.5, 6.0),
        Vector3(3.0, 0.5, 8.0),
    ]

    set_target_fps(60)
    disable_cursor()

    while not window_should_close():
        dt = get_frame_time()
        if dt > 0.1: dt = 0.1

        # --- 1. GESTION DE LA SOURIS (REGARD SANS BOUNDS) ---
        mouse_delta = get_mouse_delta()
        camera_angle_x -= mouse_delta.x * mouse_sensitivity
        camera_angle_y -= mouse_delta.y * mouse_sensitivity

        # On limite l'angle vertical pour éviter de se retourner le cou
        camera_angle_y = max(-1.4, min(1.4, camera_angle_y))

        # Calcul des vecteurs directionnels de visée
        forward = Vector3(
            math.cos(camera_angle_y) * math.sin(camera_angle_x),
            math.sin(camera_angle_y),
            math.cos(camera_angle_y) * math.cos(camera_angle_x)
        )
        
        # Le vecteur "droite" pour les pas latéraux (Strafing)
        right = Vector3(
            math.cos(camera_angle_x),
            0.0,
            -math.sin(camera_angle_x)
        )

        # --- 2. GESTION DU CLAVIER AZERTY A PLAT ---
        move_direction = Vector3(0.0, 0.0, 0.0)

        # On n'utilise que forward.x et forward.z pour interdire la montée/descente
        if is_key_down(KEY_W) or is_key_down(KEY_Z):  # Z / W # type: ignore
            move_direction.x += forward.x
            move_direction.z += forward.z
        if is_key_down(KEY_S):                        # S # type: ignore
            move_direction.x -= forward.x
            move_direction.z -= forward.z
        if is_key_down(KEY_A) or is_key_down(KEY_Q):  # Q / A # type: ignore
            move_direction.x += right.x
            move_direction.z += right.z
        if is_key_down(KEY_D):                        # D # type: ignore
            
            move_direction.x -= right.x
            move_direction.z -= right.z

        # Normalisation pour garder la même vitesse en diagonale
        length = math.sqrt(move_direction.x**2 + move_direction.z**2)
        if length > 0:
            camera.position.x += (move_direction.x / length) * player_speed * dt
            camera.position.z += (move_direction.z / length) * player_speed * dt

        # Fixation absolue de la hauteur des yeux
        camera.position.y = 0.44

        # Mise à jour de la cible du regard (Caméra Target)
        camera.target.x = camera.position.x + forward.x
        camera.target.y = camera.position.y + forward.y
        camera.target.z = camera.position.z + forward.z

        # --- 3. MISE À JOUR DU SHADER ---
        cam_pos_c = ffi.new("float[]", [camera.position.x, camera.position.y, camera.position.z])
        set_shader_value(shader, cam_pos_loc, cam_pos_c, ShaderUniformDataType.SHADER_UNIFORM_VEC3)

        # --- RENDU ---
        begin_drawing()
        clear_background(BLACK) 

        begin_mode_3d(camera)
            # Sol
        draw_model(plane_model, Vector3(0.0, 0.0, 0.0), 1.0, DARKPURPLE)

        # Cubes
        for pos in cube_positions:
            draw_model(cube_model, pos, 1.0, DARKBLUE)
            #draw_cube_wires(pos, 1.0, 1.0, 1.0, BLUE)
        end_mode_3d()

        draw_fps(10, 10)
        end_drawing()

    unload_shader(shader)
    unload_model(cube_model)
    unload_model(plane_model)
    close_window()

if __name__ == "__main__":
    main()