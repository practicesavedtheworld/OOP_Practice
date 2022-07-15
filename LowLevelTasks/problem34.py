"""
Необходимо объявить класс-декоратор с именем Handler, который можно было бы применять к функциям следующим образом:

@Handler(methods=('GET', 'POST')) # по умолчанию methods = ('GET',)
def contact(request):
    return "abc"

Здесь аргумент methods декоратора Handler содержит список разрешенных запросов для обработки.
Сама декорированная функция вызывается по аналогии с предыдущим подвигом:

res = contact({"method": "POST", "url": "contact.html"})

В результате функция contact должна возвращать строку в формате:

"<метод>: <данные из функции>"

В нашем примере - это будет:

"POST: abc"

Если ключ method в словаре request отсутствует, то по умолчанию подразумевается GET-запрос.
Если ключ method принимает значение отсутствующее в списке methods декоратора Handler, например, "PUT", то
декорированная функция contact должна возвращать значение None.

Для имитации GET и POST-запросов в классе Handler необходимо объявить два вспомогательных метода с сигнатурами:

def get(self, func, request, *args, **kwargs) - для имитации обработки GET-запроса
def post(self, func, request, *args, **kwargs) - для имитации обработки POST-запроса
"""


class Handler:
    def __init__(self, methods):
        self.__f = methods

    @staticmethod
    def get(func, request, *args, **kwargs):
        return f"GET: {func(request)}"

    @staticmethod
    def post(func, request, *args, **kwargs):
        return f"POST: {func(request)}"

    def __call__(self, func):
        def wrapper(request, *args, **kwargs):

            if request.get('method') not in self.__f and len(request) > 0:
                return
            elif 'method' not in request.keys() or request.get('method') == 'GET':
                return self.get(func, request, *args, **kwargs)
            else:

                return self.post(func, request, *args, **kwargs)

        return wrapper
