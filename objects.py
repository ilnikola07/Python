from models import NeutralObjectInterface
from stats import InstanceCounter

class HealthPotion(NeutralObjectInterface):
    def __init__(self):
        InstanceCounter.__init__(self)
        super().__init__("Аптечка", "+", "\033[31m")
    
    def __add__(self, unit):
        heal = 20
        unit.hp = min(unit.hp + heal, unit.max_hp) # увеличивает здоровье, но не больше возможного
        print(f"\033[31m{unit.name} использовал аптечку. HP +{heal}\033[0m")
        return unit

class GoldCoin(NeutralObjectInterface):
    def __init__(self):
        InstanceCounter.__init__(self)
        super().__init__("Золото", "$", "\033[33m")
    
    def __add__(self, unit):
        amount = 10  # сколько золота даёт монета
        if unit.base is not None:
            unit.base.gold += amount
            print(f"\033[33m{unit.name} собрал золото! +{amount} в казну (всего: {unit.base.gold})\033[0m")
        else:
            print(f"\033[33m{unit.name} собрал золото!\033[0m")
        return unit

class Trap(NeutralObjectInterface):
    def __init__(self):
        InstanceCounter.__init__(self)
        super().__init__("Ловушка", "x", "\033[35m")
    
    def __add__(self, unit):
        dmg = 30
        is_dead = unit.take_damage(dmg)
        print(f"\033[35m{unit.name} наступил в ловушку! -{dmg} HP\033[0m")
        if is_dead:
            print(f"\033[31m{unit.name} погиб от ловушки!\033[0m")
            # Передаём field и base, если они доступны
            # Если нет — придётся менять сигнатуру __add__ или передавать через unit
            unit.die()  
        return unit

class Tree(NeutralObjectInterface):
    def __init__(self):
        InstanceCounter.__init__(self)
        super().__init__("Дерево", "T", "\033[32m")
    def __add__(self, unit):
        print(f"\033[32m{unit.name} прошел мимо дерева.\033[0m")
        return unit