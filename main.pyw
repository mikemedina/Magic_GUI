from player.player import Player
from ui.window import Window
from util.history import load_all_players


if __name__ == '__main__':
    window = Window()

    players = load_all_players()
    for player in players:
        window.add_player(player)
    window.root.mainloop()

