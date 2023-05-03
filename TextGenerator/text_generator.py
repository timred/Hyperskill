from collections import defaultdict
from nltk.tokenize import WhitespaceTokenizer
import random


def valid_start(*tokens: str):
    return tokens[0][0].isupper() and not valid_end(*tokens)


def valid_end(*tokens: str):
    valid_ends = ('.', '!', '?')
    return tokens[-1][-1] in valid_ends


class TrigramError(Exception):
    pass


class Tokenizer:

    def __init__(self, filename=None):
        if filename:
            self.filename = filename
        else:
            self.filename = input()
        self.file = open(self.filename, "r", encoding="utf-8")
        self.token_list = self.__token_list()
        self.token_dict = self.__token_dict()
        self.token_unique = self.__token_unique()
        self.total = len(self.token_list)
        self.total_unique = len(self.token_unique)
        self.bigram_list = self.__bigram_list()
        self.trigram_list = self.__trigram_list()
        self.markov_bigram_dict = self.__markov_bigram_dict()
        self.markov_trigram_dict = self.__markov_trigram_dict()
        self.total_bigram = len(self.bigram_list)
        self.total_trigram = len(self.trigram_list)

    def __token_list(self):
        tokens = list()
        line = self.file.readline()
        tokenizer = WhitespaceTokenizer()
        while line:
            line_tokens = tokenizer.tokenize(line)
            tokens += line_tokens
            line = self.file.readline()
        self.file.close()
        return tokens

    def __token_dict(self):
        token_dict = defaultdict(int)
        for token in self.token_list:
            token_dict[str(token)] += 1
        return token_dict

    def __token_unique(self):
        return set(self.token_list)

    def __bigram_list(self):
        bigram_list = list()
        for i in range(len(self.token_list) - 1):
            bigram_list.append((self.token_list[i], self.token_list[i + 1]))
        return bigram_list

    def __trigram_list(self):
        trigram_list = list()
        for i in range(len(self.token_list) - 2):
            trigram_list.append((self.token_list[i], self.token_list[i + 1], self.token_list[i + 2]))
        return trigram_list

    def __markov_bigram_dict(self):
        markov_dict = dict()
        for bigram in self.bigram_list:
            head = bigram[0]
            tail = bigram[1]
            markov_dict.setdefault(head, {tail: 0})
            markov_dict[head].setdefault(tail, 0)
            markov_dict[head][tail] += 1
        return markov_dict

    def __markov_trigram_dict(self):
        markov_dict = dict()
        for trigram in self.trigram_list:
            head = (trigram[0], trigram[1])
            tail = trigram[2]
            markov_dict.setdefault(head, {tail: 0})
            markov_dict[head].setdefault(tail, 0)
            markov_dict[head][tail] += 1
        return markov_dict

    def get_token(self, i: int):
        return self.token_list[i]

    def get_bigram(self, i: int):
        return self.bigram_list[i]

    def get_bigram_markov(self, head: str):
        return self.markov_bigram_dict[head]

    def get_trigram_markov(self, head: tuple):
        return self.markov_trigram_dict[head]

    def get_bigram_next_word(self, current_word: str) -> str:
        next_word_options = self.get_bigram_markov(current_word)
        population = [*next_word_options]
        weights = list(next_word_options.values())
        next_word = random.choices(population, weights)[0]
        return next_word

    def get_trigram_next_word(self, current_words: tuple) -> str:
        next_word_options = self.get_trigram_markov(current_words)
        population = [*next_word_options]
        weights = list(next_word_options.values())
        next_word = random.choices(population, weights)[0]
        return next_word

    def generate_bigram_sentence(self, min_length=5):
        sentence = []
        while True:
            current_word = random.choice(self.token_list)
            if valid_start(current_word):
                sentence.append(current_word)
                break

        next_word = current_word
        while len(sentence) < min_length:
            next_word = self.get_bigram_next_word(next_word)
            if valid_end(next_word) or valid_start(next_word):
                continue
            sentence.append(next_word)

        while True:
            current_word = random.choice(self.token_list)
            if valid_end(current_word):
                sentence.append(current_word)
                break

            next_word = self.get_bigram_next_word(next_word)
            sentence.append(next_word)
            if valid_end(next_word):
                break

        return sentence

    def generate_trigram_sentence(self, min_length=5):
        sentence = []
        while True:
            first_words = random.choice(self.bigram_list)
            if valid_start(*first_words) and not valid_end(first_words[0]):
                sentence.append(first_words[0])
                sentence.append(first_words[1])
                break

        current_head = first_words
        repeats = 0
        while len(sentence) < min_length:
            next_word = self.get_trigram_next_word(current_head)

            if repeats > 100:
                raise TrigramError

            if valid_end(next_word) or valid_start(next_word):
                repeats += 1
                continue
            sentence.append(next_word)
            current_head = (current_head[1], next_word)

        while True:
            # current_words = random.choice(self.bigram_list)
            # if valid_end(*current_words):
            #     sentence.append(current_words[-1])
            #     break

            next_word = self.get_trigram_next_word(current_head)
            sentence.append(next_word)
            current_head = (current_head[1], next_word)
            if valid_end(next_word):
                break

        return sentence


