from color import Color
class Piece:
    pieces = ["●","○"]
    def __init__(self, color: Color) -> None:
        self.color = color

    def reverse_piece(self) -> None:#boardが使う
        if self.color == Color.WHITE:
            self.color = Color.BLACK
        else:
            self.color = Color.WHITE

    def get_state(self) -> str:
        if self.color == Color.WHITE:
            return Piece.pieces[1]
        else:
            return Piece.pieces[0]