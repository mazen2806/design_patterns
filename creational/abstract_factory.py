from __future__ import annotations
from abc import ABC, abstractmethod


# abstract products
class Chair(ABC):
    @abstractmethod
    def has_legs(self):
        pass

    @abstractmethod
    def sit_on(self):
        pass


class Table(ABC):
    @abstractmethod
    def has_legs(self):
        pass

    @abstractmethod
    def is_low(self):
        pass


class Sofa(ABC):
    @abstractmethod
    def is_corner_unit(self):
        pass

    @abstractmethod
    def get_size(self):
        pass


class VictorianChair(Chair):
    def __init(self):
        self.style = 'victorian_chair'

    def has_legs(self):
        return True

    def sit_on(self):
        return True


class VictorianCoffeeTable(Table):
    def __init(self):
        self.style = 'victorian_coffee_table'

    def has_legs(self):
        return True

    def is_low(self):
        return False


class VictorianSofa(Sofa):
    def __init(self):
        self.style = 'victorian_sofa'
        self.seater_cnt = 3

    def is_corner_unit(self):
        return False


class ModernChair(Chair):
    def __init__(self):
        self.style = 'modern_chair'

    def has_legs(self):
        return True

    def sit_on(self):
        return True


class ModernCoffeeTable(Table):
    def __init__(self):
        self.style = 'victorian_coffee_table'

    def has_legs(self):
        return True

    def is_low(self):
        return False


class ModernSofa(Sofa):
    def __init__(self):
        self.style = 'modern_sofa'
        self.seater_cnt = 4

    def is_corner_unit(self):
        return True

    def get_size(self):
        return self.seater_cnt


class FurnitureFactory(ABC):
    """
    Abstract Factory Design (AFD) pattern provides an interface for creating a group of related
    objects without specifying their concrete classes.
    """
    @abstractmethod
    def create_chair(self) -> Chair:
        pass

    @abstractmethod
    def create_coffee_table(self) -> Table:
        pass

    @abstractmethod
    def create_sofa(self) -> Sofa:
        pass


class VictorianFurnitureFactory(FurnitureFactory):
    def create_chair(self) -> VictorianChair:
        return VictorianChair()

    def create_coffee_table(self) -> VictorianCoffeeTable:
        return VictorianCoffeeTable()

    def create_sofa(self) -> VictorianSofa:
        return VictorianSofa()


class ModernFurnitureFactory(FurnitureFactory):
    def create_chair(self) -> VictorianChair:
        return VictorianChair()

    def create_coffee_table(self) -> VictorianCoffeeTable:
        return VictorianCoffeeTable()

    def create_sofa(self) -> VictorianSofa:
        return VictorianSofa()


def create_furniture(fabric: FurnitureFactory):
    return {
        "chair": fabric.create_chair(),
        "sofa": fabric.create_sofa(),
        "coffee_table": fabric.create_coffee_table(),
    }
