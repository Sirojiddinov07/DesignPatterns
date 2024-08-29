from abc import ABC, abstractmethod

class House:
    def __init__(self):
        self.walls = None
        self.roof = None
        self.windows = None
        self.doors = None

    def __str__(self):
        return f"House with {self.walls} walls, {self.roof} roof, {self.windows} windows, and {self.doors} doors."



class HouseBuilder(ABC):
    @abstractmethod
    def build_walls(self):
        pass

    @abstractmethod
    def build_roof(self):
        pass

    @abstractmethod
    def build_windows(self):
        pass

    @abstractmethod
    def build_doors(self):
        pass

    @abstractmethod
    def get_house(self) -> House:
        pass


class WoodenHouseBuilder(HouseBuilder):
    def __init__(self):
        self.house = House()

    def build_walls(self):
        self.house.walls = "Wooden"

    def build_roof(self):
        self.house.roof = "Wooden"

    def build_windows(self):
        self.house.windows = "Wooden framed"

    def build_doors(self):
        self.house.doors = "Wooden"

    def get_house(self) -> House:
        return self.house


class GlassHouseBuilder(HouseBuilder):
    def __init__(self):
        self.house = House()

    def build_walls(self):
        self.house.walls = "Glass"

    def build_roof(self):
        self.house.roof = "Glass"

    def build_windows(self):
        self.house.windows = "Glass framed"

    def build_doors(self):
        self.house.doors = "Glass"

    def get_house(self) -> House:
        return self.house


class HouseDirector:
    def __init__(self, builder: HouseBuilder):
        self.builder = builder

    def construct_house(self):
        self.builder.build_walls()
        self.builder.build_roof()
        self.builder.build_windows()
        self.builder.build_doors()

    def get_house(self) -> House:
        return self.builder.get_house()


# Building a wooden house
wooden_builder = WoodenHouseBuilder()
director = HouseDirector(wooden_builder)
director.construct_house()
wooden_house = director.get_house()
print(wooden_house)

# Building a glass house
glass_builder = GlassHouseBuilder()
director = HouseDirector(glass_builder)
director.construct_house()
glass_house = director.get_house()
print(glass_house)
