from collections import defaultdict
from nltk.tokenize import WhitespaceTokenizer


class Tokenizer:

    def __init__(self):
        # self.file = open("corpus.txt", "r", encoding="utf-8")
        self.file = open(input(), "r", encoding="utf-8")
        self.token_list = self.__token_list()
        self.token_dict = self.__token_dict()
        self.token_unique = self.__token_unique()
        self.total = len(self.token_list)
        self.total_unique = len(self.token_unique)
        self.bigram_list = self.__bigram_list()
        self.total_bigram = len(self.bigram_list)

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

    def get_token(self, i: int):
        return self.token_list[i]

    def get_bigram(self, i: int):
        return self.bigram_list[i]


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


def main():
    my_tokenizer = Tokenizer()
    printer = Printer(my_tokenizer)

    # Stage 1: Preprocess Corpus
    # corpus(my_tokenizer, printer)

    # Stage 2: Break into bigrams
    bigrams(printer)


if __name__ == '__main__':
    main()
