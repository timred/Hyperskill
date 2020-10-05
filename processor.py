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


def scalar_multiply(const, mat):
    for n in range(mat.n):
        for m in range(mat.m):
            mat.matrix[n][m] *= const
    return 0


def transpose(mat, choice=1):
    if choice == 2:
        matt = Matrix(mat.m, mat.n)
        for m in range(mat.m - 1, -1, -1):

            col = mat.get_col(m)[::-1]
            matt.add_row(col)
    elif choice == 3:
        matt = Matrix(mat.n, mat.m)
        for n in range(mat.n):
            row = mat.matrix[n][::-1]
            matt.add_row(row)
    elif choice == 4:
        matt = Matrix(mat.n, mat.m)
        for n in range(mat.n - 1, -1, -1):
            row = mat.matrix[n]
            matt.add_row(row)
    else:
        matt = Matrix(mat.m, mat.n)
        for m in range(mat.m):
            col = mat.get_col(m)
            matt.add_row(col)
    return matt


def minor(matrix, i, j):
    k = []
    for n in range(len(matrix)):
        if n == i:
            continue
        row = [x for x in matrix[n]]
        row = row[:j] + row[j + 1:]
        k.append(row)
    return determinant(k)


def cofactor(matrix, i, j):
    return (-1) ** (i + j) * minor(matrix, i, j)


def determinant(matrix):
    if len(matrix) == 1:
        return matrix[0][0]

    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        total = 0
        for i, e in enumerate(matrix[0]):
            k = [x[:i] + x[i + 1:] for x in matrix[1:]]
            total += (-1) ** (2 + i) * e * determinant(k)
        return total


def inverse(mat):
    cof_mat = Matrix(mat.n, mat.m)

    for n in range(mat.n):
        row = []
        for m in range(mat.m):
            row.append(cofactor(mat.matrix, n, m))
        cof_mat.add_row(row)

    cof_mat = transpose(cof_mat)
    scalar_multiply((1 / determinant(mat.matrix)), cof_mat)
    return cof_mat


def menu(i):
    if i == 0:
        print("1. Add matrices")
        print("2. Multiply matrix by a constant")
        print("3. Multiply matrices")
        print("4. Transpose matrix")
        print("5. Calculate a determinant")
        print("6. Inverse matrix")
        print("0. Exit")
    if i == 1:
        print("1. Main diagonal")
        print("2. Side diagonal")
        print("3. Vertical line")
        print("4. Horizontal line")
    return int(input("Your choice: "))


def main():
    while True:
        choice = menu(0)
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
        elif choice == 4:
            choice = menu(1)

            n, m = input("Enter matrix size: ").split()
            a = Matrix(n, m)
            print("Enter matrix:")
            a.fill_matrix()

            at = transpose(a, choice)
            at.matrix_print()
        elif choice == 5:
            n, m = input("Enter matrix size: ").split()
            a = Matrix(n, m)
            print("Enter matrix:")
            a.fill_matrix()

            det = determinant(a.matrix)
            print("The result is:")
            print(int(det) if det.is_integer() else det)
        elif choice == 6:
            n, m = input("Enter matrix size: ").split()
            a = Matrix(n, m)
            print("Enter matrix:")
            a.fill_matrix()

            inv_mat = inverse(a)
            inv_mat.matrix_print()
        elif choice == 0:
            break


main()
