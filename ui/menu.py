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

