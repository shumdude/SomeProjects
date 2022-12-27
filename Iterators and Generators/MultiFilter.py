class MultiFilter:

    def judge_half(self, pos, neg):
        # допускает элемент, если его допускает хотя бы половина фукнций (pos >= neg)
        if pos >= neg:
            return True
        return False

    def judge_any(self, pos, neg):
        # допускает элемент, если его допускает хотя бы одна функция (pos >= 1)
        if pos >= 1:
            return True
        return False

    def judge_all(self, pos, neg):
        # допускает элемент, если его допускают все функции (neg == 0)
        if neg == 0:
            return True
        return False

    def __init__(self, iterable, *funcs, judge=judge_any):
        # iterable - исходная последовательность, итерируемый объект
        self.iterable = iterable

        # funcs - допускающие функции, передаваемые на вход функции
        self.funcs = funcs

        # judge - решающая функция, куда отправлять результат
        self.judge = judge

    def __iter__(self):
        # возвращает итератор по {результирующей последовательности}
        for element in self.iterable:
            self.pos = 0
            self.neg = 0
            for func in self.funcs:
                if func(element):
                    self.pos += 1
                else:
                    self.neg += 1
            if self.judge(self, self.pos, self.neg):
                yield element


def func1(x):
    # print( f"{x} % 2 = {x % 2}" )
    return x % 2 == 0


def func2(x):
    return x % 3 == 0


def func3(x):
    return x % 5 == 0


a = [i for i in range(31)]

print(list(MultiFilter(a, func1, func2, func3)))
# [0, 2, 3, 4, 5, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30]

print(list(MultiFilter(a, func1, func2, func3, judge=MultiFilter.judge_half)))
# [0, 6, 10, 12, 15, 18, 20, 24, 30]

print(list(MultiFilter(a, func1, func2, func3, judge=MultiFilter.judge_all)))
# [0, 30]