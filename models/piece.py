from .color import Color


class Piece:
    states = Color
    def __init__(self, x: int, y: int) -> None:
        self.state = Color.SPACE
        self.x     = x
        self.y     = y

    def set_state(self, color: Color) -> None:
        self.state = color

    def reverse_piece(self) -> None: 
        # コマを反転させる
        if self.state == Color.BLACK:
            self.state = Color.WHITE
        elif self.state == Color.WHITE:
            self.state = Color.BLACK
        else:
            self.state = Color.SPACE

    def __str__(self):
        return self.state