from tkinter import *
from util.history import update_history


class PlayerCard:
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

