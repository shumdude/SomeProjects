class TumbochkaIterator:  # класс итератора
    def __init__(self, some_objects):
        self.some_objects = some_objects
        self.current = 0  # счётчик

    def __next__(self):  # магический метод __next__ характеризует класс как итератор
        if self.current < len(self.some_objects):
            result = self.some_objects[self.current]
            self.current += 1
            return result
        raise StopIteration

    def __iter__(self):  # теперь итератор ещё и итерируемый
        # При итерации самого себя возвращается сам итератор
        return self
        # Это сделано для того, чтобы мы могли перебирать объекты кастомных итераторов в цикле for точно так же,
        # как это можно делать c итераторами коллекций или генераторами

    def to_start(self):
        self.current = 0

    def to_current(self, val):
        if val >= len(self.some_objects) or val < 0:
            print("Неверное значение для курсора!")
        else:
            self.current = val


class Tumbochka:
    """Волшебная тумбочка с тремя ящиками для чего угодно"""

    def __init__(self):
        self.boxes = {
            1: [],
            2: [],
            3: []
        }

    def add_to_box(self, obj, box_num):
        if box_num not in {1, 2, 3}:
            print("Вы ввели неправильный номер ящика!")
        else:
            self.boxes[box_num].append(obj)

    def remove_from_box(self, box_num):
        if box_num not in {1, 2, 3}:
            print("Вы ввели неправильный номер ящика!")
        else:
            return self.boxes[box_num].pop()

    def __str__(self):  # строковое представление класса
        boxes_items = self.boxes[1] + self.boxes[2] + self.boxes[3]
        return ", ".join(boxes_items)

    def __iter__(self):
        return TumbochkaIterator(self.boxes[1] + self.boxes[2] + self.boxes[3])
        # при итерации класса или объекта класса возвращается кастомный итератор с входными данными класса


tumb = Tumbochka()  # экземпляр класса
tumb.add_to_box("ножницы", 1)
tumb.add_to_box("карандаш", 2)
tumb.add_to_box("яблоко", 3)
tumb.add_to_box("книга", 1)

# объявление итератора экземпляра класса Тумбочка; его итерация
it = iter(tumb)  # единожды создаём итератор для тумбочки
print(next(it))
for el in it:
    print(el)
print('---')
for el in it:  # конкретный итератор it уже перебран
    print(el)
print('---')

# перебор экземпляра класса tumb, а не его уже объявленного итератора it
print('перебор tumb, а не it')
for el in tumb:
    print(el)
print('---')
for el in tumb:  # каждый раз создаётся итератор для тумбочки (см. ниже)
    print(el)

# Это равносильно циклу for:
it = iter(tumb)  # объявление итератора, поэтому при каждом новом for новый итератор it
print('Это равносильно')
while True:
    try:
        i = next(it)
        print(i)
    except StopIteration:
        break

# перебирать объекты кастомных итераторов
print('перебирать объекты кастомных итераторов')
tumb_it = TumbochkaIterator([1, 2, 3])  # экземпляр кастомного итератора или объект кастомного итератора
tumb_it_it = iter(tumb_it)  # итератор объекта/экземпляра кастомного итератора
print(next(tumb_it_it))
print('---')
for t in tumb_it:
    print(t)
# итератор - не более, чем инструмент