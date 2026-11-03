class Position:
    def __init__(self, x, y): # конструктор класса
        self.x = x
        self.y = y

    def __eq__(self, other): # перегрузка оператора (сравнивает, если координаты х и у совпадают)
        return isinstance(other, Position) and self.x == other.x and self.y == other.y

    def __hash__(self): # делает объект Position хешируемым, что позволяет использовать его как ключ в словаре
        return hash((self.x, self.y))

    def __repr__(self): # определяет, как объект будет выглядеть при печати через print() или в отладчике.
        return f"({self.x},{self.y})"

    def distance_to(self, other): # используется для проверки находится ли цель в радиусе атаки
        return abs(self.x - other.x) + abs(self.y - other.y)


class EntityInterface:
    """Интерфейс для всех сущностей"""
    def __init__(self, name, hp, attack, symbol, color, range_=1):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.attack = attack
        self.symbol = symbol
        self.color = color
        self.range = range_  # дальность атаки/взаимодействия
        self.position = None
        self.base = None

    def take_damage(self, amount):
        self.hp -= amount
        if self.hp < 0:
            self.hp = 0
        return self.hp <= 0

    def __str__(self): # перегрузка  встроенной ф-и str, определяет как будет выглядеть при печати
        return f"{self.name} [Здороовье:{self.hp}/{self.max_hp} Урон:{self.attack} Дальность:{self.range}]"

    # перегрузка оператора - 
    def __sub__(self, target):
        dist = self.position.distance_to(target.position) if target.position else 999 # если у цели нет позиции (None) — подставляется 999, чтобы атака не прошла
        if dist <= self.range:
            print(f"\033[31m{self.name} атакует {target.name}! Нанесено {self.attack} урона.\033[0m")
            is_dead = target.take_damage(self.attack) # вызывает метод нанесения урона и узнаёт умерла ли цель
            if is_dead:
                print(f"\033[31m{target.name} уничтожен!\033[0m")
            return is_dead
        else:
            print(f"\033[33mЦель слишком далеко! (Дистанция: {dist}, Макс: {self.range})\033[0m")
            return False


class TerrainInterface:
    """Ландшафта"""
    def __init__(self, name, symbol, passable=True, color="\033[32m"):
        self.name = name
        self.symbol = symbol
        self.passable = passable # проходимость
        self.color = color


class NeutralObjectInterface:
    """Нейтральные объектов"""
    def __init__(self, name, symbol, color="\033[33m"):
        self.name = name
        self.symbol = symbol
        self.color = color