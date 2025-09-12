from objects.Chess import Chess

class dummy_player:
    def __init__(self):
        pass

    def start_game(self, game, color):
        pass

game = Chess(dummy_player(), dummy_player())

print(game.get_valid_moves("w"))