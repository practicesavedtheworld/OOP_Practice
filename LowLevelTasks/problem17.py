'''
Перед вами стоит задача выделения файлов с определенными расширениями из списка файлов, например:

filenames = ["boat.jpg", "web.png", "text.txt", "python.doc", "ava.jpg", "forest.jpeg", "eq_1.png", "eq_2.xls"]

Для этого необходимо объявить класс FileAcceptor, объекты которого создаются командой:

acceptor = FileAcceptor(ext1, ..., extN)

где ext1, ..., extN - строки с допустимыми расширениями файлов, например: 'jpg', 'bmp', 'jpeg'.

После этого предполагается использовать объект acceptor в стандартной функции filter языка Python следующим образом:

filenames = list(filter(acceptor, filenames))

То есть, объект acceptor должен вызываться как функция:

acceptor(filename)

и возвращать True, если файл с именем filename содержит расширения, указанные при создании acceptor,
и False - в противном случае. Кроме того, с объектами класса FileAcceptor должен выполняться оператор:

acceptor12 = acceptor1 + acceptor2
'''


class FileAcceptor:
    def __init__(self, *args):
        self.name = args

    def __call__(self, fr):
        a = fr[-1*int(fr[::-1].find('.')):]
        return a in self.name

    def __add__(self, other):
        if isinstance(other, FileAcceptor):
            return FileAcceptor(*self.name, *other.name)


if __name__ == '__main__':
    filenames = ["boat.jpg", "web.png", "text.txt", "python.doc", "ava.jpg", "forest.jpeg", "eq_1.png", "eq_2.xls"]
    acceptor1 = FileAcceptor("jpg", "jpeg", "png")
    acceptor2 = FileAcceptor("png", "bmp")
    acceptor12 = acceptor1 + acceptor2    # ("jpg", "jpeg", "png", "bmp")
    acceptor_images = FileAcceptor("jpg", "jpeg", "png")
    acceptor_docs = FileAcceptor("txt", "doc", "xls")
    filenames = list(filter(acceptor_images + acceptor_docs, filenames))
    print(filenames, acceptor12, acceptor_docs+acceptor12)