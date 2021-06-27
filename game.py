# Write your code here
import numpy as np
# from collections import deque


def cycle_left(n, mod):
    if n % mod == 0:
        return (n - 1) % mod + (n // mod) * mod
    else:
        return n - 1


def cycle_right(n, mod):
    if (n + 1) % mod == 0:
        return (n + 1) % mod + (n // mod) * mod
    else:
        return n + 1


class Piece:

    def __init__(self, board, positions, debug=False):
        self.positions = np.array(positions)
        self.start = positions[0]
        self.board = board
        if debug:
            print(self.positions)

    def __repr__(self):
        return str(self.positions)

    def left(self):
        for i, position in enumerate(self.positions):
            self.positions[i] = list(map(lambda x: cycle_left(x, mod=self.board.width), position))

    def right(self):
        for i, position in enumerate(self.positions):
            self.positions[i] = list(map(lambda x: cycle_right(x, mod=self.board.width), position))

    def down(self):
        self.positions += self.board.width

    def rotate(self):
        self.positions = np.vstack((self.positions[1:], self.positions[0]))

    def out_of_bounds(self):
        for position in self.positions:
            if sum(position) > self.board.limit * 4:
                return True


class O(Piece):

    def __init__(self, board, debug=False):
        # positions = [[4, 14, 15, 5]]
        positions = [[board.mid_point + board.width * i for i in range(2)]
                     + [board.mid_point + board.width * i + 1 for i in range(2)]]
        super().__init__(board, positions, debug)


class I(Piece):

    def __init__(self, board, debug=False):
        # positions = [[4, 14, 24, 34], [3, 4, 5, 6]]
        positions = [[board.mid_point + board.width * i for i in range(4)],
                     [board.mid_point - 1 + i for i in range(4)]]
        super().__init__(board, positions, debug)


class S(Piece):

    def __init__(self, board, debug=False):
        # positions = [[5, 4, 14, 13], [4, 14, 15, 25]]
        positions = [[board.mid_point + i for i in range(2)]
                     + [board.mid_point + board.width - i for i in range(2)],
                     [board.mid_point + board.width * i for i in range(2)]
                     + [board.mid_point + 1 + board.width * (i + 1) for i in range(2)]]
        super().__init__(board, positions, debug)


class Z(Piece):

    def __init__(self, board, debug=False):
        # positions = [[4, 5, 15, 16], [5, 15, 14, 24]]
        positions = [[board.mid_point + i for i in range(2)]
                     + [board.mid_point + 1 + board.width + i for i in range(2)],
                     [board.mid_point + 1 + board.width * i for i in range(2)]
                     + [board.mid_point + board.width * (i + 1) for i in range(2)]]
        super().__init__(board, positions, debug)


class L(Piece):

    def __init__(self, board, debug=False):
        # positions = [[4, 14, 24, 25], [5, 15, 14, 13], [4, 5, 15, 25], [6, 5, 4, 14]]
        positions = [[board.mid_point + board.width * i for i in range(3)] + [board.mid_point + board.width * 2 + 1],
                     [board.mid_point - 1 + board.width + i for i in range(3)] + [board.mid_point + 1],
                     [board.mid_point + i for i in range(2)] + [(board.width - 1) // 2 + 1 + board.width * (i + 1) for i in range(2)],
                     [board.mid_point + i for i in range(3)] + [(board.width - 1) // 2 + board.width]]
        super().__init__(board, positions, debug)


class J(Piece):

    def __init__(self, board, debug=False):
        # positions = [[5, 15, 25, 24], [15, 5, 4, 3], [5, 4, 14, 24], [4, 14, 15, 16]]
        positions = [[board.mid_point + 1 + board.width * i for i in range(3)] + [board.mid_point + board.width * 2],
                     [board.mid_point - 1 + i for i in range(3)] + [board.mid_point + 1 + board.width],
                     [board.mid_point + 1] + [board.mid_point + board.width * i for i in range(3)],
                     [board.mid_point] + [board.mid_point + board.width + i for i in range(3)]]
        super().__init__(board, positions, debug)


class T(Piece):

    def __init__(self, board, debug=False):
        # positions = [[4, 14, 24, 15], [4, 13, 14, 15], [5, 15, 25, 14], [4, 5, 6, 15]]
        positions = [[board.mid_point + board.width * i for i in range(3)] + [board.mid_point + 1 + board.width],
                     [board.mid_point] + [board.mid_point - 1 + board.width + i for i in range(3)],
                     [board.mid_point + 1 + board.width * i for i in range(3)] + [board.mid_point + board.width],
                     [board.mid_point + i for i in range(3)] + [board.mid_point + 1 + board.width]]
        super().__init__(board, positions, debug)


class Board:

    def __init__(self, width=None, height=None):
        if height is None:
            height = width
        self.width = width
        self.height = height
        self.limit = width * height
        self.mid_point = (self.width - 1) // 2
        self.board = np.full((self.height, self.width), "-")
        self.pieces = []

    def __repr__(self):
        self.redraw()
        board_str = ''
        for row in self.board:
            board_str += ' '.join(row)
            board_str += '\n'
        return str(board_str)

    def add_piece(self, piece: Piece):
        self.pieces.append(piece)

    def redraw(self):
        self.board = np.full((self.height, self.width), "-")
        self.clean_pieces()
        for piece in self.pieces:
            for part in piece.positions[0]:
                if part >= self.limit:
                    continue
                self.board[part // self.width][part % self.width] = "0"

    def clean_pieces(self):
        for i, piece in enumerate(self.pieces):
            if piece.out_of_bounds():
                del self.pieces[i]


if __name__ == "__main__":
    user_pieces = []
    user_boards = []
    user_piece = None
    tetris_board = None

    while True:
        user_input = input()
        if user_input in ['O', 'I', 'S', 'Z', 'L', 'J', 'T']:
            user_pieces.append(user_input)
        if len(user_input.split()) > 1:
            tetris_board = Board(int(user_input.split()[0]), int(user_input.split()[1]))
            print(tetris_board)

            pieces = {
                'O': O(tetris_board),
                'I': I(tetris_board),
                'S': S(tetris_board),
                'Z': Z(tetris_board),
                'L': L(tetris_board),
                'J': J(tetris_board),
                'T': T(tetris_board)
            }

            user_piece = pieces[user_pieces.pop()]
            tetris_board.add_piece(user_piece)
            print(tetris_board)

        if user_input == 'left':
            user_piece.down()
            user_piece.left()
            print(tetris_board)
        if user_input == 'right':
            user_piece.down()
            user_piece.right()
            print(tetris_board)
        if user_input == 'rotate':
            user_piece.down()
            user_piece.rotate()
            print(tetris_board)
        if user_input == 'down':
            user_piece.down()
            print(tetris_board)

        if user_input == 'exit':
            break
