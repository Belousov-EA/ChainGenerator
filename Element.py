from  ElementType import ElementType
from PIL import ImageFont

class Element:
    def __init__(self, w, h, p):
        self.h = h
        self.w = w
        self.p = p
        self.image_draw = None
        self.x = None
        self.y = None
        self.type = ElementType.Element
        self.number = None
        self.exponent_param = None
        self.weibull_param_a = None
        self.weibull_param_b = None

    def set_image_draw(self, image_draw):
        self.image_draw = image_draw



    def set_place(self, x, y):
        self.x = x
        self.y = y


    def draw(self):
        x = self.x
        y = self.y
        self.image_draw.line((x, y, x + self.p, y), fill=(0, 0, 0), width=2 )
        self.image_draw.line((x + self.p + self.w, y, x + self.p + self.p + self.w, y), fill=(0, 0, 0), width=2)
        self.image_draw.rectangle((x + self.p, y - int(0.5 * self.h), x + self.p + self.w, y + int(0.5 * self.h)), outline=(0, 0, 0), width=2)
        font = ImageFont.truetype('arial.ttf', self.h - 2)
        if self.number < 10:
            font_padding = (x + self.p + x + self.p + self.w)//2 - 5
        else:
            font_padding = (x + self.p + 10)
        self.image_draw.text((font_padding, y - int(0.5 * self.h)), str(self.number), fill=(0, 0, 0), font=font)

    def get_input_point(self):
        return self.x, self.y

    def get_output_point(self):
        return self.x + 2 * self.p + self.w, self.y

    def get_w_size(self):
        return self.w + 2 * self.p

    def get_h_size(self):
        return self.h

    def set_info(self, numered, exponent_param, weibull_param_a, weibull_param_b):
        self.number = numered
        self.exponent_param = exponent_param
        self.weibull_param_a = weibull_param_a
        self.weibull_param_b = weibull_param_b