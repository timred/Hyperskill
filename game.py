# Write your code here
import numpy as np


def printer(array: np.array):
    for row in array:
        print(' '.join(row))
    print()


class Piece:

    def __init__(self, positions, debug=False):
        self.positions = positions
        self.start = positions[0]
        if debug:
            print(self.positions)

    def left(self):
        pass

    def right(self):
        pass

    def down(self):
        pass

    def rotate(self):
        pass

    # def print_positions(self, start=False):
    #     for position in self.positions:
    #         # grid = base_grid.copy()
    #         for part in position:
    #             grid[part // 4][part % 4] = "0"
    #         printer(np.array(grid))
    #         if start:
    #             return


class O(Piece):

    def __init__(self, board_width, debug=False):
        # positions = [[4, 14, 15, 5]]
        positions = [[(board_width - 1) // 2 + board_width * i for i in range(2)]
                     + [(board_width - 1) // 2 + board_width * i + 1 for i in range(2)]]
        super().__init__(positions, debug)


class I(Piece):

    def __init__(self, board_width, debug=False):
        # positions = [[4, 14, 24, 34], [3, 4, 5, 6]]
        positions = [[(board_width - 1) // 2 + board_width * i for i in range(4)],
                     [board_width // 2 - 2 + i for i in range(4)]]
        super().__init__(positions, debug)


class S(Piece):

    def __init__(self, board_width, debug=False):
        # positions = [[5, 4, 14, 13], [4, 14, 15, 25]]
        positions = [[(board_width - 1) // 2 + i for i in range(2)]
                     + [(board_width - 1) // 2 + board_width - i for i in range(2)],
                     [(board_width - 1) // 2 + board_width * i for i in range(2)]
                     + [(board_width - 1) // 2 + 1 + board_width * (i + 1) for i in range(2)]]
        super().__init__(positions, debug)


class Z(Piece):

    def __init__(self, board_width, debug=False):
        # positions = [[4, 5, 15, 16], [5, 15, 14, 24]]
        positions = [[(board_width - 1) // 2 + i for i in range(2)]
                     + [(board_width - 1) // 2 + 1 + board_width + i for i in range(2)],
                     [(board_width - 1) // 2 + 1 + board_width * i for i in range(2)]
                     + [(board_width - 1) // 2 + board_width * (i + 1) for i in range(2)]]
        super().__init__(positions, debug)


class L(Piece):

    def __init__(self, board_width, debug=False):
        # positions = [[4, 14, 24, 25], [5, 15, 14, 13], [4, 5, 15, 25], [6, 5, 4, 14]]
        positions = [[(board_width - 1) // 2 + board_width * i for i in range(3)] + [(board_width - 1) // 2 + board_width * 2 + 1]]
        super().__init__(positions, debug)


class J(Piece):

    def __init__(self, board_width, debug=False):
        positions = [[5, 15, 25, 24], [15, 5, 4, 3], [5, 4, 14, 24], [4, 14, 15, 16]]
        super().__init__(positions, debug)


class T(Piece):

    def __init__(self, board_width):
        positions = [[4, 14, 24, 15], [4, 13, 14, 15], [5, 15, 25, 14], [4, 5, 6, 15]]
        super().__init__(positions)


class Board:

    def __init__(self, width=None, height=None):
        if height is None:
            height = width
        self.width = width
        self.height = height
        self.board = np.full((self.height, self.width), "-")
        self.pieces = []

    def __repr__(self):
        board_str = ''
        for row in self.board:
            board_str += ' '.join(row)
            board_str += '\n'
        return str(board_str)

    def add_piece(self, piece: Piece):
        self.pieces.append(piece)
        for part in piece.start:
            self.board[part // self.width][part % self.width] = "0"


def main():
    piece_i = Piece([[1, 5, 9, 13], [4, 5, 6, 7], [1, 5, 9, 13], [4, 5, 6, 7]])
    piece_s = Piece([[6, 5, 9, 8], [5, 9, 10, 14], [6, 5, 9, 8], [5, 9, 10, 14]])
    piece_z = Piece([[4, 5, 9, 10], [2, 5, 6, 9], [4, 5, 9, 10], [2, 5, 6, 9]])
    piece_l = Piece([[1, 5, 9, 10], [4, 5, 6, 2], [0, 1, 5, 9], [4, 5, 6, 8]])
    piece_j = Piece([[2, 6, 9, 10], [4, 5, 6, 10], [1, 2, 5, 9], [0, 4, 5, 6]])
    piece_o = Piece([[5, 6, 9, 10], [5, 6, 9, 10], [5, 6, 9, 10], [5, 6, 9, 10]])
    piece_t = Piece([[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]])

    pieces = {
        "I": piece_i,
        "S": piece_s,
        "Z": piece_z,
        "L": piece_l,
        "J": piece_j,
        "O": piece_o,
        "T": piece_t
    }

    user_input = input()
    print()
    piece = pieces.get(user_input)
    piece.print_positions()
    piece.print_positions(start=True)


if __name__ == "__main__":
    # main()
    board = Board(10, 20)
    print(board)
    i_piece = I(board.width)
    o_piece = O(board.width)
    s_piece = S(board.width)
    z_piece = Z(board.width)
    l_piece = L(board.width, debug=True)
    # board.add_piece(i_piece)
    # board.add_piece(o_piece)
    # board.add_piece(s_piece)
    # board.add_piece(z_piece)
    board.add_piece(l_piece)
    print(board)
