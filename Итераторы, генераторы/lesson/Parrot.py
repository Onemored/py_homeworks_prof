class Parrot:
    def __init__(self, vocabulary):
        self.vocabulary = vocabulary

    def __iter__(self):
        return VocabularyIterator(self.vocabulary)


class VocabularyIterator:
    def __init__(self, vocabulary):
        self.vocabulary = vocabulary
        self.cursor = -1

    def __next__(self):
        self.cursor += 1
        if self.cursor == len(self.vocabulary):
            raise StopIteration
        return self.vocabulary[self.cursor]


class NewParrot:
    def __init__(self, vocabulary):
        self.vocabulary = vocabulary

    def __iter__(self):
        self.cursor = -1
        return self

    def __next__(self):
        self.cursor += 1
        if self.cursor == len(self.vocabulary):
            raise StopIteration
        return self.vocabulary[self.cursor]


class ParrotWithLimit:
    def __init__(self, vocabulary, limit):
        self.vocabulary = vocabulary
        self.limit = limit

    def learn(self, new_word):
        self.vocabulary.append(new_word)

    def __iter__(self):
        self.cursor = -1
        self.total = -1
        return self

    def __next__(self):
        self.cursor += 1
        self.total += 1
        if self.total == self.limit:
            raise StopIteration
        if self.cursor == len(self.vocabulary):
            self.cursor = 0
        return self.vocabulary[self.cursor]


def my_parrot(vocabulary, limit):
    cursor = -1
    for _ in range(limit):
        cursor += 1
        if cursor == len(vocabulary):
            cursor = 0
        yield vocabulary[cursor]