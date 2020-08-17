class Vec:
    """A simple vector in 2D. Also used as a position vector for points"""
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __add__(self, other):
        return Vec(self.x + other.x, self.y + other.y)
        
    def __sub__(self, other):
        return Vec(self.x - other.x, self.y - other.y)
        
    def dot(self, other):
        return self.x * other.x + self.y * other.y
        
    def lensq(self):
        return self.dot(self)

    def __str__(self):
        return "({}, {})".format(self.x, self.y)
        
def is_ccw(a, b, c):
    """True iff triangle abc is counter-clockwise"""
    p = b - a
    q = c - a
    area = p.x * q.y - q.x * p.y
	 # May want to throw an exception if area == 0
    return area > 0

p = Vec(0, 0)
angus = Vec(100, 0)
erica = Vec(50, 50)
erica_is_left_of_angus = is_ccw(p, angus, erica)
print(erica_is_left_of_angus)

p = Vec(100, 200)
angus = Vec(-100, 0)
erica = Vec(0, 0)
erica_is_left_of_angus = is_ccw(p, angus, erica)
print(erica_is_left_of_angus)

p = Vec(0, 0)
angus = Vec(50, 50)
erica = Vec(100, 0)
erica_is_left_of_angus = is_ccw(p, angus, erica)
print(erica_is_left_of_angus)