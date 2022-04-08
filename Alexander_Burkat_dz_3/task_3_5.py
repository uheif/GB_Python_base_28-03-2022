#  Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов,
#  взятых из трёх списков (по одному из каждого):
#
# Например:
# >>> get_jokes(2)
# ["лес завтра зеленый", "город вчера веселый"]
# Документировать код функции.
# Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках
# (когда каждое слово можно использовать только в одной шутке)? Сможете ли вы сделать аргументы именованными?

from random import randrange, choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

def get_jokes(lst1, lst2, lst3, n=3):
    def idx(lst):
        # lst_copy = lst[:]

        return lst[randrange(len(lst))]

    jokes = []
    idxs1 = [i for i in range(len(lst1))]
    print(idxs1)
    idxs2 = [i for i in range(len(lst2))]
    idxs3 = [i for i in range(len(lst3))]

    for i in range(n):
        idx1 = idxs1.pop(choice(idxs1))
        print(idx1, idxs1)
        idx2 = idxs2.pop(choice(idxs2))
        idx3 = idxs3.pop(choice(idxs3))
        jokes.append(f'{lst1[idx1]} {lst2[idx2]} {lst3[idx3]}')

        print(jokes)
        # print(idx(lst1) in jokes[i])
        # lst1_f = filter(idx(lst1) in jokes[n], lst1)
        # print(lst1_f)

    return jokes



print(get_jokes(nouns, adjectives, lst3=adverbs))


