from player.player import Player
from ui.window import Window


if __name__ == '__main__':
    # Create Players
    players = []

    player1 = Player('Medina', 'blue')
    players.append(player1)

    player2 = Player('Corliss', 'white')
    players.append(player2)

    # Create the main window
    window = Window()
    for player in players:
        window.add_player(player)
    window.root.mainloop()

