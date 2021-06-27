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

    def __init__(self, board, debug=False):
        # positions = [[4, 14, 15, 5]]
        positions = [[board.mid_point + board.width * i for i in range(2)]
                     + [board.mid_point + board.width * i + 1 for i in range(2)]]
        super().__init__(positions, debug)


class I(Piece):

    def __init__(self, board, debug=False):
        # positions = [[4, 14, 24, 34], [3, 4, 5, 6]]
        positions = [[board.mid_point + board.width * i for i in range(4)],
                     [board.mid_point - 1 + i for i in range(4)]]
        super().__init__(positions, debug)


class S(Piece):

    def __init__(self, board, debug=False):
        # positions = [[5, 4, 14, 13], [4, 14, 15, 25]]
        positions = [[board.mid_point + i for i in range(2)]
                     + [board.mid_point + board.width - i for i in range(2)],
                     [board.mid_point + board.width * i for i in range(2)]
                     + [board.mid_point + 1 + board.width * (i + 1) for i in range(2)]]
        super().__init__(positions, debug)


class Z(Piece):

    def __init__(self, board, debug=False):
        # positions = [[4, 5, 15, 16], [5, 15, 14, 24]]
        positions = [[board.mid_point + i for i in range(2)]
                     + [board.mid_point + 1 + board.width + i for i in range(2)],
                     [board.mid_point + 1 + board.width * i for i in range(2)]
                     + [board.mid_point + board.width * (i + 1) for i in range(2)]]
        super().__init__(positions, debug)


class L(Piece):

    def __init__(self, board, debug=False):
        # positions = [[4, 14, 24, 25], [5, 15, 14, 13], [4, 5, 15, 25], [6, 5, 4, 14]]
        positions = [[board.mid_point + board.width * i for i in range(3)] + [board.mid_point + board.width * 2 + 1],
                     [board.mid_point - 1 + board.width + i for i in range(3)] + [board.mid_point + 1],
                     [board.mid_point + i for i in range(2)] + [(board.width - 1) // 2 + 1 + board.width * (i + 1) for i in range(2)],
                     [board.mid_point + i for i in range(3)] + [(board.width - 1) // 2 + board.width]]
        super().__init__(positions, debug)


class J(Piece):

    def __init__(self, board, debug=False):
        # positions = [[5, 15, 25, 24], [15, 5, 4, 3], [5, 4, 14, 24], [4, 14, 15, 16]]
        positions = [[board.mid_point + 1 + board.width * i for i in range(3)] + [board.mid_point + board.width * 2],
                     [board.mid_point - 1 + i for i in range(3)] + [board.mid_point + 1 + board.width],
                     [board.mid_point + 1] + [board.mid_point + board.width * i for i in range(3)],
                     [board.mid_point] + [board.mid_point + board.width + i for i in range(3)]]
        super().__init__(positions, debug)


class T(Piece):

    def __init__(self, board, debug=False):
        # positions = [[4, 14, 24, 15], [4, 13, 14, 15], [5, 15, 25, 14], [4, 5, 6, 15]]
        positions = [[board.mid_point + board.width * i for i in range(3)] + [board.mid_point + 1 + board.width],
                     [board.mid_point] + [board.mid_point - 1 + board.width + i for i in range(3)],
                     [board.mid_point + 1 + board.width * i for i in range(3)] + [board.mid_point + board.width],
                     [board.mid_point + i for i in range(3)] + [board.mid_point + 1 + board.width]]
        super().__init__(positions, debug)


class Board:

    def __init__(self, width=None, height=None):
        if height is None:
            height = width
        self.width = width
        self.height = height
        self.mid_point = (self.width - 1) // 2
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
    pass


if __name__ == "__main__":
    # main()
    tetris_board = Board(10, 20)
    print(tetris_board)
    i_piece = I(tetris_board)
    o_piece = O(tetris_board)
    s_piece = S(tetris_board)
    z_piece = Z(tetris_board)
    l_piece = L(tetris_board)
    j_piece = J(tetris_board)
    t_piece = T(tetris_board, debug=True)
    # tetris_board.add_piece(i_piece)
    # tetris_board.add_piece(o_piece)
    # tetris_board.add_piece(s_piece)
    # tetris_board.add_piece(z_piece)
    # tetris_board.add_piece(l_piece)
    # tetris_board.add_piece(j_piece)
    tetris_board.add_piece(t_piece)
    print(tetris_board)
