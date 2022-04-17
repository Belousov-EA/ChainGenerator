import random
from  ElementType import ElementType

from Element import Element
from SerialConnection import SerialConnection
from ParallelConnection import ParallelConnection
from PIL import Image
from PIL import ImageDraw
import math

class Chain:
    def __init__(self, image_size,
                 element_width, element_height, element_padding,
                 parallel_padding,
                 input_point):
        self.image_size = image_size
        self.element_width = element_width
        self.element_height = element_height
        self.element_padding = element_padding
        self.parallel_padding = parallel_padding
        self.input_point = input_point


    def create_chain(self, max_elements, one_max):
        image = Image.new("RGB", self.image_size, color=(255, 255, 255))
        draw = ImageDraw.Draw(image)

        if random.randint(0, 1) == 0:
            element = SerialConnection([])
            for j in range(random.randint(2, one_max)):
                element.elements.append(Element(self.element_width, self.element_height, self.element_padding, draw))
        else:
            element = ParallelConnection([], self.parallel_padding, draw)
            for j in range(random.randint(2, one_max)):
                element.elements.append(Element(self.element_width, self.element_height, self.element_padding, draw))

        elements_count = self.get_element_number(element)
        while elements_count < max_elements:
            self.change_element(element, random.randint(0, elements_count - 1), random.randint(2, min(max_elements - elements_count + 1, one_max)), draw)
            elements_count = self.get_element_number(element)
        element.set_place(*self.input_point)
        element.draw()
        return image


    def change_element(self, element, element_number, max_elements, draw):
        for i in range( len( element.elements )):
            if element.elements[i].type == ElementType.Element:
                if element_number == 0:
                    element_number -= 1
                    if element.type == ElementType.SerialConnection:
                        element.elements[i] = ParallelConnection([], self.parallel_padding, draw)
                        for j in range(max_elements):
                            element.elements[i].elements.append(Element(self.element_width, self.element_height, self.element_padding, draw))
                    if element.type == ElementType.ParallelConnection:
                        element.elements[i] = SerialConnection([])
                        for j in range(max_elements):
                            element.elements[i].elements.append(Element(self.element_width, self.element_height, self.element_padding, draw))
                else:
                    element_number -= 1
            else:
                element_number = self.change_element(element.elements[i], element_number, max_elements, draw)
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