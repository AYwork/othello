import random
from random import randint
from .color import Color

class Cpu:
    def __init__(self, name: str, color: Color) -> None:
        self.piece_has = 32 #オセロのコマの所持数
        self.name = name
        self.color = color #WHITE or BLACK

    
    # def put_piece(self) -> None:
    #     self.piece_has -= 1

    def put_piece(self) -> None:
        print("{}の手番です".format(self.name))
        p_puts = [str(randint(1, 8)), str(randint(1, 8))]
        # if p_puts[0] == 'q':
        #     self.game.finish_game()      
        px = int(p_puts[0]) - 1
        py = int(p_puts[1]) - 1
        return px, py