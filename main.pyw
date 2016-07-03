from player.player import Player
from ui.window import Window
from util.history import load_history


if __name__ == '__main__':
    # Create Players
    players = []

    player1 = Player('Medina', 'blue')
    players.append(player1)

    player2 = Player('Corliss', 'white')
    players.append(player2)

    # Load players
    players = []
    history = load_history()
    for player_name in history:
        player = history[player_name]
        players.append(Player(player_name, player['color'], player['health'], player['wins']))

    # Create the main window
    window = Window()

    for player in players:
        window.add_player(player)
    window.root.mainloop()

