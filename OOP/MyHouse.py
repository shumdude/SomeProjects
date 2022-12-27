"""Здесь я хочу применять свои знания по ООП в Python и внедрять новые по мере изучения"""


class House:
    """Класс некоторого дома"""

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)  # возвращение адреса нового созданного объекта

    def __init__(self, numbers_of_floors):
        self.numbers_of_floors = numbers_of_floors
        self.__private_local_atribute_house = 0

    def __iter__(self):  # перебор квартир?
        pass

    def get_private_local_atribute_house(self):
        return self.__private_local_atribute_house

    def set_private_local_atribute_house(self, left):
        self.__private_local_atribute_house = left

    house_privates = property(get_private_local_atribute_house, set_private_local_atribute_house)

class Flat:
    """Класс некоторой квартиры"""

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)  # возвращение адреса нового созданного объекта

    def __init__(self, numbers_of_rooms, floor):
        self.numbers_of_rooms = numbers_of_rooms
        self.floor = floor
        self.rooms = []
        for f in range(self.numbers_of_rooms):
            x = input("Введите информацию о комнате номер " + str(f+1) + ": ")
            self.rooms.append(Room(x))
        # self.flat = {i: [] for i in range(self.numbers_of_rooms)}

    def __iter__(self):  # перебор комнат?
        return FlatIterator()

    def set_room(self,):  # назначить роль комнате
        pass


"""
классы нужно связать между собой: у квартиры есть свои комнаты
это должно делаться наверное через дочерний класс, как в БД
а не хранить всё в списке rooms
"""


class Room:
    """Класс некоторой комнаты"""

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)  # возвращение адреса нового созданного объекта

    def __init__(self, *args):  # параметры комнаты
        pass


class FlatIterator:  # итератор квартир
    def __init__(self, some_objects):
        self.some_objects = some_objects
        self.current = 0  # счётчик

    def __next__(self):  # магический метод __next__ характеризует класс как итератор
        if self.current < len(self.some_objects):
            result = self.some_objects[self.current]
            self.current += 1
            return result
        raise StopIteration

    def __iter__(self):
        return self
