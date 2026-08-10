from pyray import *
import math

def main():
    init_window(2500, 1800, "test Voxel")
    set_target_fps(60)

    sun = load_shader(
        "ldauber_test/shaders/sun.vs",
        "ldauber_test/shaders/sun.fs")
    light_dir_loc = get_shader_location(sun, "lightDir")
    light_color_loc = get_shader_location(sun, "lightColor")

    light_direction = [-0.5, -1.0, -0.3]
    set_shader_value(
        sun, light_dir_loc,
        ffi.new("float[]", light_direction),
        ShaderUniformDataType.SHADER_UNIFORM_VEC3)

    light_color = [1.0, 0.95, 0.85]
    set_shader_value(
        sun, light_color_loc,
        ffi.new("float[]", light_color),
        ShaderUniformDataType.SHADER_UNIFORM_VEC3)

    # Configuration de la caméra
    camera = Camera3D()
    camera.position = Vector3(10.0, 10.0, 10.0)
    camera.target = Vector3(0.0, 0.0, 0.0)
    camera.up = Vector3(0.0, 1.0, 0.0)
    camera.fovy = 45.0
    camera.projection = CAMERA_PERSPECTIVE

    voxel_path = "ldauber_test/models/red_ghost.vox"
    model = load_model(voxel_path)
    model.materials[0].shader = sun

    voxel_scale = Vector3(0.05, 0.05, 0.05) 
    rotation_angle = 0.0

    # Variables pour notre propre logique de caméra orbitale
    distance = 15.0
    angle_x = 0.7  # Angle vertical (en radians)
    angle_y = 0.7  # Angle horizontal (en radians)

    print("--- Inspecteur de Voxel (Logique Manuelle) ---")
    print("Contrôles :")
    print("- Maintenir le CLIC DROIT ou GAUCHE pour tourner autour du voxel.")
    print("- Molette de la souris pour Zoomer / Dézoomer.")

    while not window_should_close():
        # 1. Gestion du Zoom (Molette)
        wheel = get_mouse_wheel_move()
        distance -= wheel * 1.5
        if distance < 2.0: distance = 2.0

        # 2. Gestion de la Rotation (Clic enfoncé + déplacement souris)
        if is_mouse_button_down(MOUSE_BUTTON_RIGHT) or is_mouse_button_down(MOUSE_BUTTON_LEFT):
            mouse_delta = get_mouse_delta()
            angle_y -= mouse_delta.x * 0.005
            angle_x += mouse_delta.y * 0.005
            
            # On limite l'angle vertical pour ne pas retourner la caméra à l'envers
            if angle_x > 1.5: angle_x = 1.5
            if angle_x < -1.5: angle_x = -1.5

        # 3. Calcul de la nouvelle position de la caméra (Spherical Coordinates)
        camera.position.x = camera.target.x + distance * math.cos(angle_x) * math.sin(angle_y)
        camera.position.y = camera.target.y + distance * math.sin(angle_x)
        camera.position.z = camera.target.z + distance * math.cos(angle_x) * math.cos(angle_y)

        rotation_angle += 0.5

        begin_drawing()
        clear_background(RAYWHITE)

        begin_mode_3d(camera)

        # Grille rouge/grise bien visible au centre
        draw_grid(20, 1.0)

        # Repères d'axes
        draw_line_3d(Vector3(0,0,0), Vector3(5,0,0), RED)     # X
        draw_line_3d(Vector3(0,0,0), Vector3(0,5,0), GREEN)   # Y
        draw_line_3d(Vector3(0,0,0), Vector3(0,0,5), BLUE)    # Z

        # Rendu du modèle
        draw_model_ex(
            model, 
            Vector3(0.0, 0.0, 0.0), 
            Vector3(0.0, 1.0, 0.0), 
            rotation_angle, 
            voxel_scale, 
            WHITE
        )

        end_mode_3d()

        # UI 2D d'aide
        draw_text("INSPECTEUR DE VOXELS (LOGIQUE MANUELLE)", 20, 20, 24, DARKGRAY)
        draw_text("Maintenez n'importe quel clic et glissez pour tourner", 20, 60, 18, ORANGE)
        draw_text("Utilisez la molette pour Zoomer / Dezoomer", 20, 90, 18, ORANGE)
        draw_text(f"Fichier: {voxel_path}", 20, 130, 18, BLUE)
        draw_text(f"Dist. Camera: {distance:.2f}", 20, 160, 18, GRAY)

        end_drawing()

    unload_model(model)
    unload_shader(sun)
    close_window()

if __name__ == "__main__":
    main()