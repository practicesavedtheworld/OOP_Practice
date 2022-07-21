"""
нужно объявить классы:

Stack - для представления стека в целом;
StackObj - для представления отдельных объектов стека.

В классе Stack должны быть методы:

push_back(obj) - для добавления нового объекта obj в конец стека;
push_front(obj) - для добавления нового объекта obj в начало стека.

В каждом объекте класса Stack должен быть публичный атрибут:

top - ссылка на первый объект стека (при пустом стеке top = None).

Объекты класса StackObj создаются командой:

obj = StackObj(data)

где data - данные, хранящиеся в объекте стека (строка).

Также в каждом объекте класса StackObj должны быть публичные атрибуты:

data - ссылка на данные объекта;
next - ссылка на следующий объект стека (если его нет, то next = None).

Наконец, с объектами класса Stack должны выполняться следующие команды:

st = Stack()

st[indx] = value # замена прежних данных на новые по порядковому индексу (indx); отсчет начинается с нуля
data = st[indx]  # получение данных из объекта стека по индексу
n = len(st) # получение общего числа объектов стека

for obj in st: # перебор объектов стека (с начала и до конца)
    print(obj.data)  # отображение данных в консоль

При работе с индексами (indx), нужно проверять их корректность.
Должно быть целое число от 0 до N-1, где N - число объектов в стеке. Иначе, генерировать исключение командой:

raise IndexError('неверный индекс')
"""


class StackObj:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


class Stack:
    def __init__(self, top=None):
        self.top = top

    def __iter__(self):
        self.current = self.top
        return self

    def __next__(self):
        if self.current:
            next = self.current
            self.current = self.current.next
            return next
        else:
            raise StopIteration()

    def __len__(self):
        count = 0
        for _ in self:
            count += 1
        return count

    def __getitem__(self, indx):
        return self._get_obj(indx).data

    def __setitem__(self, indx, value):
        self._get_obj(indx).data = value

    def _get_obj(self, indx):
        if type(indx) == int and indx >= 0:
            count = 0
            for obj in self:
                if count == indx:
                    return obj
                count += 1
        raise IndexError('неверный индекс')

    def push_back(self, obj):
        if self.top is None:
            self.top = obj
        else:
            self._get_obj(len(self)-1).next = obj

    def push_front(self, obj):
        if self.top is None:
            self.top = obj
        else:
            obj.next = self.top
            self.top = obj


if __name__ == '__main__':
    st = Stack()
    st.push_back(StackObj("1"))
    st.push_front(StackObj("2"))

    assert st[0] == "2" and st[1] == "1", "неверные значения данных из объектов стека, при обращении к ним по индексу"

    st[0] = "0"
    assert st[
               0] == "0", "получено неверное значение из объекта стека, возможно, некорректно работает присваивание нового значения объекту стека"

    for obj in st:
        assert isinstance(obj, StackObj), "при переборе стека через цикл должны возвращаться объекты класса StackObj"

    try:
        a = st[3]
    except IndexError:
        assert True
    else:
        assert False, "не сгенерировалось исключение IndexError"