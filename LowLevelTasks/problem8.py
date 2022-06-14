'''
Объявите класс EmailValidator для проверки корректности email-адреса. Необходимо запретить создание объектов
этого класса: при создании экземпляров должно возвращаться значение None, например:

em = EmailValidator() # None

В самом классе реализовать следующие методы класса (@classmethod):

check_email(cls, email) - возвращает True, если email записан верно и False - в противном случае;
get_random_email(cls) - для генерации случайного email-адреса по формату: xxxxxxx...xxx@gmail.com,
где x - любой допустимый символ в email (латинский буквы, цифры, символ подчеркивания и точка).

Корректность строки email определяется по следующим критериям:

- допустимые символы: латинский алфавит, цифры, символы подчеркивания, точки и собачка @ (одна);
- длина email до символа @ не должна превышать 100 (сто включительно);
- длина email после символа @ не должна быть больше 50 (включительно);
- после символа @ обязательно должна идти хотя бы одна точка;
- не должно быть двух точек подряд.

Также в классе нужно реализовать приватный статический метод класса:

is_email_str(email) - для проверки типа переменной email, если строка, то возвращается значение True, иначе - False.

Метод is_email_str() следует использовать в методе check_email() перед проверкой корректности email.
Если параметр email не является строкой, то check_email() возвращает False.
'''
import random
import re
from string import ascii_lowercase, digits


class EmailValidator:
    CHARS = ascii_lowercase + ascii_lowercase.upper() + digits + '_.'

    def __new__(cls, *args, **kwargs) -> None:
        return None

    @classmethod
    def check_email(cls, email):
        if cls.__is_email_str(email):
            if len(email[:email.find('@') + 1]) <= 100 and len(email[email.find('@'):]) <= 50:
                if re.fullmatch(
                        r'\w+([.]\w|\w)*@{1}[a-zA-Z]+[.]{1}[a-zA-Z\d?_]{1}([.]\w|\w)*',
                        email) is not None:
                    return True
                return False
        return False

    @classmethod
    def get_random_email(cls):
        res = ''.join([random.choice(cls.CHARS) for _ in range(random.choice(range(2, 25)))])
        return res + '@gmail.com'

    @staticmethod
    def __is_email_str(email):
        return isinstance(email, str)


if __name__ == '__main__':
    s = EmailValidator.get_random_email()
    assert EmailValidator.check_email("i.like.this.course@my.stepik.domen.org") is True
    assert EmailValidator.check_email('name.surname@mail.com') is True
    assert EmailValidator.check_email(1342) is False
    assert EmailValidator.check_email('a+a@m.c') is False
    assert EmailValidator.check_email('aabda..kkk@m.c') is False
    assert EmailValidator.check_email('aaaa@bbb..cc') is False
    assert EmailValidator.check_email(f"{'a' * 100}@{'b' * 45}.aaaaa") is False
    assert EmailValidator.check_email(f"{'a' * 101}@{'b' * 45}.aaaa") is False
    assert EmailValidator.check_email(f"{'a'}@{'b' * 45}aaaa") is False
    assert EmailValidator.check_email('name.surnamemail.com') is False
    assert EmailValidator.check_email('name@mail') is False
