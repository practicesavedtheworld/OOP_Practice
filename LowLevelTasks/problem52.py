"""
В нейронных сетях использую операцию под названием Max Pooling.
Суть ее состоит в сканировании прямоугольной таблицы чисел (матрицы) окном определенного размера (обычно, 2x2 элемента)
и выбора наибольшего значения в пределах этого окна:

 Или, если окна выходят за пределы матрицы, то они пропускаются (игнорируются):

Мы повторим эту процедуру. Для этого в программе нужно объявить класс с именем MaxPooling, объекты которого создаются командой:

mp = MaxPooling(step=(2, 2), size=(2,2))

где step - шаг смещения окна по горизонтали и вертикали; size - размер окна по горизонтали и вертикали.

Параметры step и size по умолчанию должны принимать кортеж со значениями (2, 2).

Для выполнения операции Max Pooling используется команда:

res = mp(matrix)

где matrix - прямоугольная таблица чисел; res - ссылка на результат обработки таблицы matrix (должна создаваться новая таблица чисел.

Прямоугольную таблицу чисел следует описывать вложенными списками. Если при сканировании таблицы часть
окна выходит за ее пределы, то эти данные отбрасывать (не учитывать все окно).

Если matrix не является прямоугольной таблицей или содержит хотя бы одно не числовое значение, то должно генерироваться исключение командой:

raise ValueError("Неверный формат для первого параметра matrix.")
"""


class MaxPooling:
    def __init__(self, step=(2, 2), size=(2, 2)):
        self.step, self.size = step, size

    def __call__(self, matrix):
        row_lens = sorted(map(len, matrix))
        is_nums = all([all(map(lambda x: type(x) in (int, float), row)) for row in matrix])
        if not (row_lens[0] == row_lens[-1] and is_nums):
            raise ValueError("Неверный формат для первого параметра matrix.")

        if len(matrix) == 0 or len(matrix[0]) == 0:
            return []

        size_x, size_y = self.size
        if size_x > len(matrix) or size_y > len(matrix[0]):
            return []

        step_x, step_y = self.step
        res = [[0] * (len(matrix[0]) // step_x) for _ in range(len(matrix) // step_y)]

        for i, row in enumerate(res):
            for j, _ in enumerate(row):
                s = []
                for r in matrix[i * step_x:i * step_x + size_x]:
                    for c in r[j * step_y:j * step_y + size_y]:
                        s.append(c)
                res[i][j] = max(s)

        return res


if __name__ == "__main__":
    mp = MaxPooling(step=(2, 2), size=(2, 2))
    m1 = [[1, 10, 10], [5, 10, 0], [0, 1, 2]]
    m2 = [[1, 10, 10, 12], [5, 10, 0, -5], [0, 1, 2, 300], [40, -100, 0, 54.5]]
    res1 = mp(m1)
    res2 = mp(m2)

    assert res1 == [[10]], "неверный результат операции MaxPooling"
    assert res2 == [[10, 12], [40, 300]], "неверный результат операции MaxPooling"

    mp = MaxPooling(step=(3, 3), size=(2, 2))
    m3 = [[1, 12, 14, 12], [5, 10, 0, -5], [0, 1, 2, 300], [40, -100, 0, 54.5]]
    res3 = mp(m3)
    assert res3 == [[12]], "неверный результат операции при MaxPooling(step=(3, 3), size=(2,2))"

    try:
        res = mp([[1, 2], [3, 4, 5]])
    except ValueError:
        assert True
    else:
        assert False, "некорректно отработала проверка (или она отсутствует) на не прямоугольную матрицу"

    try:
        res = mp([[1, 2], [3, '4']])
    except ValueError:
        assert True
    else:
        assert False, "некорректно отработала проверка (или она отсутствует) на не числовые значения в матрице"
