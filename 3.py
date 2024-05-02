import math


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to_point(self, other_point):
        distance = math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)
        return distance

    def get_coordinates(self):
        return self.x, self.y

    def set_coordinates(self, x, y):
        self.x = x
        self.y = y


point1 = Point(1, 2)
point2 = Point(5, 7)

print('Координаты точки point1: {}'.format(point1.get_coordinates()))
print('Координаты точки point2: {}'.format(point2.get_coordinates()))

distance = point1.distance_to(point2)
print('Расстояние от точки point1 до точки point2: {}'.format(distance))

point1.set_coordinates(3, 5)
print('Новые координаты точки point1: {}'.format(point1.get_coordinates()))
