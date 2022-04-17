from  ElementType import ElementType

class Element:
    def __init__(self, w, h, p, image_draw):
        self.h = h
        self.w = w
        self.p = p
        self.image_draw = image_draw
        self.x = None
        self.y = None
        self.type = ElementType.Element



    def set_place(self, x, y):
        self.x = x
        self.y = y


    def draw(self):
        x = self.x
        y = self.y
        self.image_draw.line((x, y, x + self.p, y), fill=(0, 0, 0), width=2 )
        self.image_draw.line((x + self.p + self.w, y, x + self.p + self.p + self.w, y), fill=(0, 0, 0), width=2)
        self.image_draw.rectangle((x + self.p, y - int(0.5 * self.h), x + self.p + self.w, y + int(0.5 * self.h)), outline=(0, 0, 0), width=2)

    def get_input_point(self):
        return self.x, self.y

    def get_output_point(self):
        return self.x + 2 * self.p + self.w, self.y

    def get_w_size(self):
        return self.w + 2 * self.p

    def get_h_size(self):
        return self.h