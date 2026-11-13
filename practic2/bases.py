from models import EntityInterface, Position
from stats import InstanceCounter 
import units

class Base(EntityInterface):
    def __init__(self, name):
        InstanceCounter.__init__(self)
        super().__init__(name, 100, 0, "B", "\033[31m", range_=0)
        self.my_units = []
        self.max_units = 10
        self.gold = 50
        self.unit_limits = {
            "Warrior": 3, "Guard": 3,
            "Archer": 3, "Marksman": 3,
            "Rider": 2, "Lancer": 2
        }
        self.unit_counts = {k: 0 for k in self.unit_limits} # cловарь-счётчик текущих юнитов каждого типа

    def create_unit(self, unit_type_name, pos, field, silent=False):
        if len(self.my_units) >= self.max_units: # проверяет общий лимит юнитов
            if not silent:
                print("Лимит юнитов исчерпан!")
            return None
        if self.unit_counts.get(unit_type_name, 0) >= self.unit_limits.get(unit_type_name, 0):
            if not silent: print("Лимит типа исчерпан!")
            return None
        unit_class = getattr(units, unit_type_name, None)  # динамически получает класс юнита по имени
        if not unit_class:
            if not silent: print(f"Ошибка: класс {unit_type_name} не найден")
            return None
        new_unit = unit_class()
        new_unit.base = self
        if self.gold < 10:
            if not silent: print("Недостаточно золота!")
            return None
        new_unit.position = pos
        if field.add_entity(new_unit, pos):
            self.my_units.append(new_unit) # добавляет юнита в список базы
            self.unit_counts[unit_type_name] += 1
            self.gold -= 10
            if not silent:
                print(f"Создан {new_unit.name}. Золото: {self.gold}")
            return new_unit
        return None

    def remove_unit(self, dead_unit):
        if dead_unit in self.my_units: # проверяет действительно ли принадлежит к базе
            self.my_units.remove(dead_unit)
            class_name = type(dead_unit).__name__
            if class_name in self.unit_counts:
                self.unit_counts[class_name] -= 1
            print(f"{dead_unit.name} погиб.")

    def get_status(self):
        lines = [] # пустой список строк для вывода состояния
        lines.append(f"Золото: {self.gold}")
        lines.append(f"Войска: {len(self.my_units)}/{self.max_units}")
        lines.append("Состав:")
        types_map = {
            "Warrior": "Воины", "Guard": "Стражи",
            "Archer": "Стрелки", "Marksman": "Снайперы",
            "Rider": "Всадники", "Lancer": "Повозки"
        }
        for cls_name, ru_name in types_map.items(): # итерирует по парам (имя класса - русское название)
            count = self.unit_counts.get(cls_name, 0)
            limit = self.unit_limits.get(cls_name, 0)
            lines.append(f"  {ru_name}: {count}/{limit}")
        return "\n".join(lines)