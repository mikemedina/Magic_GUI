from player.player import Player
from ui.window import Window
from util.history import load_history


if __name__ == '__main__':
    # Load players
    players = [Player(player_name, player['color'], player['health'], player['wins'])
               for player_name, player in load_history().items()]

    # Create the main window
    window = Window()

    for player in players:
        window.add_player(player)
    window.root.mainloop()

