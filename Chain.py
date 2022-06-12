import random
from  ElementType import ElementType

from Element import Element
from SerialConnection import SerialConnection
from ParallelConnection import ParallelConnection
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from random import uniform

class Chain:
    def __init__(self, element_width, element_height, element_padding,
                 parallel_padding):
        self.element_width = element_width
        self.element_height = element_height
        self.element_padding = element_padding
        self.parallel_padding = parallel_padding
        self.exp_params = None
        self.weibull_params_a = None
        self.weibull_params_b = None


    def create_chain(self, max_elements, one_max, variant,
                     exp_min, exp_max,
                     weibull_a_min, weibull_a_max,
                     weibull_b_min, weibull_b_max,
                     time_min, time_max):
        self.exp_params = {}
        self.weibull_params_a = {}
        self.weibull_params_b = {}

        self.exp_min = exp_min
        self.exp_max = exp_max
        self.weibull_a_min = weibull_a_min
        self.weibull_a_max = weibull_a_max
        self.weibull_b_min = weibull_b_min
        self.weibull_b_max = weibull_b_max

        count_time = uniform(time_min, time_max)

        if random.randint(0, 1) == 0:
            element = SerialConnection([])
            for j in range(random.randint(2, one_max)):
                element.elements.append(Element(self.element_width, self.element_height, self.element_padding))
        else:
            element = ParallelConnection([], self.parallel_padding)
            for j in range(random.randint(2, one_max)):
                element.elements.append(Element(self.element_width, self.element_height, self.element_padding))

        elements_count = self.get_element_number(element)
        while elements_count < max_elements:
            self.change_element(element, random.randint(0, elements_count - 1), random.randint(2, min(max_elements - elements_count + 1, one_max)))
            elements_count = self.get_element_number(element)

        self.set_element_info(element, 1)
        exponent_caption = 'exponent ' + str(self.exp_params)[1:-1]
        weibull_a_caption = 'weibull a ' + str(self.weibull_params_a)[1:-1]
        weibull_b_caption = 'weibull b ' + str(self.weibull_params_b)[1:-1]
        font = ImageFont.truetype('arial.ttf', 14)

        font_width = max(font.getsize(exponent_caption)[0], font.getsize(weibull_a_caption)[0], font.getsize(weibull_b_caption)[0])
        image_width = max(element.get_w_size()+100, font_width+20)


        image = Image.new("RGB", (image_width, element.get_h_size()+215), color=(255, 255, 255))
        draw = ImageDraw.Draw(image)

        element.set_place(10, element.get_h_size()//2 + 60 )
        element.set_image_draw(draw)
        element.draw()

        variant_caption = 'Вариант {}'.format(variant)
        draw.text(((image_width - font.getsize(variant_caption)[0])//2, 1), variant_caption, fill=(0, 0, 0), font=font)
        draw.text((10, element.get_h_size()+110), exponent_caption, fill=(0, 0, 0), font=font)
        draw.text((10, element.get_h_size() + 125), weibull_a_caption, fill=(0, 0, 0), font=font)
        draw.text((10, element.get_h_size() + 140), weibull_b_caption, fill=(0, 0, 0), font=font)
        draw.text((10, element.get_h_size() + 155), 'Время рассчета = {}'.format(round(count_time, 5)), fill=(0, 0, 0), font=font)
        draw.text((10, element.get_h_size() + 185), 'Ответ {} exp = {}'.format(variant, round(element.exp_count(count_time), 5)), fill=(0, 0, 0), font=font)
        draw.text((10, element.get_h_size() + 200), 'Ответ {} weibull = {}'.format(variant, round(element.weibull_count(count_time), 5)), fill=(0, 0, 0), font=font)
        return image


    # setted numbers for elements, params for distributions
    def set_element_info(self, element, numered):
        if element.type == ElementType.Element:
            exponent_param = uniform(self.exp_min, self.exp_max)
            weibull_param_a = uniform(self.weibull_a_min, self.weibull_a_max)
            weibull_param_b = uniform(self.weibull_b_min, self.weibull_b_max)

            self.exp_params[numered] = round(exponent_param, 5)
            self.weibull_params_a[numered] = round(weibull_param_a, 5)
            self.weibull_params_b[numered] = round(weibull_param_b, 5)

            element.set_info(numered, exponent_param, weibull_param_a, weibull_param_b)
            return numered + 1
        else:
            for e in element.elements:
                numered = self.set_element_info(e, numered)
            return numered


    def change_element(self, element, element_number, max_elements):
        for i in range( len( element.elements )):
            if element.elements[i].type == ElementType.Element:
                if element_number == 0:
                    element_number -= 1
                    if element.type == ElementType.SerialConnection:
                        element.elements[i] = ParallelConnection([], self.parallel_padding)
                        for j in range(max_elements):
                            element.elements[i].elements.append(Element(self.element_width, self.element_height, self.element_padding))
                    if element.type == ElementType.ParallelConnection:
                        element.elements[i] = SerialConnection([])
                        for j in range(max_elements):
                            element.elements[i].elements.append(Element(self.element_width, self.element_height, self.element_padding))
                else:
                    element_number -= 1
            else:
                element_number = self.change_element(element.elements[i], element_number, max_elements)
        return element_number


    def get_element_number(self, element):
        if element.type == ElementType.Element:
            return 1
        else:
            sum = 0
            for e in element.elements:
                sum += self.get_element_number(e)
            return sum

    def some_draw(self):
        image = Image.new("RGB", self.image_size, color=(255, 255, 255))
        draw = ImageDraw.Draw(image)

        test_element1 = Element(self.element_width, self.element_height, self.element_padding, draw)
        test_element2 = Element(self.element_width, self.element_height, self.element_padding, draw)
        test_element3 = Element(self.element_width, self.element_height, self.element_padding, draw)
        test_element4 = Element(self.element_width, self.element_height, self.element_padding, draw)

        conn1 = ParallelConnection([test_element1, test_element2], self.parallel_padding, draw)

        conn2 = SerialConnection([conn1, test_element3])

        conn3 = ParallelConnection([conn2, test_element4], self.parallel_padding, draw)

        self.change_element(conn3, 2, 5, draw)

        conn3.set_place(*self.input_point)
        conn3.draw()

        #print(self.get_element_number(conn3))

        return image