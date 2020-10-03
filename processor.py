class Matrix:

    def __init__(self, n=None, m=None, *args):
        if n is None or m is None:
            n, m = input().split()
        self.n = int(n)
        self.m = int(m)
        self.matrix = []
        for n in range(self.n):
            if len(args) == 0:
                self.add_row()
            else:
                self.add_row(args[n])

    def add_row(self, row=None):
        if row is None:
            row = [int(i) for i in input().split()]
        self.matrix.append(row)

    def matrix_print(self):
        for n in range(self.n):
            print(" ".join([str(i) for i in self.matrix[n]]))


def add(mat1, mat2):
    if mat1.n != mat2.n or mat1.m != mat2.m:
        print("ERROR")
        return
    for n in range(mat1.n):
        for m in range(mat1.m):
            mat1.matrix[n][m] += mat2.matrix[n][m]
    return 0


def scalar_multiply(c, mat):
    for n in range(mat.n):
        for m in range(mat.m):
            mat.matrix[n][m] *= c
    return 0


a = Matrix()
c = int(input())
scalar_multiply(c, a)
a.matrix_print()
