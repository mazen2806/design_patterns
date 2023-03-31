# The Builder  is a creational pattern that separates the construction of an object from its representation,
#  allowing for greater flexibility in the construction process.
class House:
    def __init__(self):
        self.basement = None
        self.roof = None
        self.doors = None
        self.walls = None
        self.windows = None

    def __str__(self):
        return f"Basement: {self.basement} Walls: {self.walls} Windows: {self.windows} Doors: {self.doors} Roof: {self.roof}"


class HouseBuilder:
    def __init__(self, house):
        self.house = house

    def build_basement(self, basement):
        self.house.basement = basement

    def build_walls(self, walls):
        self.house.walls = walls

    def build_doors(self, doors):
        self.house.doors = doors

    def build_windows(self, windows):
        self.house.windows = windows

    def build_roof(self, roof):
        self.house.roof = roof

    def get_result(self):
        return self.house


if __name__ == "__main__":
    house = House()
    house_builder = HouseBuilder(house)
    house_builder.build_basement(1)
    house_builder.build_walls(4)
    house_builder.build_doors(5)
    house_builder.build_windows(5)
    house_builder.build_roof(5)

    result = house_builder.get_result()

    print(result)
