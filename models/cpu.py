import random
from random import randint
from .color import Color
from .board import Board

class Cpu:
    def __init__(self, name: str, color: Color, board: Board) -> None:
        self.piece_has = 32 #オセロのコマの所持数
        self.name = name
        self.color = color #WHITE or BLACK
        self.board = board
    
    # def put_piece(self) -> None:
    #     self.piece_has -= 1

    def put_piece(self) -> None:
        print("{}の手番です".format(self.name))
        flag = False
        for x in str(randint(1, 8)):
            for y in str(randint(1, 8)):
                if [x, y] in self.board.list_of_placeable_square(self):
                    p_puts = [x, y]
                    flag = True
                    break
            if flag:
                break
        # p_puts = [str(randint(1, 8)), str(randint(1, 8))]
        # if p_puts[0] == 'q':
        #     self.game.finish_game()      
        px = int(p_puts[0]) - 1
        py = int(p_puts[1]) - 1
        return px, py