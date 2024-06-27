import time

import dearpygui.dearpygui as dpg


class Window:
    def __init__(self, title, width, height):
        self.title = title
        self.width = width
        self.height = height

    def render(self, objects_list=None):

        if objects_list is None:
            objects_list = []
        dpg.create_context()
        dpg.create_viewport(title=self.title, width=self.width, height=self.height)
        dpg.setup_dearpygui()
        dpg.show_viewport()

        while dpg.is_dearpygui_running():

            for obj in objects_list:
                with dpg.viewport_drawlist():

                    dpg.delete_item(obj.tag)
                    obj.draw()
                obj.move()

            dpg.render_dearpygui_frame()

        dpg.destroy_context()
