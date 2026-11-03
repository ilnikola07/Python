from models import EntityInterface, Position
from objects import NeutralObjectInterface
from stats import InstanceCounter  


class Unit(EntityInterface, InstanceCounter):
    
    def __init__(self, *args, **kwargs):
        # Инициализация счётчика и базового класса сущности
        InstanceCounter.__init__(self)
        EntityInterface.__init__(self, *args, **kwargs)
        self.is_alive = True  # Флаг жизни юнита

    def die(self, field=None, base=None):
        """Полное удаление юнита: с поля, из базы и из счётчика"""
        self.is_alive = False
        
        # Удаляем с поля
        if field and self.position:
            field.remove_entity(self.position)
        
        # Удаляем из списка юнитов базы
        if base and hasattr(base, 'units'):
            if self in base.units:
                base.units.remove(self)
        
        # Уменьшаем счётчик вручную
        class_name = self.__class__.__name__
        InstanceCounter._alive -= 1
        InstanceCounter._total_deleted += 1
        if class_name in InstanceCounter._class_stats:
            InstanceCounter._class_stats[class_name]["alive"] -= 1
            InstanceCounter._class_stats[class_name]["deleted"] += 1
        
        print(f"{self.name} погиб.")

    def move(self, new_pos, field):        
        if not field.is_valid_pos(new_pos): 
            print("За пределами карты!")
            return False
              
        entity_at_pos = field.get_entity_at(new_pos)  # есть ли на клетке объект
        if entity_at_pos:
            # если там нейтральный объект — разрешаем встать
            if isinstance(entity_at_pos, NeutralObjectInterface):
                self.position = new_pos
                return True
            else:
                print("Клетка занята!")
                return False
        
        # если объекта нет — проверяем ландшафт
        terrain = field.get_terrain(new_pos)
        if not terrain.passable:
            print(f"Нельзя пройти через {terrain.name}")
            return False
        
        self.position = new_pos
        return True


class Warrior(Unit):
    def __init__(self):
        super().__init__("Воин", 50, 10, "W", "\033[36m", range_=1)

class Guard(Unit):
    def __init__(self):
        super().__init__("Страж", 45, 12, "G", "\033[36m", range_=1)

class Archer(Unit):
    def __init__(self):
        super().__init__("Стрелок", 30, 15, "A", "\033[33m", range_=2)

class Marksman(Unit):
    def __init__(self):
        super().__init__("Снайпер", 35, 18, "S", "\033[33m", range_=3)

class Rider(Unit):
    def __init__(self):
        super().__init__("Всадник", 60, 8, "R", "\033[35m", range_=1)

class Lancer(Unit):
    def __init__(self):
        super().__init__("Повозка", 40, 14, "L", "\033[35m", range_=1)