# Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике).
# Написать скрипт, который собирает все шаблоны в одну папку templates, например:
# |--my_project
#    ...
#   |--templates
#    |   |--mainapp
#    |   |  |--base.html
#    |   |  |--index.html
#    |   |--authapp
#    |      |--base.html
#    |      |--index.html
# Примечание: исходные файлы необходимо оставить; обратите внимание, что html-файлы расположены в родительских папках
# (они играют роль пространств имён); предусмотреть возможные исключительные ситуации;
# это реальная задача, которая решена, например, во фреймворке django.

import os
import shutil


to_copy = 'templates'
main_root = os.path.join('my_project')
temp = os.path.join(main_root, to_copy)
try:
    os.mkdir(temp)
except FileExistsError as e:
    print(e)

for root, dirs, files in os.walk(main_root):
    tree = os.path.join(root)
    if to_copy in dirs:
        full_to_copy = os.path.join(tree, to_copy)
        for obj in os.listdir(full_to_copy):
            obj_path = os.path.join(full_to_copy, obj)
            try:
                if os.path.isdir(obj_path):
                    shutil.copytree(obj_path, os.path.join(temp, obj))
                elif os.path.isfile(obj_path):
                    shutil.copy2(obj_path, temp)
            except FileExistsError as e:
                print(e)
