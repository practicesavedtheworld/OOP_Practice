"""
Для последовательной обработки файлов из некоторого списка, например:

filenames = ["boat.jpg", "web.png", "text.txt", "python.doc", "ava.jpg", "forest.jpeg", "eq_1.png", "eq_2.png"]

Необходимо объявить класс ImageFileAcceptor, который бы выделял только графические файлы с указанными расширениями.

Для этого предполагается создавать объекты класса командой:

acceptor = ImageFileAcceptor(extensions)

где extensions - кортеж с допустимыми расширениями файлов, например: extensions = ('jpg', 'bmp', 'jpeg').

А, затем, использовать объект acceptor в стандартной функции filter языка Python следующим образом:

image_filenames = filter(acceptor, filenames)

"""


class ImageFileAcceptor:
    def __init__(self, val):
        self.value = val

    def __call__(self, arg):
        return arg.split('.')[1] in self.value


if __name__ == '__main__':
    filenames = ["boat.jpg", "web.png", "text.txt", "python.doc", "ava.jpg", "forest.jpeg", "eq_1.png", "eq_2.png"]
    acceptor = ImageFileAcceptor(('jpg', 'bmp', 'jpeg'))
    image_filenames = filter(acceptor, filenames)
    print(list(image_filenames))  # ["boat.jpg", "ava.jpg", "forest.jpeg"]