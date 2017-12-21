import sys
from string import ascii_lowercase
from genetic import geneticPrint


# считать строки из файла
def process_file(filename):
    sentences = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.lower()
            line = ''.join([c for c in line
                            if c in (ascii_lowercase + ' ')])
            if line:
                sentences.append(line)
    return sentences


if __name__ == '__main__':
    sentences = process_file('input.txt')
    for sentence in sentences:
        geneticPrint(sentence)
        sys.stdout.flush()