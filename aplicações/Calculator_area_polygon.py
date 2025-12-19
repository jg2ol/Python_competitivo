# Calculadora de áreas (e outras medidas) de retângulos e quadrados

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def set_width(self, new_width):
        self.width = new_width
    
    def set_height(self, new_height):
        self.height = new_height
    
    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return 2 * (self.width + self.height)
    
    def get_diagonal(self):
        return (self.width**2 + self.height**2)**(0.5)
    
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        return ("*"*self.width + "\n")*self.height
    
    def get_amount_inside(self, other):
        return self.width//other.width * self.height//other.height
    
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

class Square(Rectangle):
    def __init__(self, comp):
        self.width = comp
        self.height = comp
    
    def set_width(self, comp):
        self.width = comp
        self.height = comp
    def set_height(self, comp):
        self.width = comp
        self.height = comp
    def set_side(self, comp):
        self.width = comp
        self.height = comp
    
    def __str__(self):
        return f"Square(side={self.width})"

rec = Rectangle(3, 6)
print(rec)
print(rec.get_picture())
rec.set_width(4)
rec.set_height(5)
print(rec)
print(rec.get_picture())

sq = Square(4)
print(sq)
print(sq.get_picture())
sq.set_height(2)
print(sq)
print(sq.get_picture())
sq.set_side(5)
print(sq)
print(sq.get_picture())
sq.set_side(52)
print(sq)
print(sq.get_picture())
