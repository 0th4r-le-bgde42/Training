from pyray import *
import pyray as pr

GLSL_VERSION = 330

width = 2500
height = 1500

set_config_flags(ConfigFlags.FLAG_MSAA_4X_HINT)
init_window(width, height, "Normalmap")

camera = Camera3D()
camera.position = Vector3(0.0, 2.0, -4.0)
camera.target = Vector3(0.0, 0.0, 0.0)
camera.up = Vector3(0.0, 1.0, 0.0)
camera.fovy = 45.0
camera.projection = CameraProjection.CAMERA_PERSPECTIVE

shader = load_shader("ldauber_test/shaders/normalmap.vs", "ldauber_test/shaders/normalmap.fs")
shader.locs[ShaderLocationIndex.SHADER_LOC_MAP_NORMAL] = get_shader_location(shader, "normalMap")
shader.locs[ShaderLocationIndex.SHADER_LOC_VECTOR_VIEW] = get_shader_location(shader, "viewPos")

light_position = Vector3(0.0, 1.0, 0.0)
light_pos_loc = get_shader_location(shader, "lightPos")

plane = load_model("ldauber_test/models/plane.glb")
plane.materials[0].shader = shader
plane.materials[0].maps[MATERIAL_MAP_DIFFUSE].texture = load_texture("ldauber_test/resources/tiles_diffuse.png") # type: ignore
plane.materials[0].maps[MATERIAL_MAP_NORMAL].texture = load_texture("ldauber_test/resources/tiles_normal.png") # type: ignore

gen_texture_mipmaps(plane.materials[0].maps[MATERIAL_MAP_DIFFUSE].texture) # type: ignore
gen_texture_mipmaps(plane.materials[0].maps[MATERIAL_MAP_NORMAL].texture) # type: ignore

set_texture_filter(plane.materials[0].maps[MATERIAL_MAP_DIFFUSE].texture, TextureFilter.TEXTURE_FILTER_TRILINEAR) # type: ignore
set_texture_filter(plane.materials[0].maps[MATERIAL_MAP_NORMAL].texture, TextureFilter.TEXTURE_FILTER_TRILINEAR) # type: ignore

specular_exponent = 8.0
specular_exponent_loc = get_shader_location(shader, "specularExponent")

use_normalmap = 1
use_normalmap_loc = get_shader_location(shader, "useNormalMap")

set_target_fps(60)

while not window_should_close():
	direction = Vector3()
	if is_key_down(KEY_W): # type: ignore
		direction = vector3_add(direction, Vector3(0.0, 0.0, 1.0))
	if is_key_down(KEY_S): # type: ignore
		direction = vector3_add(direction, Vector3(0.0, 0.0, -1.0))
	if is_key_down(KEY_D): # type: ignore
		direction = vector3_add(direction, Vector3(-1.0, 0.0, .0))
	if is_key_down(KEY_A): # type: ignore
		direction = vector3_add(direction, Vector3(1.0, 0.0, 0.0))
	
	direction = vector3_normalize(direction)
	light_position = vector3_add(light_position, vector3_scale(direction, get_frame_time()*3.0))

	if is_key_down(KEY_UP): # type: ignore
		specular_exponent = clamp(specular_exponent + 40.0*get_frame_time(), 2.0, 128.0)
	if is_key_down(KEY_DOWN): # type: ignore
		specular_exponent = clamp(specular_exponent - 40.0*get_frame_time(), 2.0, 128.0)
	
	if is_key_pressed(KEY_N): # type: ignore
		use_normalmap = not use_normalmap
	
	plane.transform = matrix_rotate_y(float(get_time()*0.5))

	light_pos = pr.ffi.new("float[]", [light_position.x, light_position.y, light_position.z])
	set_shader_value_v(shader, light_pos_loc, light_pos, ShaderUniformDataType.SHADER_UNIFORM_VEC3, 1)

	cam_pos = pr.ffi.new("float[]", [camera.position.x, camera.position.y, camera.position.z])
	set_shader_value_v(shader, shader.locs[ShaderLocationIndex.SHADER_LOC_VECTOR_VIEW], cam_pos, ShaderUniformDataType.SHADER_UNIFORM_VEC3, 1)

	specular_exponent_c = pr.ffi.new("float *", specular_exponent)
	set_shader_value(shader, specular_exponent_loc, specular_exponent_c, ShaderUniformDataType.SHADER_UNIFORM_FLOAT)

	use_normalmap_c = pr.ffi.new("int *", use_normalmap)
	set_shader_value_v(shader, use_normalmap_loc, use_normalmap_c, ShaderUniformDataType.SHADER_UNIFORM_INT, 1)

	begin_drawing()
	clear_background(RAYWHITE)
	begin_mode_3d(camera)
	begin_shader_mode(shader)
	draw_model(plane, vector3_zero(), 2.0, WHITE)
	end_shader_mode()

	draw_sphere_wires(light_position, 0.2, 8, 8, ORANGE)
	end_mode_3d()

	text_color = DARKGREEN if use_normalmap else RED
	toggle_str = "On" if use_normalmap else "Off"
	draw_text(f"Use key [N] to toggle normal map: {toggle_str}", 10, 10, 10, text_color)

	y_offset = 24
	draw_text("Use keys [W][S][A][D] to move the light", 10, 10+y_offset*1, 10, BLACK)
	draw_text("Use keys [Up][Down] to change specular exponent", 10, 10+y_offset*2, 10, BLACK)
	draw_text(f"Specular Exponent: {specular_exponent}", 10, 10+y_offset*3, 10, BLUE)

	draw_fps(width-90, 10)

	end_drawing()

unload_shader(shader)
unload_model(plane)

close_window()
