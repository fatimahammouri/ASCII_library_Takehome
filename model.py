class Canvas():
    """canvas with height and width """

    def __init__(self, height, width):
        self.height = height
        self.width = width
        

    def print_canvas(self):
        for row in range(self.height):
            print('*' * self.width)
        # outer_list = [[0] * 4] * 3
            

    # def add_shape(self, Shape, x, y):
       

    # def clear_all(self):
    
   

class Shape(Canvas(height, width)):
    def __init__(self, start_x, start_y, end_x, end_y, fill_char):
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y
        self.fill_char = fill_char

    def draw_shape(self):
        width = self.end_x - self.start_x
        height = self.end_y - self.start_y
        for row in range(height):
            print(self.fill_char * width)

    def change_fill_char(self, new_char): 
        self.fill_char = new_char

    def translate_rect(self, x_axis, y_axis, num):
        self.start_x = self.start_x + x_axis
        self.start_y = self.start_y + y_axis
        self.end_x = self.end_x + x_axis
        self.end_y = self.end_y + y_axis
 
