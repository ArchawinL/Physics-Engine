from particle import Particle


def window():
    import dearpygui.dearpygui as dpg

    dpg.create_context()

    dpg.create_viewport(title='Custom Title', width=1600, height=900)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    rand_part = Particle(2, 450, 5)

    while dpg.is_dearpygui_running():
        with dpg.viewport_drawlist():
            dpg.delete_item("rand_part")
            dpg.draw_circle(center=(800, rand_part.position), radius=50, tag="rand_part")
            rand_part.move()

        if rand_part.position > 800:
            rand_part.position = 0
        dpg.render_dearpygui_frame()
    dpg.destroy_context()
