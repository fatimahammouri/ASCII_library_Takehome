class Canvas():
    """canvas with height and width """

    def __init__(self, height, width, char):
        self.height = height
        self.width = width
        self.char = char

    # def print_canvas(self):
    # def clear_all(self):
    # def add_shape():
    
   

class Rectangle():
    def __init__(self, start_x, start_y, end_x, end_y, fill_char):
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y
        self.fill_char = fill_char

    # def change_fill_char(self, new_char): 
    #     self.fill_char = new_char

    # def translate_rect(self, x_axis, y_axis, num):
