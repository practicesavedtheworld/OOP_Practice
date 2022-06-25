'''
Необходимо объявить класс-декоратор с именем HandlerGET, который будет имитировать обработку GET-запросов на
стороне сервера. Для этого сам класс HandlerGET нужно оформить так, чтобы его можно было применять к любой
 функции как декоратор. Например:

@HandlerGET
def contact(request):
    return "Pentagon"

Здесь request - это произвольный словарь с данными текущего запроса, например,
такой: {"method": "GET", "url": "contact.html"}. А функция должна возвращать строку.

Затем, при вызове декорированной функции:

res = contact({"method": "GET", "url": "contact.html"})

должна возвращаться строка в формате:

"GET: <данные из функции>"

Если ключ method в словаре request отсутствует, то по умолчанию подразумевается GET-запрос.
Если же ключ method принимает другое значение, например, "POST", то декорированная функция contact
должна возвращать значение None.

Для реализации имитации GET-запроса в классе HandlerGET следует объявить вспомогательный метод со следующей сигнатурой:

def get(self, func, request, *args, **kwargs): ...

Здесь func - ссылка на декорируемую функцию; request - словарь с переданными данными при вызове
 декорированной функции. Именно в этом методе следует формировать возвращаемую строку в указанном формате:
'''

class HandlerGET:
    def __init__(self, f):
        self.__f = f

    def __call__(self, request, **kwargs):
        if request.get('method') == 'GET' or 'method' not in request.keys():
            return f"GET: {self.__f(request)}"
        return


@HandlerGET
def contact(request):
    return "Pentagon"


if __name__ == '__main__':
    res = contact({"method": "GET", "url": "contact.html"})
