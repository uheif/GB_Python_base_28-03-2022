def thesaurus_adv(*args):
    def sourname(full_name):
        return full_name.split(' ')[-1]

    my_dict = {}
    for arg in map(sourname, args):
        if arg[0] not in my_dict:
            my_dict[arg[0]] = list(filter(lambda x: sourname(x).startswith(arg[0]), args))

    return my_dict


print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))
