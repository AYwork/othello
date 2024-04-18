from .color import Color
from .piece import Piece


class Board:
    board = []
    last_puted_rocation = [0, 0]  # x, y #これ書いてみたけど使えそう。Boardクラスで大丈夫?
    last_puted_color = None
    def __init__(self) -> None:
        self.board = []
        for y in range(8):
            row = []
            for x in range(8):
                row.append(Piece(Color.SPACE, x, y))
                # row.append(Color.SPACE)
            self.board.append(row)

    def __str__(self) -> str:
        stage = ""
        for i in range(len(self.board)):
            stage += "".join([str(i) for i in self.board[i]]) + "\n"
        return stage

    def __add__(self, another: str) -> str:
        return self.__str__() + another
    
    def is_already_put(self, x, y) -> bool:

        if self.board[y-1][x-1].color != Color.SPACE:
            return True
    
    def set_piece_to(self, x: int, y: int, color: Color) -> None: #pieceを置くときに呼ぶ
        piece = Piece(color, x, y)
        raw_row = self.board[y-1]
        raw_row[x-1] = piece.color
        self.board[y-1] = raw_row

        
    def calc_black_area(self):
        area = 0
        for y in self.board:
            for x in y:
                if x.color == "○":
                    area += 1
        return area

    def calc_white_area(self):
        area = 0
        for y in self.board:
            for x in y:
                if x.color == "●":
                    area += 1
        return area



    def update(self):  # boad上のpiece色を演算し、更新
        x_offset = self.last_puted_rocation[0]
        y_offset = self.last_puted_rocation[1]
        ########################################
        # 行
        ########################################
        # コマを置いた左側
        target_x_left = x_offset
        for x_left in range(x_offset - 1, -1, -1):
            if self.board[y_offset][x_left].color != self.last_puted_color and self.is_already_put(x_left, y_offset): #違う色なら
                continue
            if (self.board[y_offset][x_left].color == self.last_puted_color) and (x_left is not x_offset):
                target_x_left = x_left
                break
            else:
                break

        # コマを置いた右側
        target_x_right = x_offset
        for x_right in range(x_offset + 1, 8):
            if self.board[y_offset][x_right].color != self.last_puted_color and self.is_already_put(x_right, y_offset):
                continue
            if (self.board[y_offset][x_right].color == self.last_puted_color) and (x_right is not x_offset):
                target_x_right = x_right
                break
            else:
                break

        # 書き換え
        for x in range(x_offset - 1, target_x_left, -1):
            self.board[y_offset][x].reverse_piece()

        for x in range(x_offset + 1, target_x_right):
            self.board[y_offset][x].reverse_piece()

        ########################################
        # 列
        ########################################
        # コマを置いた上側
        target_y_upper = y_offset
        for y_upper in range(y_offset - 1, -1, -1):
            if self.board[y_upper][x_offset].color != self.last_puted_color and self.is_already_put(x_offset, y_upper):
                continue
            if (self.board[y_upper][x_offset].color == self.last_puted_color) and (y_upper is not y_offset):
                target_y_upper = y_upper
                break
            else:
                break

        # コマを置いた下側
        target_y_lower = y_offset
        for y_lower in range(y_offset + 1, 8):
            if self.board[y_lower][x_offset].color != self.last_puted_color and self.is_already_put(x_offset, y_lower):
                continue
            if (self.board[y_lower][x_offset].color == self.last_puted_color) and (y_lower is not y_offset):
                target_y_lower = y_lower
                break
            else:
                break

        # 書き換え
        for y in range(y_offset - 1, target_y_upper, -1):
            self.board[y][x_offset].reverse_piece()

        for y in range(y_offset + 1, target_y_lower):
            self.board[y][x_offset].reverse_piece()


        ########################################
        # 右上がり斜め
        ########################################
        # コマを置いた左下側
        target_x_left = x_offset
        target_y_lower = y_offset
        for i in range(1, 8):
            x_left = x_offset - i
            y_lower = y_offset + i
            if x_left < 0 or y_lower > 7: #壁にぶつかったら
                break
            if self.board[y_lower][x_left].color != self.last_puted_color and self.is_already_put(x_left,y_lower):  # 違う色なら
                continue
            if (self.board[y_lower][x_left].color == self.last_puted_color) and (x_left is not x_offset) and (y_lower is not y_offset):
                target_x_left = x_left
                target_y_lower = y_lower
                break
            else:
                break

        # コマを置いた右上側
        target_x_right = x_offset
        target_y_upper = y_offset
        for i in range(1, 8):
            x_right = x_offset + i
            y_upper = y_offset - i
            if x_right > 7 or y_upper < 0:  # 壁にぶつかったら
                break
            if self.board[y_upper][x_right].color != self.last_puted_color and self.is_already_put(x_right,y_upper):
                continue
            if (self.board[y_upper][x_right].color == self.last_puted_color) and (x_right is not x_offset) and (y_upper is not y_offset):
                target_x_right = x_right
                target_y_upper = y_upper
                break
            else:
                break

        # 書き換え
        for i in range(1, abs(target_x_left - x_offset)):
            x = x_offset - i
            y = y_offset + i
            self.board[y][x].reverse_piece()

        for i in range(1, abs(target_x_right - x_offset)):
            x = x_offset + i
            y = y_offset - i
            self.board[y][x].reverse_piece()

        ########################################
        # 右下がり斜め
        ########################################
        # コマを置いた左上側
        target_x_left = x_offset
        target_y_upper = y_offset
        for i in range(1, 8):
            x_left = x_offset - i
            y_upper = y_offset - i
            if x_left < 0 or y_upper < 0: #壁にぶつかったら
                break
            if self.board[y_upper][x_left].color != self.last_puted_color and self.is_already_put(x_left,y_upper):  # 違う色なら
                continue
            if (self.board[y_upper][x_left].color == self.last_puted_color) and (x_left is not x_offset) and (y_upper is not y_offset):
                target_x_left = x_left
                target_y_upper = y_upper
                break
            else:
                break

        # コマを置いた右上側
        target_x_right = x_offset
        target_y_lower = y_offset
        for i in range(1, 8):
            x_right = x_offset + i
            y_lower = y_offset + i
            if x_right > 7 or y_lower > 7:  # 壁にぶつかったら
                break
            if self.board[y_lower][x_right].color != self.last_puted_color and self.is_already_put(x_right,y_lower):
                continue
            if (self.board[y_lower][x_right].color == self.last_puted_color) and (x_right is not x_offset) and (y_lower is not y_offset):
                target_x_right = x_right
                target_y_lower = y_lower
                break
            else:
                break

        # 書き換え
        for i in range(1, abs(target_x_left - x_offset)):
            x = x_offset - i
            y = y_offset - i
            self.board[y][x].reverse_piece()

        for i in range(1, abs(target_x_right - x_offset)):
            x = x_offset + i
            y = y_offset + i
            self.board[y][x].reverse_piece()


    def black_is_win(self):
        if self.calc_black_area() > self.calc_white_area():
            return True
        if self.calc_black_area() < self.calc_white_area():
            return False
        return None  # Noneを返せば引き分け