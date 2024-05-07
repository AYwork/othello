from .color import Color




class Player:
    def __init__(self, name: str, color: Color) -> None:
        self.piece_has = 32 # オセロのコマの所持数
        self.name      = name
        self.color     = color # WHITE or BLACK
    
    def put_piece(self, placeable_list: list) -> None:  
        # プレイヤー1がコマを置く操作
        print(placeable_list)
        while True:
            p_puts = input("{}の手番です([x y]で座標を指定してください):".format(self.name))
            p_puts = p_puts.strip().split(" ")
            if ((int(p_puts[0])-1) < 0) or ((int(p_puts[0])-1) >= 8) or ((int(p_puts[1])-1) < 0) or ((int(p_puts[1])-1) >= 8):
                print("範囲外です。")
                continue
            print(placeable_list)
            print(p_puts)
            if not p_puts in placeable_list:
                print("その場所にはコマを置けません")
                continue
            else:
                break
        # if p_puts[0] == 'q':
        #     self.game.finish_game()      
        px = int(p_puts[0]) - 1
        py = int(p_puts[1]) - 1
        return px, py