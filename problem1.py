class Notes:
    pass


d = {
    'uid': 1005435,
    'title': "Шутка",
    'author': "И.С. Бах",
    'pages': 2
}
[setattr(Notes, k, v) for k, v in d.items()]
print(getattr(Notes, 'author'))
