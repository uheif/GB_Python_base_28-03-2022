# Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов,
# взятых из трёх списков (по одному из каждого)
# Например:
# >>> get_jokes(2)
# ["лес завтра зеленый", "город вчера веселый"]
# Документировать код функции.
# Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках
# (когда каждое слово можно использовать только в одной шутке)? Сможете ли вы сделать аргументы именованными?

from random import choice, shuffle


def get_jokes(n=3, repeat=True):
    """
    The function returns the specified number of jokes (3 by default)
    with or without word repetitions (with by default)
    """

    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    if repeat:
        jokes = [f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}' for _ in range(n)]
    else:
        shuffle(nouns)
        shuffle(adverbs)
        shuffle(adjectives)
        if n > len(nouns):
            n = len(nouns)
            print(f'ой, я умею только {n} шуток без повторов :(')
        jokes = [f'{nouns.pop()} {adverbs.pop()} {adjectives.pop()}' for _ in range(n)]

    return jokes


print(get_jokes(6, repeat=False))
