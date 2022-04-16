# 3. Есть два списка:
# tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
# klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']
# Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>), например:
# ('Иван', '9А')
# ('Анастасия', '7В')
# ...
# Количество генерируемых кортежей не должно быть больше длины списка tutors.
# Если в списке klasses меньше элементов, чем в списке tutors, необходимо вывести последние кортежи в виде:
# (<tutor>, None), например: ('Станислав', None)
# Доказать, что вы создали именно генератор. Проверить его работу вплоть до истощения.

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А']


def tut_kls(tuts, klss):
    if len(klasses) < len(tutors):
        for i in range(len(tutors) - len(klasses)):
            klasses.append(None)
    for tut, kls in zip(tuts, klss):
        yield tut, kls


t_k = tut_kls(tutors, klasses)
print(*t_k, type(t_k))
print(next(t_k))


t_k_2 = ((tutors[i], klasses[i]) if i < len(klasses) else (tutors[i], None) for i in range(len(tutors)))
print(*t_k_2, type(t_k_2))
print(next(t_k_2))

