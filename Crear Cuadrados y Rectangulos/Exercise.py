class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def __repr__(self):
        return "Rectangle(width={}, height={})".format(self.width, self.height)

    def get_picture(self):
        line = ""
        if self.height > 50 or self.width > 50:
            return "Too big for picture."

        else:
            for i in range(self.height):
                if i != range(self.height):
                    for y in range(self.width):
                        line = line + "*"
                        y += y
                    line = line + "\n"
                    i += i
                else:
                    for y in range(self.width):
                        line = line + "*"
                        y += y
                    i += i
            return line

    def get_amount_inside(self, shape):
        new_area = shape.width * shape.height
        old_area = self.get_area()
        return int(old_area / new_area)


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def set_side(self, side):
        self.width = side
        self.height = side

    def __repr__(self):
        return "Square(side={})".format(self.width)

rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))











