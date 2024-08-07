import time

import dearpygui.dearpygui as dpg


class Window:
    def __init__(self, title, width, height):
        self.title = title
        self.width = width
        self.height = height
        self.frame_count = 0
        self.last_time = time.time()
        self.fps = 0

    def count_fps(self):
        self.frame_count += 1
        current_time = time.time()
        elapsed_time = current_time - self.last_time

        if elapsed_time >= 1.0:
            self.fps = self.frame_count / elapsed_time
            self.frame_count = 0
            self.last_time = current_time

    def render(self, objects_list=None, elasticity=1):

        if objects_list is None:
            objects_list = []
        dpg.create_context()
        dpg.create_viewport(title=self.title, width=self.width, height=self.height)
        dpg.setup_dearpygui()
        dpg.show_viewport()

        with dpg.viewport_drawlist():
            while dpg.is_dearpygui_running():

                self.count_fps()

                dpg.delete_item(item="fps")
                dpg.draw_text(pos=[1320, 0], text=f"FPS: {self.fps}", size=50, tag="fps")
                dpg.draw_text(pos=[0, 0], text=f"Elasticity: {elasticity}", size=80)

                objects_list.sort(key=lambda p: p.s[0])

                for obj in objects_list:

                    if dpg.does_item_exist(obj.tag):
                        dpg.delete_item(obj.tag)
                    obj.draw()

                    obj.detect_collision(*objects_list, elasticity=elasticity)
                    obj.gravity(*objects_list)
                    obj.move(elasticity=elasticity)

                dpg.render_dearpygui_frame()

        dpg.destroy_context()
