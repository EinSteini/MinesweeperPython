import tkinter as tk


class Window:
    hf = tk.Tk()
    menu = tk.Menu(hf)
    buttonPictures = [[],[],[],[],[],[],[],[]]
    bgPictures = [[],[],[],[],[],[],[],[]]
    buttons = [[],[],[],[],[],[],[],[]]
    zahlen = []

    def __init__(self):
        self.hf.title("Minesweeper")
        self.hf.resizable(0, 0)
        self.hf.config(menu=self.menu)

        self.designmenu = tk.Menu(self.menu)
        self.wmenu = tk.Menu(self.menu)
        self.menu.add_cascade(label="Design", menu=self.designmenu)
        self.menu.add_cascade(label="Weiteres", menu=self.wmenu)
        selected_design = tk.StringVar(self.hf, "Normal")
        self.designmenu.add_radiobutton(label="Normal", variable=selected_design,
                                   command=self.normaldesign)  # Zum Designmenu werden beide Optionen hinzugefügt
        self.designmenu.add_radiobutton(label="Sommer", variable=selected_design, command=self.sommerdesign)
        self.wmenu.add_command(label="Highscoreliste",
                            command=self.highscorel)  # Zum weiteren Menu werden alle 3 Optionen hinzugefügt
        self.wmenu.add_command(label="Tutorial", command=self.tutorial)
        self.wmenu.add_command(label="About", command=self.about)

        self.nichts = tk.PhotoImage(file="Pictures/nichts.gif")  # es werden alle Bilder hinzugefügt
        self.flagge = tk.PhotoImage(file="Pictures/flagge.gif")
        self.fragezeichen = tk.PhotoImage(file="Pictures/fragezeichen.gif")
        self.bombe = tk.PhotoImage(file="Pictures/bombe.gif")
        self.smileylebt = tk.PhotoImage(file="Pictures/smileylebt.gif")
        self.smileytot = tk.PhotoImage(file="Pictures/smileytot.gif")
        self.hintergrund_zeit = tk.PhotoImage(file="Pictures/hintergrund.gif")

        for i in range(8):
            for j in range(8):
                self.buttonPictures[i].append(tk.PhotoImage(file="Pictures/"+str(i)+str(j)+".gif"))
                self.bgPictures[i].append(tk.Label(self.hf, image=self.nichts))
                self.bgPictures[i][j].grid(row=j+1, column=i)
                self.buttons[i].append(Button(self.hf, row=j+1, column=i, height=20, width=20, image=self.nichts))

        self.zahlen.append(tk.PhotoImage(file="Pictures/eins.gif"))
        self.zahlen.append(tk.PhotoImage(file="Pictures/zwei.gif"))
        self.zahlen.append(tk.PhotoImage(file="Pictures/drei.gif"))
        self.zahlen.append(tk.PhotoImage(file="Pictures/vier.gif"))
        self.zahlen.append(tk.PhotoImage(file="Pictures/fuenf.gif"))
        self.zahlen.append(tk.PhotoImage(file="Pictures/sechs.gif"))
        self.zahlen.append(tk.PhotoImage(file="Pictures/sieben.gif"))
        self.zahlen.append(tk.PhotoImage(file="Pictures/acht.gif"))

        self.hf.mainloop()

    def normaldesign(self):
        print("Todo")

    def sommerdesign(self):
        print("Todo")

    def highscorel(self):
        print("Todo")

    def tutorial(self):
        print("Todo")

    def about(self):
        print("Todo")

class Button:
    def __init__(self, parent, row, column, image, height=20, width=20):
        self.button = tk.Button(parent, height=height, width=width, image=image)
        self.button.grid(row=row, column=column)

class Background:
    def __init__(self, parent, row, column, image, height=20, width=20):

