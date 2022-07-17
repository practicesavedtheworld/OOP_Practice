"""
Stack - для управления односвязным списком в целом;
StackObj - для представления отдельных объектов в односвязным списком.

Объекты класса StackObj должны создаваться командой:

obj = StackObj(data)

где data - строка с некоторыми данными.

Каждый объект класса StackObj должен иметь локальные приватные атрибуты:

__data - ссылка на строку с переданными данными;
__next - ссылка на следующий объект односвязного списка (если следующего нет, то __next = None).

Объекты класса Stack создаются командой:

st = Stack()

и каждый из них должен содержать локальный атрибут:

top - ссылка на первый объект односвязного списка (если объектов нет, то top = None).

Также в классе Stack следует объявить следующие методы:

push_back(self, obj) - добавление объекта класса StackObj в конец односвязного списка;
pop_back(self) - удаление последнего объекта из односвязного списка.

Дополнительно нужно реализовать следующий функционал (в этих операциях копии односвязного списка создавать не нужно):

# добавление нового объекта класса StackObj в конец односвязного списка st
st = st + obj
st += obj

# добавление нескольких объектов в конец односвязного списка
st = st * ['data_1', 'data_2', ..., 'data_N']
st *= ['data_1', 'data_2', ..., 'data_N']

В последних двух строчках должны автоматически создаваться N объектов класса StackObj
с данными, взятыми из списка (каждый элемент списка для очередного добавляемого объекта).
"""


from typing import Optional, List, Tuple


class Descriptor:
    def __set_name__(self, owner, name):
        self.name = f'_{owner.__name__}__{name}'

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        setattr(instance, self.name, value)


class Stack:
    top: Optional["StackObj"]

    def __init__(self):
        self.top = None

    def __add__(self, other: "StackObj"):
        self.push_back(other)
        return self

    def __mul__(self, other: List[str]):
        for obj in map(StackObj, other):
            self.push_back(obj)
        return self

    @property
    def last_two(self) -> Tuple[Optional["StackObj"], Optional["StackObj"]]:
        if self.top is None:
            return None, None
        obj = self.top
        next_obj = self.top.next
        if next_obj is None:
            return obj, None
        while next_obj.next is not None:
            obj = next_obj
            next_obj = obj.next
        return obj, next_obj

    def push_back(self, obj: "StackObj"):
        if self.top is None:
            self.top = obj
        elif self.top.next is None:
            self.top.next = obj
        else:
            _, last_obj = self.last_two
            last_obj.next = obj

    def pop_back(self):
        if self.top is None:
            return None
        if self.top.next is not None:
            self.top.next = None
        else:
            last_obj1, last_obj2 = self.last_two
            last_obj2.next = None
            last_obj1.next = None


class StackObj:
    data = Descriptor()
    next: Optional["StackObj"] = Descriptor()

    def __init__(self, data: str):
        self.data = data
        self.next = None


if __name__ == '__main__':
    assert hasattr(Stack, 'pop_back'), "класс Stack должен иметь метод pop_back"

    st = Stack()
    top = StackObj("1")
    st.push_back(top)
    assert st.top == top, "неверное значение атрибута top"

    st = st + StackObj("2")
    st = st + StackObj("3")
    obj = StackObj("4")
    st += obj

    st = st * ['data_1', 'data_2']
    st *= ['data_3', 'data_4']

    d = ["1", "2", "3", "4", 'data_1', 'data_2', 'data_3', 'data_4']
    h = top
    i = 0
    while h:
        assert h._StackObj__data == d[
            i], "неверное значение атрибута __data, возможно, некорректно работают операторы + и *"
        h = h._StackObj__next
        i += 1

    assert i == len(d), "неверное число объектов в стеке"