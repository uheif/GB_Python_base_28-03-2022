#  Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов,
#  взятых из трёх списков (по одному из каждого):
#
# Например:
# >>> get_jokes(2)
# ["лес завтра зеленый", "город вчера веселый"]
# Документировать код функции.
# Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках
# (когда каждое слово можно использовать только в одной шутке)? Сможете ли вы сделать аргументы именованными?

from random import randrange

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

def get_jokes(lst1, lst2, lst3, n=3):
    def idx(lst):
        # lst_copy = lst[:]

        return lst[randrange(len(lst))]

    for i in range(n):
        print(f'{lst1.pop(lst1.index(idx(lst1)))} {idx(lst2)} {idx(lst3)}')
    print(lst1)

    jokes = [f'{idx(lst1)} {idx(lst2)} {idx(lst3)}' for i in range(n)]
    return jokes


print(get_jokes(nouns, adjectives, lst3=adverbs))


