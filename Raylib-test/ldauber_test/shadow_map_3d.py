from pyray import *
import pyray as pr

# --- INTERFACE BAS NIVEAU CONFIGURÉE ---
try:
    import _raylib # type: ignore
    rl = _raylib.lib
except ImportError:
    if hasattr(pr, "raylib") and hasattr(pr.raylib, "lib"):
        rl = pr.raylib.lib
    elif hasattr(pr, "_raylib") and hasattr(pr._raylib, "lib"):
        rl = pr._raylib.lib
    else:
        rl = pr

RLGL_SRC_ALPHA = 0x0302
RLGL_MIN = 0x8007
RLGL_MAX = 0x8008

MAX_BOXES = 20
MAX_SHADOWS = MAX_BOXES * 3

class ShadowGeometry:
    def __init__(self):
        self.vertices = [Vector2(0, 0) for _ in range(4)]

class LightInfo:
    def __init__(self):
        self.active = False
        self.dirty = True
        self.valid = False
        self.position = Vector2(0, 0)
        self.mask = None          
        self.outerRadius = 0.0
        self.bounds = Rectangle(0, 0, 0, 0)
        self.shadows = [ShadowGeometry() for _ in range(MAX_SHADOWS)]
        self.shadowCount = 0

pac_light = LightInfo()

def move_light(x: float, y: float):
    global pac_light
    pac_light.dirty = True
    pac_light.position.x = x
    pac_light.position.y = y
    pac_light.bounds.x = x - pac_light.outerRadius
    pac_light.bounds.y = y - pac_light.outerRadius

def compute_shadow_volume_for_edge(sp: Vector2, ep: Vector2):
    global pac_light
    if pac_light.shadowCount >= MAX_SHADOWS:
        return

    extension = 5000.0  

    spVector = vector2_normalize(vector2_subtract(sp, pac_light.position))
    spProjection = vector2_add(sp, vector2_scale(spVector, extension))

    epVector = vector2_normalize(vector2_subtract(ep, pac_light.position))
    epProjection = vector2_add(ep, vector2_scale(epVector, extension))

    idx = pac_light.shadowCount
    pac_light.shadows[idx].vertices[0] = sp
    pac_light.shadows[idx].vertices[1] = ep
    pac_light.shadows[idx].vertices[2] = epProjection
    pac_light.shadows[idx].vertices[3] = spProjection
    pac_light.shadowCount += 1

def setup_light(x: float, y: float, radius: float):
    global pac_light
    pac_light.active = True
    pac_light.valid = False
    pac_light.mask = load_render_texture(get_screen_width(), get_screen_height())
    pac_light.outerRadius = radius
    pac_light.bounds.width = radius * 2.0
    pac_light.bounds.height = radius * 2.0
    move_light(x, y)
    draw_light_mask()

def update_light(boxes, count):
    global pac_light
    if not pac_light.active or not pac_light.dirty:
        return False

    pac_light.dirty = False
    pac_light.shadowCount = 0
    pac_light.valid = False

    for i in range(count):
        if check_collision_point_rec(pac_light.position, boxes[i]):
            return False
        if not check_collision_recs(pac_light.bounds, boxes[i]):
            continue

        bx, by, bw, bh = boxes[i].x, boxes[i].y, boxes[i].width, boxes[i].height

        if pac_light.position.y < by:
            compute_shadow_volume_for_edge(Vector2(bx + bw, by), Vector2(bx, by))
        if pac_light.position.x > bx + bw:
            compute_shadow_volume_for_edge(Vector2(bx + bw, by + bh), Vector2(bx + bw, by))
        if pac_light.position.y > by + bh:
            compute_shadow_volume_for_edge(Vector2(bx, by + bh), Vector2(bx + bw, by + bh))
        if pac_light.position.x < bx:
            compute_shadow_volume_for_edge(Vector2(bx, by), Vector2(bx, by + bh))

        idx = pac_light.shadowCount
        pac_light.shadows[idx].vertices[0] = Vector2(bx, by)
        pac_light.shadows[idx].vertices[1] = Vector2(bx, by + bh)
        pac_light.shadows[idx].vertices[2] = Vector2(bx + bw, by + bh)
        pac_light.shadows[idx].vertices[3] = Vector2(bx + bw, by)
        pac_light.shadowCount += 1

    pac_light.valid = True
    draw_light_mask()
    return True

def draw_light_mask():
    global pac_light
    begin_texture_mode(pac_light.mask)
    clear_background(WHITE)

    blend_custom = BlendMode.BLEND_CUSTOM.value if hasattr(BlendMode.BLEND_CUSTOM, 'value') else BlendMode.BLEND_CUSTOM
    blend_alpha = BlendMode.BLEND_ALPHA.value if hasattr(BlendMode.BLEND_ALPHA, 'value') else BlendMode.BLEND_ALPHA
    func_factors = getattr(rl, "rlSetBlendFactors", getattr(pr, "rl_set_blend_factors", None))
    func_mode = getattr(rl, "rlSetBlendMode", getattr(pr, "rl_set_blend_mode", None))
    func_batch = getattr(rl, "rlDrawRenderBatchActive", getattr(pr, "rl_draw_render_batch_active", None))

    if func_factors: func_factors(RLGL_SRC_ALPHA, RLGL_SRC_ALPHA, RLGL_MIN)
    if func_mode: func_mode(blend_custom)

    if pac_light.valid:
        draw_circle_gradient(pac_light.position, pac_light.outerRadius, color_alpha(WHITE, 0.0), WHITE)

    if func_batch: func_batch()
    if func_mode: func_mode(blend_alpha)
    if func_factors: func_factors(RLGL_SRC_ALPHA, RLGL_SRC_ALPHA, RLGL_MAX)
    if func_mode: func_mode(blend_custom)

    for i in range(pac_light.shadowCount):
        draw_triangle_fan(pac_light.shadows[i].vertices, 4, WHITE)

    if func_batch: func_batch()
    if func_mode: func_mode(blend_alpha) 
    end_texture_mode()

