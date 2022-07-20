"""
в программе объявлялись два класса:

StackObj - для описания объектов стека;
Stack - для управления стек-подобной структурой.

И, далее, объекты класса StackObj следовало создавать командой:

obj = StackObj(data)

где data - это строка с некоторым содержимым объекта (данными). При этом каждый объект класса StackObj должен иметь следующие локальные атрибуты:

data - ссылка на строку с данными, указанными при создании объекта;
next - ссылка на следующий объект класса StackObj (при создании объекта принимает значение None).

Класс Stack предполагается использовать следующим образом:

st = Stack() # создание объекта стек-подобной структуры

В каждом объекте класса Stack должен быть локальный публичный атрибут:

top - ссылка на первый объект стека (если стек пуст, то top = None).

А в самом классе Stack следующие методы:

push(self, obj) - добавление объекта класса StackObj в конец стека;
pop(self) - извлечение последнего объекта с его удалением из стека;

Дополнительно в классе Stack нужно объявить магические методы для обращения к объекту стека по его индексу, например:

obj_top = st[0] # получение первого объекта
obj = st[4] # получение 5-го объекта стека
st[2] = StackObj("obj3") # замена прежнего (3-го) объекта стека на новый

Если индекс не целое число или число меньше нуля или больше числа объектов в стеке, то должно генерироваться исключение командой:

raise IndexError('неверный индекс')
"""


class StackObj:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return str(self)



class Stack:
    def __init__(self):
        self.top = None
        self.__count = 0

    def __check(self, idx):
        if idx not in range(self.items):
            raise IndexError('неверный индекс')

    @property
    def items(self):
        return self.__count

    def push(self, obj):
        self.__count += 1
        if self.top is None:
            self.top = obj
        else:
            el = self.top
            while el.next is not None:
                el = el.next
            el.next = obj

    def pop(self):
        el = self.top
        if el and self.top.next is None:
            self.top = None
            self.__count -= 1
        elif el and el.next:
            self.__count -= 1
            last = el
            el = el.next
            while el.next:
                last = el
                el = el.next
            last.next = None
        return el

    def __get_obj(self, idx):
        cnt = 0
        el = self.top
        while cnt != idx:
            el = el.next
            cnt += 1
        return el

    def __getitem__(self, item):
        self.__check(item)
        return self.__get_obj(item)

    def __setitem__(self, key, value):
        self.__check(key)
        if key == 0:
            value.next = self.top.next
            self.top = value
        else:
            prev = self.__get_obj(key - 1)
            cur = prev.next
            prev.next = value
            value.next = cur.next


if __name__ == '__main__':

    st = Stack()
    st.push(StackObj("obj11"))
    st.push(StackObj("obj12"))
    st.push(StackObj("obj13"))
    st[1] = StackObj("obj2-new")
    assert st[0].data == "obj11" and st[
        1].data == "obj2-new", "атрибут data объекта класса StackObj содержит неверные данные"

    try:
        obj = st[3]
    except IndexError:
        assert True
    else:
        assert False, "не сгенерировалось исключение IndexError"

    obj = st.pop()
    assert obj.data == "obj13", "метод pop должен удалять последний объект стека и возвращать его"

    n = 0
    h = st.top
    while h:
        assert isinstance(h, StackObj), "объект стека должен быть экземпляром класса StackObj"
        n += 1
        h = h.next

    assert n == 2, "неверное число объектов в стеке (возможно, нарушена его структура)"
