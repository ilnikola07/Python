import random
from models import Position
from terrain import Grass, Water, Mountain
from objects import HealthPotion, GoldCoin, Trap, Tree
from bases import Base
from units import Unit 
from stats import InstanceCounter 

RESET = "\033[0m" # константа для сброса цвета

class GameField:
    def __init__(self, width, height):

        InstanceCounter.__init__(self)
        
        self.width = width
        self.height = height
        self.grid = [[None for _ in range(width)] for _ in range(height)] # создаёт матрицу для хранения объектов ландшафта
        self.entities = {} # словарь для хранения сущностей
        
        for y in range(height):
            for x in range(width):
                r = random.random()
                if r < 0.85: # с вероятностью 85% клетка - трава
                    self.grid[y][x] = Grass()
                elif r < 0.95:
                    self.grid[y][x] = Water()  # с оставшейся вероятностью 10% клетка - вода
                else: 
                    self.grid[y][x] = Mountain() # остаток - горы
        
        self._place_neutrals() 

    def _place_neutrals(self): # размещение нейтральных объектов
        neutrals = [HealthPotion(), GoldCoin(), Trap(), Tree()]
        for _ in range(10): # размещает 10 нейтральных объектов на карте 
            attempts = 0
            while attempts < 50: # до 50 попыток найти подходящую клетку
                pos = Position(random.randint(0, self.width-1), random.randint(0, self.height-1))
                terrain = self.grid[pos.y][pos.x] # генерирует случайные координаты в пределах поля
                if terrain.passable and not self.get_entity_at(pos): # если ландшафт проходимый и пустая клетка
                    obj = random.choice(neutrals)
                    self.entities[pos] = obj
                    break
                attempts += 1

    def is_valid_pos(self, pos): # проверка границ поля
        return 0 <= pos.x < self.width and 0 <= pos.y < self.height

    def get_terrain(self, pos): # проверка ландшафта
        if self.is_valid_pos(pos): return self.grid[pos.y][pos.x]
        return None

    def get_entity_at(self, pos):
        return self.entities.get(pos)

    def add_entity(self, entity, pos):
        if self.is_valid_pos(pos) and pos not in self.entities:
            entity.position = pos
            self.entities[pos] = entity #записывает позицию в атрибут сущности (чтобы юнит "знал", где он находится)
            return True
        return False

    def remove_entity(self, pos): # удаление сущности
        if pos in self.entities:
            del self.entities[pos]

    def move_entity(self, entity, new_pos):
        old_pos = entity.position
        if entity.move(new_pos, self):
            obj = self.get_entity_at(new_pos)
            if obj:
                try:
                    obj + entity  # Ловушка наносит урон, но НЕ удаляет юнита
                
                # Проверяем смерть ПОСЛЕ взаимодействия 
                    if not entity.is_alive:
                    # Полное удаление юнита
                        entity.die(field=self, base=player_base)  # <-- передай свою базу
                        return False  # Юнит мёртв, не ставим на клетку
                
                    if isinstance(obj, (HealthPotion, GoldCoin)):
                        self.remove_entity(new_pos)
                except Exception as e:
                    print(f"Ошибка взаимодействия: {e}")
                    pass
        
        # Ставим на поле ТОЛЬКО живого юнита
            self.entities[new_pos] = entity
            if old_pos in self.entities and self.entities[old_pos] == entity:
                del self.entities[old_pos]
            return True
        return False

    def draw(self):
        CELL = 3
        print(" " * 4, end="")
        for x in range(self.width): 
            print(f"{x:>{CELL}}", end="") # печатает 4 пробела — отступ слева для номеров строк (чтобы верхняя координатная строка выравнивалась по колонкам)
        print()
        
        for y in range(self.height): # цикл по строкам поля
            print(f"{y:3} ", end="")# печатает номера столбцов, каждый выровнен по правому краю в поле шириной 3 символа
            for x in range(self.width): 
                pos = Position(x, y)
                ent = self.get_entity_at(pos)
                if ent: # если сущность есть — печатает её символ в её цвете
                    print(f" {ent.color}{ent.symbol}{RESET} ", end="")
                else:
                    terrain = self.grid[y][x]
                    print(f" {terrain.color}{terrain.symbol}{RESET} ", end="")
            print(f"{y}")
        
        print(" " * 4, end="")
        for x in range(self.width): print(f"{x:>{CELL}}", end="") # печать координат снизу
        print()


def print_legend():
    print("\nЛЕГЕНДА ")
    print("Юниты:      W-Воин  G-Страж  A-Стрелок  S-Снайпер  R-Всадник  L-Повозка")
    print("Объекты:    +-Аптечка  $-Золото  x-Ловушка  T-Дерево")
    print("Ландшафт:   .-Трава  ~-Вода  ^-Горы")
    print(" \n")


