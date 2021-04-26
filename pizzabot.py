import re
import sys
from copy import copy


class PizzaBotDelivering:
    MOVE_NORTH = 'N'
    MOVE_SOUTH = 'S'
    MOVE_EAST = 'E'
    MOVE_WEST = 'W'
    DROP_PIZZA = 'D'
    current_point = (0, 0)

    def __init__(self, input_string):
        self.area_size = self.get_area_size(input_string)
        self.points = self.get_delivery_points(input_string)
        self.validate()

    @staticmethod
    def get_area_size(input_string):
        reg_exp = r'^([\w]+)x([\w]+)'
        return [
            (int(size[0]), int(size[1])) for size
            in re.findall(reg_exp, input_string)
        ]

    @staticmethod
    def get_delivery_points(input_string):
        reg_exp = r'([-]?[\w]*)\s*\,\s*([-]?[\w]*)'
        return [
            (int(point[0]), int(point[1])) for point
            in re.findall(reg_exp, input_string)
        ]

    def validate(self):
        if not self.area_size:
            raise ValueError("Area size hasn't been detected")
        if not self.points:
            raise ValueError("No one delivery point has been found")

        area = self.area_size[0]
        for point in self.points:
            if any([
                point[0] < 0,
                point[1] < 0,
                point[0] > area[0],
                point[1] > area[1],
            ]):
                raise ValueError("\"%s\" point is out of area range. Please correct" % str(point))

    def sort_by_distance(self, points):
        curr = self.current_point
        return sorted(
            points,
            key=lambda p: (
                abs(p[0] - curr[0]) + abs(p[1] - curr[1]),  # getting total count of steps
                abs(p[0] - curr[0]),  # getting x-based order if steps are same
            )
        )

    def get_road_map(self, points=None):
        points = copy(self.points) if points is None else points
        if not points:
            return ''
        points = self.sort_by_distance(points)
        next_point = points.pop(0)
        x = next_point[0] - self.current_point[0]
        y = next_point[1] - self.current_point[1]

        road_map = abs(x)*(self.MOVE_EAST if x > 0 else self.MOVE_WEST)
        road_map += abs(y)*(self.MOVE_NORTH if y > 0 else self.MOVE_SOUTH)
        road_map += self.DROP_PIZZA

        self.current_point = next_point
        return road_map+self.get_road_map(points)


def pizzabot(input_string):
    return PizzaBotDelivering(input_string).get_road_map()


if __name__ == "__main__":
    try:
        print(pizzabot(sys.argv[-1]))
    except ValueError as e:
        message = "Please check your input. Example: ./pizzabot \"5x5 (1,2) (4, 4)\""
        print("You've got an error: %s" % e)
        print(message)
