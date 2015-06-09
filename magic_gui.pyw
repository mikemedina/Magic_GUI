#             To Do
#
# 1. Implement menu button
#     a. A way to add players on the fly
#     b. Player color picker
#         i. Error checking on color entry
# 2. An 'X' to remove a player panel
# 3. Fix documentation and indentation
# 4. Fix frm_menu columnspan
# 5. Fix win label overlap when single digit health
# 6. Add way to edit history data
#

from json import dump, load
from tkinter import *

HISTORY_PATH = 'c:/users/mike/desktop/MAGIC_GUI/magic_score.json'

class Window:
    """The main window"""
    def __init__(self):
        gen_font = ('Times', 12, 'bold')

        self.root = Tk()
        self.root.title('Magic Scoreboard')
        self.root.resizable(0, 0)

        self.frm_menu_container = Frame(self.root, bg='blue')
        self.frm_menu_container.grid(row=1, columnspan=100, sticky=W+E)

        self.btn_menu = Button(self.frm_menu_container, text='Menu',
            command=lambda: Menu(self.root), font=gen_font) 
        self.btn_menu.configure(fg='white', bg='black', bd=0)
        self.btn_menu.pack(fill=X)

    def add_player(self, player):
        new_player = PlayerGUI(self.root, player)


class Menu:
    """The settings menu"""
    def __init__(self, parent):

        self.parent = parent

        self.root = Tk()
        self.root.title('Settings')
        self.root.resizable(0, 0)

        self.btn_add_player = Button(self.root, text='Add player',
            command=lambda: self.window_add_player())
        self.btn_add_player.pack()
        
        self.root.mainloop()

    def window_add_player(self):
        new_player_dialog = Tk()
        new_player_dialog.title('New Player')
        new_player_dialog.resizable(0, 0)

        lbl_player_name = Label(new_player_dialog, text='Player name:')
        lbl_player_name.grid(row=0)
        txt_player_name = Entry(new_player_dialog)
        txt_player_name.grid(row=0, column=1)

        lbl_player_color = Label(new_player_dialog, text='Player color:')
        lbl_player_color.grid(row=1)
        txt_player_color = Entry(new_player_dialog)
        txt_player_color.grid(row=1, column=1)

        btn_accept = Button(new_player_dialog, text='Accept',
            command=lambda: self.add_player(
                txt_player_name.get(), txt_player_color.get().lower()))
        btn_accept.grid(row=2, column=1, sticky=E)


    def add_player(self, name, color):
        new_player = Player(name, color)
        new_player_gui = PlayerGUI(self.parent, new_player)


