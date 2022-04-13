# *(вместо задачи 3) Написать функцию thesaurus_adv(), принимающую в качестве аргументов строки в формате «Имя Фамилия»
# и возвращающую словарь, в котором ключи — первые буквы фамилий, а значения — словари,
# реализованные по схеме предыдущего задания и содержащие записи, в которых фамилия начинается с соответствующей буквы.
# Например:
# >>> thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
# {
# "А": {
# "П": ["Петр Алексеев"]
# },
# "И": {
# "И": ["Илья Иванов"]
# },
# "С": {
# "И": ["Иван Сергеев", "Инна Серова"],
# "А": ["Анна Савельева"]
# }
# }
# Как поступить, если потребуется сортировка по ключам?


def thesaurus_adv(*args):
    def nm_i(full_name):
        return full_name.split(' ')[0][0]

    def snm_i(full_name):
        return full_name.split(' ')[-1][0]

    out_dict = {}
    for arg in args:
        if snm_i(arg) not in out_dict:
            snm = snm_i(arg)
            in_dict = {}
            for arg in args:
                if nm_i(arg) not in in_dict:
                    in_lst = list(filter(lambda el: nm_i(el) == nm_i(arg) and snm_i(el) == snm, args))
                    if in_lst:
                        in_dict[nm_i(arg)] = in_lst
            out_dict[snm] = in_dict

    return out_dict


print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))