def setup_boxes():
    boxes = [Rectangle(0, 0, 0, 0) for _ in range(MAX_BOXES)]
    boxes[0] = Rectangle(150, 80, 40, 40)
    boxes[1] = Rectangle(600, 350, 40, 40)
    boxes[2] = Rectangle(200, 300, 40, 40)
    boxes[3] = Rectangle(650, 50, 40, 40)
    boxes[4] = Rectangle(400, 200, 40, 40)

    for i in range(5, MAX_BOXES):
        boxes[i] = Rectangle(
            float(get_random_value(50, 750)),
            float(get_random_value(50, 400)),
            float(get_random_value(20, 60)),
            float(get_random_value(20, 60))
        )
    return boxes

def main():
    screen_width = 800
    screen_height = 450
    init_window(screen_width, screen_height, "3D Top-Down Shadow Mapping")

    box_count = MAX_BOXES
    boxes = setup_boxes()

    # --- CONFIGURATION CAMÉRA 3D ORTHOGRAPHIQUE ---
    camera = Camera3D()
    camera.position = Vector3(400.0, 500.0, 225.0) 
    camera.target = Vector3(400.0, 0.0, 225.0)   
    camera.up = Vector3(0.0, 0.0, -1.0)           
    camera.fovy = 450.0 # En mode orthographique, fovy définit la largeur de la zone visible (ici 450 pixels de haut)
    camera.projection = CameraProjection.CAMERA_ORTHOGRAPHIC # <-- ON PASSE EN ORTHOGRAPHIQUE !

    light_mask = load_render_texture(get_screen_width(), get_screen_height())
    setup_light(400, 225, 250)
    
    speed = 4.0
    set_target_fps(60)

    blend_custom = BlendMode.BLEND_CUSTOM.value if hasattr(BlendMode.BLEND_CUSTOM, 'value') else BlendMode.BLEND_CUSTOM
    blend_alpha = BlendMode.BLEND_ALPHA.value if hasattr(BlendMode.BLEND_ALPHA, 'value') else BlendMode.BLEND_ALPHA
    func_factors = getattr(rl, "rlSetBlendFactors", getattr(pr, "rl_set_blend_factors", None))
    func_mode = getattr(rl, "rlSetBlendMode", getattr(pr, "rl_set_blend_mode", None))
    func_batch = getattr(rl, "rlDrawRenderBatchActive", getattr(pr, "rl_draw_render_batch_active", None))

    while not window_should_close():
        new_x = pac_light.position.x
        new_y = pac_light.position.y

        if is_key_down(KeyboardKey.KEY_W): new_y -= speed
        if is_key_down(KeyboardKey.KEY_S): new_y += speed
        if is_key_down(KeyboardKey.KEY_A): new_x -= speed
        if is_key_down(KeyboardKey.KEY_D): new_x += speed

        if new_x != pac_light.position.x or new_y != pac_light.position.y:
            move_light(new_x, new_y)

        dirty_lights = update_light(boxes, box_count)

        if dirty_lights:
            begin_texture_mode(light_mask)
            clear_background(BLACK)
            if func_factors: func_factors(RLGL_SRC_ALPHA, RLGL_SRC_ALPHA, RLGL_MIN)
            if func_mode: func_mode(blend_custom)
            if pac_light.active:
                draw_texture_rec(pac_light.mask.texture, Rectangle(0, 0, float(get_screen_width()), -float(get_screen_height())), Vector2(0, 0), WHITE)
            if func_batch: func_batch()
            if func_mode: func_mode(blend_alpha)
            end_texture_mode()

        # --- RENDU MIXTE 3D / 2D ---
        begin_drawing()
        clear_background(BLACK)

        # 1. Rendu de la géométrie en vraie 3D
        begin_mode_3d(camera)
            # Le sol en gris foncé
        draw_plane(Vector3(400.0, 0.0, 225.0), Vector2(1000.0, 1000.0), DARKGRAY)

        # On transforme nos rectangles 2D en cubes 3D d'une hauteur de 40 unités
        for b in range(box_count):
            cube_pos = Vector3(
                boxes[b].x + boxes[b].width / 2.0,
                20.0, # Hauteur moyenne
                boxes[b].y + boxes[b].height / 2.0
            )
            draw_cube(cube_pos, boxes[b].width, 40.0, boxes[b].height, DARKBLUE)
            draw_cube_wires(cube_pos, boxes[b].width, 40.0, boxes[b].height, BLUE)
        end_mode_3d()

        # 2. Application instantanée de notre masque d'ombres géométriques par-dessus la 3D
        draw_texture_rec(light_mask.texture, Rectangle(0, 0, float(get_screen_width()), -float(get_screen_height())), Vector2(0, 0), WHITE)

        # 3. Petit repère de la lampe
        if pac_light.active:
            draw_circle(int(pac_light.position.x), int(pac_light.position.y), 5, YELLOW)

        draw_fps(screen_width - 80, 10)
        end_drawing()

    unload_render_texture(light_mask)
    if pac_light.active:
        unload_render_texture(pac_light.mask)
    close_window()

if __name__ == "__main__":
    main()