class PlayerGUI:
    """Player information"""
    existing_players = []

    def __init__(self, parent_frame, player):
        gen_font = ('Times', 30, 'bold')
        name_font = ('Times', 30)
        health_font = ('Times', 70)
        wins_font = ('Times', 16)

        # Player representations
        self.player = player
        self.existing_players.append(self)

        # Container
        col_num = len(self.existing_players)-1
        self.frm_container = Frame(parent_frame, bg='black')
        self.frm_container.grid(row=0, column=col_num)

        # Wins Frame
        self.frm_wins = Frame(self.frm_container, bg='black')
        self.frm_wins.grid_columnconfigure(0, weight=1)
        self.frm_wins.grid_columnconfigure(1, weight=1)
        self.frm_wins.pack(fill=X)

        self.lbl_wins = Label(self.frm_wins, font=gen_font,
            text=self.player.wins, bg='black', fg='white')
        self.lbl_wins.grid(row=0, rowspan=2, columnspan=2)

        # Wins up
        self.btn_wins_up = Button(self.frm_wins, text='+', font=wins_font,
            command=lambda: self.update_wins(1))
        self.btn_wins_up.configure(fg='white', bg='black', bd=0)
        self.btn_wins_up.grid(row=0, column=1, sticky=S)

        # Wins down
        self.btn_wins_down = Button(self.frm_wins, text='-', font=wins_font,
            command=lambda: self.update_wins(-1))
        self.btn_wins_down.configure(fg='white', bg='black', bd=0)
        self.btn_wins_down.grid(row=1, column=1, sticky=N)

        # Stats Frame
        self.frm_stats = Frame(self.frm_container, bg='black')
        self.frm_stats.pack()

        # Player button
        self.btn_name = Button(self.frm_stats, text=self.player.name, font=name_font,
            command=lambda: self.game_over())
        self.btn_name.configure(bg=self.player.color, bd=0)
        self.btn_name.grid(row=0, columnspan=2, padx=3, sticky=N+S+E+W)

        # Health
        self.lbl_health = Label(self.frm_stats, font=health_font,
            text=self.player.health, fg='white')
        self.lbl_health.bind('<Button-1>', self.health_by_5)
        self.lbl_health.bind('<Button-3>', self.health_by_5)
        self.lbl_health.configure(bg='black')
        self.lbl_health.grid(row=1, rowspan=2, padx=(10, 0))

        # Health up
        self.btn_health_up = Button(self.frm_stats, text='+', font=gen_font,
            command=lambda: self.update_health(1))
        self.btn_health_up.configure(bg='black', fg='white', bd=0)
        self.btn_health_up.grid(row=1, column=1, sticky=W+E)

        # Health down
        self.btn_health_down = Button(self.frm_stats, text='-', font=gen_font,
            command=lambda: self.update_health(-1))
        self.btn_health_down.configure(background='black', fg='white', bd=0)
        self.btn_health_down.grid(row=2, column=1, sticky=W+E)

    def update_health(self, change=None):
        """Update the player's health"""
        self.player.health_change(change)
        self.lbl_health['text'] = self.player.health
        update_history(self.player)

    def update_wins(self, change=1):
        """Update the player's score"""
        self.player.wins_change(change)
        self.lbl_wins['text'] = self.player.wins
        update_history(self.player)

    def health_by_5(self, event):
        """Left/Right click on health to change it by +5/-5 respectively"""
        if event.num == 1:
            self.update_health(5)
        else:
            self.update_health(-5)

    def game_over(self):
        """Increase the winner's wins by one and reset the health of all players"""
        self.update_wins()
        for p in self.existing_players:
            p.player.reset_health()
            p.update_health()

    def remove_player(self):
        self.existing_players
        self.frm_container.destroy()


class Player:
    def __init__(self, name, color, health=20, wins=0):
        """Create a new player"""
        self.name = name
        self.color = color
        self.health = health
        self.wins = 0

        try:
            self.load_stats()
        except KeyError:
            pass

    def __repr__(self):
        return self.name

    def load_stats(self):
        """Update player stats from game_history"""
        game_history = HISTORY_PATH

        data = {}
        with open(game_history, 'r') as f:
            data = load(f)
        self.wins = data[self.name]['wins']
        self.health = data[self.name]['health']

    def reset_health(self):
        """Set player's health to default"""
        self.health = 20

    def health_change(self, change=None):
        """Change player's health by given amount, or reset to default"""
        if not change:
            self.reset_health()
            return

        self.health += change

    def wins_change(self, change):
        """Change player's wins by given amount"""
        if self.wins + change >= 0:
            self.wins += change


def update_history(player):
    """Update the player's wins and health"""
    game_history = HISTORY_PATH

    data = {}
    with open(game_history, 'r') as f:
        data = load(f)

    try:
        data[player.name]['health'] = player.health
        data[player.name]['wins'] = player.wins
    except KeyError:
        data[player.name] = {'health': player.health,
                             'wins': player.wins}

    with open(game_history, 'w') as f:
        dump(data, f)


if __name__ == '__main__':
    # Create Players
    players = []
    player1 = Player('Medina', 'blue')
    players.append(player1)
    player2 = Player('Corliss', 'white')
    players.append(player2)

    ##Example players
    #player3 = Player('Callie', 'green')
    #players.append(player3)
    #player4 = Player('Victoria', 'purple')
    #players.append(player4)
    #player5 = Player('Caitlin', 'red')
    #players.append(player5)

    # Create Main
    window = Window()
    for player in players:
        window.add_player(player)
    window.root.mainloop()
