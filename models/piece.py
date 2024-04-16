from .color import Color


class Piece:
    def __init__(self, color: Color) -> None:
        self.color = color

    def reverse_piece(self) -> None:#boardが使う
        if self.color == 0:
            self.color = 1
        else:
            self.color = 0

    def get_state(self) -> str:
        if self.color == Color.WHITE.value["value"]:
            return Color.BLACK.value["value"]
        else:
            return Color.WHITE.value["value"]