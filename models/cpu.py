import random
from random import randint
from .color import Color


class Cpu:
    def __init__(self, name: str, color: Color) -> None:
        self.piece_has = 32 # オセロのコマの所持数
        self.name      = name
        self.color     = color # WHITE or BLACK
        
    def put_piece(self, placeable_list: list) -> None:
        #cpuがコマをおく操作
        print("{}の手番です".format(self.name))
        p_puts = random.choice(placeable_list)

        px = int(p_puts[0]) - 1
        py = int(p_puts[1]) - 1
        return px, py
    
    def has_no_piece(self) -> bool:
        if self.piece_has == 0:
            return True
        else:
            return False        
        
    # if p_puts[0] == 'q':
        #     self.game.finish_game()      