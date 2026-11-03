from models import TerrainInterface
from stats import InstanceCounter


class Grass(TerrainInterface, InstanceCounter):
    def __init__(self):
        InstanceCounter.__init__(self)
        super().__init__("Трава", ".", True, "\033[32m")


class Water(TerrainInterface, InstanceCounter):
    def __init__(self):
        InstanceCounter.__init__(self)
        super().__init__("Вода", "~", False, "\033[34m")


class Mountain(TerrainInterface, InstanceCounter):
    def __init__(self):
        InstanceCounter.__init__(self)
        super().__init__("Горы", "^", False, "\033[37m")