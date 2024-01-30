import random


def generated_file():
    path = rf'G:/pythonProject/step.skroy.ru/filetest{random.randint(0, 999)}.png'
    file = open(path, 'w+')
    file.write(f'Hello World{random.randint(0, 999)}')
    file.close()
    return file.name, path
