from pyray import *
import pyray as pr

GLSL_VERSION = 330
MAX_LIGHT = 4

class LightType:
    LIGHT_DIRECTIONAL = 0
    LIGHT_POINT = 1
    LIGHT_SPOT = 2


class Light:
    def __init__(self):
        self.type: int = LightType.LIGHT_POINT
        self.enabled: int = 0
        self.position: Vector3 = Vector3(0.0, 0.0, 0.0)
        self.target: Vector3 = Vector3(0.0, 0.0, 0.0)
        self.color: list[float] = [1.0, 1.0, 1.0, 1.0]
        self.intensity: float = 1.0

        self.type_loc: int = -1
        self.enable_loc: int = -1
        self.position_loc: int = -1
        self.target_loc: int = -1
        self.color_loc: int = -1
        self.intensity_loc: int = -1


light_count = 0

def create_light(type, position, target, color, intensity, shader):
    global light_count

    if light_count < MAX_LIGHT:
        light = Light()
        light.enabled = 1
        light.type = type
        light.position = position
        light.target = target
        light.color[0] = float(color[0]/255.0)
        light.color[1] = float(color[1]/255.0)
        light.color[2] = float(color[2]/255.0)
        light.color[3] = float(color[3]/255.0)
        light.intensity = intensity

        light.enable_loc = get_shader_location(shader, f"lights[{light_count}].enabled")
        light.type_loc = get_shader_location(shader, f"lights[{light_count}].type")
        light.position_loc = get_shader_location(shader, f"lights[{light_count}].position")
        light.target_loc = get_shader_location(shader, f"lights[{light_count}].target")
        light.color_loc = get_shader_location(shader, f"lights[{light_count}].color")
        light.intensity_loc = get_shader_location(shader, f"lights[{light_count}].intensity")

        update_light(shader, light)

        light_count += 1
        return light
    
    return None


def update_light(shader, light: Light):
    enabled_c = pr.ffi.new("int *", light.enabled)
    type_c = pr.ffi.new("int *", light.type)
    intensity_c = pr.ffi.new("float *", light.intensity)

    set_shader_value(shader, light.enable_loc, enabled_c, SHADER_UNIFORM_INT) # type: ignore
    set_shader_value(shader, light.type_loc, type_c, SHADER_UNIFORM_INT) # type: ignore
    set_shader_value(shader, light.intensity_loc, intensity_c, SHADER_UNIFORM_FLOAT) # type: ignore

    position_c = pr.ffi.new("float[]", [light.position.x, light.position.y, light.position.z])
    set_shader_value_v(shader, light.position_loc, position_c, SHADER_UNIFORM_VEC3, 1) # type: ignore

    target_c = pr.ffi.new("float[]", [light.target.x, light.target.y, light.target.z])
    set_shader_value_v(shader, light.target_loc, target_c, SHADER_UNIFORM_VEC3, 1) # type: ignore
    
    color_c = pr.ffi.new("float[]", light.color)
    set_shader_value_v(shader, light.color_loc, color_c, SHADER_UNIFORM_VEC4, 1) # type: ignore
    

def lights():
    width = 800
    height = 450

    set_config_flags(FLAG_MSAA_4X_HINT) # type: ignore
    init_window(width, height, "Basic light")

    camera = Camera3D()
    camera.position = Vector3(2.0, 2.0, 6.0)
    camera.target  = Vector3(0.0, 0.5, 0.0)
    camera.up = Vector3(0.0, 1.0, 0.0)
    camera.fovy = 45.0
    camera.projection = CAMERA_PERSPECTIVE # type: ignore

    shader = load_shader("ldauber_test/shaders/lighting.vs", "ldauber_test/shaders/lighting.fs")
    shader.locs[SHADER_LOC_VECTOR_VIEW] - get_shader_location(shader, "viewPos") # type: ignore

    ambient_loc = get_shader_location(shader, "ambient")
    ambient_color = pr.ffi.new("float[]", [0.1, 0.1, 0.1, 1.0])
    set_shader_value_v(shader, ambient_loc, ambient_color, SHADER_UNIFORM_VEC4, 1) # type: ignore

    lights: Light = []
    lights.append(create_light(LightType.LIGHT_POINT, Vector3(-2,1,-2), Vector3(0,0,0), YELLOW, 1.0, shader))
    lights.append(create_light(LightType.LIGHT_POINT, Vector3(2,1,2), Vector3(0,0,0), RED, 1.0, shader))
    lights.append(create_light(LightType.LIGHT_POINT, Vector3(-2,1,2), Vector3(0,0,0), GREEN, 1.0, shader))
    lights.append(create_light(LightType.LIGHT_POINT, Vector3(2,1,-2), Vector3(0,0,0), BLUE, 1.0, shader))

    set_target_fps(60)

    while not window_should_close():
        update_camera(camera, CAMERA_ORBITAL) # type: ignore

        camera_pos_c = pr.ffi.new("float[]", [camera.position.x, camera.position.y, camera.position.z])
        set_shader_value_v(shader, shader.locs[SHADER_LOC_VECTOR_VIEW], camera_pos_c, SHADER_UNIFORM_VEC3, 1) # type: ignore

        if is_key_pressed(KEY_ONE): lights[0].enabled = 0 if lights[0].enabled == 1 else 1 # type: ignore
        if is_key_pressed(KEY_TWO): lights[1].enabled = 0 if lights[1].enabled == 1 else 1 # type: ignore
        if is_key_pressed(KEY_THREE): lights[2].enabled = 0 if lights[2].enabled == 1 else 1 # type: ignore
        if is_key_pressed(KEY_FOUR): lights[3].enabled = 0 if lights[3].enabled == 1 else 1 # type: ignore

        for i in range(MAX_LIGHT):
            update_light(shader, lights[i])
        
        begin_drawing()
        clear_background(RAYWHITE)

        begin_mode_3d(camera)
        begin_shader_mode(shader)

        draw_plane(Vector3(0,0,0), Vector2(10.0,10.0), WHITE)
        draw_cube(Vector3(0,0,0), 2.0, 4.0, 2.0, WHITE)

        end_shader_mode()

        for i in range(MAX_LIGHT):
            r = int(lights[i].color[0] * 255)
            g = int(lights[i].color[1] * 255)
            b = int(lights[i].color[2] * 255)
            a = int(lights[i].color[3] * 255)
            c = Color(r,g,b,a)

            if lights[i].enabled == 1:
                draw_sphere_ex(lights[i].position, 0.2, 8, 8, c)
            else:
                draw_sphere_wires(lights[i].position, 0.2, 8, 8, color_alpha(c, 0.3))
        
        draw_grid(10,1.0)
        end_mode_3d()

        end_drawing()

    unload_shader(shader)
    close_window()


if __name__ == "__main__":
    lights()
