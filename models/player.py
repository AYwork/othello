from color import Color
class Player:
    def __init__(self, name: str, color: Color) -> None:
        self.piece_has = 32 #オセロのコマの所持数
        self.name = name
        self.color = color #WHITE or BLACK
    
    def put_piece(self) -> None:
        self.piece_has -= 1