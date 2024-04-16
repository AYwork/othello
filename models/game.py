from .player import Player
from .color import Color
from .board import Board

class Game:
    def __init__(self) -> None:
        self.p1 = Player("Player1", Color.WHITE) #white
        self.p2 = Player("Player2", Color.BLACK) #black
        self.board = Board()

    def turn(self, player: Player) -> None:
        while True:
            p_puts = input("{}の手番です([x y]で座標を指定してください):".format(player.name)).split(" ")
            px = int(p_puts[0])
            py = int(p_puts[1])
            if self.board.is_already_put(px, py):
                print("その場所には既にコマが置かれています。")
                continue
            self.board.set_piece_to(px, py, player.color)
            print(self.board)
            break

    def play_game(self) -> None:
        self.board.set_piece_to(4, 4, Color.WHITE.value["value"])
        self.board.set_piece_to(5, 5, Color.WHITE.value["value"])
        self.board.set_piece_to(4, 5, Color.BLACK.value["value"])
        self.board.set_piece_to(5, 4, Color.BLACK.value["value"])
        print(self.board + "\nゲームスタート!")
       
        while True:
            self.turn(self.p1)
            self.turn(self.p2)