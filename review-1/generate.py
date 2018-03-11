import argparse
import random


def get_model(f):
    pairs = []
    for line in f:
        pairs.append(line.split())
    return pairs


def get_next(pairs, seed):
    next = []
    for pair in pairs:
        if pair[0] == seed:
            for i in range(int(pair[2])):
                next.append(pair[1])
    return next

def write(pairs, seed, length, out = None):
    if out == None:
        for i in range(length):
            next = get_next(pairs, seed)
            print(seed, end=' ')
            seed = random.choice(next)
    else:
        for i in range(length):
            next = get_next(pairs, seed)
            out.write(seed + ' ')
            seed = random.choice(next)


if __name__ == '__main__':
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
    SEED = args.seed

    with open(PATH_TO_MODEL + 'model.txt') as f:
        pairs = get_model(f)
        if SEED == None:
            seed = random.choice(pairs)[0]
        else:
            seed = SEED
        if PATH_TO_OUTPUT != None:
            out = open(PATH_TO_OUTPUT + 'output.txt', 'w')
            write(pairs, seed, LENGTH, out)
        else:
            write(pairs, seed, LENGTH)


