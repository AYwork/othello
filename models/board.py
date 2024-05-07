from .color import Color
from .piece import Piece
from .player import Player


class Board:
    pieces = [["" for i in range(8)] for j in range(8)]
    last_puted_rocation   = [0, 0]  # x, y
    last_puted_color      = None
    last_puted_piece_copy = None
    
    def __init__(self):
        # 盤面の生成(Piece64個)
        for x in range(0, 8):
            for y in range(0, 8):
                self.pieces[y][x] = Piece(x, y)

    def __str__(self) -> str:
        stage = ""
        for y in range(0, 8):
            for x in range(0, 8):
                stage += str(self.pieces[y][x].state)
            stage += "\n"
        return stage
    
    def __add__(self, another: str) -> str:
        return self.__str__() + another
    
    def is_already_put(self, x: int, y: int) -> bool:
        # 指定されたマスに既にコマが置かれているか判断する
        if self.pieces[y][x].state != Color.SPACE:
            return True
        return False
    
    def get_placeable_list(self, player: Player) -> list:
        # 置けるマスの一覧を返す
        placeable_list =[]
        for px in range(8):
            for py in range(8):
                if (self.enable_to_put(px, py, player.color)) and not (self.is_already_put(px,py)):
                    placeable_list.append([str(px+1), str(py+1)])
        return placeable_list

    def enable_to_put(self, px: int, py: int, color: Color) -> bool:
        # 指定のマスにコマを置けるか判断する
        flag = False
        x_offset = px
        y_offset = py

        # print(f"enable_to_put: {px}, {py}")
        ########################################
        # 行
        ########################################
        # コマを置いた左側
        target_x_left = x_offset
        for x_left in range(x_offset - 1, -1, -1):
            if not self.pieces[y_offset][x_left].is_same_color(color) and self.is_already_put(x_left, y_offset): # 違う色なら
                flag = True
                continue
            if (self.pieces[y_offset][x_left].is_same_color(color)) and (x_left is not x_offset) and flag is True:
                print("左がTrue")
                return True
            else:
                break
    
        # コマを置いた右側
        target_x_right = x_offset
        flag = False
        for x_right in range(x_offset + 1, 8):
            if not self.pieces[y_offset][x_right].is_same_color(color) and self.is_already_put(x_right, y_offset): # 違う色なら
                flag = True
                continue
            if (self.pieces[y_offset][x_right].is_same_color(color)) and (x_right is not x_offset) and flag is True:
               print("右がTrue")
               return True
            else:
                break

        ########################################
        # 列
        ########################################
        # コマを置いた上側
        target_y_upper = y_offset
        flag = False
        for y_upper in range(y_offset - 1, -1, -1):
            if not self.pieces[y_upper][x_offset].is_same_color(color) and self.is_already_put(x_offset, y_upper): # 違う色なら
                flag = True
                continue
            if (self.pieces[y_upper][x_offset].is_same_color(color)) and (y_upper is not y_offset) and flag is True:
                print("上がTrue")
                return True
            else:
                break

        # コマを置いた下側
        target_y_lower = y_offset
        flag = False
        for y_lower in range(y_offset + 1, 8):
            if not self.pieces[y_lower][x_offset].is_same_color(color) and self.is_already_put(x_offset, y_lower): # 違う色なら
                flag = True
                continue
            if (self.pieces[y_lower][x_offset].is_same_color(color)) and (y_lower is not y_offset) and flag is True:
                print("下がTrue")
                return True
            else:
                break

        ########################################
        # 右上がり斜め
        ########################################
        # コマを置いた左下側
        target_x_left  = x_offset
        target_y_lower = y_offset
        flag = False
        for i in range(1, 8):
            x_left = x_offset - i
            y_lower = y_offset + i
            if x_left < 0 or y_lower > 7: #壁にぶつかったら
                break
            if not self.pieces[y_lower][x_left].is_same_color(color) and self.is_already_put(x_left,y_lower):  # 違う色なら
                flag = True
                continue
            if (self.pieces[y_lower][x_left].is_same_color(color)) and (x_left is not x_offset) and (y_lower is not y_offset) and flag is True:
                print("左下がTrue")
                return True
            else:
                break

        # コマを置いた右上側
        target_x_right = x_offset
        target_y_upper = y_offset
        flag = False
        for i in range(1, 8):
            x_right = x_offset + i
            y_upper = y_offset - i
            if x_right > 7 or y_upper < 0:  # 壁にぶつかったら
                break
            if not self.pieces[y_upper][x_right].is_same_color(color) and self.is_already_put(x_right,y_upper): # 違う色なら
                flag = True
                continue
            if (self.pieces[y_upper][x_right].is_same_color(color)) and (x_right is not x_offset) and (y_upper is not y_offset) and flag is True:
                print("右下がTrue")
                return True
            else:
                break
            
        ########################################
        # 右下がり斜め
        ########################################
        # コマを置いた左上側
        target_x_left = x_offset
        target_y_upper = y_offset
        flag = False
        for i in range(1, 8):
            x_left = x_offset - i
            y_upper = y_offset - i
            if x_left < 0 or y_upper < 0: # 壁にぶつかったら
                break
            if not self.pieces[y_upper][x_left].is_same_color(color) and self.is_already_put(x_left,y_upper):  # 違う色なら
                flag = True
                continue
            if (self.pieces[y_upper][x_left].is_same_color(color)) and (x_left is not x_offset) and (y_upper is not y_offset) and flag is True:
                print("左上がTrue")
                return True
            else:
                break

        # コマを置いた右上側
        target_x_right = x_offset
        target_y_lower = y_offset
        flag = False
        for i in range(1, 8):
            x_right = x_offset + i
            y_lower = y_offset + i
            if x_right > 7 or y_lower > 7:  # 壁にぶつかったら
                break
            # print(type(self.pieces[y_lower][x_right]))
            if not self.pieces[y_lower][x_right].is_same_color(color) and self.is_already_put(x_right,y_lower): # 違う色なら
                flag = True
                continue
            if (self.pieces[y_lower][x_right].is_same_color(color)) and (x_right is not x_offset) and (y_lower is not y_offset) and flag is True:
                target_x_right = x_right
                target_y_lower = y_lower
                print("右上がTrue")
                return True
            else:
                break

        return False




    def set_piece_to(self, x: int, y: int, color: Color) -> None: 
        # pieceを置くときに呼ぶ
        self.pieces[y][x].set_state(color)
        self.last_puted_rocation[0] = x
        self.last_puted_rocation[1] = y
        self.last_puted_color = color   # "● or ○ or ."
     

    def calc_black_area(self):
        area = 0
        for y in self.pieces:
            for x in y:
                if x.state == Color.WHITE:
                    area += 1
        return area

    def calc_white_area(self):
        area = 0
        for y in self.pieces:
            for x in y:
                if x.state == Color.BLACK:
                    area += 1
        return area

    def update(self):  
        # boad上のpiece色を演算し、更新
        x_offset = self.last_puted_rocation[0]
        y_offset = self.last_puted_rocation[1]
        ########################################
        # 行
        ########################################
        # コマを置いた左側
        target_x_left = x_offset
        for x_left in range(x_offset - 1, -1, -1):
            if self.pieces[y_offset][x_left].state != self.last_puted_color and self.is_already_put(x_left, y_offset): # 違う色なら
                continue
            if (self.pieces[y_offset][x_left].state == self.last_puted_color) and (x_left is not x_offset):
                target_x_left = x_left
                break
            else:
                break

        # コマを置いた右側
        target_x_right = x_offset
        for x_right in range(x_offset + 1, 8):
            if self.pieces[y_offset][x_right].state != self.last_puted_color and self.is_already_put(x_right, y_offset): # 違う色なら
                continue
            if (self.pieces[y_offset][x_right].state == self.last_puted_color) and (x_right is not x_offset):
                target_x_right = x_right
                break
            else:
                break

        # 書き換え
        for x in range(x_offset - 1, target_x_left, -1):
            self.pieces[y_offset][x].reverse_piece()

        for x in range(x_offset + 1, target_x_right):
            self.pieces[y_offset][x].reverse_piece()

        ########################################
        # 列
        ########################################
        # コマを置いた上側
        target_y_upper = y_offset
        for y_upper in range(y_offset - 1, -1, -1):
            if self.pieces[y_upper][x_offset].state != self.last_puted_color and self.is_already_put(x_offset, y_upper): # 違う色なら
                continue
            if (self.pieces[y_upper][x_offset].state == self.last_puted_color) and (y_upper is not y_offset):
                target_y_upper = y_upper
                break
            else:
                break

        # コマを置いた下側
        target_y_lower = y_offset
        for y_lower in range(y_offset + 1, 8):
            if self.pieces[y_lower][x_offset].state != self.last_puted_color and self.is_already_put(x_offset, y_lower): # 違う色なら
                continue
            if (self.pieces[y_lower][x_offset].state == self.last_puted_color) and (y_lower is not y_offset):
                target_y_lower = y_lower
                break
            else:
                break

        # 書き換え
        for y in range(y_offset - 1, target_y_upper, -1):
            self.pieces[y][x_offset].reverse_piece()

        for y in range(y_offset + 1, target_y_lower):
            self.pieces[y][x_offset].reverse_piece()


        ########################################
        # 右上がり斜め
        ########################################
        # コマを置いた左下側
        target_x_left = x_offset
        target_y_lower = y_offset
        for i in range(1, 8):
            x_left = x_offset - i
            y_lower = y_offset + i
            if x_left < 0 or y_lower > 7: # 壁にぶつかったら
                break
            if self.pieces[y_lower][x_left].state != self.last_puted_color and self.is_already_put(x_left,y_lower):  # 違う色なら
                continue
            if (self.pieces[y_lower][x_left].state == self.last_puted_color) and (x_left is not x_offset) and (y_lower is not y_offset):
                target_x_left  = x_left
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
            if self.pieces[y_upper][x_right].state != self.last_puted_color and self.is_already_put(x_right,y_upper): # 違う色なら
                continue
            if (self.pieces[y_upper][x_right].state == self.last_puted_color) and (x_right is not x_offset) and (y_upper is not y_offset):
                target_x_right = x_right
                target_y_upper = y_upper
                break
            else:
                break

        # 書き換え
        for i in range(1, abs(target_x_left - x_offset)):
            x = x_offset - i
            y = y_offset + i
            self.pieces[y][x].reverse_piece()

        for i in range(1, abs(target_x_right - x_offset)):
            x = x_offset + i
            y = y_offset - i
            self.pieces[y][x].reverse_piece()

        ########################################
        # 右下がり斜め
        ########################################
        # コマを置いた左上側
        target_x_left  = x_offset
        target_y_upper = y_offset
        for i in range(1, 8):
            x_left  = x_offset - i
            y_upper = y_offset - i
            if x_left < 0 or y_upper < 0: # 壁にぶつかったら
                break
            if self.pieces[y_upper][x_left].state != self.last_puted_color and self.is_already_put(x_left,y_upper): # 違う色なら
                continue
            if (self.pieces[y_upper][x_left].state == self.last_puted_color) and (x_left is not x_offset) and (y_upper is not y_offset):
                target_x_left  = x_left
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
            # print(type(self.pieces[y_lower][x_right]))
            if self.pieces[y_lower][x_right].state != self.last_puted_color and self.is_already_put(x_right,y_lower): # 違う色なら
                continue
            if (self.pieces[y_lower][x_right].state == self.last_puted_color) and (x_right is not x_offset) and (y_lower is not y_offset):
                target_x_right = x_right
                target_y_lower = y_lower
                break
            else:
                break

        # 書き換え
        for i in range(1, abs(target_x_left - x_offset)):
            x = x_offset - i
            y = y_offset - i
            self.pieces[y][x].reverse_piece()

        for i in range(1, abs(target_x_right - x_offset)):
            x = x_offset + i
            y = y_offset + i
            self.pieces[y][x].reverse_piece()

    def black_is_win(self):
        if self.calc_black_area() > self.calc_white_area():
            return True
        if self.calc_black_area() < self.calc_white_area():
            return False
        return None  # Noneを返せば引き分け