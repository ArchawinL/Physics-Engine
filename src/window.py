from particle import Particle


def window():
    import dearpygui.dearpygui as dpg

    dpg.create_context()

    dpg.create_viewport(title='Custom Title', width=1600, height=900)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    rand_part = Particle(2, (800, 450), (3, 7))

    while dpg.is_dearpygui_running():
        with dpg.viewport_drawlist():
            dpg.delete_item("rand_part")
            dpg.draw_circle(center=(rand_part.x, rand_part.y), radius=25, tag="rand_part", fill=(255, 255, 255, 255))

        rand_part.move()
        if rand_part.y > 800 or rand_part.y < 50:
            rand_part.set_velocity((rand_part.get_x_velocity(), -rand_part.get_y_velocity()))

        if rand_part.x > 1550 or rand_part.x < 50:
            rand_part.set_velocity((-rand_part.get_x_velocity(), rand_part.get_y_velocity()))

        dpg.render_dearpygui_frame()

    dpg.destroy_context()
