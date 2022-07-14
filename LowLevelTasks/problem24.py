"""
Объявите класс SmartPhone, объекты которого предполагается создавать командой:

sm = SmartPhone(марка смартфона)

Каждый объект должен содержать локальные атрибуты:

model - марка смартфона (строка);
apps - список из установленных приложений (изначально пустой).

Также в классе SmartPhone должны быть объявлены следующие методы:

add_app(self, app) - добавление нового приложения на смартфон (в конец списка apps);
remove_app(self, app) - удаление приложения по ссылке на объект app.

При добавлении нового приложения проверять, что оно отсутствует в списке apps (отсутствует объект соответствующего класса).

Каждое приложение должно определяться своим классом. Для примера объявите следующие классы:

AppVK - класс приложения ВКонтаке;
AppYouTube - класс приложения YouTube;
AppPhone - класс приложения телефона.
"""


class SmartPhone:
    def __init__(self, mark):
        self.model = mark
        self.apps = []

    def add_app(self, app):
        if len(self.apps) == 0:
            self.apps.append(app)
        elif len(self.apps) > 0:
            for i in self.apps:
                if i.name != app.name:
                    self.apps.append(app)
                    break

    def remove_app(self, app):
        self.apps.remove(app)


class AppVK:
    def __init__(self):
        self.name = "ВКонтакте"


class AppYouTube:
    def __init__(self, mm=1024):
        self.name = "YouTube"
        self.memory_max = mm


class AppPhone:
    def __init__(self, d):
        self.name = "Phone"
        self.phone_list = d


if __name__ == '__main__':
    app_1 = AppVK()  # name = "ВКонтакте"
    app_2 = AppYouTube(1024)  # name = "YouTube", memory_max = 1024
    app_3 = AppPhone({"Феров": 1234567890, "Антон": 98450647365,
                      "Работа": 112})

    sm = SmartPhone("Honor 1.0")
    sm.add_app(AppVK())
    sm.add_app(AppVK())  # второй раз добавляться не должно
    sm.add_app(AppYouTube(2048))
    for a in sm.apps:
        print(a.name)