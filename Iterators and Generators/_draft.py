import itertools


class MyList:
    def __init__(self, lst, func):
        self.iterable = lst  # итерируемый объект
        self.func = func  # передаваемая на вход функция
        self.index = 0  # счётчик

    def judge(self, num):  # ещё какая-то функция
        return "element = " + str(num)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.iterable):  # условие перебора
            self.index += 1  # обновляем счётчик

            self.result_of_f2 = self.func(self.iterable[self.index - 1])
            # результат выполнения переданной функции func для элемента итерируемого объекта (ИО)
            # к элементам ИО обращаемся через 'счётчик минус один', то есть по индексу

            self.result_of_judge = self.judge(self.result_of_f2)
            # результат работы какой-то функции с результатом выше

            return self.result_of_judge
        raise StopIteration


def f2(n):  # функция для передачи в аргумент класса
    return n / 2


l = MyList([1, 2, 3, 4, 5], f2)


# for i in l:
#     print(i)


# with open("dataset_24465_4.txt", "r") as f, open("dataset_copy.txt", "w") as w:
#     x = reversed(list(f))
#     for line in x:
#         w.write(line)


# def mod_checker(x, mod=0):
#     f = lambda y: y % x == mod
#     return f
#
# mod_3 = mod_checker(3)
#
# print(mod_3(3)) # True
# print(mod_3(4)) # False
#
# mod_3_1 = mod_checker(3, 1)
# print(mod_3_1(4)) # True


flat = {i: [] for i in range(7)}
# print(flat)

suit = [i for i in range(3) for j in range(2)]
print(suit)