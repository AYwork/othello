from .color import Color
from .board import Board



class Player:
    def __init__(self, name: str, color: Color,board: Board) -> None:
        self.piece_has = 32 #オセロのコマの所持数
        self.name = name
        self.color = color #WHITE or BLACK
        self.board = board
     
    # def put_piece(self) -> None:
    #     self.piece_has -= 1

    def put_piece(self) -> None:
        p_puts = input("{}の手番です([x y]で座標を指定してください):".format(self.name))
        p_puts = p_puts.strip().split(" ")

        # if p_puts[0] == 'q':
        #     self.game.finish_game()      
        px = int(p_puts[0]) - 1
        py = int(p_puts[1]) - 1
        return px, py