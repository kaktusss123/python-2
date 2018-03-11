import argparse
import fileinput


def to_words(line, lc):
    words = line.split()
    if lc:
        for word_index in range(len(words)):
            words[word_index] = words[word_index].lower()
    return words


def clear(words):
    for word_index in range(len(words)):
        if not words[word_index].isalpha():
            new_word = ''
            for symbol in words[word_index]:
                if symbol.isalpha():
                    new_word += symbol
            words[word_index] = new_word
    while '' in words:
        words.remove('')
    return words


def parse(words, pairs):
    for word_index in range(len(words) - 1):
        if (words[word_index], words[word_index + 1]) in pairs:
            pairs[(words[word_index], words[word_index + 1])] += 1
        else:
            pairs[(words[word_index], words[word_index + 1])] = 1
    return pairs


def write(pairs, path):
    with open(path + 'model.txt', 'w') as f:
        for pair in pairs:
            f.write(pair[0] + ' ' + pair[1] + ' ' + str(pairs[pair]) + '\n')


if __name__ == '__main__':
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

    with open(PATH_TO_INPUT + 'input.txt') as f:
        pairs = {}
        text = []
        for line in f:
            words = to_words(line, args.lc)
            words = clear(words)
            text.extend(words)
        pairs = parse(text, pairs)
        write(pairs, PATH_TO_MODEL)