class Printer:

    def __init__(self, tokenizer: Tokenizer):
        self.tokenizer = tokenizer

    def summary_stats(self):
        print("Corpus statistics")
        print(f"All tokens: {self.tokenizer.total}")
        print(f"Unique tokens: {self.tokenizer.total_unique}")

    def summary_bigram(self):
        print(f"Number of bigrams: {self.tokenizer.total_bigram}")

    def bigram(self, i: int):
        bigram = self.tokenizer.get_bigram(i)
        print(f"Head: {bigram[0]}\tTail: {bigram[1]}")

    def markov(self, head: str):
        tails = self.tokenizer.get_bigram_markov(head)
        print(f"Head: {head}")
        for tail, count in tails.items():
            print(f"Tail: {tail}\tCount: {count}")

    def random_text(self):
        sentence = self.tokenizer.generate_bigram_sentence()
        print(" ".join(sentence))

    def trigram_sentence(self):
        try:
            sentence = self.tokenizer.generate_trigram_sentence()
        except TrigramError:
            return 0
        print(" ".join(sentence))
        return 1


def corpus(tokenizer: Tokenizer, printer: Printer) -> None:

    printer.summary_stats()

    while True:
        user_input = input()
        if user_input == "exit":
            break
        try:
            token_int = int(user_input)
            print(tokenizer.get_token(token_int))
        except IndexError:
            print("Index Error. Please input an integer that is in the range or corpus.")
        except (TypeError, ValueError):
            print("Type Error. Please input an integer.")


def bigrams(printer: Printer) -> None:

    printer.summary_bigram()

    while True:
        user_input = input()
        if user_input == "exit":
            break
        try:
            bigram_int = int(user_input)
            printer.bigram(bigram_int)
        except IndexError:
            print("Index Error. Please input a value that is not greater than the number of all bigrams.")
        except (TypeError, ValueError):
            print("Type Error. Please input an integer.")


def markov(printer: Printer) -> None:

    while True:
        user_input = input()
        if user_input == "exit":
            break
        try:
            head = str(user_input)
            printer.markov(head)
        except KeyError:
            print("Key Error. The requested word is not in the model. Please input another word.")


def random_text(printer: Printer) -> None:
    for _ in range(10):
        printer.random_text()


def full_sentence(printer: Printer) -> None:
    i = 0
    while i < 10:
        i += printer.trigram_sentence()


def main():
    # filename = input()
    my_tokenizer = Tokenizer()
    printer = Printer(my_tokenizer)

    # Stage 1: Preprocess Corpus
    # corpus(my_tokenizer, printer)

    # Stage 2: Break into bigrams
    # bigrams(printer)

    # Stage 3: Create a Markov Chain model
    # markov(printer)

    # Stage 4: Generate Random Text
    # random_text(printer)

    # Stage 5: Generate Full Sentences
    # random_text(printer)

    # Stage 6: Generate sentences based on trigrams
    full_sentence(printer)


if __name__ == '__main__':
    main()
