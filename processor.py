def result(func):
    def wrapper(arg):
        print("The result is: ")
        func(arg)
    return wrapper


class Matrix:

    def __init__(self, n, m):
        self.n = int(n)
        self.m = int(m)
        self.matrix = []

    def fill_matrix(self):
        for n in range(self.n):
            self.add_row()

    def add_row(self, row=None):
        if row is None:
            row = [float(i) for i in input().split()]
        self.matrix.append(row)

    def get_col(self, col):
        return [self.matrix[i][col] for i in range(self.n)]

    @result
    def matrix_print(self):
        for n in range(self.n):
            print(" ".join([str(int(i)) if i.is_integer() else str(float(i)) for i in self.matrix[n]]))


def add(mat1, mat2):
    if mat1.n != mat2.n or mat1.m != mat2.m:
        print("The operation cannot be performed.")
        return 1
    for n in range(mat1.n):
        for m in range(mat1.m):
            mat1.matrix[n][m] += mat2.matrix[n][m]
    return 0


def multiply(mat1, mat2):
    if mat1.m != mat2.n:
        print("The operation cannot be performed.")
        return 1

    c = Matrix(mat1.n, mat2.m)
    for n in range(mat1.n):
        row = []
        for m in range(mat2.m):
            row.append(sum(map(lambda x, y: x * y, mat1.matrix[n], mat2.get_col(m))))
        c.add_row(row)
    return c


def scalar_multiply(c, mat):
    for n in range(mat.n):
        for m in range(mat.m):
            mat.matrix[n][m] *= c
    return 0


def menu():
    print("1. Add matrices")
    print("2. Multiply matrix by a constant")
    print("3. Multiply matrices")
    print("0. Exit")


def main():
    while True:
        menu()
        choice = int(input("Your choice: "))
        if choice == 1 or choice == 3:
            n, m = input("Enter size of first matrix: ").split()
            a = Matrix(n, m)
            print("Enter first matrix:")
            a.fill_matrix()

            n, m = input("Enter size of second matrix: ").split()
            b = Matrix(n, m)
            print("Enter second matrix:")
            b.fill_matrix()

            if choice == 1:
                add(a, b)
                a.matrix_print()

            if choice == 3:
                c = multiply(a, b)
                c.matrix_print()
        elif choice == 2:
            n, m = input("Enter size of matrix: ").split()
            a = Matrix(n, m)
            print("Enter matrix:")
            a.fill_matrix()

            c = float(input("Enter constant: "))

            scalar_multiply(c, a)
            a.matrix_print()
        elif choice == 0:
            break


main()
