from  ElementType import ElementType

class SerialConnection:
    def __init__(self, elements):
        self.elements = elements
        self.x = None
        self.y = None
        self.type = ElementType.SerialConnection

    def set_place(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        self.elements[0].set_place(self.x, self.y)
        for i in range(1, len(self.elements)):
            self.elements[i].set_place(*self.elements[i-1].get_output_point())
        for element in self.elements:
            element.draw()


    def get_input_point(self):
        return self.x, self.y

    def get_output_point(self):
        return self.elements[-1].get_output_point()

    def get_w_size(self):
        w_size = 0
        for element in self.elements:
            w_size += element.get_w_size()
        return w_size

    def get_h_size(self):
        max_h = 0
        for element in self.elements:
            if (max_h < element.get_h_size()):
                max_h = element.get_h_size()
        return max_h