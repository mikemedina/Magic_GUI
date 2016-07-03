from ui.player_card import PlayerCard
from tkinter import *
import ui.menu

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
            command=lambda: ui.menu.Menu(self.root), font=gen_font) 
        self.btn_menu.configure(fg='white', bg='black', bd=0)
        self.btn_menu.pack(fill=X)

    def add_player(self, player):
        new_player = PlayerCard(self.root, player)

