from string import ascii_lowercase
from random import choice


class Creature:
    #
    def __init__(self, appearance, genes):
        self.appearance = appearance
        self.genes = genes
    #
    def __lt__(self, other):
        return self.appearance < other.appearance
    #
    def __str__(self):
        return str(self.appearance)
    #
    def get_appearance(self):
        return self.appearance
    #
    def get_genes(self):
        return self.genes[:]


# генерация рандомной строчки заданной длины
def random_str(str_len):
    out_str = []
    for i in range(0, str_len):
        out_str.append(choice(ascii_lowercase + " "))
    out_str = "".join(out_str)
    return out_str


# дальность двух существ
def match(member1, member2):
    str1 = member1.get_appearance()
    str2 = member2.get_appearance()
    mismatch = 0
    for c1, c2 in zip(str1, str2):
        if c1 != c2:
            mismatch += 1
    return mismatch


# мутация существа
def mutate(member):
    #
    input_str = member.get_appearance()
    genes = member.get_genes()
    genes.append(input_str)
    #
    input_str = list(input_str)
    max_index = len(input_str)
    mutated_index = choice(range(0, max_index))
    mutation_char = choice(ascii_lowercase + " ")
    output_str = input_str[:]
    output_str[mutated_index] = mutation_char
    output_str = "".join(output_str)
    #
    mutated = Creature(output_str, genes)
    return mutated


# создание заданного количества мутировавших потомков
def reproduce(member, k):
    output = []
    for i in range(0, k):
        output.append(mutate(member))
    return output


# селекция (отбор выживших)
def select(offsprings, selection, size):
    survival_value = map(lambda x: (match(x, selection), x), offsprings)
    select = [xy[1] for xy in sorted(survival_value)[:size]]
    return select


# новое поколение
def next_generation(generation, offspring_size, survival_size, selection_word):
    offsprings = []
    for member in generation:
        offsprings += reproduce(member, offspring_size)
    next_generation = select(offsprings, selection_word, survival_size)
    return next_generation


# достигли искомой строки
def isPresent(selection, generation):
    selection_word = selection.appearance
    generation_words = [x.appearance for x in generation]
    if selection_word in generation_words:
        return True
    else:
        return False


# все в итоге
def evolution(selection_word, max_num_generations=2000):
    selection_word = selection_word.lower()
    random = random_str(len(selection_word))
    selection = Creature(selection_word, [])
    root = Creature(random, [])
    # print("Random word: " + random)
    generation = [root]
    num_of_offsprings = 100
    num_of_select = 10
    generation_index = 1
    while True:
        generation = next_generation(generation, num_of_offsprings, num_of_select, selection)
        if isPresent(selection, generation):
            break
        generation_index += 1
        if generation_index > max_num_generations:
            raise Exception("Not reached in the maximal number of generations")
    return generation[0], generation_index


# печать в файл
def geneticPrint(sentence):
    out = evolution(sentence, 500)
    number_of_generations = out[1]
    best = out[0]
    # верхняя граница
    print('┏', '━' * (len(best.appearance) + 2), '┓', sep='')
    # гены
    for gene in best.genes:
        print('┃ ', gene, ' ┃', sep='')
    # граница посередине
    print('┣', '━' * (len(best.appearance) + 2), '┫', sep='')
    # результат работы
    print('┃ {1} ┃ >> {0}'.format(number_of_generations, best.appearance))
    # нижняя граница
    print('┗', '━' * (len(best.appearance) + 2), '┛', sep='')
    print('\n')