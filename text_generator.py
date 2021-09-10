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

    def get_token(self, i: int):
        return self.token_list[i]

    def print_stats(self):
        print("Corpus statistics")
        print(f"All tokens: {self.total}")
        print(f"Unique tokens: {self.total_unique}")


def main():
    my_tokenizer = Tokenizer()
    my_tokenizer.print_stats()

    while True:
        user_input = input()
        if user_input == "exit":
            break
        try:
            token_int = int(user_input)
            print(my_tokenizer.get_token(token_int))
        except IndexError:
            print("Index Error. Please input an integer that is in the range or corpus.")
        except (TypeError, ValueError):
            print("Type Error. Please input an integer.")


if __name__ == '__main__':
    main()
