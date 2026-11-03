# stats.py
import json
import os


class InstanceCounter:

    # общие счётчики
    _total_created = 0
    _alive = 0
    _total_deleted = 0
    
    # счётчики по конкретным классам
    _class_stats = {}  # {имя_класса: {"created": N, "alive": N, "deleted": N}}
    
    _filepath = "instances.json"

    def __init__(self):
        class_name = self.__class__.__name__ # получает имя класса
        InstanceCounter._total_created += 1
        InstanceCounter._alive += 1
        
        if class_name not in InstanceCounter._class_stats:
            InstanceCounter._class_stats[class_name] = {"created": 0, "alive": 0, "deleted": 0}
        InstanceCounter._class_stats[class_name]["created"] += 1
        InstanceCounter._class_stats[class_name]["alive"] += 1

    def __del__(self): # магический метод, используется когда объект удаляется из памяти
        class_name = self.__class__.__name__
        InstanceCounter._alive -= 1
        InstanceCounter._total_deleted += 1
        
        if class_name in InstanceCounter._class_stats:
            InstanceCounter._class_stats[class_name]["alive"] -= 1
            InstanceCounter._class_stats[class_name]["deleted"] += 1

    @classmethod
    def get_stats(cls):
        return {
            "total_created": cls._total_created,
            "alive": cls._alive,
            "total_deleted": cls._total_deleted,
            "by_class": dict(cls._class_stats)  
        }

    # @classmethod
    # def save_to_json(cls, filepath=None):
    #     filepath = filepath or cls._filepath
    #     data = cls.get_stats()
    #     with open(filepath, "w", encoding="utf-8") as f:
    #         json.dump(data, f, ensure_ascii=False, indent=2)

    # @classmethod
    # def load_from_json(cls, filepath=None):
    #     filepath = filepath or cls._filepath
    #     if not os.path.exists(filepath):
    #         return
    #     with open(filepath, "r", encoding="utf-8") as f:
    #         data = json.load(f)
    #     cls._total_created = data.get("total_created", 0)
    #     cls._alive = data.get("alive", 0)
    #     cls._total_deleted = data.get("total_deleted", 0)
    #     cls._class_stats = data.get("by_class", {})  

    @classmethod
    def reset(cls):
        cls._total_created = 0
        cls._alive = 0
        cls._total_deleted = 0
        cls._class_stats = {}