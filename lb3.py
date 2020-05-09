import json


class Series:
    series_list = list(map(int, input("Введите последовательность: ").split()))


class Linear:
    d = Series.series_list[1] - Series.series_list[0]

    def call_n(self):
        Linear.n = int(input("Введите порядковый номер n: "))

    def find_an(self):
        Linear().call_n()
        Linear.an = Series.series_list[0] + (Linear.n - 1) * self.d

    def find_sn(self):
        Linear().find_an()

        Linear.sn = (Series.series_list[0] + self.an) * self.n / 2

    def find_snm(self):
        Linear().find_sn()
        Linear.m = int(input("Введите m:"))
        Linear.am = Series.series_list[0] + (Linear.m - 1) * self.d
        Linear.snm = ((Linear.am + Linear.an) * (Linear.m - Linear.n + 1)) / 2
        Linear.sn = (Series.series_list[0] + self.an) * self.n / 2


class Exponential:
    q = Series.series_list[1] / Series.series_list[0]

    def call_n(self):
        Exponential.n = int(input("Введите порядковый номер n: "))

    def find_bn(self):
        Exponential().call_n()
        Exponential.bn = Series.series_list[0] * Exponential.q ** (self.n - 1)

    def find_sn(self):
        Exponential().find_bn()
        Exponential.sn = (self.bn * self.q - Series.series_list[0]) / (self.q - 1)

    def find_snm(self):
        Exponential().find_sn()
        Exponential.m = int(input("Введите m:"))
        Exponential.bm = Series.series_list[0] * Exponential.q ** (self.m - 1)
        Exponential.sbm = (self.bm * self.q - Series.series_list[0]) / (self.q - 1)
        Exponential.snm = self.sbm - (self.sn - Series.series_list[0] * Exponential.q ** (self.n - 1))


class Progression:
    def linear_all_calculate(self):
        Linear().find_snm()
        print("<------------------------------------------------------------->")
        print("n = ", Linear().n)
        print("a" + str(Linear.n) + " = ", Linear.an)
        print("S" + str(Linear.n) + " = ", Linear.sn)
        print("S" + str(Linear.n) + "-" + str(Linear.m) + " = ", Linear.snm)
        print("<------------------------------------------------------------->")

    def exponential_all_calculate(self):
        Exponential().find_snm()
        print("<------------------------------------------------------------->")
        print("n = ", Exponential.n)
        print("b" + str(Exponential.n) + " = ", Exponential.bn)
        print("S" + str(Exponential.n) + " = ", Exponential.sn)
        print("S" + str(Exponential.n) + "-" + str(Exponential.m) + " = ", Exponential.snm)
        print("<------------------------------------------------------------->")

    def bubble_sort(self, li):
        ln = len(li)
        # внешний цикл отсчитывает количество "проходов" по списку
        for j in range(0, ln - 1):
            # вложенный цикл сравнивает i-ый c i+1 -ым элементом и при необходимости меняет их местами
            # количество сравнений каждый раз уменьшается на величину j
            for i in range(0, ln - j - 1):
                if li[i] < li[i + 1]:
                    li[i], li[i + 1] = li[i + 1], li[i]
        return li

    def save_the_mas(arr):
        with open('mas.txt', 'w') as fw:
            # записываем
            json.dump(arr, fw)

    def open_mass_file():
        with open('mas.txt', 'r') as fr:
            # читаем из файла
            Series.series_list = json.load(fr)
        return Series.series_list

print("Выберите прогрессию")
print("Если арифметическая введите '1'")
print("Если геометрическая введите '2'")

l = int(input())

if l == 1:
    Progression().linear_all_calculate()

elif l == 2:
    Progression().exponential_all_calculate()
else:
    print("Недопустимое значение")


w = input("Сортировать последовательность по убыванию и сохранить в файл ДА / НЕТ ")

if w == "ДА":
    Progression.save_the_mas(Progression().bubble_sort(Series.series_list))
    print("Сортировка завершена и сохранена в файл mass.txt")
    Progression.open_mass_file()
    print(Series.series_list)
    print("<------------------------------------------------------------->")

elif w == "НЕТ":
    print("Компиляция завершена")

else:
    print("Недопустимое значение")
