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
        self.static = False
        if debug:
            print(self.positions)

    def __repr__(self):
        return str(self.positions)

    def left(self):
        if self.static:
            return
        for part in self.positions[0]:
            if part % self.board.width == 0:
                return
        self.positions -= 1

    def right(self):
        if self.static:
            return
        for part in self.positions[0]:
            if (part + 1) % self.board.width == 0:
                return
        self.positions += 1

    def down(self, lowering=False):
        if self.static and not lowering:
            return
        self.positions += self.board.width
        for part in self.positions[0]:
            if part in self.board.floor:
                self.static = True
                return

    def rotate(self):
        if self.static:
            return
        self.positions = np.vstack((self.positions[1:], self.positions[0]))

    def out_of_bounds(self):
        for part in self.positions[0]:
            if part < self.board.limit:
                return False
        return True

    def collided(self):
        current_position = self.positions[0]
        for element in current_position:
            for other_piece in self.board.pieces:
                if id(self) == id(other_piece):
                    continue
                if element + self.board.width in other_piece.positions[0]:
                    self.static = True
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
        self.floor = [self.limit - 1 - i for i in range(self.width)]
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

    # TODO: Remove clean_pieces
    def clean_pieces(self):
        for i, piece in enumerate(self.pieces):
            if piece.out_of_bounds():
                del self.pieces[i]

    def lower_pieces(self, above):
        for piece in self.pieces:
            for part in piece.positions[0]:
                if part < above * self.width:
                    piece.down(lowering=True)

    def completed_row(self):
        for i, row in enumerate(self.board):
            if "-" not in row:
                return i
        return False

    def clear_row(self, i):
        parts = [i * self.width + j for j in range(self.width)]
        for piece in self.pieces:
            if piece.static:
                for i, part in enumerate(piece.positions[0]):
                    if part in parts:
                        piece.positions[0][i] = self.limit
        self.redraw()

    def game_over(self):
        for piece in self.pieces:
            if not piece.static:
                return False
        if "0" in self.board[0]:
            return True


if __name__ == "__main__":
    user_pieces = []
    user_boards = []
    user_piece = None
    tetris_board = None

    while True:
        user_input = input()
        if user_input == 'exit':
            break

        if len(user_input.split()) > 1:
            tetris_board = Board(int(user_input.split()[0]), int(user_input.split()[1]))

        if tetris_board:

            pieces = {
                'O': O(tetris_board),
                'I': I(tetris_board),
                'S': S(tetris_board),
                'Z': Z(tetris_board),
                'L': L(tetris_board),
                'J': J(tetris_board),
                'T': T(tetris_board)
            }

            if user_input == 'piece':
                piece_input = input()
                if piece_input.upper() in ['O', 'I', 'S', 'Z', 'L', 'J', 'T']:
                    user_pieces.append(piece_input.upper())

            if len(user_pieces) > 0:
                user_piece = pieces[user_pieces.pop()]
                tetris_board.add_piece(user_piece)

            if user_input.lower() == 'left':
                user_piece.left()
                user_piece.down()
                user_piece.collided()
            if user_input.lower() == 'right':
                user_piece.right()
                user_piece.down()
                user_piece.collided()
            if user_input.lower() == 'rotate':
                user_piece.rotate()
                user_piece.down()
                user_piece.collided()
            if user_input.lower() == 'down':
                user_piece.collided()
                user_piece.down()

            if user_input == 'break':
                completed_row = tetris_board.completed_row()
                for _ in range(tetris_board.height):
                    if completed_row and completed_row > 0:
                        tetris_board.clear_row(completed_row)
                        tetris_board.lower_pieces(above=completed_row)
                        completed_row = tetris_board.completed_row()

            print(tetris_board)

            if tetris_board.game_over():
                print("Game Over!")
                break
