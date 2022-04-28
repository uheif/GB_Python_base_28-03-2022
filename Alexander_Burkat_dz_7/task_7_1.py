# Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
# |--my_project
#    |--settings
#    |--mainapp
#    |--adminapp
#    |--authapp
# Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?);
# как лучше хранить конфигурацию этого стартера, чтобы в будущем можно было менять имена папок под конкретный проект;
# можно ли будет при этом расширять конфигурацию и хранить данные о вложенных папках и файлах (добавлять детали)?

import os

structure = {'project': {'name': 'my_project'},
             'settings': {'name': 'settings'},
             'mainapp': {'name': 'mainapp'},
             'adminapp': {'name': 'adminapp'},
             'authapp': {'name': 'authapp'}
             }

project_path = os.path.join(structure['project']['name'])

for dr in structure.values():
    try:
        os.makedirs(os.path.join(project_path, dr['name']))
    except FileExistsError as e:
        print(e)
