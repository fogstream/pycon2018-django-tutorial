from django.shortcuts import render


# todo реализовать симуляцию игры камень ножницы бумага

# Правила камень бьет ножницы, ножницы бьют бумагу, бумага бьет камень.
# В иигре присутствуют 2 игрока:
# игрок в длинном плаще
# игрок в шляпе

# задача сгенерировать и вывести в шаблон dict cо следующим содержимым.
# {
#     'current_time': текущее время,
#     'winner': Кто победил в серии трех игр,
#     'games': Список строк, каждая из которых содержит информацию о ходе,
#           какой игрок, как ходил.
# }

# шаблон для view лежит тут
# mysite/templates/mysite.html
