import dearpygui.dearpygui as dpg


class Window:
    def __init__(self, title, width, height):
        self.title = title
        self.width = width
        self.height = height

        dpg.create_context()
