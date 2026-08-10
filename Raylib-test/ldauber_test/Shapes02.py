from pyray import *
from math import sin, cos

def CalculatePendulumEndPoint(l, theta) -> Vector2:
    return Vector2(10*l*sin(theta), 10*l*cos(theta))

def CalculateDoublePendulumEndPoint(l1, theta1, l2, theta2) -> Vector2:
    endpoint = CalculatePendulumEndPoint(l1, theta1)
    x2 = endpoint.x + (10*l2*sin(theta2))
    y2 = endpoint.y + (10*l2*cos(theta2))
    return Vector2(x2, y2)

simulation_steps = 60
G = 25.0

width = 700
height = 700

set_config_flags(FLAG_WINDOW_HIGHDPI) # type: ignore
init_window(width, height, "Double Pendulum")

l1 = 15.0
m1 = 0.2
theta1 = DEG2RAD*170 # type: ignore
w1 = 0
l2 = 15.0
m2 = 0.1
theta2 = DEG2RAD*90 # type: ignore
w2 = 0
lengthScaler = 0.1
totalM = m1 + m2

previousPosition = CalculateDoublePendulumEndPoint(l1, theta1, l2, theta2)
previousPosition.x += (float(width/2))
previousPosition.y += (float(height/2))

lineThick: float = 20
trailThick: float = 2
fateAlpha= 0.002

rainbow_timer = 0.0
rainbow_speed = 2.0

target = load_render_texture(width, height)
set_texture_filter(target.texture, TEXTURE_FILTER_BILINEAR) # type: ignore
begin_texture_mode(target)
clear_background(BLANK)
end_texture_mode()

set_target_fps(60)

while not window_should_close():
    dt = get_frame_time() * 2.0
    rainbow_timer += dt * rainbow_speed
    r = int((sin(rainbow_timer) * 127) + 128)
    g = int((sin(rainbow_timer + 2) * 127) + 128)
    b = int((sin(rainbow_timer + 4) * 127) + 128)
    rainbow_color = Color(r, g, b, 255)
    step = dt/simulation_steps
    step2 = step*step

    for i in range(simulation_steps):
        delta = theta1 - theta2
        sinD = sin(delta)
        cosD = cos(delta)
        cos2D = cos(2*delta)
        ww1 = w1*w1
        ww2 = w2*w2

        # Formule a1 (Uniformisée avec l1 et l2)
        num1 = -G*(2*m1 + m2)*sin(theta1) - m2*G*sin(theta1 - 2*theta2) - 2*sinD*m2*(ww2*l2 + ww1*l1*cosD)
        den1 = l1*(2*m1 + m2 - m2*cos2D)
        a1 = num1 / den1
        
        # Formule a2 (Correction du cos en sin + uniformisation l1 et l2)
        num2 = 2*sinD*(ww1*l1*totalM + G*totalM*sin(theta1) + ww2*l2*m2*cosD)
        den2 = l2*(2*m1 + m2 - m2*cos2D)
        a2 = num2 / den2
        
        # Mise à jour des angles et vitesses
        theta1 += w1*step + 0.5*a1*step2
        theta2 += w2*step + 0.5*a2*step2

        w1 += a1*step
        w2 += a2*step
        i += 1
    
    currentPosition = CalculateDoublePendulumEndPoint(l1, theta1, l2, theta2)
    currentPosition.x += float(width/2)
    currentPosition.y += float(height/2)

    begin_texture_mode(target)
    draw_circle_v(previousPosition, trailThick, rainbow_color)
    draw_line_ex(previousPosition, currentPosition, trailThick*2, rainbow_color)
    end_texture_mode()

    previousPosition = currentPosition

    begin_drawing()
    clear_background(BLACK)
    draw_texture_rec(
        target.texture,
        Rectangle(0, 0, target.texture.width, -target.texture.height),
        Vector2(0, 0),
        WHITE
    )

    center = Vector2(width/2.0, height/2.0)
    joint = CalculatePendulumEndPoint(l1, theta1)
    joint.x += center.x
    joint.y += center.y

    draw_line_ex(center, joint, lineThick, RAYWHITE)
    draw_line_ex(joint, currentPosition, lineThick, RAYWHITE)
    # draw_rectangle_pro(
    #     Rectangle(width/2.0, height/2.0-100, 10*l1, lineThick),
    #     Vector2(0, lineThick*0.5),
    #     90 - RAD2DEG*theta1,
    #     RAYWHITE
    # )

    # endpoint1 = CalculatePendulumEndPoint(l1, theta1)
    # draw_rectangle_pro(
    #     Rectangle(width/2.0+endpoint1.x, height/2.0 - 100 + endpoint1.y, 10*12, lineThick),
    #     Vector2(0, lineThick*0.5),
    #     90 - RAD2DEG*theta2,
    #     RAYWHITE
    # )
    end_drawing()

unload_render_texture(target)
close_window()

