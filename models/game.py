from typing import Union
from .color import Color
from .board import Board
from .player import Player
from .cpu import Cpu
from .piece import Piece

class Game:
    def __init__(self) -> None:
        self.p1 = Player("Player1", Color.WHITE) #white
        self.p2 = Cpu("Player2", Color.BLACK) #black
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

    def turn(self, player: Union[Player, Cpu]) -> None:
        while True: # 石をおく
            # print(self.board.list_of_placeable_squares(player))
            px, py = player.put_piece()
            if (px < 0) or (px >= 8) or (py < 0) or (py >= 8):
                print("範囲外です。")
                continue
            if self.board.judge_to_put(px, py, player.color):
                print("その場所にはコマを置けません")
                continue
            # print(px, py)
            if self.board.is_already_put(px, py):
                print("その場所には既にコマが置かれています。")
                continue
            # print(px, py)
            self.board.set_piece_to(px, py, player.color)
            break
       

    def play_game(self) -> None:
        self.board.set_piece_to(3, 3, Color.WHITE)
        self.board.set_piece_to(4, 4, Color.WHITE)
        self.board.set_piece_to(3, 4, Color.BLACK)
        self.board.set_piece_to(4, 3, Color.BLACK)
        print(self.board + "\nゲームスタート!\n(qでゲームを中断して終了します)")

        while (self.p1.piece_has != 0) and (self.p2.piece_has != 0):
            self.turn(self.p1)
            self.board.update()
            print(self.board)

            self.turn(self.p2)
            self.board.update()
            print(self.board)
        self.finish_game()