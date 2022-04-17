from  ElementType import ElementType

class ParallelConnection:
    def __init__(self, elements, padding, image_draw):
        self.elements = elements
        self.p = padding
        self.image_draw = image_draw
        self.x = None
        self.y = None
        self.type = ElementType.ParallelConnection

    def set_place(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        height = self.get_h_size() - self.elements[0].get_h_size()//2 - self.elements[-1].get_h_size()//2
        self.elements[0].set_place(self.x + self.p * 2, self.y - height // 2)
        for i in range(1, len(self.elements)):
            self.elements[i].set_place(self.x + self.p * 2,
                                       self.elements[i-1].get_input_point()[1] +
                                       self.elements[i].get_h_size()//2 +
                                       self.elements[i-1].get_h_size()//2 + self.p)

        self.image_draw.line((self.x, self.y, self.x + self.p, self.y),
                             fill=(0, 0, 0), width=2)
        self.image_draw.line((self.x + self.p, self.y + height//2,
                              self.x + self.p, self.y - height//2),
                             fill=(0, 0, 0), width=2)
        self.image_draw.line((self.x + self.get_w_size() - self.p, self.y + height//2,
                              self.x + self.get_w_size() - self.p, self.y - height//2),
                             fill=(0, 0, 0), width=2)
        self.image_draw.line((self.x + self.get_w_size() - self.p, self.y,
                              self.x + self.get_w_size(), self.y), fill=(0, 0, 0), width=2)

        for element in self.elements:
            element.draw()
            self.image_draw.line((self.x + self.p, element.get_input_point()[1],
                                  self.x+self.p * 2, element.get_input_point()[1]),
                                 fill=(0, 0, 0), width=2)
            self.image_draw.line(
                (element.get_output_point()[0], element.get_output_point()[1],
                 self.x + self.get_w_size() - self.p, element.get_output_point()[1]),
                fill=(0, 0, 0), width=2)


    def get_input_point(self):
        return self.x, self.y

    def get_output_point(self):
        return self.x + self.get_w_size(), self.y

    def get_w_size(self):
        max_w = 0
        for element in self.elements:
            if max_w < element.get_w_size():
                max_w = element.get_w_size()
        return max_w + self.p * 4

    def get_h_size(self):
        height = 0
        for element in self.elements:
            height += element.get_h_size()
            height += self.p
        height -= self.p    # delete last
        return height