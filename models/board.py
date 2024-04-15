from color import Color
from piece import Piece
class Board:
    board = []
    def __init__(self) -> None:
        self.board.append("・・・・・・・・")
        self.board = self.board * 8

    def __str__(self) -> str:
        stage = "\n".join(self.board)
        return stage
    
    def __add__(self, another: str) -> str:
        return self.__str__() + another
    
    def is_already_put(self, x: int, y: int) -> bool:
        if self.board[y-1][x-1] != "・":
            return True
    
    def set_piece_to(self, x: int, y: int, color: Color) -> None: #pieceを置くときに呼ぶ
        piece = Piece(color)
        raw_row = self.board[y-1]

        tmp_row = raw_row[:(x-1)] + piece.get_state() + raw_row[x:]
        self.board[y-1] = tmp_row

    def update_board(self) -> None:#board上のpiece色を演算し、更新　#pieceプレイヤーが置くのと、boardで裏返ったりする２種類の挙動がある
        pass