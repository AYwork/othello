from typing import Union
from .color import Color
from .board import Board
from .player import Player
from .cpu import Cpu
from .piece import Piece

class Game:
    def __init__(self) -> None:
        self.p1    = Player("Player1", Color.WHITE) # white
        self.p2    = Cpu("Player2", Color.BLACK) # black
        self.board = Board()

    def finish_game(self):
        # ゲームを終わらせる
        if self.board.black_is_win() is not None:
            if self.board.black_is_win():
                print("黒が勝ちです。")
            if not self.board.black_is_win():
                print("白が勝ちです。")
        if self.board.black_is_win() is None:
            print("引き分けです。")
        exit()

    def turn(self, player: Union[Player, Cpu]) -> None:
        # 石をおく
        placeable_list = self.board.get_placeable_list(player)
        px, py = player.put_piece(placeable_list)
        self.board.set_piece_to(px, py, player.color)
    
    def play_game(self) -> None:
        # ゲームスタートから終わりまでの流れ
        self.board.set_piece_to(3, 3, Color.WHITE)
        self.board.set_piece_to(4, 4, Color.WHITE)
        self.board.set_piece_to(3, 4, Color.BLACK)
        self.board.set_piece_to(4, 3, Color.BLACK)
        print(self.board + "\nゲームスタート!\n(qでゲームを中断して終了します)")

        # while (self.p1.piece_has != 0) and (self.p2.piece_has != 0):
        while not (self.p1.has_no_piece) and not (self.p2.has_no_piece):    
            self.turn(self.p1)
            self.board.update()
            print(self.board)

            self.turn(self.p2)
            self.board.update()
            print(self.board)
        self.finish_game()