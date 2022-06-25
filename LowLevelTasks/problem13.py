'''
Предположим, вам необходимо создать программу по преобразованию списка строк, например:

lst = ["Пункт меню 1", "Пункт меню 2", "Пункт меню 3"]

в следующий фрагмент HTML-разметки (многострочной строки):

"""<ul>
<li>Пункт меню 1</li>
<li>Пункт меню 2</li>
<li>Пункт меню 3</li>
</ul>"""

Для этого необходимо объявить класс RenderList, объекты которого создаются командой:

render = RenderList(type_list)

где type_list - тип списка (принимает значения: "ul" - для списка с тегом <ul> и
"ol" - для списка с тегом <ol>). Если значение параметра type_list другое (не "ul" и не "ol"), то формируется
список с тегом <ul>.
'''

class RenderList:
    def __init__(self, type_list):
        self.type_list = type_list

    def __call__(self, lst):
        li = '\n'.join([f'{el}'.join(['<li>', '</li>']) for el in lst])
        tag = ('<ol>', '</ol>') if self.type_list == 'ol' else ('<ul>', '</ul>')
        return f"""{tag[0]}\n{li}\n{tag[1]}"""


if __name__ == '__main__':
    lst = ["Пункт меню 1", "Пункт меню 2", "Пункт меню 3"]
    render = RenderList("ol")
    html = render(lst)
