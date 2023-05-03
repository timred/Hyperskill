import itertools
import string

max_length = 3
lowercase = list(string.ascii_lowercase)
digits = list(string.digits)

for i in range(1, max_length):
    complexity = itertools.chain(lowercase, digits)
    for password in itertools.product(complexity, repeat=i):
        print("".join(password))
