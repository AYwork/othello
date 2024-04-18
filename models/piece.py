from .color import Color


class Piece:
    def __init__(self, color: Color, x: int, y: int) -> None:
        self.color = color
        self.x = x
        self.y = y
    
    def __str__(self):
        return self.color.val


    def reverse_piece(self) -> None:#boardが使う
        if self.color == Color.BLACK:
            self.color = Color.WHITE
        elif self.color == Color.WHITE:
            self.color = Color.BLACK
        else:
            self.color = Color.SPACE

    def get_state(self) -> str:
        if self.color == Color.WHITE:
            return Color.BLACK
        else:
            return Color.WHITE
        