def main():
    width, height = 15, 15
    field = GameField(width, height) # экземпляр класса поля
    
    player_base = Base(" ")
    base_pos = Position(1, 1)
    field.add_entity(player_base, base_pos) # размещает баз на поле
    
    print("Консольная стратегия \n")
    
    while True:
        field.draw()
        print_legend()
        
        print("ГЛАВНОЕ МЕНЮ ")
        print("1 - Управление базой")
        print("2 - Управление юнитом")
        print("3 - Состояние базы")
        print("4 - Выход")


        stats = InstanceCounter.get_stats()
        print(f"\n[Всего создано: {stats['total_created']} | текущие: {stats['alive']} | удаленные: {stats['total_deleted']}]")
        print("[По классам:]")
        for class_name, class_stats in stats['by_class'].items():
            print(f"  {class_name}: создано={class_stats['created']}, текущие={class_stats['alive']}, удаленные={class_stats['deleted']}")
        
        choice = input("\nВыбор: ").strip()# считывает выбор пользователя с клавиатуры
        
        if choice == "1":
            print("\nУправление базой ")
            print("1 - Создать юнита (10 золота)")
            print("2 - Назад")
            sub = input("Выбор: ").strip()
            
            if sub == "1":
                print("\nДоступные типы:")
                print("1 - Воин (Здоровье:50, Урон:10, Дальноость:1)")
                print("2 - Страж (Здоровье:45, Урон:12, Дальноость:1)")
                print("3 - Стрелок (Здоровье:30, Урон:15, Дальноость:2)")
                print("4 - Снайпер (Здоровье:35, Урон:18, Дальноость:3)")
                print("5 - Всадник (Здоровье:60, Урон:8, Дальноость:1)")
                print("6 - Повозка (Здоровье:40, Урон:14, Дальноость:1)")
                
                t_map = {"1":"Warrior","2":"Guard","3":"Archer","4":"Marksman","5":"Rider","6":"Lancer"}
                t_choice = input("Тип: ").strip() # считывает номер выбранного юнита
                
                if t_choice in t_map:
                    spawn_pos = Position(base_pos.x + 1, base_pos.y) # вычисляет позицию спавна
                    if not field.get_entity_at(spawn_pos):
                        # вызывает метод базы для создания юнита, передаёт имя класса, позицию и поле, проверяет золото, лимиты, создаёт экземпляр класса и добавляет его на поле
                        new_u = player_base.create_unit(t_map[t_choice], spawn_pos, field)
                        if new_u:
                            print(f"Юнит {new_u.name} создан и готов к бою!")
                    else:
                        print("Клетка рядом с базой занята! Освободите её или переместите юнитов.")
                else:
                    print("Неверный выбор.")
                    
        elif choice == "2":
            units_list = player_base.my_units #получает список всех юнитов, принадлежащих базе
            if not units_list:
                print("\nНет юнитов! Создайте их через меню базы.")
                continue
                
            print("\nВыберите юнита ")
            for i, u in enumerate(units_list):
                print(f"{i+1}. {u} на {u.position}") # выводит список юнитов
            
            try:
                u_idx = int(input("Номер юнита: ")) - 1
                if 0 <= u_idx < len(units_list):
                    active_unit = units_list[u_idx]
                    
                    while True:
                        field.draw()
                        print_legend()

                        print(f"\nУправление: {active_unit.name} ")
                        print("1 - Переместить")
                        print("2 - Атаковать")
                        print("3 - Состояние")
                        print("4 - Назад в меню юнитов")
                        
                        act = input("Действие: ").strip()
                        
                        if act == "1":
                            print("Направления: 1-Вверх 2-Вниз 3-Влево 4-Вправо")
                            d = input("Куда: ").strip()
                            x, y = active_unit.position.x, active_unit.position.y
                            if d=="1": y-=1
                            elif d=="2": y+=1
                            elif d=="3": x-=1
                            elif d=="4": x+=1
                            
                            field.move_entity(active_unit, Position(x, y))
                            if active_unit.hp <= 0:
                                player_base.remove_unit(active_unit)
                                break
                                
                        elif act == "2":
                            # поиск целей в радиусе: вражеские юниты (нету) + деревья
                            targets = []
                            for e_pos, e in field.entities.items():
                                if e == active_unit:
                                    continue
                                if active_unit.position.distance_to(e_pos) <= active_unit.range:
                                    if isinstance(e, Unit):
                                        targets.append((e_pos, e, "unit"))
                                    elif isinstance(e, Tree):
                                        targets.append((e_pos, e, "tree"))
                            
                            if not targets:
                                print("Нет целей в радиусе атаки!")
                            else:
                                print("Доступные цели:")
                                for i, (pos, t, ttype) in enumerate(targets):
                                    if ttype == "unit":
                                        print(f"{i+1}. {t} на {pos} [Враг]")
                                    else:
                                        print(f"{i+1}. {t.name} на {pos} [Дерево]")
                                try:
                                    t_idx = int(input("Цель: ")) - 1
                                    target_pos, target, ttype = targets[t_idx]
                                    if ttype == "unit":
                                        is_dead = active_unit - target
                                        if is_dead:
                                            player_base.remove_unit(target)
                                            field.remove_entity(target_pos)
                                    else:
                                        field.remove_entity(target_pos)
                                        print(f"\033[32m{active_unit.name} срубил дерево!\033[0m")
                                except (ValueError, IndexError):
                                    print("Ошибка выбора цели.")
                                
                        elif act == "3":
                            print(f"\nИмя: {active_unit.name}")
                            print(f"Здоровье: {active_unit.hp}/{active_unit.max_hp}")
                            print(f"Атака: {active_unit.attack}")
                            print(f"Дальность: {active_unit.range}")
                            print(f"Позиция: {active_unit.position}")
                            input("Enter...")
                            
                        elif act == "4":
                            break
                else:
                    print("Неверный номер.")
            except ValueError:
                print("Введите число!")
                
        elif choice == "3":
            print("\n" + player_base.get_status())
            input("\nНажмите Enter...")
            
        elif choice == "4":
            print("Игра завершена.")
            break
            
        else:
            print("Неверная команда.")

if __name__ == "__main__": #если файл запущен напрямую (а не импортирован как модуль), вызывается функция main()
    main()