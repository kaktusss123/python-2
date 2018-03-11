import argparse
import sys


# Преобразует строку в список слов
def to_words(line, lc):
    words = line.split()  # Разделяет слова
    if lc:
        for word_index in range(len(words)):  # Каждое слово к lowercase
            words[word_index] = words[word_index].lower()
    return words


# Очищает список слов от всего, что не буква
def clear(words):
    for word_index in range(len(words)):
        if not words[word_index].isalpha():  # Если слово состоит не только из букв
            new_word = ''  # Создаем новое слово, в котором и сохраним очищенный вариант
            for symbol in words[word_index]:  # Проходим по каждому символу
                if symbol.isalpha():  # Если он буква, приписываем его к новому слову, иначе нет
                    new_word += symbol
            words[word_index] = new_word  # Заменяем слово очищенным
    while '' in words:  # Очищаю от пустых слов, оставшихся после
        words.remove('')  # очистки запятых
    return words


# Разбирает все пары слов
def parse(words, pairs):
    for word_index in range(len(words) - 1):  # Проходим по всем словам, кроме последнего
        if (words[word_index], words[word_index + 1]) in pairs:  # Если такая пара слов уже встречалась
            pairs[(words[word_index], words[word_index + 1])] += 1  # просто добавляем +1 к счетчику
        else:
            pairs[(words[word_index], words[word_index + 1])] = 1  # Иначе создаем такую пару, и счетчик = 1
    return pairs


# Вывод в файл
def write(pairs, path):
    with open(path + 'model.txt', 'w') as f:  # PATH_TO_MODEL не может быть None
        for pair in pairs:
            f.write(
                pair[0] + ' ' + pair[1] + ' ' + str(pairs[pair]) + '\n')  # Каждую пару запиываем всместе с счетчиком


if __name__ == '__main__':
    # Парсинг аргументов
    parser = argparse.ArgumentParser()
    parser.add_argument('--dir', action='store',
                        help='the path to the directory containing the collection of documents')
    parser.add_argument('--model', action='store',
                        help='the path to the file in which the model is stored')
    parser.add_argument('--lc', action='store_true',
                        help='make the texts lowercase')
    args = parser.parse_args()

    PATH_TO_MODEL = args.model
    PATH_TO_INPUT = args.dir

    # Если --dir не задан, то считывать из stdin
    if PATH_TO_INPUT != None:
        f = open(PATH_TO_INPUT + 'input.txt')
    else:
        f = sys.stdin

    pairs = {}
    text = []
    for line in f:
        words = to_words(line, args.lc)  # Разбивает строку на слова, при --lc приводит к lowercase
        words = clear(words)  # Убирает все, что не является буквами
        text.extend(words)  # Текст, разбитый по словам и очищенный от мусора
    pairs = parse(text, pairs)  # Создает модель
    write(pairs, PATH_TO_MODEL)  # Записывает модель в файл

    f.close()
