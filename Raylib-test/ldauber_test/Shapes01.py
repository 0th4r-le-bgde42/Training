from pyray import *


width = 800
height = 450

init_window(width, height, "basic shapes")
rotation = 0.0
set_target_fps(60)

while not window_should_close():
    rotation += 2.0

    begin_drawing()
    clear_background(RAYWHITE)
    draw_text("Basic Shapes", 20, 20, 20, DARKGRAY)

    draw_circle(int(width/5), 120, 35, DARKBLUE)
    draw_circle_gradient(Vector2(width/5.0, 220.0), 60, GREEN, SKYBLUE)
    draw_circle_lines(int(width/5), 340, 80, DARKBLUE)
    draw_ellipse(int(width/5), 120, 25, 20, YELLOW)
    draw_ellipse_lines(int(width/5), 120, 30, 25, YELLOW)
    draw_text("L dl", 146, 112, 20, DARKBLUE)
    draw_text("  i", 145, 112, 20, RED)

    draw_triangle(
        Vector2(width/4.0 * 3.0, 80.0),
        Vector2(width/4.0 * 3.0 - 60.0, 150.0),
        Vector2(width/4.0 * 3.0 + 60.0, 150.0),
        VIOLET
    )
    draw_triangle_lines(
        Vector2(width/4.0 * 3.0, 160.0),
        Vector2(width/4.0 * 3.0 - 20.0, 230.0),
        Vector2(width/4.0 * 3.0 + 20.0, 230.0),
        DARKBLUE
    )

    draw_poly(Vector2(width/4.0*3, 330), 6, 80, rotation, BROWN)
    draw_poly_lines(Vector2(width/4.0*3, 330), 6,90, rotation, BROWN)
    draw_poly_lines_ex(Vector2(width/4.0*3, 330), 6, 85, rotation, 6, BEIGE)

    draw_line(18, 42, width-18, 42, BLACK)
    end_drawing()

close_window()