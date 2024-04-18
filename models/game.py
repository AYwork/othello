from .player import Player
from .color import Color
from .board import Board

class Game:
    def __init__(self) -> None:
        self.p1 = Player("Player1", Color.WHITE) #white
        self.p2 = Player("Player2", Color.BLACK) #black
        self.board = Board()

    def finish_game(self):
        if self.board.black_is_win() is not None:
            if self.board.black_is_win():
                print("黒が勝ちです。")
            if not self.board.black_is_win():
                print("白が勝ちです。")
        if self.board.black_is_win() is None:
            print("引き分けです。")
        exit()


    def turn(self, player: Player) -> None:
        while True:
            p_puts = input("{}の手番です([x y]で座標を指定してください):".format(player.name)).split(" ")

            px = int(p_puts[0])
            py = int(p_puts[1])
            if p_puts[0] == 'q':
                self.finish_game()
            px = int(p_puts[0]) - 1
            py = int(p_puts[1]) - 1
            if self.board.is_already_put(px, py):
                print("その場所には既にコマが置かれています。")
                continue
            self.board.set_piece_to(px, py, player.color)
            print(self.board)
            break

    def play_game(self) -> None:
        self.board.set_piece_to(4, 4, Color.WHITE)
        self.board.set_piece_to(5, 5, Color.WHITE)
        self.board.set_piece_to(4, 5, Color.BLACK)
        self.board.set_piece_to(5, 4, Color.BLACK)
        print(self.board + "\nゲームスタート!")
       
     
        while (self.p1.piece_has != 0) and (self.p2.piece_has != 0):
            self.turn(self.p1)
            self.board.update()
            print(self.board)

            self.turn(self.p2)
            self.board.update()
            print(self.board)

        self.finish_game()