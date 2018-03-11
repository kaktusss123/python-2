import argparse
import random


# Загружает из файла модель
def get_model(f):
    pairs = []
    for line in f:  # Читает все строки
        pairs.append(line.split())  # И записывает полученные листы из <слово1 слово2 счетчик> в pairs
    return pairs


# Получает все возможные слова, идущие за текущим seed'ом
def get_next(pairs, seed):
    next = []
    for pair in pairs:
        if pair[0] == seed:  # Если за seed'ом что-то следует
            for i in range(int(pair[2])):  # <счетчик> раз добавь его в список
                next.append(pair[1])
    return next


# Выполняет вывод
def write(pairs, seed, length, out=None):
    if out == None:                         # Если --output не задан
        for i in range(length):
            next = get_next(pairs, seed)    # Получаю следующие слова
            print(seed, end=' ')            # Вывожу seed через обычный print()
            seed = random.choice(next)      # И изменяю сид на одно из следующих слов
    else:                                   # Если --output задан
        for i in range(length):
            next = get_next(pairs, seed)
            out.write(seed + ' ')           # Пишу в out через пробел
            seed = random.choice(next)
        # out.write('\n')   Для личных целей


if __name__ == '__main__':
    # Парсинг аргументов
    parser = argparse.ArgumentParser()
    parser.add_argument('--model', action='store',
                        help='the path to the file in which the model is stored')
    parser.add_argument('--seed', action='store',
                        help='initial word')
    parser.add_argument('--length', action='store',
                        help='length of the generated sequence', type=int)
    parser.add_argument('--output', action='store',
                        help='the file to which the result will be recorded')
    args = parser.parse_args()

    PATH_TO_MODEL = args.model
    PATH_TO_OUTPUT = args.output
    LENGTH = args.length

    seed = args.seed

    # PATH_TO_MODEL обязательный аргумент
    with open(PATH_TO_MODEL + 'model.txt') as f:
        pairs = get_model(f)

        if seed == None:  # Если --seed не задан, выбираем случайное первое слово из пар
            seed = random.choice(pairs)[0]

        if PATH_TO_OUTPUT != None:  # Если задан --output, то используем его
            out = open(PATH_TO_OUTPUT + 'output.txt', 'a')
            write(pairs, seed, LENGTH, out)
        else:
            write(pairs, seed, LENGTH)  # Иначе не передаем параметр out
