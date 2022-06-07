"""
Объявите класс с именем Notes и определите в нем, следующие атрибуты, без использования конструктора:

uid: 1005435
title: "Шутка"
author: "И.С. Бах"
pages: 2

Затем, с помощью функции getattr() прочитайте и выведите на экран значение атрибута author.
"""


class Notes:
    pass


d = {
    'uid': 1005435,
    'title': "Шутка",
    'author': "И.С. Бах",
    'pages': 2
}
[setattr(Notes, key, value) for key, value in d.items()]

if __name__ == '__main__':
    print(getattr(Notes, 'author'))
