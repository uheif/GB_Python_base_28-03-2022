# (вместо 1) Написать скрипт, создающий из config.yaml стартер для проекта со следующей структурой:
# |--my_project
#    |--settings
#    |  |--__init__.py
#    |  |--dev.py
#    |  |--prod.py
#    |--mainapp
#    |  |--__init__.py
#    |  |--models.py
#    |  |--views.py
#    |  |--templates
#    |     |--mainapp
#    |        |--base.html
#    |        |--index.html
#    |--authapp
#    |  |--__init__.py
#    |  |--models.py
#    |  |--views.py
#    |  |--templates
#    |     |--authapp
#    |        |--base.html
#    |        |--index.html
# Примечание: структуру файла config.yaml придумайте сами,
# его можно создать в любом текстовом редакторе «руками» (не программно);
# предусмотреть возможные исключительные ситуации, библиотеки использовать нельзя.


def make_tree(dct, out_dir_name=''):
    for dir_name, lst in dct.items():
        in_dir_name = os.path.join(out_dir_name, dir_name)
        try:
            os.makedirs(in_dir_name)
        except FileExistsError as e:
            print(e)
        for el in lst:
            if type(el) is dict:
                make_tree(el, in_dir_name)
            else:
                file_name = os.path.join(in_dir_name, el)
                with open(file_name, 'w') as _:
                    pass


if __name__ == '__main__':
    import os
    import yaml  # не по условию, но сначала решил так, переделать уже не успел
    from pprint import pprint

    with open('config.yaml') as f:
        config = yaml.full_load(f)

    pprint(config)

    make_tree(config)