class Canvas():
    """canvas with height and width """

    def __init__(self, height, width):
        self.height = height
        self.width = width
        

    def print_canvas(self):
        for row in range(self.height):
            print('*' * self.width)
            

    # def add_shape(self, Shape, x, y):

    # def clear_all(self):
    
   

class Shape():
    def __init__(self, start_x, start_y, end_x, end_y, fill_char):
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y
        self.fill_char = fill_char

    def draw_shape(self):
        width = x_end - x_start
        height = y_end - y_start
        for row in range(self.height):
            print(self.fill_char * self.width)

    # def change_fill_char(self, new_char): 
    #     self.fill_char = new_char

    # def translate_rect(self, x_axis, y_axis, num):
