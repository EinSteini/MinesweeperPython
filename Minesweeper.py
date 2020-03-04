
## -- BIBLIOTHEKEN --
from random import randint
from tkinter import *
from time import clock
from threading import Thread

## -- VARIABLEN --
amine = 1
zaever1 = -1
zaever2 = 0
anomi = [   [" "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "]   ]

anomis =[   ["O","O","O","O","O","O","O","O"],
            ["O","O","O","O","O","O","O","O"],
            ["O","O","O","O","O","O","O","O"],
            ["O","O","O","O","O","O","O","O"],
            ["O","O","O","O","O","O","O","O"],
            ["O","O","O","O","O","O","O","O"],
            ["O","O","O","O","O","O","O","O"],
            ["O","O","O","O","O","O","O","O"]   ]
bidnl = []
bidn = 0
tot = False
fehlende_flaggen = 0
gewonnen = 0
rfx = []
rfy = []
xben = []
yben = []
ende = 0
altezeit = -1
ersterzug = True
uhrstart = False
timestr = "00 : 00"
score=[["",0],["",0],["",0],["",0],["",0],["",0],["",0],["",0],["",0],["",0]]

## -- FUNKTIONEN --
def tutorial(): # Das Tutorialfenster
    tut = Tk() # Fenster aufbauen
    tut.title("Tutorial") # Fenstertitel setzen
    tut.iconbitmap("Pictures/icon.ico") # Fenstericon setzen
    tut.resizable(0,0) # Die Größe des Fensters lässt sich nicht mehr verändern
    Label(tut, text=("Bei Minesweeper muss man veruschen, alle Felder aufzudecken,\n",# Text, \n ist ein Zeilenumbruch
                     "ohne dabei Bomben zu treffen. Dabei helfen die Zahlen. Diese \n",
                     "haben den Wert der Anzahl der umliegenden Bomben. Wenn also \n",
                     "eine Eins auf dem Spielfeld steht, ist im direkten Umfeld \n",
                     "dieses Felds eine Bombe. Nicht mehr und nicht weniger.")).pack()
    tut.mainloop()
    
def about(): # Das Aboutfenster
    ab = Tk() # tkinter
    ab.title("About")
    ab.iconbitmap("Pictures/icon.ico")
    ab.resizable(0,0)
    Label(ab, text="Ein Spiel von:").pack()
    Label(ab).pack()
    Label(ab, text="Connor Frede").pack()
    Label(ab, text="Louis Kopetzki").pack()
    Label(ab, text="Alexander Raffler").pack()
    Label(ab, text="Nils Steinkamp").pack()
    ab.mainloop()
    
def highscore(winnername, zeit): # Highscores lesen und eintragen
    global score
    t = 0
    f = open("score.txt", "r") # Datei öffnen
    for line in f: # Jede Zeile der Datei lesen
        data = line.strip().split("\t") #"\n" am Ende löschen und am "\t" aufsplitten
        score[t][0] = data[0]
        dataint = int(data[1])
        score[t][1] = dataint# Daten in score einfügen
        t += 1
    f.close() # Datei schließen

    for i in range(10): # Den neuen Wert einsortieren
        if zeit < score[i][1]: # Falls der Highscore kleiner ist als der i-te Wert der Liste,
            for j in range(10-i):# wird dieser dort eingetragen und alle anderen Werte nach hinten geschoben
                score[9-j] = score[8-j]
            score[i] = [winnername, zeit]
            break

    f = open("score.txt", "w") # Datei öffnen
    for name, punkte in score: # Wertepaare aus string lesen
        f.write("%s\t%i\n" % (name, punkte)) # Als String in Datei schreiben
    f.close() # Datei schließen
    
def stoppuhr(): # Die Stoppuhr
    global altezeit, zeit, zeitanzeige, anomis, timestr, uhrstart, az
    if uhrstart == True: # Damit die Uhr erst beim aufdecken des ersten Feldes startet
        zeit = clock() -az # Beim Start wird einmal clock() aufgerufen. az sorgt dafür, dass, wenn neugestartet wurde, die Zeit bei 0 startet.
        while zeit - altezeit <= 1: # Damit nicht ständig die Grafik geupdatet wird, wird solange gewartet, bis zeit einen neuen Wert hat
            zeit = clock() - az
            if uhrstart == False: # Falls währenddessen das Spiel beendet wird, läuft auch die Uhr nicht weiter
                break
        altezeit = zeit
        minutes = zeit /  60 
        seconds = zeit % 60
        timestr = ('%02d : %02d' % (minutes, seconds))
        zeitanzeige["text"] = timestr # Die Grafik wird geupdatet
        zeit = int(zeit)
        stoppuhr() # Die Funktion wird neu gestartet
    while uhrstart == False: # Sobald das Spiel wieder startet, wird auch die Uhr wieder gestartet
        if uhrstart == True:
            stoppuhr()
            
def winnerfunc(): 
    global zeit, score
    gewinner = winnername.get() # Der eigegebenen Name wird eingelesen
    highscore(gewinner, zeit) # und die Funtion Highscore mit beiden Werten ausgeführt
    gwf.destroy() # Danach wird das Fenster geschlossen
    highscorel() # und die Highscoreliste aufgerufen
    
def highscorel(): # Die Higscoreliste wird angezeigt
    hs = Tk() # tkinter 
    hs.title("Highscoreliste")
    hs.iconbitmap("Pictures/icon.ico")
    hs.resizable(0,0)
    Label(hs, text="PLATZ").grid(row=0, column=0)
    Label(hs, text="NAME").grid(row=0, column=1)
    Label(hs, text="ZEIT").grid(row=0, column=2)
    Label(hs).grid(row=1)
    for i in range(10): # Highscoreliste wird abgebildet
        zeit = score[i][1]
        minutes = zeit / 60
        seconds = zeit % 60
        timestr = ('%02d : %02d' % (minutes, seconds))
        Label(hs, text=(i+1)).grid(row=i+2, column=0)
        Label(hs, text=score[i][0]).grid(row=i+2, column=1)
        Label(hs, text=timestr).grid(row=i+2, column=2)
    hs.mainloop()
    
def f00l(event): # Linksklick auf die verschiedenen Buttons
    if anomis[0][0] != "f" and anomis[0][0] != "?": # Wenn das Feld nicht als Flagge oder Fragezeichen markiert ist, 
        anomis[0][0] = anomi[0][0] # wird das Feld aufgedeckt
        bombenfeld(0,0) # Es wird getestet, ob auf dem Feld eine Bombe ist und, ob es der erste Zug ist.
        if anomis[0][0] == " ": # Wenn das Feld frei ist,
            felderaufdecken(0,0) # wird felderaufdecken() ausgeführt
        refresh() # Am Ende wird die Grafik geupdatet
def f01l(event): # Genau das selbe für deie verchsiedenen Felder, weil wir es nicht geschafft haben beim Aufrufen Attribute zu übergeben.
    if anomis[1][0] != "f" and anomis[1][0] != "?":
        anomis[1][0] = anomi[1][0]
        bombenfeld(0,1)
        if anomis[1][0] == " ":
            felderaufdecken(0,1)
        refresh()
def f02l(event):
    if anomis[2][0] != "f" and anomis[2][0] != "?":
        anomis[2][0] = anomi[2][0]
        bombenfeld(0,2)
        if anomis[2][0] == " ":
            felderaufdecken(0,2)
        refresh()
def f03l(event):
    if anomis[3][0] != "f" and anomis[3][0] != "?":
        anomis[3][0] = anomi[3][0]
        bombenfeld(0,3)
        if anomis[3][0] == " ":
            felderaufdecken(0,3)
        refresh()
def f04l(event):
    if anomis[4][0] != "f" and anomis[4][0] != "?":
        anomis[4][0] = anomi[4][0]
        bombenfeld(0,4)
        if anomis[4][0] == " ":
            felderaufdecken(0,4)
        refresh()
def f05l(event):
    if anomis[5][0] != "f" and anomis[5][0] != "?":
        anomis[5][0] = anomi[5][0]
        bombenfeld(0,5)
        if anomis[5][0] == " ":
            felderaufdecken(0,5)
        refresh()
def f06l(event):
    if anomis[6][0] != "f" and anomis[6][0] != "?":
        anomis[6][0] = anomi[6][0]
        bombenfeld(0,6)
        if anomis[6][0] == " ":
            felderaufdecken(0,6)
        refresh()
def f07l(event):
    if anomis[7][0] != "f" and anomis[7][0] != "?":
        anomis[7][0] = anomi[7][0]
        bombenfeld(0,7)
        if anomis[7][0] == " ":
            felderaufdecken(0,7)
        refresh()
def f10l(event):
    if anomis[0][1] != "f" and anomis[0][1] != "?":
        anomis[0][1] = anomi[0][1]
        bombenfeld(1,0)
        if anomis[0][1] == " ":
            felderaufdecken(1,0)
        refresh()
def f11l(event):
    if anomis[1][1] != "f" and anomis[1][1] != "?":
        anomis[1][1] = anomi[1][1]
        bombenfeld(1,1)
        if anomis[1][1] == " ":
            felderaufdecken(1,1)
        refresh()
def f12l(event):
    if anomis[2][1] != "f" and anomis[2][1] != "?":
        anomis[2][1] = anomi[2][1]
        bombenfeld(1,2)
        if anomis[2][1] == " ":
            felderaufdecken(1,2)
        refresh()
def f13l(event):
    if anomis[3][1] != "f" and anomis[3][1] != "?":
        anomis[3][1] = anomi[3][1]
        bombenfeld(1,3)
        if anomis[3][1] == " ":
            felderaufdecken(1,3)
        refresh()
def f14l(event):
    if anomis[4][1] != "f" and anomis[4][1] != "?":
        anomis[4][1] = anomi[4][1]
        bombenfeld(1,4)
        if anomis[4][1] == " ":
            felderaufdecken(1,4)
        refresh()
def f15l(event):
    if anomis[5][1] != "f" and anomis[5][1] != "?":
        anomis[5][1] = anomi[5][1]
        bombenfeld(1,5)
        if anomis[5][1] == " ":
            felderaufdecken(1,5)
        refresh()
def f16l(event):
    if anomis[6][1] != "f" and anomis[6][1] != "?":
        anomis[6][1] = anomi[6][1]
        bombenfeld(1,6)
        if anomis[6][1] == " ":
            felderaufdecken(1,6)
        refresh()
def f17l(event):
    if anomis[7][1] != "f" and anomis[7][1] != "?":
        anomis[7][1] = anomi[7][1]
        bombenfeld(1,7)
        if anomis[7][1] == " ":
            felderaufdecken(1,7)
        refresh()
def f20l(event):
    if anomis[0][2] != "f" and anomis[0][2] != "?":
        anomis[0][2] = anomi[0][2]
        bombenfeld(2,0)
        if anomis[0][2] == " ":
            felderaufdecken(2,0)
        refresh()
def f21l(event):
    if anomis[1][2] != "f" and anomis[1][2] != "?":
        anomis[1][2] = anomi[1][2]
        bombenfeld(2,1)
        if anomis[1][2] == " ":
            felderaufdecken(2,1)
        refresh()
def f22l(event):
    if anomis[2][2] != "f" and anomis[2][2] != "?":
        anomis[2][2] = anomi[2][2]
        bombenfeld(2,2)
        if anomis[2][2] == " ":
            felderaufdecken(2,2)
        refresh()
def f23l(event):
    if anomis[3][2] != "f" and anomis[3][2] != "?":
        anomis[3][2] = anomi[3][2]
        bombenfeld(2,3)
        if anomis[3][2] == " ":
            felderaufdecken(2,3)
        refresh()
def f24l(event):
    if anomis[4][2] != "f" and anomis[4][2] != "?":
        anomis[4][2] = anomi[4][2]
        bombenfeld(2,4)
        if anomis[4][2] == " ":
            felderaufdecken(2,4)
        refresh()
def f25l(event):
    if anomis[5][2] != "f" and anomis[5][2] != "?":
        anomis[5][2] = anomi[5][2]
        bombenfeld(2,5)
        if anomis[5][2] == " ":
            felderaufdecken(2,5)
        refresh()
def f26l(event):
    if anomis[6][2] != "f" and anomis[6][2] != "?":
        anomis[6][2] = anomi[6][2]
        bombenfeld(2,6)
        if anomis[6][2] == " ":
            felderaufdecken(2,6)
        refresh()
def f27l(event):
    if anomis[7][2] != "f" and anomis[7][2] != "?":
        anomis[7][2] = anomi[7][2]
        bombenfeld(2,7)
        if anomis[7][2] == " ":
            felderaufdecken(2,7)
        refresh()
def f30l(event):
    if anomis[0][3] != "f" and anomis[0][3] != "?":
        anomis[0][3] = anomi[0][3]
        bombenfeld(3,0)
        if anomis[0][3] == " ":
            felderaufdecken(3,0)
        refresh()
def f31l(event):
    if anomis[1][3] != "f" and anomis[1][3] != "?":
        anomis[1][3] = anomi[1][3]
        bombenfeld(3,1)
        if anomis[1][3] == " ":
            felderaufdecken(3,1)
        refresh()
def f32l(event):
    if anomis[2][3] != "f" and anomis[2][3] != "?":
        anomis[2][3] = anomi[2][3]
        bombenfeld(3,2)
        if anomis[2][3] == " ":
            felderaufdecken(3,2)
        refresh()
def f33l(event):
    if anomis[3][3] != "f" and anomis[3][3] != "?":
        anomis[3][3] = anomi[3][3]
        bombenfeld(3,3)
        if anomis[3][3] == " ":
            felderaufdecken(3,3)
        refresh()
def f34l(event):
    if anomis[4][3] != "f" and anomis[4][3] != "?":
        anomis[4][3] = anomi[4][3]
        bombenfeld(3,4)
        if anomis[4][3] == " ":
            felderaufdecken(3,4)
        refresh()
def f35l(event):
    if anomis[5][3] != "f" and anomis[5][3] != "?":
        anomis[5][3] = anomi[5][3]
        bombenfeld(3,5)
        if anomis[5][3] == " ":
            felderaufdecken(3,5)
        refresh()
def f36l(event):
    if anomis[6][3] != "f" and anomis[6][3] != "?":
        anomis[6][3] = anomi[6][3]
        bombenfeld(3,6)
        if anomis[6][3] == " ":
            felderaufdecken(3,6)
        refresh()
def f37l(event):
    if anomis[7][3] != "f" and anomis[7][3] != "?":
        anomis[7][3] = anomi[7][3]
        bombenfeld(3,7)
        if anomis[7][3] == " ":
            felderaufdecken(3,7)
        refresh()
def f40l(event):
    if anomis[0][4] != "f" and anomis[0][4] != "?":
        anomis[0][4] = anomi[0][4]
        bombenfeld(4,0)
        if anomis[0][4] == " ":
            felderaufdecken(4,0)
        refresh()
def f41l(event):
    if anomis[1][4] != "f" and anomis[1][4] != "?":
        anomis[1][4] = anomi[1][4]
        bombenfeld(4,1)
        if anomis[1][4] == " ":
            felderaufdecken(4,1)
        refresh()
def f42l(event):
    if anomis[2][4] != "f" and anomis[2][4] != "?":
        anomis[2][4] = anomi[2][4]
        bombenfeld(4,2)
        if anomis[2][4] == " ":
            felderaufdecken(4,2)
        refresh()
def f43l(event):
    if anomis[3][4] != "f" and anomis[3][4] != "?":
        anomis[3][4] = anomi[3][4]
        bombenfeld(4,3)
        if anomis[3][4] == " ":
            felderaufdecken(4,3)
        refresh()
def f44l(event):
    if anomis[4][4] != "f" and anomis[4][4] != "?":
        anomis[4][4] = anomi[4][4]
        bombenfeld(4,4)
        if anomis[4][4] == " ":
            felderaufdecken(4,4)
        refresh()
def f45l(event):
    if anomis[5][4] != "f" and anomis[5][4] != "?":
        anomis[5][4] = anomi[5][4]
        bombenfeld(4,5)
        if anomis[5][4] == " ":
            felderaufdecken(4,5)
        refresh()
def f46l(event):
    if anomis[6][4] != "f" and anomis[6][4] != "?":
        anomis[6][4] = anomi[6][4]
        bombenfeld(4,6)
        if anomis[6][4] == " ":
            felderaufdecken(4,6)
        refresh()
def f47l(event):
    if anomis[7][4] != "f" and anomis[7][4] != "?":
        anomis[7][4] = anomi[7][4]
        bombenfeld(4,7)
        if anomis[7][4] == " ":
            felderaufdecken(4,7)
        refresh()
def f50l(event):
    if anomis[0][5] != "f" and anomis[0][5] != "?":
        anomis[0][5] = anomi[0][5]
        bombenfeld(5,0)
        if anomis[0][5] == " ":
            felderaufdecken(5,0)
        refresh()
def f51l(event):
    if anomis[1][5] != "f" and anomis[1][5] != "?":
        anomis[1][5] = anomi[1][5]
        bombenfeld(5,1)
        if anomis[1][5] == " ":
            felderaufdecken(5,1)
        refresh()
def f52l(event):
    if anomis[2][5] != "f" and anomis[2][5] != "?":
        anomis[2][5] = anomi[2][5]
        bombenfeld(5,2)
        if anomis[2][5] == " ":
            felderaufdecken(5,2)
        refresh()
def f53l(event):
    if anomis[3][5] != "f" and anomis[3][5] != "?":
        anomis[3][5] = anomi[3][5]
        bombenfeld(5,3)
        if anomis[3][5] == " ":
            felderaufdecken(5,3)
        refresh()
def f54l(event):
    if anomis[4][5] != "f" and anomis[4][5] != "?":
        anomis[4][5] = anomi[4][5]
        bombenfeld(5,4)
        if anomis[4][5] == " ":
            felderaufdecken(5,4)
        refresh()
def f55l(event):
    if anomis[5][5] != "f" and anomis[5][5] != "?":
        anomis[5][5] = anomi[5][5]
        bombenfeld(5,5)
        if anomis[5][5] == " ":
            felderaufdecken(5,5)
        refresh()
def f56l(event):
    if anomis[6][5] != "f" and anomis[6][5] != "?":
        anomis[6][5] = anomi[6][5]
        bombenfeld(5,6)
        if anomis[6][5] == " ":
            felderaufdecken(5,6)
        refresh()
def f57l(event):
    if anomis[7][5] != "f" and anomis[7][5] != "?":
        anomis[7][5] = anomi[7][5]
        bombenfeld(5,7)
        if anomis[7][5] == " ":
            felderaufdecken(5,7)
        refresh()
def f60l(event):
    if anomis[0][6] != "f" and anomis[0][6] != "?":
        anomis[0][6] = anomi[0][6]
        bombenfeld(6,0)
        if anomis[0][6] == " ":
            felderaufdecken(6,0)
        refresh()
def f61l(event):
    if anomis[1][6] != "f" and anomis[1][6] != "?":
        anomis[1][6] = anomi[1][6]
        bombenfeld(6,1)
        if anomis[1][6] == " ":
            felderaufdecken(6,1)
        refresh()
def f62l(event):
    if anomis[2][6] != "f" and anomis[2][6] != "?":
        anomis[2][6] = anomi[2][6]
        bombenfeld(6,2)
        if anomis[2][6] == " ":
            felderaufdecken(6,2)
        refresh()
def f63l(event):
    if anomis[3][6] != "f" and anomis[3][6] != "?":
        anomis[3][6] = anomi[3][6]
        bombenfeld(6,3)
        if anomis[3][6] == " ":
            felderaufdecken(6,3)
        refresh()
def f64l(event):
    if anomis[4][6] != "f" and anomis[4][6] != "?":
        anomis[4][6] = anomi[4][6]
        bombenfeld(6,4)
        if anomis[4][6] == " ":
            felderaufdecken(6,4)
        refresh()
def f65l(event):
    if anomis[5][6] != "f" and anomis[5][6] != "?":
        anomis[5][6] = anomi[5][6]
        bombenfeld(6,5)
        if anomis[5][6] == " ":
            felderaufdecken(6,5)
        refresh()
def f66l(event):
    if anomis[6][6] != "f" and anomis[6][6] != "?":
        anomis[6][6] = anomi[6][6]
        bombenfeld(6,6)
        if anomis[6][6] == " ":
            felderaufdecken(6,6)
        refresh()
def f67l(event):
    if anomis[7][6] != "f" and anomis[7][6] != "?":
        anomis[7][6] = anomi[7][6]
        bombenfeld(6,7)
        if anomis[7][6] == " ":
            felderaufdecken(6,7)
        refresh()
def f70l(event):
    if anomis[0][7] != "f" and anomis[0][7] != "?":
        anomis[0][7] = anomi[0][7]
        bombenfeld(7,0)
        if anomis[0][7] == " ":
            felderaufdecken(7,0)
        refresh()
def f71l(event):
    if anomis[1][7] != "f" and anomis[1][7] != "?":
        anomis[1][7] = anomi[1][7]
        bombenfeld(7,1)
        if anomis[1][7] == " ":
            felderaufdecken(7,1)
        refresh()
def f72l(event):
    if anomis[2][7] != "f" and anomis[2][7] != "?":
        anomis[2][7] = anomi[2][7]
        bombenfeld(7,2)
        if anomis[2][7] == " ":
            felderaufdecken(7,2)
        refresh()
def f73l(event):
    if anomis[3][7] != "f" and anomis[3][7] != "?":
        anomis[3][7] = anomi[3][7]
        bombenfeld(7,3)
        if anomis[3][7] == " ":
            felderaufdecken(7,3)
        refresh()
def f74l(event):
    if anomis[4][7] != "f" and anomis[4][7] != "?":
        anomis[4][7] = anomi[4][7]
        bombenfeld(7,4)
        if anomis[4][7] == " ":
            felderaufdecken(7,4)
        refresh()
def f75l(event):
    if anomis[5][7] != "f" and anomis[5][7] != "?":
        anomis[5][7] = anomi[5][7]
        bombenfeld(7,5)
        if anomis[5][7] == " ":
            felderaufdecken(7,5)
        refresh()
def f76l(event):
    if anomis[6][7] != "f" and anomis[6][7] != "?":
        anomis[6][7] = anomi[6][7]
        bombenfeld(7,6)
        if anomis[6][7] == " ":
            felderaufdecken(7,6)
        refresh()
def f77l(event):
    if anomis[7][7] != "f" and anomis[7][7] != "?":
        anomis[7][7] = anomi[7][7]
        bombenfeld(7,7)
        if anomis[7][7] == " ":
            felderaufdecken(7,7)
        refresh()
def f00r(event): # Rechtsklick auf die verschiedenen Buttons
    global fehlende_flaggen
    if anomis[0][0] != "f" and anomis[0][0] != "?": # Wenn das Feld nicht als Flagge oder Fragezeichen markiert ist,
        anomis[0][0] = "f" # wird dort eine Flagge gesetzt.
    elif anomis[0][0] == "f": # Wenn das Feld eine Flagge ist,
        anomis[0][0] = "?" # wird es ein Fragezeichen.
        fehlende_flaggen -= 1 # fehlende_flaggen wird um 1 vermindert
    else:
        anomis[0][0] = "O" # Im letzten Fall wird das Feld wieder in den Ursprungszustand zurückgesetzt
    refresh() # Die Grafik wird geupdtatet
def f01r(event):
    global fehlende_flaggen
    if anomis[1][0] != "f" and anomis[1][0] != "?":
        anomis[1][0] = "f"
    elif anomis[1][0] == "f":
        anomis[1][0] = "?"
        fehlende_flaggen -= 1
    else:
        anomis[1][0] = "O"
    refresh()
def f02r(event):
    global fehlende_flaggen
    if anomis[2][0] != "f" and anomis[2][0] != "?":
        anomis[2][0] = "f"
    elif anomis[2][0] == "f":
        anomis[2][0] = "?"
        fehlende_flaggen -= 1
    else:
        anomis[2][0] = "O"
    refresh()
def f03r(event):
    global fehlende_flaggen
    if anomis[3][0] != "f" and anomis[3][0] != "?":
        anomis[3][0] = "f"
    elif anomis[3][0] == "f":
        anomis[3][0] = "?"
        fehlende_flaggen -= 1
    else:
        anomis[3][0] = "O"
    refresh()
def f04r(event):
    global fehlende_flaggen
    if anomis[4][0] != "f" and anomis[4][0] != "?":
        anomis[4][0] = "f"
    elif anomis[4][0] == "f":
        anomis[4][0] = "?"
        fehlende_flaggen -= 1
    else:
        anomis[4][0] = "O"
    refresh()
def f05r(event):
    global fehlende_flaggen
    if anomis[5][0] != "f" and anomis[5][0] != "?":
        anomis[5][0] = "f"
    elif anomis[5][0] == "f":
        anomis[5][0] = "?"
        fehlende_flaggen -= 1
    else:
        anomis[5][0] = "O"
    refresh()
def f06r(event):
    global fehlende_flaggen
    if anomis[6][0] != "f" and anomis[6][0] != "?":
        anomis[6][0] = "f"
    elif anomis[6][0] == "f":
        anomis[6][0] = "?"
        fehlende_flaggen -= 1
    else:
        anomis[6][0] = "O"
    refresh()
def f07r(event):
    global fehlende_flaggen
    if anomis[7][0] != "f" and anomis[7][0] != "?":
        anomis[7][0] = "f"
    elif anomis[7][0] == "f":
        anomis[7][0] = "?"
        fehlende_flaggen -= 1
    else:
        anomis[7][0] = "O"
    refresh()
def f10r(event):
    global fehlende_flaggen
    if anomis[0][1] != "f" and anomis[0][1] != "?":
        anomis[0][1] = "f"
    elif anomis[0][1] == "f":
        anomis[0][1] = "?"
        fehlende_flaggen -= 1
    else:
        anomis[0][1] = "O"
    refresh()
def f11r(event):
    global fehlende_flaggen
    if anomis[1][1] != "f" and anomis[1][1] != "?":
        anomis[1][1] = "f"
    elif anomis[1][1] == "f":
        anomis[1][1] = "?"
        fehlende_flaggen -= 1
    else:
        anomis[1][1] = "O"
    refresh()
def f12r(event):
    global fehlende_flaggen
    if anomis[2][1] != "f" and anomis[2][1] != "?":
        anomis[2][1] = "f"
    elif anomis[2][1] == "f":
        anomis[2][1] = "?"
        fehlende_flaggen -= 1
    else:
        anomis[2][1] = "O"
    refresh()
def f13r(event):
    global fehlende_flaggen
    if anomis[3][1] != "f" and anomis[3][1] != "?":
        anomis[3][1] = "f"
    elif anomis[3][1] == "f":
        anomis[3][1] = "?"
        fehlende_flaggen -= 1
    else:
        anomis[3][1] = "O"
    refresh()
def f14r(event):
    global fehlende_flaggen
    if anomis[4][1] != "f" and anomis[4][1] != "?":
        anomis[4][1] = "f"
    elif anomis[4][1] == "f":
        anomis[4][1] = "?"
        fehlende_flaggen -= 1
    else:
        anomis[4][1] = "O"
    refresh()
def f15r(event):
    global fehlende_flaggen
    if anomis[5][1] != "f" and anomis[5][1] != "?":
        anomis[5][1] = "f"
    elif anomis[5][1] == "f":
        anomis[5][1] = "?"
        fehlende_flaggen -= 1
    else:
        anomis[5][1] = "O"
    refresh()
def f16r(event):
    global fehlende_flaggen
    if anomis[6][1] != "f" and anomis[6][1] != "?":
        anomis[6][1] = "f"
    elif anomis[6][1] == "f":
        anomis[6][1] = "?"
        fehlende_flaggen -= 1
    else:
        anomis[6][1] = "O"
    refresh()
def f17r(event):
    global fehlende_flaggen
    if anomis[7][1] != "f" and anomis[7][1] != "?":
        anomis[7][1] = "f"
    elif anomis[7][1] == "f":
        anomis[7][1] = "?"
        fehlende_flaggen -= 1
    else:
        anomis[7][1] = "O"
    refresh()
def f20r(event):
    global fehlende_flaggen
    if anomis[0][2] != "f" and anomis[0][2] != "?":
        anomis[0][2] = "f"
    elif anomis[0][2] == "f":
        anomis[0][2] = "?"
        fehlende_flaggen -= 1
    else:
        anomis[0][2] = "O"
    refresh()
def f21r(event):
    global fehlende_flaggen
    if anomis[1][2] != "f" and anomis[1][2] != "?":
        anomis[1][2] = "f"
    elif anomis[1][2] == "f":
        anomis[1][2] = "?"
        fehlende_flaggen -= 1
    else:
        anomis[1][2] = "O"
    refresh()
def f22r(event):
    global fehlende_flaggen
    if anomis[2][2] != "f" and anomis[2][2] != "?":
        anomis[2][2] = "f"
    elif anomis[2][2] == "f":
        anomis[2][2] = "?"
        fehlende_flaggen -= 1
    else:
        anomis[2][2] = "O"
    refresh()
def f23r(event):
    global fehlende_flaggen
    if anomis[3][2] != "f" and anomis[3][2] != "?":
        anomis[3][2] = "f"
    elif anomis[3][2] == "f":
        anomis[3][2] = "?"
        fehlende_flaggen -= 1
    else:
        anomis[3][2] = "O"
    refresh()
def f24r(event):
    global fehlende_flaggen
    if anomis[4][2] != "f" and anomis[4][2] != "?":
        anomis[4][2] = "f"
    elif anomis[4][2] == "f":
        anomis[4][2] = "?"
        fehlende_flaggen -= 1
    else:
        anomis[4][2] = "O"
    refresh()
def f25r(event):
    global fehlende_flaggen
    if anomis[5][2] != "f" and anomis[5][2] != "?":
        anomis[5][2] = "f"
    elif anomis[5][2] == "f":
        anomis[5][2] = "?"
        fehlende_flaggen -= 1
    else:
        anomis[5][2] = "O"
    refresh()
def f26r(event):
    global fehlende_flaggen
    if anomis[6][2] != "f" and anomis[6][2] != "?":
        anomis[6][2] = "f"
    elif anomis[6][2] == "f":
        anomis[6][2] = "?"
        fehlende_flaggen -= 1
    else:
        anomis[6][2] = "O"
    refresh()
def f27r(event):
    global fehlende_flaggen
    if anomis[7][2] != "f" and anomis[7][2] != "?":
        anomis[7][2] = "f"
    elif anomis[7][2] == "f":
        anomis[7][2] = "?"
        fehlende_flaggen -= 1
    else:
        anomis[7][2] = "O"
    refresh()
def f30r(event):
    global fehlende_flaggen
    if anomis[0][3] != "f" and anomis[0][3] != "?":
        anomis[0][3] = "f"
    elif anomis[0][3] == "f":
        anomis[0][3] = "?"
        fehlende_flaggen -= 1
    else:
        anomis[0][3] = "O"
    refresh()
def f31r(event):
    global fehlende_flaggen
    if anomis[1][3] != "f" and anomis[1][3] != "?":
        anomis[1][3] = "f"
    elif anomis[1][3] == "f":
        anomis[1][3] = "?"
        fehlende_flaggen -= 1
    else:
        anomis[1][3] = "O"
    refresh()
def f32r(event):
    global fehlende_flaggen
    if anomis[2][3] != "f" and anomis[2][3] != "?":
        anomis[2][3] = "f"
    elif anomis[2][3] == "f":
        anomis[2][3] = "?"
        fehlende_flaggen -= 1
    else:
        anomis[2][3] = "O"
    refresh()
def f33r(event):
    global fehlende_flaggen
    if anomis[3][3] != "f" and anomis[3][3] != "?":
        anomis[3][3] = "f"
    elif anomis[3][3] == "f":
        anomis[3][3] = "?"
        fehlende_flaggen -= 1
    else:
        anomis[3][3] = "O"
    refresh()
def f34r(event):
    global fehlende_flaggen
    if anomis[4][3] != "f" and anomis[4][3] != "?":
        anomis[4][3] = "f"
    elif anomis[4][3] == "f":
        anomis[4][3] = "?"
        fehlende_flaggen -= 1
    else:
        anomis[4][3] = "O"
    refresh()
def f35r(event):
    global fehlende_flaggen
    if anomis[5][3] != "f" and anomis[5][3] != "?":
        anomis[5][3] = "f"
    elif anomis[5][3] == "f":
        anomis[5][3] = "?"
        fehlende_flaggen -= 1
    else:
        anomis[5][3] = "O"
    refresh()
def f36r(event):
    global fehlende_flaggen
    if anomis[6][3] != "f" and anomis[6][3] != "?":
        anomis[6][3] = "f"
    elif anomis[6][3] == "f":
        anomis[6][3] = "?"
        fehlende_flaggen -= 1
    else:
        anomis[6][3] = "O"
    refresh()
def f37r(event):
    global fehlende_flaggen
    if anomis[7][3] != "f" and anomis[7][3] != "?":
        anomis[7][3] = "f"
    elif anomis[7][3] == "f":
        anomis[7][3] = "?"
        fehlende_flaggen -= 1
    else:
        anomis[7][3] = "O"
    refresh()
def f40r(event):
    global fehlende_flaggen
    if anomis[0][4] != "f" and anomis[0][4] != "?":
        anomis[0][4] = "f"
    elif anomis[0][4] == "f":
        anomis[0][4] = "?"
        fehlende_flaggen -= 1
    else:
        anomis[0][4] = "O"
    refresh()
def f41r(event):
    global fehlende_flaggen
    if anomis[1][4] != "f" and anomis[1][4] != "?":
        anomis[1][4] = "f"
    elif anomis[1][4] == "f":
        anomis[1][4] = "?"
        fehlende_flaggen -= 1
    else:
        anomis[1][4] = "O"
    refresh()
def f42r(event):
    global fehlende_flaggen
    if anomis[2][4] != "f" and anomis[2][4] != "?":
        anomis[2][4] = "f"
    elif anomis[2][4] == "f":
        anomis[2][4] = "?"
        fehlende_flaggen -= 1
    else:
        anomis[2][4] = "O"
    refresh()
def f43r(event):
    global fehlende_flaggen
    if anomis[3][4] != "f" and anomis[3][4] != "?":
        anomis[3][4] = "f"
    elif anomis[3][4] == "f":
        anomis[3][4] = "?"
        fehlende_flaggen -= 1
    else:
        anomis[3][4] = "O"
    refresh()
def f44r(event):
    global fehlende_flaggen
    if anomis[4][4] != "f" and anomis[4][4] != "?":
        anomis[4][4] = "f"
    elif anomis[4][4] == "f":
        anomis[4][4] = "?"
        fehlende_flaggen -= 1
    else:
        anomis[4][4] = "O"
    refresh()
def f45r(event):
    global fehlende_flaggen
    if anomis[5][4] != "f" and anomis[5][4] != "?":
        anomis[5][4] = "f"
    elif anomis[5][4] == "f":
        anomis[5][4] = "?"
        fehlende_flaggen -= 1
    else:
        anomis[5][4] = "O"
    refresh()
def f46r(event):
    global fehlende_flaggen
    if anomis[6][4] != "f" and anomis[6][4] != "?":
        anomis[6][4] = "f"
    elif anomis[6][4] == "f":
        anomis[6][4] = "?"
        fehlende_flaggen -= 1
    else:
        anomis[6][4] = "O"
    refresh()
def f47r(event):
    global fehlende_flaggen
    if anomis[7][4] != "f" and anomis[7][4] != "?":
        anomis[7][4] = "f"
    elif anomis[7][4] == "f":
        anomis[7][4] = "?"
        fehlende_flaggen -= 1
    else:
        anomis[7][4] = "O"
    refresh()
def f50r(event):
    global fehlende_flaggen
    if anomis[0][5] != "f" and anomis[0][5] != "?":
        anomis[0][5] = "f"
    elif anomis[0][5] == "f":
        anomis[0][5] = "?"
        fehlende_flaggen -= 1
    else:
        anomis[0][5] = "O"
    refresh()
def f51r(event):
    global fehlende_flaggen
    if anomis[1][5] != "f" and anomis[1][5] != "?":
        anomis[1][5] = "f"
    elif anomis[1][5] == "f":
        anomis[1][5] = "?"
        fehlende_flaggen -= 1
    else:
        anomis[1][5] = "O"
    refresh()
def f52r(event):
    global fehlende_flaggen
    if anomis[2][5] != "f" and anomis[2][5] != "?":
        anomis[2][5] = "f"
    elif anomis[2][5] == "f":
        anomis[2][5] = "?"
        fehlende_flaggen -= 1
    else:
        anomis[2][5] = "O"
    refresh()
def f53r(event):
    global fehlende_flaggen
    if anomis[3][5] != "f" and anomis[3][5] != "?":
        anomis[3][5] = "f"
    elif anomis[3][5] == "f":
        anomis[3][5] = "?"
        fehlende_flaggen -= 1
    else:
        anomis[3][5] = "O"
    refresh()
def f54r(event):
    global fehlende_flaggen
    if anomis[4][5] != "f" and anomis[4][5] != "?":
        anomis[4][5] = "f"
    elif anomis[4][5] == "f":
        anomis[4][5] = "?"
        fehlende_flaggen -= 1
    else:
        anomis[4][5] = "O"
    refresh()
def f55r(event):
    global fehlende_flaggen
    if anomis[5][5] != "f" and anomis[5][5] != "?":
        anomis[5][5] = "f"
    elif anomis[5][5] == "f":
        anomis[5][5] = "?"
        fehlende_flaggen -= 1
    else:
        anomis[5][5] = "O"
    refresh()
def f56r(event):
    global fehlende_flaggen
    if anomis[6][5] != "f" and anomis[6][5] != "?":
        anomis[6][5] = "f"
    elif anomis[6][5] == "f":
        anomis[6][5] = "?"
        fehlende_flaggen -= 1
    else:
        anomis[6][5] = "O"
    refresh()
def f57r(event):
    global fehlende_flaggen
    if anomis[7][5] != "f" and anomis[7][5] != "?":
        anomis[7][5] = "f"
    elif anomis[7][5] == "f":
        anomis[7][5] = "?"
        fehlende_flaggen -= 1
    else:
        anomis[7][5] = "O"
    refresh()
def f60r(event):
    global fehlende_flaggen
    if anomis[0][6] != "f" and anomis[0][6] != "?":
        anomis[0][6] = "f"
    elif anomis[0][6] == "f":
        anomis[0][6] = "?"
        fehlende_flaggen -= 1
    else:
        anomis[0][6] = "O"
    refresh()
def f61r(event):
    global fehlende_flaggen
    if anomis[1][6] != "f" and anomis[1][6] != "?":
        anomis[1][6] = "f"
    elif anomis[1][6] == "f":
        anomis[1][6] = "?"
        fehlende_flaggen -= 1
    else:
        anomis[1][6] = "O"
    refresh()
def f62r(event):
    global fehlende_flaggen
    if anomis[2][6] != "f" and anomis[2][6] != "?":
        anomis[2][6] = "f"
    elif anomis[2][6] == "f":
        anomis[2][6] = "?"
        fehlende_flaggen -= 1
    else:
        anomis[2][6] = "O"
    refresh()
def f63r(event):
    global fehlende_flaggen
    if anomis[3][6] != "f" and anomis[3][6] != "?":
        anomis[3][6] = "f"
    elif anomis[3][6] == "f":
        anomis[3][6] = "?"
        fehlende_flaggen -= 1
    else:
        anomis[3][6] = "O"
    refresh()
def f64r(event):
    global fehlende_flaggen
    if anomis[4][6] != "f" and anomis[4][6] != "?":
        anomis[4][6] = "f"
    elif anomis[4][6] == "f":
        anomis[4][6] = "?"
        fehlende_flaggen -= 1
    else:
        anomis[4][6] = "O"
    refresh()
def f65r(event):
    global fehlende_flaggen
    if anomis[5][6] != "f" and anomis[5][6] != "?":
        anomis[5][6] = "f"
    elif anomis[5][6] == "f":
        anomis[5][6] = "?"
        fehlende_flaggen -= 1
    else:
        anomis[5][6] = "O"
    refresh()
def f66r(event):
    global fehlende_flaggen
    if anomis[6][6] != "f" and anomis[6][6] != "?":
        anomis[6][6] = "f"
    elif anomis[6][6] == "f":
        anomis[6][6] = "?"
        fehlende_flaggen -= 1
    else:
        anomis[6][6] = "O"
    refresh()
def f67r(event):
    global fehlende_flaggen
    if anomis[7][6] != "f" and anomis[7][6] != "?":
        anomis[7][6] = "f"
    elif anomis[7][6] == "f":
        anomis[7][6] = "?"
        fehlende_flaggen -= 1
    else:
        anomis[7][6] = "O"
    refresh()
def f70r(event):
    global fehlende_flaggen
    if anomis[0][7] != "f" and anomis[0][7] != "?":
        anomis[0][7] = "f"
    elif anomis[0][7] == "f":
        anomis[0][7] = "?"
        fehlende_flaggen -= 1
    else:
        anomis[0][7] = "O"
    refresh()
def f71r(event):
    global fehlende_flaggen
    if anomis[1][7] != "f" and anomis[1][7] != "?":
        anomis[1][7] = "f"
    elif anomis[1][7] == "f":
        anomis[1][7] = "?"
        fehlende_flaggen -= 1
    else:
        anomis[1][7] = "O"
    refresh()
def f72r(event):
    global fehlende_flaggen
    if anomis[2][7] != "f" and anomis[2][7] != "?":
        anomis[2][7] = "f"
    elif anomis[2][7] == "f":
        anomis[2][7] = "?"
        fehlende_flaggen -= 1
    else:
        anomis[2][7] = "O"
    refresh()
def f73r(event):
    global fehlende_flaggen
    if anomis[3][7] != "f" and anomis[3][7] != "?":
        anomis[3][7] = "f"
    elif anomis[3][7] == "f":
        anomis[3][7] = "?"
        fehlende_flaggen -= 1
    else:
        anomis[3][7] = "O"
    refresh()
def f74r(event):
    global fehlende_flaggen
    if anomis[4][7] != "f" and anomis[4][7] != "?":
        anomis[4][7] = "f"
    elif anomis[4][7] == "f":
        anomis[4][7] = "?"
        fehlende_flaggen -= 1
    else:
        anomis[4][7] = "O"
    refresh()
def f75r(event):
    global fehlende_flaggen
    if anomis[5][7] != "f" and anomis[5][7] != "?":
        anomis[5][7] = "f"
    elif anomis[5][7] == "f":
        anomis[5][7] = "?"
        fehlende_flaggen -= 1
    else:
        anomis[5][7] = "O"
    refresh()
def f76r(event):
    global fehlende_flaggen
    if anomis[6][7] != "f" and anomis[6][7] != "?":
        anomis[6][7] = "f"
    elif anomis[6][7] == "f":
        anomis[6][7] = "?"
        fehlende_flaggen -= 1
    else:
        anomis[6][7] = "O"
    refresh()
def f77r(event):
    global fehlende_flaggen
    if anomis[7][7] != "f" and anomis[7][7] != "?":
        anomis[7][7] = "f"
    elif anomis[7][7] == "f":
        anomis[7][7] = "?"
        fehlende_flaggen -= 1
    else:
        anomis[7][7] = "O"
    refresh()
    
def bombenfeld(AufFeldX, AufFeldY): 
    global tot, ersterzug, uhrstart, az, zeitanzeige, altezeit
    if ersterzug == True: # Wenn es der erste Zug ist,
        anomirefresh() # wird das Hintergrundfeld (Zahlen & Bomben) zur Grafik hinzugefügt. Die passiert erst dann, weil auf schwächeren System sonst das Hintergrundfeld schon vorher sichtbar wäre.
        altezeit = -1 # altezeit wird zurückgesetzt
        az = clock() # Damit die Uhr wieder bei 0 startet
        uhrstart = True # Damit die Uhr startet
        t = Thread(target=stoppuhr).start() # Falls es die allererste Spielrunde ist, wird nun die Uhr gestartet.
        ersterzug = False
    if anomi[AufFeldY][AufFeldX] == "X": # Wenn das Feld eine Bombe ist,
        smiley["image"] = smileytot # wird der Smiley auf tot gesetzt
        leeren() # & alle Felder vom Spielfeld genommen
        tot = True
        uhrstart = False
        ersterzug = True
        
def leeren():
        f00.grid_forget() # Alle Felder werden vom Spielfeld genommen
        f01.grid_forget()
        f02.grid_forget()
        f03.grid_forget()
        f04.grid_forget()
        f05.grid_forget()
        f06.grid_forget()
        f07.grid_forget()
        f10.grid_forget()
        f11.grid_forget()
        f12.grid_forget()
        f13.grid_forget()
        f14.grid_forget()
        f15.grid_forget()
        f16.grid_forget()
        f17.grid_forget()
        f20.grid_forget()
        f21.grid_forget()
        f22.grid_forget()
        f23.grid_forget()
        f24.grid_forget()
        f25.grid_forget()
        f26.grid_forget()
        f27.grid_forget()
        f30.grid_forget()
        f31.grid_forget()
        f32.grid_forget()
        f33.grid_forget()
        f34.grid_forget()
        f35.grid_forget()
        f36.grid_forget()
        f37.grid_forget()
        f40.grid_forget()
        f41.grid_forget()
        f42.grid_forget()
        f43.grid_forget()
        f44.grid_forget()
        f45.grid_forget()
        f46.grid_forget()
        f47.grid_forget()
        f50.grid_forget()
        f51.grid_forget()
        f52.grid_forget()
        f53.grid_forget()
        f54.grid_forget()
        f55.grid_forget()
        f56.grid_forget()
        f57.grid_forget()
        f60.grid_forget()
        f61.grid_forget()
        f62.grid_forget()
        f63.grid_forget()
        f64.grid_forget()
        f65.grid_forget()
        f66.grid_forget()
        f67.grid_forget()
        f70.grid_forget()
        f71.grid_forget()
        f72.grid_forget()
        f73.grid_forget()
        f74.grid_forget()
        f75.grid_forget()
        f76.grid_forget()
        f77.grid_forget()
        
def refresh(): #  Das Spielfeld wird geupdatet
    global tot, uhrstart, ersterzug
    global gwf, winnername, score, zeit
    global p00, p01, p02, p03, p04, p05, p06, p07, p10, p11, p12, p13, p14, p15, p16, p17, p20, p21, p22, p23, p24, p25, p26, p27, p30, p31, p32, p33, p34, p35, p36, p37, p40, p41, p42, p43, p44, p45, p46, p47, p50, p51, p52, p53, p54, p55, p56, p57, p60, p61, p62, p63, p64, p65, p66, p67, p70, p71, p72, p73, p74, p75, p76, p77
    if tot != True:
        global fehlende_flaggen
        global gewonnen # Es wird für jedes Feld geschaut,
        if anomis[0][0] == "O": # ob es frei ist,
            f00["image"] = p00 # (das normale Bild wird wieder draufgesetzt)
        elif anomis[0][0] == "f": # ob es eine Flagge ist,
            f00["image"] = flagge # (es wird eine Flagge auf den Button gesetzt)
        elif anomis[0][0] == "?": # oder ob es ein Fragezeichen ist.
            f00["image"] = fragezeichen # (es wird ein Fragezeichen auf den Button gesetzt)
        else: # Andernfalls wird der Button vom Spielfeld genommen.
            f00.grid_forget()
        if anomis[1][0] == "O":
            f01["image"] = p01
        elif anomis[1][0] == "f":
            f01["image"] = flagge
        elif anomis[1][0] == "?":
            f01["image"] = fragezeichen
        else:
            f01.grid_forget()
        if anomis[2][0] == "O":
            f02["image"] = p02
        elif anomis[2][0] == "f":
            f02["image"] = flagge
        elif anomis[2][0] == "?":
            f02["image"] = fragezeichen
        else:
            f02.grid_forget()
        if anomis[3][0] == "O":
            f03["image"] = p03
        elif anomis[3][0] == "f":
            f03["image"] = flagge
        elif anomis[3][0] == "?":
            f03["image"] = fragezeichen
        else:
            f03.grid_forget()
        if anomis[4][0] == "O":
            f04["image"] = p04
        elif anomis[4][0] == "f":
            f04["image"] = flagge
        elif anomis[4][0] == "?":
            f04["image"] = fragezeichen
        else:
            f04.grid_forget()
        if anomis[5][0] == "O":
            f05["image"] = p05
        elif anomis[5][0] == "f":
            f05["image"] = flagge
        elif anomis[5][0] == "?":
            f05["image"] = fragezeichen
        else:
            f05.grid_forget()
        if anomis[6][0] == "O":
            f06["image"] = p06
        elif anomis[6][0] == "f":
            f06["image"] = flagge
        elif anomis[6][0] == "?":
            f06["image"] = fragezeichen
        else:
            f06.grid_forget()
        if anomis[7][0] == "O":
            f07["image"] = p07
        elif anomis[7][0] == "f":
            f07["image"] = flagge
        elif anomis[7][0] == "?":
            f07["image"] = fragezeichen
        else:
            f07.grid_forget()
        if anomis[0][1] == "O":
            f10["image"] = p10
        elif anomis[0][1] == "f":
            f10["image"] = flagge
        elif anomis[0][1] == "?":
            f10["image"] = fragezeichen
        else:
            f10.grid_forget()
        if anomis[1][1] == "O":
            f11["image"] = p11
        elif anomis[1][1] == "f":
            f11["image"] = flagge
        elif anomis[1][1] == "?":
            f11["image"] = fragezeichen
        else:
            f11.grid_forget()
        if anomis[2][1] == "O":
            f12["image"] = p12
        elif anomis[2][1] == "f":
            f12["image"] = flagge
        elif anomis[2][1] == "?":
            f12["image"] = fragezeichen
        else:
            f12.grid_forget()
        if anomis[3][1] == "O":
            f13["image"] = p13
        elif anomis[3][1] == "f":
            f13["image"] = flagge
        elif anomis[3][1] == "?":
            f13["image"] = fragezeichen
        else:
            f13.grid_forget()
        if anomis[4][1] == "O":
            f14["image"] = p14
        elif anomis[4][1] == "f":
            f14["image"] = flagge
        elif anomis[4][1] == "?":
            f14["image"] = fragezeichen
        else:
            f14.grid_forget()
        if anomis[5][1] == "O":
            f15["image"] = p15
        elif anomis[5][1] == "f":
            f15["image"] = flagge
        elif anomis[5][1] == "?":
            f15["image"] = fragezeichen
        else:
            f15.grid_forget()
        if anomis[6][1] == "O":
            f16["image"] = p16
        elif anomis[6][1] == "f":
            f16["image"] = flagge
        elif anomis[6][1] == "?":
            f16["image"] = fragezeichen
        else:
            f16.grid_forget()
        if anomis[7][1] == "O":
            f17["image"] = p17
        elif anomis[7][1] == "f":
            f17["image"] = flagge
        elif anomis[7][1] == "?":
            f17["image"] = fragezeichen
        else:
            f17.grid_forget()
        if anomis[0][2] == "O":
            f20["image"] = p20
        elif anomis[0][2] == "f":
            f20["image"] = flagge
        elif anomis[0][2] == "?":
            f20["image"] = fragezeichen
        else:
            f20.grid_forget()
        if anomis[1][2] == "O":
            f21["image"] = p21
        elif anomis[1][2] == "f":
            f21["image"] = flagge
        elif anomis[1][2] == "?":
            f21["image"] = fragezeichen
        else:
            f21.grid_forget()
        if anomis[2][2] == "O":
            f22["image"] = p22
        elif anomis[2][2] == "f":
            f22["image"] = flagge
        elif anomis[2][2] == "?":
            f22["image"] = fragezeichen
        else:
            f22.grid_forget()
        if anomis[3][2] == "O":
            f23["image"] = p23
        elif anomis[3][2] == "f":
            f23["image"] = flagge
        elif anomis[3][2] == "?":
            f23["image"] = fragezeichen
        else:
            f23.grid_forget()
        if anomis[4][2] == "O":
            f24["image"] = p24
        elif anomis[4][2] == "f":
            f24["image"] = flagge
        elif anomis[4][2] == "?":
            f24["image"] = fragezeichen
        else:
            f24.grid_forget()
        if anomis[5][2] == "O":
            f25["image"] = p25
        elif anomis[5][2] == "f":
            f25["image"] = flagge
        elif anomis[5][2] == "?":
            f25["image"] = fragezeichen
        else:
            f25.grid_forget()
        if anomis[6][2] == "O":
            f26["image"] = p26
        elif anomis[6][2] == "f":
            f26["image"] = flagge
        elif anomis[6][2] == "?":
            f26["image"] = fragezeichen
        else:
            f26.grid_forget()
        if anomis[7][2] == "O":
            f27["image"] = p27
        elif anomis[7][2] == "f":
            f27["image"] = flagge
        elif anomis[7][2] == "?":
            f27["image"] = fragezeichen
        else:
            f27.grid_forget()
        if anomis[0][3] == "O":
            f30["image"] = p30
        elif anomis[0][3] == "f":
            f30["image"] = flagge
        elif anomis[0][3] == "?":
            f30["image"] = fragezeichen
        else:
            f30.grid_forget()
        if anomis[1][3] == "O":
            f31["image"] = p31
        elif anomis[1][3] == "f":
            f31["image"] = flagge
        elif anomis[1][3] == "?":
            f31["image"] = fragezeichen
        else:
            f31.grid_forget()
        if anomis[2][3] == "O":
            f32["image"] = p32
        elif anomis[2][3] == "f":
            f32["image"] = flagge
        elif anomis[2][3] == "?":
            f32["image"] = fragezeichen
        else:
            f32.grid_forget()
        if anomis[3][3] == "O":
            f33["image"] = p33
        elif anomis[3][3] == "f":
            f33["image"] = flagge
        elif anomis[3][3] == "?":
            f33["image"] = fragezeichen
        else:
            f33.grid_forget()
        if anomis[4][3] == "O":
            f34["image"] = p34
        elif anomis[4][3] == "f":
            f34["image"] = flagge
        elif anomis[4][3] == "?":
            f34["image"] = fragezeichen
        else:
            f34.grid_forget()
        if anomis[5][3] == "O":
            f35["image"] = p35
        elif anomis[5][3] == "f":
            f35["image"] = flagge
        elif anomis[5][3] == "?":
            f35["image"] = fragezeichen
        else:
            f35.grid_forget()
        if anomis[6][3] == "O":
            f36["image"] = p36
        elif anomis[6][3] == "f":
            f36["image"] = flagge
        elif anomis[6][3] == "?":
            f36["image"] = fragezeichen
        else:
            f36.grid_forget()
        if anomis[7][3] == "O":
            f37["image"] = p37
        elif anomis[7][3] == "f":
            f37["image"] = flagge
        elif anomis[7][3] == "?":
            f37["image"] = fragezeichen
        else:
            f37.grid_forget()
        if anomis[0][4] == "O":
            f40["image"] = p40
        elif anomis[0][4] == "f":
            f40["image"] = flagge
        elif anomis[0][4] == "?":
            f40["image"] = fragezeichen
        else:
            f40.grid_forget()
        if anomis[1][4] == "O":
            f41["image"] = p41
        elif anomis[1][4] == "f":
            f41["image"] = flagge
        elif anomis[1][4] == "?":
            f41["image"] = fragezeichen
        else:
            f41.grid_forget()
        if anomis[2][4] == "O":
            f42["image"] = p42
        elif anomis[2][4] == "f":
            f42["image"] = flagge
        elif anomis[2][4] == "?":
            f42["image"] = fragezeichen
        else:
            f42.grid_forget()
        if anomis[3][4] == "O":
            f43["image"] = p43
        elif anomis[3][4] == "f":
            f43["image"] = flagge
        elif anomis[3][4] == "?":
            f43["image"] = fragezeichen
        else:
            f43.grid_forget()
        if anomis[4][4] == "O":
            f44["image"] = p44
        elif anomis[4][4] == "f":
            f44["image"] = flagge
        elif anomis[4][4] == "?":
            f44["image"] = fragezeichen
        else:
            f44.grid_forget()
        if anomis[5][4] == "O":
            f45["image"] = p45
        elif anomis[5][4] == "f":
            f45["image"] = flagge
        elif anomis[5][4] == "?":
            f45["image"] = fragezeichen
        else:
            f45.grid_forget()
        if anomis[6][4] == "O":
            f46["image"] = p46
        elif anomis[6][4] == "f":
            f46["image"] = flagge
        elif anomis[6][4] == "?":
            f46["image"] = fragezeichen
        else:
            f46.grid_forget()
        if anomis[7][4] == "O":
            f47["image"] = p47
        elif anomis[7][4] == "f":
            f47["image"] = flagge
        elif anomis[7][4] == "?":
            f47["image"] = fragezeichen
        else:
            f47.grid_forget()
        if anomis[0][5] == "O":
            f50["image"] = p50
        elif anomis[0][5] == "f":
            f50["image"] = flagge
        elif anomis[0][5] == "?":
            f50["image"] = fragezeichen
        else:
            f50.grid_forget()
        if anomis[1][5] == "O":
            f51["image"] = p51
        elif anomis[1][5] == "f":
            f51["image"] = flagge
        elif anomis[1][5] == "?":
            f51["image"] = fragezeichen
        else:
            f51.grid_forget()
        if anomis[2][5] == "O":
            f52["image"] = p52
        elif anomis[2][5] == "f":
            f52["image"] = flagge
        elif anomis[2][5] == "?":
            f52["image"] = fragezeichen
        else:
            f52.grid_forget()
        if anomis[3][5] == "O":
            f53["image"] = p53
        elif anomis[3][5] == "f":
            f53["image"] = flagge
        elif anomis[3][5] == "?":
            f53["image"] = fragezeichen
        else:
            f53.grid_forget()
        if anomis[4][5] == "O":
            f54["image"] = p54
        elif anomis[4][5] == "f":
            f54["image"] = flagge
        elif anomis[4][5] == "?":
            f54["image"] = fragezeichen
        else:
            f54.grid_forget()
        if anomis[5][5] == "O":
            f55["image"] = p55
        elif anomis[5][5] == "f":
            f55["image"] = flagge
        elif anomis[5][5] == "?":
            f55["image"] = fragezeichen
        else:
            f55.grid_forget()
        if anomis[6][5] == "O":
            f56["image"] = p56
        elif anomis[6][5] == "f":
            f56["image"] = flagge
        elif anomis[6][5] == "?":
            f56["image"] = fragezeichen
        else:
            f56.grid_forget()
        if anomis[7][5] == "O":
            f57["image"] = p57
        elif anomis[7][5] == "f":
            f57["image"] = flagge
        elif anomis[7][5] == "?":
            f57["image"] = fragezeichen
        else:
            f57.grid_forget()
        if anomis[0][6] == "O":
            f60["image"] = p60
        elif anomis[0][6] == "f":
            f60["image"] = flagge
        elif anomis[0][6] == "?":
            f60["image"] = fragezeichen
        else:
            f60.grid_forget()
        if anomis[1][6] == "O":
            f61["image"] = p61
        elif anomis[1][6] == "f":
            f61["image"] = flagge
        elif anomis[1][6] == "?":
            f61["image"] = fragezeichen
        else:
            f61.grid_forget()
        if anomis[2][6] == "O":
            f62["image"] = p62
        elif anomis[2][6] == "f":
            f62["image"] = flagge
        elif anomis[2][6] == "?":
            f62["image"] = fragezeichen
        else:
            f62.grid_forget()
        if anomis[3][6] == "O":
            f63["image"] = p63
        elif anomis[3][6] == "f":
            f63["image"] = flagge
        elif anomis[3][6] == "?":
            f63["image"] = fragezeichen
        else:
            f63.grid_forget()
        if anomis[4][6] == "O":
            f64["image"] = p64
        elif anomis[4][6] == "f":
            f64["image"] = flagge
        elif anomis[4][6] == "?":
            f64["image"] = fragezeichen
        else:
            f64.grid_forget()
        if anomis[5][6] == "O":
            f65["image"] = p65
        elif anomis[5][6] == "f":
            f65["image"] = flagge
        elif anomis[5][6] == "?":
            f65["image"] = fragezeichen
        else:
            f65.grid_forget()
        if anomis[6][6] == "O":
            f66["image"] = p66
        elif anomis[6][6] == "f":
            f66["image"] = flagge
        elif anomis[6][6] == "?":
            f66["image"] = fragezeichen
        else:
            f66.grid_forget()
        if anomis[7][6] == "O":
            f67["image"] = p67
        elif anomis[7][6] == "f":
            f67["image"] = flagge            
        elif anomis[7][6] == "?":
            f67["image"] = fragezeichen
        else:
            f67.grid_forget()            
        if anomis[0][7] == "O":
            f70["image"] = p70
        elif anomis[0][7] == "f":
            f70["image"] = flagge            
        elif anomis[0][7] == "?":
            f70["image"] = fragezeichen
        else:
            f70.grid_forget()            
        if anomis[1][7] == "O":
            f71["image"] = p71
        elif anomis[1][7] == "f":
            f71["image"] = flagge            
        elif anomis[1][7] == "?":
            f71["image"] = fragezeichen
        else:
            f71.grid_forget()            
        if anomis[2][7] == "O":
            f72["image"] = p72
        elif anomis[2][7] == "f":
            f72["image"] = flagge 
        elif anomis[2][7] == "?":
            f72["image"] = fragezeichen
        else:
            f72.grid_forget()           
        if anomis[3][7] == "O":
            f73["image"] = p73
        elif anomis[3][7] == "f":
            f73["image"] = flagge            
        elif anomis[3][7] == "?":
            f73["image"] = fragezeichen
        else:
            f73.grid_forget()            
        if anomis[4][7] == "O":
            f74["image"] = p74
        elif anomis[4][7] == "f":
            f74["image"] = flagge            
        elif anomis[4][7] == "?":
            f74["image"] = fragezeichen
        else:
            f74.grid_forget()            
        if anomis[5][7] == "O":
            f75["image"] = p75
        elif anomis[5][7] == "f":
            f75["image"] = flagge            
        elif anomis[5][7] == "?":
            f75["image"] = fragezeichen
        else:
            f75.grid_forget()            
        if anomis[6][7] == "O":
            f76["image"] = p76
        elif anomis[6][7] == "f":
            f76["image"] = flagge            
        elif anomis[6][7] == "?":
            f76["image"] = fragezeichen
        else:
            f76.grid_forget()            
        if anomis[7][7] == "O":
            f77["image"] = p77
        elif anomis[7][7] == "f":
            f77["image"] = flagge            
        elif anomis[7][7] == "?":
            f77["image"] = fragezeichen
        else:
            f77.grid_forget()
        fehlende_flaggen = 0
        gewonnen = 0
        for i in range(8):
            for j in range(8):  
                if anomi[i][j] == anomis[i][j]: # Es werden aufgedeckte 
                    gewonnen += 1
                if anomis[i][j] == "f": # und markierte Felder gezählt.
                    fehlende_flaggen += 1
        if gewonnen == 54: # Falls man alle Felder außer die Bomben aufgedeckt hat (64 Felder - 10 Bomben)
            uhrstart = False
            ersterzug = True
            gwf = Tk() # Es wird ein Fenster geöffnet
            gwf.title("Du hast gewonnen")
            gwf.iconbitmap("icon.ico")
            gwf.resizable(0,0)
            Label(gwf, text="Du hast in der Zeit von "+timestr+" gewonnen!").grid(columnspan=2,row=0)
            if zeit < score[9][1]: # Falls die zeit für die Highscoreliste reicht,
                Label(gwf, text="Gib hier deinen Namen ein, um \n dich in die Highscoreliste eizutragen:").grid(columnspan=2,row=1) # Kann man diese eintragen
                winnername = Entry(gwf)
                winnername.grid(row=2, column=0)
                Button(gwf, text="Enter", command=winnerfunc).grid(row=2, column=1)
            else: # Falls nicht,
                Label(gwf, text="Leider reicht deine Zeit nicht für die Highscoreliste.").grid(row=1) # kann man sich lediglich die Higscoreliste anzeigen lassen.
                Button(gwf, text="Highscoreliste ansehen", command=highscorel).grid(row=2)
    gw["text"] = 10 - fehlende_flaggen # Die Grafik wird geupdatet
    
def felderaufdecken(RundFeldX, RundFeldY):
    global rfx
    global rfy
    global xben
    global yben
    sdel = [] #Die Liste sdel(Stellen + delete) wird definiert bzw. geleert.
    xben.append(RundFeldX) #An die Listen xben (X-Werte + Benutzt) und yben(Y-Werte + Benutzt)
    yben.append(RundFeldY)
    if len(rfx) != 0: #Falls die Liste rfx nicht leer ist, wird ihr erster Wert gelöscht
        del rfy[0]
        del rfx[0]
    if 0<RundFeldX<7:   #Jetzt wird je nach Fall (also, ob sich das aktuelle Feld am Rand, in der Ecke oder in der Mitte befindet) die Felder um das aktuelle
        if 0<RundFeldY<7: #Feld aufgedeckt und es werden diese Felder außerdem in die Listen rfx(RundFeldX) und rfy(RundFeldY) angehängt.
            rfx.append(RundFeldX-1)#Runterscrollen
            rfy.append(RundFeldY-1)
            anomis[RundFeldY-1][RundFeldX-1] = anomi[RundFeldY-1][RundFeldX-1]
            rfx.append(RundFeldX)
            rfy.append(RundFeldY-1)
            anomis[RundFeldY-1][RundFeldX] = anomi[RundFeldY-1][RundFeldX]
            rfx.append(RundFeldX+1)
            rfy.append(RundFeldY-1)
            anomis[RundFeldY-1][RundFeldX+1] = anomi[RundFeldY-1][RundFeldX+1]
            rfx.append(RundFeldX-1)
            rfy.append(RundFeldY)
            anomis[RundFeldY][RundFeldX-1] = anomi[RundFeldY][RundFeldX-1]
            anomis[RundFeldY][RundFeldX] = anomi[RundFeldY][RundFeldX]
            rfx.append(RundFeldX+1)
            rfy.append(RundFeldY)
            anomis[RundFeldY][RundFeldX+1] = anomi[RundFeldY][RundFeldX+1]
            rfx.append(RundFeldX-1)
            rfy.append(RundFeldY+1)
            anomis[RundFeldY+1][RundFeldX-1] = anomi[RundFeldY+1][RundFeldX-1]
            rfx.append(RundFeldX)
            rfy.append(RundFeldY+1)
            anomis[RundFeldY+1][RundFeldX] = anomi[RundFeldY+1][RundFeldX]
            rfx.append(RundFeldX+1)
            rfy.append(RundFeldY+1)
            anomis[RundFeldY+1][RundFeldX+1] = anomi[RundFeldY+1][RundFeldX+1]
        elif RundFeldY == 0:
            rfx.append(RundFeldX-1)
            rfy.append(RundFeldY)
            anomis[RundFeldY][RundFeldX-1] = anomi[RundFeldY][RundFeldX-1]
            anomis[RundFeldY][RundFeldX] = anomi[RundFeldY][RundFeldX]
            rfx.append(RundFeldX+1)
            rfy.append(RundFeldY)
            anomis[RundFeldY][RundFeldX+1] = anomi[RundFeldY][RundFeldX+1]
            rfx.append(RundFeldX-1)
            rfy.append(RundFeldY+1)
            anomis[RundFeldY+1][RundFeldX-1] = anomi[RundFeldY+1][RundFeldX-1]
            rfx.append(RundFeldX)
            rfy.append(RundFeldY+1)
            anomis[RundFeldY+1][RundFeldX] = anomi[RundFeldY+1][RundFeldX]
            rfx.append(RundFeldX+1)
            rfy.append(RundFeldY+1)
            anomis[RundFeldY+1][RundFeldX+1] = anomi[RundFeldY+1][RundFeldX+1]             
        elif RundFeldY == 7:
            rfx.append(RundFeldX-1)
            rfy.append(RundFeldY-1)
            anomis[RundFeldY-1][RundFeldX-1] = anomi[RundFeldY-1][RundFeldX-1]
            rfx.append(RundFeldX)
            rfy.append(RundFeldY-1)
            anomis[RundFeldY-1][RundFeldX] = anomi[RundFeldY-1][RundFeldX]
            rfx.append(RundFeldX+1)
            rfy.append(RundFeldY-1)
            anomis[RundFeldY-1][RundFeldX+1] = anomi[RundFeldY-1][RundFeldX+1]
            rfx.append(RundFeldX-1)
            rfy.append(RundFeldY)
            anomis[RundFeldY][RundFeldX-1] = anomi[RundFeldY][RundFeldX-1]
            anomis[RundFeldY][RundFeldX] = anomi[RundFeldY][RundFeldX]
            rfx.append(RundFeldX+1)
            rfy.append(RundFeldY)
            anomis[RundFeldY][RundFeldX+1] = anomi[RundFeldY][RundFeldX+1]
    elif RundFeldX == 0:
        if 0<RundFeldY<7:
            rfx.append(RundFeldX)
            rfy.append(RundFeldY-1)
            anomis[RundFeldY-1][RundFeldX] = anomi[RundFeldY-1][RundFeldX]
            rfx.append(RundFeldX+1)
            rfy.append(RundFeldY-1)
            anomis[RundFeldY-1][RundFeldX+1] = anomi[RundFeldY-1][RundFeldX+1]
            anomis[RundFeldY][RundFeldX] = anomi[RundFeldY][RundFeldX]
            rfx.append(RundFeldX+1)
            rfy.append(RundFeldY)
            anomis[RundFeldY][RundFeldX+1] = anomi[RundFeldY][RundFeldX+1]
            rfx.append(RundFeldX)
            rfy.append(RundFeldY+1)
            anomis[RundFeldY+1][RundFeldX] = anomi[RundFeldY+1][RundFeldX]
            rfx.append(RundFeldX+1)
            rfy.append(RundFeldY+1)
            anomis[RundFeldY+1][RundFeldX+1] = anomi[RundFeldY+1][RundFeldX+1]
        elif RundFeldY == 0:
            anomis[RundFeldY][RundFeldX] = anomi[RundFeldY][RundFeldX]
            rfx.append(RundFeldX+1)
            rfy.append(RundFeldY)
            anomis[RundFeldY][RundFeldX+1] = anomi[RundFeldY][RundFeldX+1]
            rfx.append(RundFeldX)
            rfy.append(RundFeldY+1)
            anomis[RundFeldY+1][RundFeldX] = anomi[RundFeldY+1][RundFeldX]
            rfx.append(RundFeldX+1)
            rfy.append(RundFeldY+1)
            anomis[RundFeldY+1][RundFeldX+1] = anomi[RundFeldY+1][RundFeldX+1]
        elif RundFeldY == 7:
            rfx.append(RundFeldX)
            rfy.append(RundFeldY-1)
            anomis[RundFeldY-1][RundFeldX] = anomi[RundFeldY-1][RundFeldX]
            rfx.append(RundFeldX+1)
            rfy.append(RundFeldY-1)
            anomis[RundFeldY-1][RundFeldX+1] = anomi[RundFeldY-1][RundFeldX+1]
            anomis[RundFeldY][RundFeldX] = anomi[RundFeldY][RundFeldX]
            rfx.append(RundFeldX+1)
            rfy.append(RundFeldY)
            anomis[RundFeldY][RundFeldX+1] = anomi[RundFeldY][RundFeldX+1]
    elif RundFeldX == 7:
        if 0<RundFeldY<7:
            rfx.append(RundFeldX-1)
            rfy.append(RundFeldY-1)
            anomis[RundFeldY-1][RundFeldX-1] = anomi[RundFeldY-1][RundFeldX-1]
            rfx.append(RundFeldX)
            rfy.append(RundFeldY-1)
            anomis[RundFeldY-1][RundFeldX] = anomi[RundFeldY-1][RundFeldX]
            rfx.append(RundFeldX-1)
            rfy.append(RundFeldY)
            anomis[RundFeldY][RundFeldX-1] = anomi[RundFeldY][RundFeldX-1]
            anomis[RundFeldY][RundFeldX] = anomi[RundFeldY][RundFeldX]
            rfx.append(RundFeldX-1)
            rfy.append(RundFeldY+1)
            anomis[RundFeldY+1][RundFeldX-1] = anomi[RundFeldY+1][RundFeldX-1]         
            rfx.append(RundFeldX)
            rfy.append(RundFeldY+1)
            anomis[RundFeldY+1][RundFeldX] = anomi[RundFeldY+1][RundFeldX]
        elif RundFeldY == 0:
            rfx.append(RundFeldX-1)
            rfy.append(RundFeldY)
            anomis[RundFeldY][RundFeldX-1] = anomi[RundFeldY][RundFeldX-1]
            anomis[RundFeldY][RundFeldX] = anomi[RundFeldY][RundFeldX]
            rfx.append(RundFeldX-1)
            rfy.append(RundFeldY+1)
            anomis[RundFeldY+1][RundFeldX-1] = anomi[RundFeldY+1][RundFeldX-1]
            rfx.append(RundFeldX)
            rfy.append(RundFeldY+1)
            anomis[RundFeldY+1][RundFeldX] = anomi[RundFeldY+1][RundFeldX]
        elif RundFeldY == 7:
            rfx.append(RundFeldX-1)
            rfy.append(RundFeldY-1)
            anomis[RundFeldY-1][RundFeldX-1] = anomi[RundFeldY-1][RundFeldX-1]
            rfx.append(RundFeldX)
            rfy.append(RundFeldY-1)
            anomis[RundFeldY-1][RundFeldX] = anomi[RundFeldY-1][RundFeldX]
            rfx.append(RundFeldX-1)
            rfy.append(RundFeldY)
            anomis[RundFeldY][RundFeldX-1] = anomi[RundFeldY][RundFeldX-1]
            anomis[RundFeldY][RundFeldX] = anomi[RundFeldY][RundFeldX]
    for f in range(len(rfy)-1,-1,-1): #In dieser Schleife werden die Wertepaare aus rfx/rfy gelöscht, falls sie kein freies Feld sind.
        if anomi[rfy[f]][rfx[f]] != " ":
            del rfx[f]
            del rfy[f]
    for i in range(len(rfx)): #Jetzt werden zum Schluss noch die Wertepaare aussortiert, die bereits einmal durch die Funktion liefen.
        for j in range(len(xben)):
            if rfx[i] == xben[j] and rfy[i] == yben[j]:
                sdel.append(i)
    if len(sdel) != 0 and len(rfx) != 0: #Da dabei nur die Stellen der Wertepaare zu sdel hinzugefügt wurden, werden diese Stellen nun aus rfx/rfy gelöscht. 
        for k in range(len(sdel)-1,-1,-1):
            del rfx[sdel[k]]
            del rfy[sdel[k]]
    if len(rfx) != 0: #Falls es noch Wertepaare gibt, wird Funktion mit dem ersten Wertepaar der Liste neu gestartet
        RundFeldX = rfx[0]
        RundFeldY = rfy[0]
        felderaufdecken(RundFeldX, RundFeldY)
    else:
        xben = []
        yben = []
        
def start(event):
    global tot, ersterzug, uhrstart, score
    t = 0
    f = open("score.txt", "r") # Wie oben
    for line in f: 
        data = line.strip().split("\t") 
        score[t][0] = data[0]
        dataint = int(data[1])
        score[t][1] = dataint
        t += 1
    f.close() 
    ersterzug = True
    uhrstart = False
    tot = False
    for i in range(8): # Die Felder werden zurückgesetzt
        for j in range(8):
            anomi[i][j] = " "
            anomis[i][j] = "O"
    f00.grid(row=1, column=0)
    f01.grid(row=2, column=0)
    f02.grid(row=3, column=0)
    f03.grid(row=4, column=0)
    f04.grid(row=5, column=0)
    f05.grid(row=6, column=0)
    f06.grid(row=7, column=0)
    f07.grid(row=8, column=0)
    f10.grid(row=1, column=1)
    f11.grid(row=2, column=1)
    f12.grid(row=3, column=1)
    f13.grid(row=4, column=1)
    f14.grid(row=5, column=1)
    f15.grid(row=6, column=1)
    f16.grid(row=7, column=1)
    f17.grid(row=8, column=1)
    f20.grid(row=1, column=2)
    f21.grid(row=2, column=2)
    f22.grid(row=3, column=2)
    f23.grid(row=4, column=2)
    f24.grid(row=5, column=2)
    f25.grid(row=6, column=2)
    f26.grid(row=7, column=2)
    f27.grid(row=8, column=2)
    f30.grid(row=1, column=3)
    f31.grid(row=2, column=3)
    f32.grid(row=3, column=3)
    f33.grid(row=4, column=3)
    f34.grid(row=5, column=3)
    f35.grid(row=6, column=3)
    f36.grid(row=7, column=3)
    f37.grid(row=8, column=3)
    f40.grid(row=1, column=4)
    f41.grid(row=2, column=4)
    f42.grid(row=3, column=4)
    f43.grid(row=4, column=4)
    f44.grid(row=5, column=4)
    f45.grid(row=6, column=4)
    f46.grid(row=7, column=4)
    f47.grid(row=8, column=4)
    f50.grid(row=1, column=5)
    f51.grid(row=2, column=5)
    f52.grid(row=3, column=5)
    f53.grid(row=4, column=5)
    f54.grid(row=5, column=5)
    f55.grid(row=6, column=5)
    f56.grid(row=7, column=5)
    f57.grid(row=8, column=5)
    f60.grid(row=1, column=6)
    f61.grid(row=2, column=6)
    f62.grid(row=3, column=6)
    f63.grid(row=4, column=6)
    f64.grid(row=5, column=6)
    f65.grid(row=6, column=6)
    f66.grid(row=7, column=6)
    f67.grid(row=8, column=6)
    f70.grid(row=1, column=7)
    f71.grid(row=2, column=7)
    f72.grid(row=3, column=7)
    f73.grid(row=4, column=7)
    f74.grid(row=5, column=7)
    f75.grid(row=6, column=7)
    f76.grid(row=7, column=7)
    f77.grid(row=8, column=7)
    refresh()
    f00h["image"] = nichts
    f01h["image"] = nichts
    f02h["image"] = nichts
    f03h["image"] = nichts
    f04h["image"] = nichts
    f05h["image"] = nichts
    f06h["image"] = nichts
    f07h["image"] = nichts
    f10h["image"] = nichts
    f11h["image"] = nichts
    f12h["image"] = nichts
    f13h["image"] = nichts
    f14h["image"] = nichts
    f15h["image"] = nichts
    f16h["image"] = nichts
    f17h["image"] = nichts
    f20h["image"] = nichts
    f21h["image"] = nichts
    f22h["image"] = nichts
    f23h["image"] = nichts
    f24h["image"] = nichts
    f25h["image"] = nichts
    f26h["image"] = nichts
    f27h["image"] = nichts
    f30h["image"] = nichts
    f31h["image"] = nichts
    f32h["image"] = nichts
    f33h["image"] = nichts
    f34h["image"] = nichts
    f35h["image"] = nichts
    f36h["image"] = nichts
    f37h["image"] = nichts
    f40h["image"] = nichts
    f41h["image"] = nichts
    f42h["image"] = nichts
    f43h["image"] = nichts
    f44h["image"] = nichts
    f45h["image"] = nichts
    f46h["image"] = nichts
    f47h["image"] = nichts
    f50h["image"] = nichts
    f51h["image"] = nichts
    f52h["image"] = nichts
    f53h["image"] = nichts
    f54h["image"] = nichts
    f55h["image"] = nichts
    f56h["image"] = nichts
    f57h["image"] = nichts
    f60h["image"] = nichts
    f61h["image"] = nichts
    f62h["image"] = nichts
    f63h["image"] = nichts
    f64h["image"] = nichts
    f65h["image"] = nichts
    f66h["image"] = nichts
    f67h["image"] = nichts
    f70h["image"] = nichts
    f71h["image"] = nichts
    f72h["image"] = nichts
    f73h["image"] = nichts
    f74h["image"] = nichts
    f75h["image"] = nichts
    f76h["image"] = nichts
    f77h["image"] = nichts
    gewonnen = 0
    smiley["image"] = smileylebt
    amine = 0
    lolol = anomi.count("X")
    while amine<10 - lolol: 
        xmine = randint(0,7) # Es werden zwei zufällige Zahlen generiert,
        ymine = randint(0,7)
        if anomi[ymine][xmine] != "X": # und wenn dieses Feld noch nicht als Bombe eingetragen wurde,
            anomi[ymine][xmine] = "X" # wird es nun als Bombe eingetragen werden
            amine += 1
    zaever1 = -1
    zaever2 = 0
    for i in range(71):
        bidn = 0
        bidnl = []
        zaever1 += 1 # Es werden die verscheidenen Felder durchgegengen
        if zaever1 == 8:
            zaever1 = -1
            zaever2 += 1
        if zaever2==8:
            zaever2 = 0
        if 0<zaever1<7: # Je nach Fall werden die umgebenen Werte in die Liste bidnl
            if 0<zaever2<7:
                bidnl.append(anomi[zaever2-1][zaever1-1])
                bidnl.append(anomi[zaever2-1][zaever1])
                bidnl.append(anomi[zaever2-1][zaever1+1])
                bidnl.append(anomi[zaever2][zaever1-1])
                bidnl.append(anomi[zaever2][zaever1+1])
                bidnl.append(anomi[zaever2+1][zaever1+1])
                bidnl.append(anomi[zaever2+1][zaever1])
                bidnl.append(anomi[zaever2+1][zaever1-1])
            elif zaever2 == 0:
                bidnl.append(anomi[zaever2][zaever1-1])
                bidnl.append(anomi[zaever2][zaever1+1])
                bidnl.append(anomi[zaever2+1][zaever1+1])
                bidnl.append(anomi[zaever2+1][zaever1])
                bidnl.append(anomi[zaever2+1][zaever1-1])      
            elif zaever2 == 7:
                bidnl.append(anomi[zaever2-1][zaever1-1])
                bidnl.append(anomi[zaever2-1][zaever1])
                bidnl.append(anomi[zaever2-1][zaever1+1])
                bidnl.append(anomi[zaever2][zaever1-1])
                bidnl.append(anomi[zaever2][zaever1+1])
        elif zaever1 == 0:
            if 0<zaever2<7:
                bidnl.append(anomi[zaever2-1][zaever1])
                bidnl.append(anomi[zaever2-1][zaever1+1])
                bidnl.append(anomi[zaever2][zaever1+1])
                bidnl.append(anomi[zaever2+1][zaever1+1])
                bidnl.append(anomi[zaever2+1][zaever1])         
            elif zaever2 == 0:
                bidnl.append(anomi[zaever2][zaever1+1])
                bidnl.append(anomi[zaever2+1][zaever1+1])
                bidnl.append(anomi[zaever2+1][zaever1])        
            elif zaever2 == 7:
                bidnl.append(anomi[zaever2-1][zaever1])
                bidnl.append(anomi[zaever2-1][zaever1+1])
                bidnl.append(anomi[zaever2][zaever1+1])         
        elif zaever1 == 7:
            if 0<zaever2<7:
                bidnl.append(anomi[zaever2+1][zaever1])
                bidnl.append(anomi[zaever2+1][zaever1-1])
                bidnl.append(anomi[zaever2][zaever1-1])
                bidnl.append(anomi[zaever2-1][zaever1-1])
                bidnl.append(anomi[zaever2-1][zaever1])         
            elif zaever2 == 0:
                bidnl.append(anomi[zaever2][zaever1-1])
                bidnl.append(anomi[zaever2+1][zaever1-1])
                bidnl.append(anomi[zaever2+1][zaever1])        
            elif zaever2 == 7:
                bidnl.append(anomi[zaever2-1][zaever1])
                bidnl.append(anomi[zaever2-1][zaever1-1])
                bidnl.append(anomi[zaever2][zaever1-1])          
        bidn = bidnl.count("X") # Dann wird gezählt, wie viele Xs in dieser Liste ist
        if bidn != 0: # und wenn diese Zahl nicht 0 ist,
            if anomi[zaever2][zaever1] == " ": # und wenn diese Zahl ein freies Feld ist,
                anomi[zaever2][zaever1] = bidn # wird diese Zahl dort hinein geschrieben

                
def anomirefresh():
    if anomi[0][0] == "X": # Es wird für jedes Feld geschaut, welche Zahl auf die Felder kommt
        f00h["image"] = bombe
    elif anomi[0][0] == 1:
        f00h["image"] = eins
    elif anomi[0][0] == 2:
        f00h["image"] = zwei
    elif anomi[0][0] == 3:
        f00h["image"] = drei
    elif anomi[0][0] == 4:
        f00h["image"] = vier
    elif anomi[0][0] == 5:
        f00h["image"] = fuenf
    elif anomi[0][0] == 6:
        f00h["image"] = sechs
    elif anomi[0][0] == 7:
        f00h["image"] = sieben
    elif anomi[0][0] == 8:
        f00h["image"] = acht
    if anomi[1][0] == "X":
        f01h["image"] = bombe
    elif anomi[1][0] == 1:
        f01h["image"] = eins
    elif anomi[1][0] == 2:
        f01h["image"] = zwei
    elif anomi[1][0] == 3:
        f01h["image"] = drei
    elif anomi[1][0] == 4:
        f01h["image"] = vier
    elif anomi[1][0] == 5:
        f01h["image"] = fuenf
    elif anomi[1][0] == 6:
        f01h["image"] = sechs
    elif anomi[1][0] == 7:
        f01h["image"] = sieben
    elif anomi[1][0] == 8:
        f01h["image"] = acht
    if anomi[2][0] == "X":
        f02h["image"] = bombe
    elif anomi[2][0] == 1:
        f02h["image"] = eins
    elif anomi[2][0] == 2:
        f02h["image"] = zwei
    elif anomi[2][0] == 3:
        f02h["image"] = drei
    elif anomi[2][0] == 4:
        f02h["image"] = vier
    elif anomi[2][0] == 5:
        f02h["image"] = fuenf
    elif anomi[2][0] == 6:
        f02h["image"] = sechs
    elif anomi[2][0] == 7:
        f02h["image"] = sieben
    elif anomi[2][0] == 8:
        f02h["image"] = acht
    if anomi[3][0] == "X":
        f03h["image"] = bombe
    elif anomi[3][0] == 1:
        f03h["image"] = eins
    elif anomi[3][0] == 2:
        f03h["image"] = zwei
    elif anomi[3][0] == 3:
        f03h["image"] = drei
    elif anomi[3][0] == 4:
        f03h["image"] = vier
    elif anomi[3][0] == 5:
        f03h["image"] = fuenf
    elif anomi[3][0] == 6:
        f03h["image"] = sechs
    elif anomi[3][0] == 7:
        f03h["image"] = sieben
    elif anomi[3][0] == 8:
        f03h["image"] = acht
    if anomi[4][0] == "X":
        f04h["image"] = bombe
    elif anomi[4][0] == 1:
        f04h["image"] = eins
    elif anomi[4][0] == 2:
        f04h["image"] = zwei
    elif anomi[4][0] == 3:
        f04h["image"] = drei
    elif anomi[4][0] == 4:
        f04h["image"] = vier
    elif anomi[4][0] == 5:
        f04h["image"] = fuenf
    elif anomi[4][0] == 6:
        f04h["image"] = sechs
    elif anomi[4][0] == 7:
        f04h["image"] = sieben
    elif anomi[4][0] == 8:
        f04h["image"] = acht
    if anomi[5][0] == "X":
        f05h["image"] = bombe
    elif anomi[5][0] == 1:
        f05h["image"] = eins
    elif anomi[5][0] == 2:
        f05h["image"] = zwei
    elif anomi[5][0] == 3:
        f05h["image"] = drei
    elif anomi[5][0] == 4:
        f05h["image"] = vier
    elif anomi[5][0] == 5:
        f05h["image"] = fuenf
    elif anomi[5][0] == 6:
        f05h["image"] = sechs
    elif anomi[5][0] == 7:
        f05h["image"] = sieben
    elif anomi[5][0] == 8:
        f05h["image"] = acht
    if anomi[6][0] == "X":
        f06h["image"] = bombe
    elif anomi[6][0] == 1:
        f06h["image"] = eins
    elif anomi[6][0] == 2:
        f06h["image"] = zwei
    elif anomi[6][0] == 3:
        f06h["image"] = drei
    elif anomi[6][0] == 4:
        f06h["image"] = vier
    elif anomi[6][0] == 5:
        f06h["image"] = fuenf
    elif anomi[6][0] == 6:
        f06h["image"] = sechs
    elif anomi[6][0] == 7:
        f06h["image"] = sieben
    elif anomi[6][0] == 8:
        f06h["image"] = acht
    if anomi[7][0] == "X":
        f07h["image"] = bombe
    elif anomi[7][0] == 1:
        f07h["image"] = eins
    elif anomi[7][0] == 2:
        f07h["image"] = zwei
    elif anomi[7][0] == 3:
        f07h["image"] = drei
    elif anomi[7][0] == 4:
        f07h["image"] = vier
    elif anomi[7][0] == 5:
        f07h["image"] = fuenf
    elif anomi[7][0] == 6:
        f07h["image"] = sechs
    elif anomi[7][0] == 7:
        f07h["image"] = sieben
    elif anomi[7][0] == 8:
        f07h["image"] = acht
    if anomi[0][1] == "X":
        f10h["image"] = bombe
    elif anomi[0][1] == 1:
        f10h["image"] = eins
    elif anomi[0][1] == 2:
        f10h["image"] = zwei
    elif anomi[0][1] == 3:
        f10h["image"] = drei
    elif anomi[0][1] == 4:
        f10h["image"] = vier
    elif anomi[0][1] == 5:
        f10h["image"] = fuenf
    elif anomi[0][1] == 6:
        f10h["image"] = sechs
    elif anomi[0][1] == 7:
        f10h["image"] = sieben
    elif anomi[0][1] == 8:
        f10h["image"] = acht
    if anomi[1][1] == "X":
        f11h["image"] = bombe
    elif anomi[1][1] == 1:
        f11h["image"] = eins
    elif anomi[1][1] == 2:
        f11h["image"] = zwei
    elif anomi[1][1] == 3:
        f11h["image"] = drei
    elif anomi[1][1] == 4:
        f11h["image"] = vier
    elif anomi[1][1] == 5:
        f11h["image"] = fuenf
    elif anomi[1][1] == 6:
        f11h["image"] = sechs
    elif anomi[1][1] == 7:
        f11h["image"] = sieben
    elif anomi[1][1] == 8:
        f11h["image"] = acht
    if anomi[2][1] == "X":
        f12h["image"] = bombe
    elif anomi[2][1] == 1:
        f12h["image"] = eins
    elif anomi[2][1] == 2:
        f12h["image"] = zwei
    elif anomi[2][1] == 3:
        f12h["image"] = drei
    elif anomi[2][1] == 4:
        f12h["image"] = vier
    elif anomi[2][1] == 5:
        f12h["image"] = fuenf
    elif anomi[2][1] == 6:
        f12h["image"] = sechs
    elif anomi[2][1] == 7:
        f12h["image"] = sieben
    elif anomi[2][1] == 8:
        f12h["image"] = acht
    if anomi[3][1] == "X":
        f13h["image"] = bombe
    elif anomi[3][1] == 1:
        f13h["image"] = eins
    elif anomi[3][1] == 2:
        f13h["image"] = zwei
    elif anomi[3][1] == 3:
        f13h["image"] = drei
    elif anomi[3][1] == 4:
        f13h["image"] = vier
    elif anomi[3][1] == 5:
        f13h["image"] = fuenf
    elif anomi[3][1] == 6:
        f13h["image"] = sechs
    elif anomi[3][1] == 7:
        f13h["image"] = sieben
    elif anomi[3][1] == 8:
        f13h["image"] = acht
    if anomi[4][1] == "X":
        f14h["image"] = bombe
    elif anomi[4][1] == 1:
        f14h["image"] = eins
    elif anomi[4][1] == 2:
        f14h["image"] = zwei
    elif anomi[4][1] == 3:
        f14h["image"] = drei
    elif anomi[4][1] == 4:
        f14h["image"] = vier
    elif anomi[4][1] == 5:
        f14h["image"] = fuenf
    elif anomi[4][1] == 6:
        f14h["image"] = sechs
    elif anomi[4][1] == 7:
        f14h["image"] = sieben
    elif anomi[4][1] == 8:
        f14h["image"] = acht
    if anomi[5][1] == "X":
        f15h["image"] = bombe
    elif anomi[5][1] == 1:
        f15h["image"] = eins
    elif anomi[5][1] == 2:
        f15h["image"] = zwei
    elif anomi[5][1] == 3:
        f15h["image"] = drei
    elif anomi[5][1] == 4:
        f15h["image"] = vier
    elif anomi[5][1] == 5:
        f15h["image"] = fuenf
    elif anomi[5][1] == 6:
        f15h["image"] = sechs
    elif anomi[5][1] == 7:
        f15h["image"] = sieben
    elif anomi[5][1] == 8:
        f15h["image"] = acht
    if anomi[6][1] == "X":
        f16h["image"] = bombe
    elif anomi[6][1] == 1:
        f16h["image"] = eins
    elif anomi[6][1] == 2:
        f16h["image"] = zwei
    elif anomi[6][1] == 3:
        f16h["image"] = drei
    elif anomi[6][1] == 4:
        f16h["image"] = vier
    elif anomi[6][1] == 5:
        f16h["image"] = fuenf
    elif anomi[6][1] == 6:
        f16h["image"] = sechs
    elif anomi[6][1] == 7:
        f16h["image"] = sieben
    elif anomi[6][1] == 8:
        f16h["image"] = acht
    if anomi[7][1] == "X":
        f17h["image"] = bombe
    elif anomi[7][1] == 1:
        f17h["image"] = eins
    elif anomi[7][1] == 2:
        f17h["image"] = zwei
    elif anomi[7][1] == 3:
        f17h["image"] = drei
    elif anomi[7][1] == 4:
        f17h["image"] = vier
    elif anomi[7][1] == 5:
        f17h["image"] = fuenf
    elif anomi[7][1] == 6:
        f17h["image"] = sechs
    elif anomi[7][1] == 7:
        f17h["image"] = sieben
    elif anomi[7][1] == 8:
        f17h["image"] = acht
    if anomi[0][2] == "X":
        f20h["image"] = bombe
    elif anomi[0][2] == 1:
        f20h["image"] = eins
    elif anomi[0][2] == 2:
        f20h["image"] = zwei
    elif anomi[0][2] == 3:
        f20h["image"] = drei
    elif anomi[0][2] == 4:
        f20h["image"] = vier
    elif anomi[0][2] == 5:
        f20h["image"] = fuenf
    elif anomi[0][2] == 6:
        f20h["image"] = sechs
    elif anomi[0][2] == 7:
        f20h["image"] = sieben
    elif anomi[0][2] == 8:
        f20h["image"] = acht
    if anomi[1][2] == "X":
        f21h["image"] = bombe
    elif anomi[1][2] == 1:
        f21h["image"] = eins
    elif anomi[1][2] == 2:
        f21h["image"] = zwei
    elif anomi[1][2] == 3:
        f21h["image"] = drei
    elif anomi[1][2] == 4:
        f21h["image"] = vier
    elif anomi[1][2] == 5:
        f21h["image"] = fuenf
    elif anomi[1][2] == 6:
        f21h["image"] = sechs
    elif anomi[1][2] == 7:
        f21h["image"] = sieben
    elif anomi[1][2] == 8:
        f21h["image"] = acht
    if anomi[2][2] == "X":
        f22h["image"] = bombe
    elif anomi[2][2] == 1:
        f22h["image"] = eins
    elif anomi[2][2] == 2:
        f22h["image"] = zwei
    elif anomi[2][2] == 3:
        f22h["image"] = drei
    elif anomi[2][2] == 4:
        f22h["image"] = vier
    elif anomi[2][2] == 5:
        f22h["image"] = fuenf
    elif anomi[2][2] == 6:
        f22h["image"] = sechs
    elif anomi[2][2] == 7:
        f22h["image"] = sieben
    elif anomi[2][2] == 8:
        f22h["image"] = acht
    if anomi[3][2] == "X":
        f23h["image"] = bombe
    elif anomi[3][2] == 1:
        f23h["image"] = eins
    elif anomi[3][2] == 2:
        f23h["image"] = zwei
    elif anomi[3][2] == 3:
        f23h["image"] = drei
    elif anomi[3][2] == 4:
        f23h["image"] = vier
    elif anomi[3][2] == 5:
        f23h["image"] = fuenf
    elif anomi[3][2] == 6:
        f23h["image"] = sechs
    elif anomi[3][2] == 7:
        f23h["image"] = sieben
    elif anomi[3][2] == 8:
        f23h["image"] = acht
    if anomi[4][2] == "X":
        f24h["image"] = bombe
    elif anomi[4][2] == 1:
        f24h["image"] = eins
    elif anomi[4][2] == 2:
        f24h["image"] = zwei
    elif anomi[4][2] == 3:
        f24h["image"] = drei
    elif anomi[4][2] == 4:
        f24h["image"] = vier
    elif anomi[4][2] == 5:
        f24h["image"] = fuenf
    elif anomi[4][2] == 6:
        f24h["image"] = sechs
    elif anomi[4][2] == 7:
        f24h["image"] = sieben
    elif anomi[4][2] == 8:
        f24h["image"] = acht
    if anomi[5][2] == "X":
        f25h["image"] = bombe
    elif anomi[5][2] == 1:
        f25h["image"] = eins
    elif anomi[5][2] == 2:
        f25h["image"] = zwei
    elif anomi[5][2] == 3:
        f25h["image"] = drei
    elif anomi[5][2] == 4:
        f25h["image"] = vier
    elif anomi[5][2] == 5:
        f25h["image"] = fuenf
    elif anomi[5][2] == 6:
        f25h["image"] = sechs
    elif anomi[5][2] == 7:
        f25h["image"] = sieben
    elif anomi[5][2] == 8:
        f25h["image"] = acht
    if anomi[6][2] == "X":
        f26h["image"] = bombe
    elif anomi[6][2] == 1:
        f26h["image"] = eins
    elif anomi[6][2] == 2:
        f26h["image"] = zwei
    elif anomi[6][2] == 3:
        f26h["image"] = drei
    elif anomi[6][2] == 4:
        f26h["image"] = vier
    elif anomi[6][2] == 5:
        f26h["image"] = fuenf
    elif anomi[6][2] == 6:
        f26h["image"] = sechs
    elif anomi[6][2] == 7:
        f26h["image"] = sieben
    elif anomi[6][2] == 8:
        f26h["image"] = acht
    if anomi[7][2] == "X":
        f27h["image"] = bombe
    elif anomi[7][2] == 1:
        f27h["image"] = eins
    elif anomi[7][2] == 2:
        f27h["image"] = zwei
    elif anomi[7][2] == 3:
        f27h["image"] = drei
    elif anomi[7][2] == 4:
        f27h["image"] = vier
    elif anomi[7][2] == 5:
        f27h["image"] = fuenf
    elif anomi[7][2] == 6:
        f27h["image"] = sechs
    elif anomi[7][2] == 7:
        f27h["image"] = sieben
    elif anomi[7][2] == 8:
        f27h["image"] = acht
    if anomi[0][3] == "X":
        f30h["image"] = bombe
    elif anomi[0][3] == 1:
        f30h["image"] = eins
    elif anomi[0][3] == 2:
        f30h["image"] = zwei
    elif anomi[0][3] == 3:
        f30h["image"] = drei
    elif anomi[0][3] == 4:
        f30h["image"] = vier
    elif anomi[0][3] == 5:
        f30h["image"] = fuenf
    elif anomi[0][3] == 6:
        f30h["image"] = sechs
    elif anomi[0][3] == 7:
        f30h["image"] = sieben
    elif anomi[0][3] == 8:
        f30h["image"] = acht
    if anomi[1][3] == "X":
        f31h["image"] = bombe
    elif anomi[1][3] == 1:
        f31h["image"] = eins
    elif anomi[1][3] == 2:
        f31h["image"] = zwei
    elif anomi[1][3] == 3:
        f31h["image"] = drei
    elif anomi[1][3] == 4:
        f31h["image"] = vier
    elif anomi[1][3] == 5:
        f31h["image"] = fuenf
    elif anomi[1][3] == 6:
        f31h["image"] = sechs
    elif anomi[1][3] == 7:
        f31h["image"] = sieben
    elif anomi[1][3] == 8:
        f31h["image"] = acht
    if anomi[2][3] == "X":
        f32h["image"] = bombe
    elif anomi[2][3] == 1:
        f32h["image"] = eins
    elif anomi[2][3] == 2:
        f32h["image"] = zwei
    elif anomi[2][3] == 3:
        f32h["image"] = drei
    elif anomi[2][3] == 4:
        f32h["image"] = vier
    elif anomi[2][3] == 5:
        f32h["image"] = fuenf
    elif anomi[2][3] == 6:
        f32h["image"] = sechs
    elif anomi[2][3] == 7:
        f32h["image"] = sieben
    elif anomi[2][3] == 8:
        f32h["image"] = acht
    if anomi[3][3] == "X":
        f33h["image"] = bombe
    elif anomi[3][3] == 1:
        f33h["image"] = eins
    elif anomi[3][3] == 2:
        f33h["image"] = zwei
    elif anomi[3][3] == 3:
        f33h["image"] = drei
    elif anomi[3][3] == 4:
        f33h["image"] = vier
    elif anomi[3][3] == 5:
        f33h["image"] = fuenf
    elif anomi[3][3] == 6:
        f33h["image"] = sechs
    elif anomi[3][3] == 7:
        f33h["image"] = sieben
    elif anomi[3][3] == 8:
        f33h["image"] = acht
    if anomi[4][3] == "X":
        f34h["image"] = bombe
    elif anomi[4][3] == 1:
        f34h["image"] = eins
    elif anomi[4][3] == 2:
        f34h["image"] = zwei
    elif anomi[4][3] == 3:
        f34h["image"] = drei
    elif anomi[4][3] == 4:
        f34h["image"] = vier
    elif anomi[4][3] == 5:
        f34h["image"] = fuenf
    elif anomi[4][3] == 6:
        f34h["image"] = sechs
    elif anomi[4][3] == 7:
        f34h["image"] = sieben
    elif anomi[4][3] == 8:
        f34h["image"] = acht
    if anomi[5][3] == "X":
        f35h["image"] = bombe
    elif anomi[5][3] == 1:
        f35h["image"] = eins
    elif anomi[5][3] == 2:
        f35h["image"] = zwei
    elif anomi[5][3] == 3:
        f35h["image"] = drei
    elif anomi[5][3] == 4:
        f35h["image"] = vier
    elif anomi[5][3] == 5:
        f35h["image"] = fuenf
    elif anomi[5][3] == 6:
        f35h["image"] = sechs
    elif anomi[5][3] == 7:
        f35h["image"] = sieben
    elif anomi[5][3] == 8:
        f35h["image"] = acht
    if anomi[6][3] == "X":
        f36h["image"] = bombe
    elif anomi[6][3] == 1:
        f36h["image"] = eins
    elif anomi[6][3] == 2:
        f36h["image"] = zwei
    elif anomi[6][3] == 3:
        f36h["image"] = drei
    elif anomi[6][3] == 4:
        f36h["image"] = vier
    elif anomi[6][3] == 5:
        f36h["image"] = fuenf
    elif anomi[6][3] == 6:
        f36h["image"] = sechs
    elif anomi[6][3] == 7:
        f36h["image"] = sieben
    elif anomi[6][3] == 8:
        f36h["image"] = acht
    if anomi[7][3] == "X":
        f37h["image"] = bombe
    elif anomi[7][3] == 1:
        f37h["image"] = eins
    elif anomi[7][3] == 2:
        f37h["image"] = zwei
    elif anomi[7][3] == 3:
        f37h["image"] = drei
    elif anomi[7][3] == 4:
        f37h["image"] = vier
    elif anomi[7][3] == 5:
        f37h["image"] = fuenf
    elif anomi[7][3] == 6:
        f37h["image"] = sechs
    elif anomi[7][3] == 7:
        f37h["image"] = sieben
    elif anomi[7][3] == 8:
        f37h["image"] = acht
    if anomi[0][4] == "X":
        f40h["image"] = bombe
    elif anomi[0][4] == 1:
        f40h["image"] = eins
    elif anomi[0][4] == 2:
        f40h["image"] = zwei
    elif anomi[0][4] == 3:
        f40h["image"] = drei
    elif anomi[0][4] == 4:
        f40h["image"] = vier
    elif anomi[0][4] == 5:
        f40h["image"] = fuenf
    elif anomi[0][4] == 6:
        f40h["image"] = sechs
    elif anomi[0][4] == 7:
        f40h["image"] = sieben
    elif anomi[0][4] == 8:
        f40h["image"] = acht
    if anomi[1][4] == "X":
        f41h["image"] = bombe
    elif anomi[1][4] == 1:
        f41h["image"] = eins
    elif anomi[1][4] == 2:
        f41h["image"] = zwei
    elif anomi[1][4] == 3:
        f41h["image"] = drei
    elif anomi[1][4] == 4:
        f41h["image"] = vier
    elif anomi[1][4] == 5:
        f41h["image"] = fuenf
    elif anomi[1][4] == 6:
        f41h["image"] = sechs
    elif anomi[1][4] == 7:
        f41h["image"] = sieben
    elif anomi[1][4] == 8:
        f41h["image"] = acht
    if anomi[2][4] == "X":
        f42h["image"] = bombe
    elif anomi[2][4] == 1:
        f42h["image"] = eins
    elif anomi[2][4] == 2:
        f42h["image"] = zwei
    elif anomi[2][4] == 3:
        f42h["image"] = drei
    elif anomi[2][4] == 4:
        f42h["image"] = vier
    elif anomi[2][4] == 5:
        f42h["image"] = fuenf
    elif anomi[2][4] == 6:
        f42h["image"] = sechs
    elif anomi[2][4] == 7:
        f42h["image"] = sieben
    elif anomi[2][4] == 8:
        f42h["image"] = acht
    if anomi[3][4] == "X":
        f43h["image"] = bombe
    elif anomi[3][4] == 1:
        f43h["image"] = eins
    elif anomi[3][4] == 2:
        f43h["image"] = zwei
    elif anomi[3][4] == 3:
        f43h["image"] = drei
    elif anomi[3][4] == 4:
        f43h["image"] = vier
    elif anomi[3][4] == 5:
        f43h["image"] = fuenf
    elif anomi[3][4] == 6:
        f43h["image"] = sechs
    elif anomi[3][4] == 7:
        f43h["image"] = sieben
    elif anomi[3][4] == 8:
        f43h["image"] = acht
    if anomi[4][4] == "X":
        f44h["image"] = bombe
    elif anomi[4][4] == 1:
        f44h["image"] = eins
    elif anomi[4][4] == 2:
        f44h["image"] = zwei
    elif anomi[4][4] == 3:
        f44h["image"] = drei
    elif anomi[4][4] == 4:
        f44h["image"] = vier
    elif anomi[4][4] == 5:
        f44h["image"] = fuenf
    elif anomi[4][4] == 6:
        f44h["image"] = sechs
    elif anomi[4][4] == 7:
        f44h["image"] = sieben
    elif anomi[4][4] == 8:
        f44h["image"] = acht
    if anomi[5][4] == "X":
        f45h["image"] = bombe
    elif anomi[5][4] == 1:
        f45h["image"] = eins
    elif anomi[5][4] == 2:
        f45h["image"] = zwei
    elif anomi[5][4] == 3:
        f45h["image"] = drei
    elif anomi[5][4] == 4:
        f45h["image"] = vier
    elif anomi[5][4] == 5:
        f45h["image"] = fuenf
    elif anomi[5][4] == 6:
        f45h["image"] = sechs
    elif anomi[5][4] == 7:
        f45h["image"] = sieben
    elif anomi[5][4] == 8:
        f45h["image"] = acht
    if anomi[6][4] == "X":
        f46h["image"] = bombe
    elif anomi[6][4] == 1:
        f46h["image"] = eins
    elif anomi[6][4] == 2:
        f46h["image"] = zwei
    elif anomi[6][4] == 3:
        f46h["image"] = drei
    elif anomi[6][4] == 4:
        f46h["image"] = vier
    elif anomi[6][4] == 5:
        f46h["image"] = fuenf
    elif anomi[6][4] == 6:
        f46h["image"] = sechs
    elif anomi[6][4] == 7:
        f46h["image"] = sieben
    elif anomi[6][4] == 8:
        f46h["image"] = acht
    if anomi[7][4] == "X":
        f47h["image"] = bombe
    elif anomi[7][4] == 1:
        f47h["image"] = eins
    elif anomi[7][4] == 2:
        f47h["image"] = zwei
    elif anomi[7][4] == 3:
        f47h["image"] = drei
    elif anomi[7][4] == 4:
        f47h["image"] = vier
    elif anomi[7][4] == 5:
        f47h["image"] = fuenf
    elif anomi[7][4] == 6:
        f47h["image"] = sechs
    elif anomi[7][4] == 7:
        f47h["image"] = sieben
    elif anomi[7][4] == 8:
        f47h["image"] = acht
    if anomi[0][5] == "X":
        f50h["image"] = bombe
    elif anomi[0][5] == 1:
        f50h["image"] = eins
    elif anomi[0][5] == 2:
        f50h["image"] = zwei
    elif anomi[0][5] == 3:
        f50h["image"] = drei
    elif anomi[0][5] == 4:
        f50h["image"] = vier
    elif anomi[0][5] == 5:
        f50h["image"] = fuenf
    elif anomi[0][5] == 6:
        f50h["image"] = sechs
    elif anomi[0][5] == 7:
        f50h["image"] = sieben
    elif anomi[0][5] == 8:
        f50h["image"] = acht
    if anomi[1][5] == "X":
        f51h["image"] = bombe
    elif anomi[1][5] == 1:
        f51h["image"] = eins
    elif anomi[1][5] == 2:
        f51h["image"] = zwei
    elif anomi[1][5] == 3:
        f51h["image"] = drei
    elif anomi[1][5] == 4:
        f51h["image"] = vier
    elif anomi[1][5] == 5:
        f51h["image"] = fuenf
    elif anomi[1][5] == 6:
        f51h["image"] = sechs
    elif anomi[1][5] == 7:
        f51h["image"] = sieben
    elif anomi[1][5] == 8:
        f51h["image"] = acht
    if anomi[2][5] == "X":
        f52h["image"] = bombe
    elif anomi[2][5] == 1:
        f52h["image"] = eins
    elif anomi[2][5] == 2:
        f52h["image"] = zwei
    elif anomi[2][5] == 3:
        f52h["image"] = drei
    elif anomi[2][5] == 4:
        f52h["image"] = vier
    elif anomi[2][5] == 5:
        f52h["image"] = fuenf
    elif anomi[2][5] == 6:
        f52h["image"] = sechs
    elif anomi[2][5] == 7:
        f52h["image"] = sieben
    elif anomi[2][5] == 8:
        f52h["image"] = acht
    if anomi[3][5] == "X":
        f53h["image"] = bombe
    elif anomi[3][5] == 1:
        f53h["image"] = eins
    elif anomi[3][5] == 2:
        f53h["image"] = zwei
    elif anomi[3][5] == 3:
        f53h["image"] = drei
    elif anomi[3][5] == 4:
        f53h["image"] = vier
    elif anomi[3][5] == 5:
        f53h["image"] = fuenf
    elif anomi[3][5] == 6:
        f53h["image"] = sechs
    elif anomi[3][5] == 7:
        f53h["image"] = sieben
    elif anomi[3][5] == 8:
        f53h["image"] = acht
    if anomi[4][5] == "X":
        f54h["image"] = bombe
    elif anomi[4][5] == 1:
        f54h["image"] = eins
    elif anomi[4][5] == 2:
        f54h["image"] = zwei
    elif anomi[4][5] == 3:
        f54h["image"] = drei
    elif anomi[4][5] == 4:
        f54h["image"] = vier
    elif anomi[4][5] == 5:
        f54h["image"] = fuenf
    elif anomi[4][5] == 6:
        f54h["image"] = sechs
    elif anomi[4][5] == 7:
        f54h["image"] = sieben
    elif anomi[4][5] == 8:
        f54h["image"] = acht
    if anomi[5][5] == "X":
        f55h["image"] = bombe
    elif anomi[5][5] == 1:
        f55h["image"] = eins
    elif anomi[5][5] == 2:
        f55h["image"] = zwei
    elif anomi[5][5] == 3:
        f55h["image"] = drei
    elif anomi[5][5] == 4:
        f55h["image"] = vier
    elif anomi[5][5] == 5:
        f55h["image"] = fuenf
    elif anomi[5][5] == 6:
        f55h["image"] = sechs
    elif anomi[5][5] == 7:
        f55h["image"] = sieben
    elif anomi[5][5] == 8:
        f55h["image"] = acht
    if anomi[6][5] == "X":
        f56h["image"] = bombe
    elif anomi[6][5] == 1:
        f56h["image"] = eins
    elif anomi[6][5] == 2:
        f56h["image"] = zwei
    elif anomi[6][5] == 3:
        f56h["image"] = drei
    elif anomi[6][5] == 4:
        f56h["image"] = vier
    elif anomi[6][5] == 5:
        f56h["image"] = fuenf
    elif anomi[6][5] == 6:
        f56h["image"] = sechs
    elif anomi[6][5] == 7:
        f56h["image"] = sieben
    elif anomi[6][5] == 8:
        f56h["image"] = acht
    if anomi[7][5] == "X":
        f57h["image"] = bombe
    elif anomi[7][5] == 1:
        f57h["image"] = eins
    elif anomi[7][5] == 2:
        f57h["image"] = zwei
    elif anomi[7][5] == 3:
        f57h["image"] = drei
    elif anomi[7][5] == 4:
        f57h["image"] = vier
    elif anomi[7][5] == 5:
        f57h["image"] = fuenf
    elif anomi[7][5] == 6:
        f57h["image"] = sechs
    elif anomi[7][5] == 7:
        f57h["image"] = sieben
    elif anomi[7][5] == 8:
        f57h["image"] = acht
    if anomi[0][6] == "X":
        f60h["image"] = bombe
    elif anomi[0][6] == 1:
        f60h["image"] = eins
    elif anomi[0][6] == 2:
        f60h["image"] = zwei
    elif anomi[0][6] == 3:
        f60h["image"] = drei
    elif anomi[0][6] == 4:
        f60h["image"] = vier
    elif anomi[0][6] == 5:
        f60h["image"] = fuenf
    elif anomi[0][6] == 6:
        f60h["image"] = sechs
    elif anomi[0][6] == 7:
        f60h["image"] = sieben
    elif anomi[0][6] == 8:
        f60h["image"] = acht
    if anomi[1][6] == "X":
        f61h["image"] = bombe
    elif anomi[1][6] == 1:
        f61h["image"] = eins
    elif anomi[1][6] == 2:
        f61h["image"] = zwei
    elif anomi[1][6] == 3:
        f61h["image"] = drei
    elif anomi[1][6] == 4:
        f61h["image"] = vier
    elif anomi[1][6] == 5:
        f61h["image"] = fuenf
    elif anomi[1][6] == 6:
        f61h["image"] = sechs
    elif anomi[1][6] == 7:
        f61h["image"] = sieben
    elif anomi[1][6] == 8:
        f61h["image"] = acht
    if anomi[2][6] == "X":
        f62h["image"] = bombe
    elif anomi[2][6] == 1:
        f62h["image"] = eins
    elif anomi[2][6] == 2:
        f62h["image"] = zwei
    elif anomi[2][6] == 3:
        f62h["image"] = drei
    elif anomi[2][6] == 4:
        f62h["image"] = vier
    elif anomi[2][6] == 5:
        f62h["image"] = fuenf
    elif anomi[2][6] == 6:
        f62h["image"] = sechs
    elif anomi[2][6] == 7:
        f62h["image"] = sieben
    elif anomi[2][6] == 8:
        f62h["image"] = acht
    if anomi[3][6] == "X":
        f63h["image"] = bombe
    elif anomi[3][6] == 1:
        f63h["image"] = eins
    elif anomi[3][6] == 2:
        f63h["image"] = zwei
    elif anomi[3][6] == 3:
        f63h["image"] = drei
    elif anomi[3][6] == 4:
        f63h["image"] = vier
    elif anomi[3][6] == 5:
        f63h["image"] = fuenf
    elif anomi[3][6] == 6:
        f63h["image"] = sechs
    elif anomi[3][6] == 7:
        f63h["image"] = sieben
    elif anomi[3][6] == 8:
        f63h["image"] = acht
    if anomi[4][6] == "X":
        f64h["image"] = bombe
    elif anomi[4][6] == 1:
        f64h["image"] = eins
    elif anomi[4][6] == 2:
        f64h["image"] = zwei
    elif anomi[4][6] == 3:
        f64h["image"] = drei
    elif anomi[4][6] == 4:
        f64h["image"] = vier
    elif anomi[4][6] == 5:
        f64h["image"] = fuenf
    elif anomi[4][6] == 6:
        f64h["image"] = sechs
    elif anomi[4][6] == 7:
        f64h["image"] = sieben
    elif anomi[4][6] == 8:
        f64h["image"] = acht
    if anomi[5][6] == "X":
        f65h["image"] = bombe
    elif anomi[5][6] == 1:
        f65h["image"] = eins
    elif anomi[5][6] == 2:
        f65h["image"] = zwei
    elif anomi[5][6] == 3:
        f65h["image"] = drei
    elif anomi[5][6] == 4:
        f65h["image"] = vier
    elif anomi[5][6] == 5:
        f65h["image"] = fuenf
    elif anomi[5][6] == 6:
        f65h["image"] = sechs
    elif anomi[5][6] == 7:
        f65h["image"] = sieben
    elif anomi[5][6] == 8:
        f65h["image"] = acht
    if anomi[6][6] == "X":
        f66h["image"] = bombe
    elif anomi[6][6] == 1:
        f66h["image"] = eins
    elif anomi[6][6] == 2:
        f66h["image"] = zwei
    elif anomi[6][6] == 3:
        f66h["image"] = drei
    elif anomi[6][6] == 4:
        f66h["image"] = vier
    elif anomi[6][6] == 5:
        f66h["image"] = fuenf
    elif anomi[6][6] == 6:
        f66h["image"] = sechs
    elif anomi[6][6] == 7:
        f66h["image"] = sieben
    elif anomi[6][6] == 8:
        f66h["image"] = acht
    if anomi[7][6] == "X":
        f67h["image"] = bombe
    elif anomi[7][6] == 1:
        f67h["image"] = eins
    elif anomi[7][6] == 2:
        f67h["image"] = zwei
    elif anomi[7][6] == 3:
        f67h["image"] = drei
    elif anomi[7][6] == 4:
        f67h["image"] = vier
    elif anomi[7][6] == 5:
        f67h["image"] = fuenf
    elif anomi[7][6] == 6:
        f67h["image"] = sechs
    elif anomi[7][6] == 7:
        f67h["image"] = sieben
    elif anomi[7][6] == 8:
        f67h["image"] = acht
    if anomi[0][7] == "X":
        f70h["image"] = bombe
    elif anomi[0][7] == 1:
        f70h["image"] = eins
    elif anomi[0][7] == 2:
        f70h["image"] = zwei
    elif anomi[0][7] == 3:
        f70h["image"] = drei
    elif anomi[0][7] == 4:
        f70h["image"] = vier
    elif anomi[0][7] == 5:
        f70h["image"] = fuenf
    elif anomi[0][7] == 6:
        f70h["image"] = sechs
    elif anomi[0][7] == 7:
        f70h["image"] = sieben
    elif anomi[0][7] == 8:
        f70h["image"] = acht
    if anomi[1][7] == "X":
        f71h["image"] = bombe
    elif anomi[1][7] == 1:
        f71h["image"] = eins
    elif anomi[1][7] == 2:
        f71h["image"] = zwei
    elif anomi[1][7] == 3:
        f71h["image"] = drei
    elif anomi[1][7] == 4:
        f71h["image"] = vier
    elif anomi[1][7] == 5:
        f71h["image"] = fuenf
    elif anomi[1][7] == 6:
        f71h["image"] = sechs
    elif anomi[1][7] == 7:
        f71h["image"] = sieben
    elif anomi[1][7] == 8:
        f71h["image"] = acht
    if anomi[2][7] == "X":
        f72h["image"] = bombe
    elif anomi[2][7] == 1:
        f72h["image"] = eins
    elif anomi[2][7] == 2:
        f72h["image"] = zwei
    elif anomi[2][7] == 3:
        f72h["image"] = drei
    elif anomi[2][7] == 4:
        f72h["image"] = vier
    elif anomi[2][7] == 5:
        f72h["image"] = fuenf
    elif anomi[2][7] == 6:
        f72h["image"] = sechs
    elif anomi[2][7] == 7:
        f72h["image"] = sieben
    elif anomi[2][7] == 8:
        f72h["image"] = acht
    if anomi[3][7] == "X":
        f73h["image"] = bombe
    elif anomi[3][7] == 1:
        f73h["image"] = eins
    elif anomi[3][7] == 2:
        f73h["image"] = zwei
    elif anomi[3][7] == 3:
        f73h["image"] = drei
    elif anomi[3][7] == 4:
        f73h["image"] = vier
    elif anomi[3][7] == 5:
        f73h["image"] = fuenf
    elif anomi[3][7] == 6:
        f73h["image"] = sechs
    elif anomi[3][7] == 7:
        f73h["image"] = sieben
    elif anomi[3][7] == 8:
        f73h["image"] = acht
    if anomi[4][7] == "X":
        f74h["image"] = bombe
    elif anomi[4][7] == 1:
        f74h["image"] = eins
    elif anomi[4][7] == 2:
        f74h["image"] = zwei
    elif anomi[4][7] == 3:
        f74h["image"] = drei
    elif anomi[4][7] == 4:
        f74h["image"] = vier
    elif anomi[4][7] == 5:
        f74h["image"] = fuenf
    elif anomi[4][7] == 6:
        f74h["image"] = sechs
    elif anomi[4][7] == 7:
        f74h["image"] = sieben
    elif anomi[4][7] == 8:
        f74h["image"] = acht
    if anomi[5][7] == "X":
        f75h["image"] = bombe
    elif anomi[5][7] == 1:
        f75h["image"] = eins
    elif anomi[5][7] == 2:
        f75h["image"] = zwei
    elif anomi[5][7] == 3:
        f75h["image"] = drei
    elif anomi[5][7] == 4:
        f75h["image"] = vier
    elif anomi[5][7] == 5:
        f75h["image"] = fuenf
    elif anomi[5][7] == 6:
        f75h["image"] = sechs
    elif anomi[5][7] == 7:
        f75h["image"] = sieben
    elif anomi[5][7] == 8:
        f75h["image"] = acht
    if anomi[6][7] == "X":
        f76h["image"] = bombe
    elif anomi[6][7] == 1:
        f76h["image"] = eins
    elif anomi[6][7] == 2:
        f76h["image"] = zwei
    elif anomi[6][7] == 3:
        f76h["image"] = drei
    elif anomi[6][7] == 4:
        f76h["image"] = vier
    elif anomi[6][7] == 5:
        f76h["image"] = fuenf
    elif anomi[6][7] == 6:
        f76h["image"] = sechs
    elif anomi[6][7] == 7:
        f76h["image"] = sieben
    elif anomi[6][7] == 8:
        f76h["image"] = acht
    if anomi[7][7] == "X":
        f77h["image"] = bombe
    elif anomi[7][7] == 1:
        f77h["image"] = eins
    elif anomi[7][7] == 2:
        f77h["image"] = zwei
    elif anomi[7][7] == 3:
        f77h["image"] = drei
    elif anomi[7][7] == 4:
        f77h["image"] = vier
    elif anomi[7][7] == 5:
        f77h["image"] = fuenf
    elif anomi[7][7] == 6:
        f77h["image"] = sechs
    elif anomi[7][7] == 7:
        f77h["image"] = sieben
    elif anomi[7][7] == 8:
        f07h["image"] = acht
def normaldesign():
    global p00, p01, p02, p03, p04, p05, p06, p07, p10, p11, p12, p13, p14, p15, p16, p17, p20, p21, p22, p23, p24, p25, p26, p27, p30, p31, p32, p33, p34, p35, p36, p37, p40, p41, p42, p43, p44, p45, p46, p47, p50, p51, p52, p53, p54, p55, p56, p57, p60, p61, p62, p63, p64, p65, p66, p67, p70, p71, p72, p73, p74, p75, p76, p77
    p00 = nichts # Beim normalen Design , wird das Bild eines jeden Feldes auf nichts gesetzt
    p01 = nichts
    p02 = nichts
    p03 = nichts
    p04 = nichts
    p05 = nichts
    p06 = nichts
    p07 = nichts
    p10 = nichts
    p11 = nichts
    p12 = nichts
    p13 = nichts
    p14 = nichts
    p15 = nichts
    p16 = nichts
    p17 = nichts
    p20 = nichts
    p21 = nichts
    p22 = nichts
    p23 = nichts
    p24 = nichts
    p25 = nichts
    p26 = nichts
    p27 = nichts
    p30 = nichts
    p31 = nichts
    p32 = nichts
    p33 = nichts
    p34 = nichts
    p35 = nichts
    p36 = nichts
    p37 = nichts
    p40 = nichts
    p41 = nichts
    p42 = nichts
    p43 = nichts
    p44 = nichts
    p45 = nichts
    p46 = nichts
    p47 = nichts
    p50 = nichts
    p51 = nichts
    p52 = nichts
    p53 = nichts
    p54 = nichts
    p55 = nichts
    p56 = nichts
    p57 = nichts
    p60 = nichts
    p61 = nichts
    p62 = nichts
    p63 = nichts
    p64 = nichts
    p65 = nichts
    p66 = nichts
    p67 = nichts
    p70 = nichts
    p71 = nichts
    p72 = nichts
    p73 = nichts
    p74 = nichts
    p75 = nichts
    p76 = nichts
    p77 = nichts
    refresh()
def sommerdesign():
    global p00, p01, p02, p03, p04, p05, p06, p07, p10, p11, p12, p13, p14, p15, p16, p17, p20, p21, p22, p23, p24, p25, p26, p27, p30, p31, p32, p33, p34, p35, p36, p37, p40, p41, p42, p43, p44, p45, p46, p47, p50, p51, p52, p53, p54, p55, p56, p57, p60, p61, p62, p63, p64, p65, p66, p67, p70, p71, p72, p73, p74, p75, p76, p77
    p00 = b00 # Und beim Sommerdesign wird jedes Feld zu seinem passenden Bild zugeordnet
    p01 = b01
    p02 = b02
    p03 = b03
    p04 = b04
    p05 = b05
    p06 = b06
    p07 = b07
    p10 = b10
    p11 = b11
    p12 = b12
    p13 = b13
    p14 = b14
    p15 = b15
    p16 = b16
    p17 = b17
    p20 = b20
    p21 = b21
    p22 = b22
    p23 = b23
    p24 = b24
    p25 = b25
    p26 = b26
    p27 = b27
    p30 = b30
    p31 = b31
    p32 = b32
    p33 = b33
    p34 = b34
    p35 = b35
    p36 = b36
    p37 = b37
    p40 = b40
    p41 = b41
    p42 = b42
    p43 = b43
    p44 = b44
    p45 = b45
    p46 = b46
    p47 = b47
    p50 = b50
    p51 = b51
    p52 = b52
    p53 = b53
    p54 = b54
    p55 = b55
    p56 = b56
    p57 = b57
    p60 = b60
    p61 = b61
    p62 = b62
    p63 = b63
    p64 = b64
    p65 = b65
    p66 = b66
    p67 = b67
    p70 = b70
    p71 = b71
    p72 = b72
    p73 = b73
    p74 = b74
    p75 = b75
    p76 = b76
    p77 = b77
    refresh()
    
## --GRAFIK--
if True:
    hf = Tk() # Das Fenster wird erstellt
    hf.title("Minesweeper") # Der Titel wird auf Minesweeper geändert
    hf.iconbitmap("Pictures/icon.ico") # Das Icon wird verändert
    hf.resizable(0,0) # Die Größe des Fensters lässt sich nicht mehr verändern
    menu = Menu(hf) # Es wird ein Menu hinzugefügt
    hf.config(menu=menu) # Das Menu wird festgelegt
    designmenu = Menu(menu) # Zum Menu werden das Designmenu
    wmenu = Menu(menu) # und das Menu "Weiteres" hinzugefügt
    selected_design = StringVar(hf, "Normal") # Damit im Designmenu der Punkt "Normal" vorausgewählt ist
    menu.add_cascade(label="Design", menu=designmenu) # Die beiden Menus werden zur Leiste hinzugefügt
    menu.add_cascade(label="Weiteres", menu=wmenu)
    designmenu.add_radiobutton(label="Normal", variable = selected_design, command=normaldesign) # Zum Designmenu werden beide Optionen hinzugefügt
    designmenu.add_radiobutton(label="Sommer", variable = selected_design, command=sommerdesign)
    wmenu.add_command(label="Highscoreliste", command=highscorel) # Zum weiteren Menu werden alle 3 Optionen hinzugefügt
    wmenu.add_command(label="Tutorial", command=tutorial)
    wmenu.add_command(label="About", command=about) 
    nichts = PhotoImage(file="Pictures/nichts.gif") # es werden alle Bilder hinzugefügt
    flagge = PhotoImage(file="Pictures/flagge.gif")
    fragezeichen = PhotoImage(file="Pictures/fragezeichen.gif")
    bombe = PhotoImage(file="Pictures/bombe.gif")
    smileylebt = PhotoImage(file="Pictures/smileylebt.gif")
    smileytot = PhotoImage(file="Pictures/smileytot.gif")
    eins = PhotoImage(file="Pictures/eins.gif")
    zwei = PhotoImage(file="Pictures/zwei.gif")
    drei = PhotoImage(file="Pictures/drei.gif")
    vier = PhotoImage(file="Pictures/vier.gif")
    fuenf = PhotoImage(file="Pictures/fünf.gif")
    sechs = PhotoImage(file="Pictures/sechs.gif")
    sieben = PhotoImage(file="Pictures/sieben.gif")
    acht = PhotoImage(file="Pictures/acht.gif")
    hintergrund_zeit = PhotoImage(file="Pictures/hintergrund.gif")
    b00 = PhotoImage(file="Pictures/00.gif")
    b01 = PhotoImage(file="Pictures/01.gif")
    b02 = PhotoImage(file="Pictures/02.gif")
    b03 = PhotoImage(file="Pictures/03.gif")
    b04 = PhotoImage(file="Pictures/04.gif")
    b05 = PhotoImage(file="Pictures/05.gif")
    b06 = PhotoImage(file="Pictures/06.gif")
    b07 = PhotoImage(file="Pictures/07.gif")
    b10 = PhotoImage(file="Pictures/10.gif")
    b11 = PhotoImage(file="Pictures/11.gif")
    b12 = PhotoImage(file="Pictures/12.gif")
    b13 = PhotoImage(file="Pictures/13.gif")
    b14 = PhotoImage(file="Pictures/14.gif")
    b15 = PhotoImage(file="Pictures/15.gif")
    b16 = PhotoImage(file="Pictures/16.gif")
    b17 = PhotoImage(file="Pictures/17.gif")
    b20 = PhotoImage(file="Pictures/20.gif")
    b21 = PhotoImage(file="Pictures/21.gif")
    b22 = PhotoImage(file="Pictures/22.gif")
    b23 = PhotoImage(file="Pictures/23.gif")
    b24 = PhotoImage(file="Pictures/24.gif")
    b25 = PhotoImage(file="Pictures/25.gif")
    b26 = PhotoImage(file="Pictures/26.gif")
    b27 = PhotoImage(file="Pictures/27.gif")
    b30 = PhotoImage(file="Pictures/30.gif")
    b31 = PhotoImage(file="Pictures/31.gif")
    b32 = PhotoImage(file="Pictures/32.gif")
    b33 = PhotoImage(file="Pictures/33.gif")
    b34 = PhotoImage(file="Pictures/34.gif")
    b35 = PhotoImage(file="Pictures/35.gif")
    b36 = PhotoImage(file="Pictures/36.gif")
    b37 = PhotoImage(file="Pictures/37.gif")
    b40 = PhotoImage(file="Pictures/40.gif")
    b41 = PhotoImage(file="Pictures/41.gif")
    b42 = PhotoImage(file="Pictures/42.gif")
    b43 = PhotoImage(file="Pictures/43.gif")
    b44 = PhotoImage(file="Pictures/44.gif")
    b45 = PhotoImage(file="Pictures/45.gif")
    b46 = PhotoImage(file="Pictures/46.gif")
    b47 = PhotoImage(file="Pictures/47.gif")
    b50 = PhotoImage(file="Pictures/50.gif")
    b51 = PhotoImage(file="Pictures/51.gif")
    b52 = PhotoImage(file="Pictures/52.gif")
    b53 = PhotoImage(file="Pictures/53.gif")
    b54 = PhotoImage(file="Pictures/54.gif")
    b55 = PhotoImage(file="Pictures/55.gif")
    b56 = PhotoImage(file="Pictures/56.gif")
    b57 = PhotoImage(file="Pictures/57.gif")
    b60 = PhotoImage(file="Pictures/60.gif")
    b61 = PhotoImage(file="Pictures/61.gif")
    b62 = PhotoImage(file="Pictures/62.gif")
    b63 = PhotoImage(file="Pictures/63.gif")
    b64 = PhotoImage(file="Pictures/64.gif")
    b65 = PhotoImage(file="Pictures/65.gif")
    b66 = PhotoImage(file="Pictures/66.gif")
    b67 = PhotoImage(file="Pictures/67.gif")
    b70 = PhotoImage(file="Pictures/70.gif")
    b71 = PhotoImage(file="Pictures/71.gif")
    b72 = PhotoImage(file="Pictures/72.gif")
    b73 = PhotoImage(file="Pictures/73.gif")
    b74 = PhotoImage(file="Pictures/74.gif")
    b75 = PhotoImage(file="Pictures/75.gif")
    b76 = PhotoImage(file="Pictures/76.gif")
    b77 = PhotoImage(file="Pictures/77.gif")
    gw = Label(hf, text=10-fehlende_flaggen) # Fehlende Flaggen werden hinzugefügt
    smiley = Button(hf, image=smileylebt, height=20, width=20) # Der Neustartknopf wird hinzugefügt
    smiley.grid(row=0, column=3, columnspan=2)
    zeitanzeige = Label(hf, text=timestr) # Der Timer wird hinzugefügt
    zeitanzeige.grid(columnspan = 3, column = 5, row = 0)
    gw.grid(row=0, column=0, columnspan=3)
    f00h= Label(hf, image=nichts) # Alle Feledr werden hinzugefügt
    f01h= Label(hf, image=nichts)
    f02h= Label(hf, image=nichts)
    f03h= Label(hf, image=nichts)
    f04h= Label(hf, image=nichts)
    f05h= Label(hf, image=nichts)
    f05h= Label(hf, image=nichts)
    f06h= Label(hf, image=nichts)
    f07h= Label(hf, image=nichts)
    f10h= Label(hf, image=nichts)
    f11h= Label(hf, image=nichts)
    f12h= Label(hf, image=nichts)
    f13h= Label(hf, image=nichts)
    f14h= Label(hf, image=nichts)
    f15h= Label(hf, image=nichts)
    f16h= Label(hf, image=nichts)
    f17h= Label(hf, image=nichts)
    f20h= Label(hf, image=nichts)
    f21h= Label(hf, image=nichts)
    f22h= Label(hf, image=nichts)
    f23h= Label(hf, image=nichts)
    f24h= Label(hf, image=nichts)
    f25h= Label(hf, image=nichts)
    f26h= Label(hf, image=nichts)
    f27h= Label(hf, image=nichts)
    f30h= Label(hf, image=nichts)
    f31h= Label(hf, image=nichts)
    f32h= Label(hf, image=nichts)
    f33h= Label(hf, image=nichts)
    f34h= Label(hf, image=nichts)
    f35h= Label(hf, image=nichts)
    f36h= Label(hf, image=nichts)
    f37h= Label(hf, image=nichts)
    f40h= Label(hf, image=nichts)
    f41h= Label(hf, image=nichts)
    f42h= Label(hf, image=nichts)
    f43h= Label(hf, image=nichts)
    f44h= Label(hf, image=nichts)
    f45h= Label(hf, image=nichts)
    f46h= Label(hf, image=nichts)
    f47h= Label(hf, image=nichts)
    f50h= Label(hf, image=nichts)
    f51h= Label(hf, image=nichts)
    f52h= Label(hf, image=nichts)
    f53h= Label(hf, image=nichts)
    f54h= Label(hf, image=nichts)
    f55h= Label(hf, image=nichts)
    f56h= Label(hf, image=nichts)
    f57h= Label(hf, image=nichts)
    f60h= Label(hf, image=nichts)
    f61h= Label(hf, image=nichts)
    f62h= Label(hf, image=nichts)
    f63h= Label(hf, image=nichts)
    f64h= Label(hf, image=nichts)
    f65h= Label(hf, image=nichts)
    f66h= Label(hf, image=nichts)
    f67h= Label(hf, image=nichts)
    f70h= Label(hf, image=nichts)
    f71h= Label(hf, image=nichts)
    f72h= Label(hf, image=nichts)
    f73h= Label(hf, image=nichts)
    f74h= Label(hf, image=nichts)
    f75h= Label(hf, image=nichts)
    f76h= Label(hf, image=nichts)
    f77h= Label(hf, image=nichts)
    f00h.grid(row=1, column=0)
    f01h.grid(row=2, column=0)
    f02h.grid(row=3, column=0)
    f03h.grid(row=4, column=0)
    f04h.grid(row=5, column=0)
    f05h.grid(row=6, column=0)
    f06h.grid(row=7, column=0)
    f07h.grid(row=8, column=0)
    f10h.grid(row=1, column=1)
    f11h.grid(row=2, column=1)
    f12h.grid(row=3, column=1)
    f13h.grid(row=4, column=1)
    f14h.grid(row=5, column=1)
    f15h.grid(row=6, column=1)
    f16h.grid(row=7, column=1)
    f17h.grid(row=8, column=1)
    f20h.grid(row=1, column=2)
    f21h.grid(row=2, column=2)
    f22h.grid(row=3, column=2)
    f23h.grid(row=4, column=2)
    f24h.grid(row=5, column=2)
    f25h.grid(row=6, column=2)
    f26h.grid(row=7, column=2)
    f27h.grid(row=8, column=2)
    f30h.grid(row=1, column=3)
    f31h.grid(row=2, column=3)
    f32h.grid(row=3, column=3)
    f33h.grid(row=4, column=3)
    f34h.grid(row=5, column=3)
    f35h.grid(row=6, column=3)
    f36h.grid(row=7, column=3)
    f37h.grid(row=8, column=3)
    f40h.grid(row=1, column=4)
    f41h.grid(row=2, column=4)
    f42h.grid(row=3, column=4)
    f43h.grid(row=4, column=4)
    f44h.grid(row=5, column=4)
    f45h.grid(row=6, column=4)
    f46h.grid(row=7, column=4)
    f47h.grid(row=8, column=4)
    f50h.grid(row=1, column=5)
    f51h.grid(row=2, column=5)
    f52h.grid(row=3, column=5)
    f53h.grid(row=4, column=5)
    f54h.grid(row=5, column=5)
    f55h.grid(row=6, column=5)
    f56h.grid(row=7, column=5)
    f57h.grid(row=8, column=5)
    f60h.grid(row=1, column=6)
    f61h.grid(row=2, column=6)
    f62h.grid(row=3, column=6)
    f63h.grid(row=4, column=6)
    f64h.grid(row=5, column=6)
    f65h.grid(row=6, column=6)
    f66h.grid(row=7, column=6)
    f67h.grid(row=8, column=6)
    f70h.grid(row=1, column=7)
    f71h.grid(row=2, column=7)
    f72h.grid(row=3, column=7)
    f73h.grid(row=4, column=7)
    f74h.grid(row=5, column=7)
    f75h.grid(row=6, column=7)
    f76h.grid(row=7, column=7)
    f77h.grid(row=8, column=7)
    f00= Button(hf, height=20, width=20, image=nichts)
    f00.bind("<Button-1>", f00l) # Die Commands werden den Buttons zugeordnet
    f00.bind("<Button-3>", f00r)
    f01= Button(hf, height=20, width=20, image=nichts)
    f01.bind("<Button-1>", f01l)
    f01.bind("<Button-3>", f01r)
    f02= Button(hf, height=20, width=20, image=nichts)
    f02.bind("<Button-1>", f02l)
    f02.bind("<Button-3>", f02r)
    f03= Button(hf, height=20, width=20, image=nichts)
    f03.bind("<Button-1>", f03l)
    f03.bind("<Button-3>", f03r)
    f04= Button(hf, height=20, width=20, image=nichts)
    f04.bind("<Button-1>", f04l)
    f04.bind("<Button-3>", f04r)
    f05= Button(hf, height=20, width=20, image=nichts)
    f05.bind("<Button-1>", f05l)
    f05.bind("<Button-3>", f05r)
    f06= Button(hf, height=20,width=20, image=nichts)
    f06.bind("<Button-1>", f06l)
    f06.bind("<Button-3>", f06r)
    f07= Button(hf, height=20, width=20, image=nichts)
    f07.bind("<Button-1>", f07l)
    f07.bind("<Button-3>", f07r)
    f10= Button(hf, height=20, width=20, image=nichts)
    f10.bind("<Button-1>", f10l)
    f10.bind("<Button-3>", f10r)
    f11= Button(hf, height=20, width=20, image=nichts)
    f11.bind("<Button-1>", f11l)
    f11.bind("<Button-3>", f11r)
    f12= Button(hf, height=20, width=20, image=nichts)
    f12.bind("<Button-1>", f12l)
    f12.bind("<Button-3>", f12r)
    f13= Button(hf, height=20, width=20, image=nichts)
    f13.bind("<Button-1>", f13l)
    f13.bind("<Button-3>", f13r)
    f14= Button(hf, height=20, width=20, image=nichts)
    f14.bind("<Button-1>", f14l)
    f14.bind("<Button-3>", f14r)
    f15= Button(hf, height=20, width=20, image=nichts)
    f15.bind("<Button-1>", f15l)
    f15.bind("<Button-3>", f15r)
    f16= Button(hf, height=20, width=20, image=nichts)
    f16.bind("<Button-1>", f16l)
    f16.bind("<Button-3>", f16r)
    f17= Button(hf, height=20, width=20, image=nichts)
    f17.bind("<Button-1>", f17l)
    f17.bind("<Button-3>", f17r)
    f20= Button(hf, height=20, width=20, image=nichts)
    f20.bind("<Button-1>", f20l)
    f20.bind("<Button-3>", f20r)
    f21= Button(hf, height=20, width=20, image=nichts)
    f21.bind("<Button-1>", f21l)
    f21.bind("<Button-3>", f21r)
    f22= Button(hf, height=20, width=20, image=nichts)
    f22.bind("<Button-1>", f22l)
    f22.bind("<Button-3>", f22r)
    f23= Button(hf, height=20, width=20, image=nichts)
    f23.bind("<Button-1>", f23l)
    f23.bind("<Button-3>", f23r)
    f24= Button(hf, height=20, width=20, image=nichts)
    f24.bind("<Button-1>", f24l)
    f24.bind("<Button-3>", f24r)
    f25= Button(hf, height=20, width=20, image=nichts)
    f25.bind("<Button-1>", f25l)
    f25.bind("<Button-3>", f25r)
    f26= Button(hf, height=20, width=20, image=nichts)
    f26.bind("<Button-1>", f26l)
    f26.bind("<Button-3>", f26r)
    f27= Button(hf, height=20, width=20, image=nichts)
    f27.bind("<Button-1>", f27l)
    f27.bind("<Button-3>", f27r)
    f30= Button(hf, height=20, width=20, image=nichts)
    f30.bind("<Button-1>", f30l)
    f30.bind("<Button-3>", f30r)
    f31= Button(hf, height=20, width=20, image=nichts)
    f31.bind("<Button-1>", f31l)
    f31.bind("<Button-3>", f31r)
    f32= Button(hf, height=20, width=20, image=nichts)
    f32.bind("<Button-1>", f32l)
    f32.bind("<Button-3>", f32r)
    f33= Button(hf, height=20, width=20, image=nichts)
    f33.bind("<Button-1>", f33l)
    f33.bind("<Button-3>", f33r)
    f34= Button(hf, height=20, width=20, image=nichts)
    f34.bind("<Button-1>", f34l)
    f34.bind("<Button-3>", f34r)
    f35= Button(hf, height=20, width=20, image=nichts)
    f35.bind("<Button-1>", f35l)
    f35.bind("<Button-3>", f35r)
    f36= Button(hf, height=20, width=20, image=nichts)
    f36.bind("<Button-1>", f36l)
    f36.bind("<Button-3>", f36r)
    f37= Button(hf, height=20, width=20, image=nichts)
    f37.bind("<Button-1>", f37l)
    f37.bind("<Button-3>", f37r)
    f40= Button(hf, height=20, width=20, image=nichts)
    f40.bind("<Button-1>", f40l)
    f40.bind("<Button-3>", f40r)
    f41= Button(hf, height=20, width=20, image=nichts)
    f41.bind("<Button-1>", f41l)
    f41.bind("<Button-3>", f41r)
    f42= Button(hf, height=20, width=20, image=nichts)
    f42.bind("<Button-1>", f42l)
    f42.bind("<Button-3>", f42r)
    f43= Button(hf, height=20, width=20, image=nichts)
    f43.bind("<Button-1>", f43l)
    f43.bind("<Button-3>", f43r)
    f44= Button(hf, height=20, width=20, image=nichts)
    f44.bind("<Button-1>", f44l)
    f44.bind("<Button-3>", f44r)
    f45= Button(hf, height=20, width=20, image=nichts)
    f45.bind("<Button-3>", f45r)
    f45.bind("<Button-1>", f45l)
    f46= Button(hf, height=20, width=20, image=nichts)
    f46.bind("<Button-1>", f46l)
    f46.bind("<Button-3>", f46r)
    f47= Button(hf, height=20, width=20, image=nichts)
    f47.bind("<Button-1>", f47l)
    f47.bind("<Button-3>", f47r)
    f50= Button(hf, height=20, width=20, image=nichts)
    f50.bind("<Button-1>", f50l)
    f50.bind("<Button-3>", f50r)
    f51= Button(hf, height=20, width=20, image=nichts)
    f51.bind("<Button-1>", f51l)
    f51.bind("<Button-3>", f51r)
    f52= Button(hf, height=20, width=20, image=nichts)
    f52.bind("<Button-1>", f52l)
    f52.bind("<Button-3>", f52r)
    f53= Button(hf, height=20, width=20, image=nichts)
    f53.bind("<Button-1>", f53l)
    f53.bind("<Button-3>", f53r)
    f54= Button(hf, height=20, width=20, image=nichts)
    f54.bind("<Button-1>", f54l)
    f54.bind("<Button-3>", f54r)
    f55= Button(hf, height=20, width=20, image=nichts)
    f55.bind("<Button-1>", f55l)
    f55.bind("<Button-3>", f55r)
    f56= Button(hf, height=20, width=20, image=nichts)
    f56.bind("<Button-1>", f56l)
    f56.bind("<Button-3>", f56r)
    f57= Button(hf, height=20, width=20, image=nichts)
    f57.bind("<Button-1>", f57l)
    f57.bind("<Button-3>", f57r)
    f60= Button(hf, height=20, width=20, image=nichts)
    f60.bind("<Button-1>", f60l)
    f60.bind("<Button-3>", f60r)
    f61= Button(hf, height=20, width=20, image=nichts)
    f61.bind("<Button-1>", f61l)
    f61.bind("<Button-3>", f61r)
    f62= Button(hf, height=20, width=20, image=nichts)
    f62.bind("<Button-1>", f62l)
    f62.bind("<Button-3>", f62r)
    f63= Button(hf, height=20, width=20, image=nichts)
    f63.bind("<Button-1>", f63l)
    f63.bind("<Button-3>", f63r)
    f64= Button(hf, height=20, width=20, image=nichts)
    f64.bind("<Button-1>", f64l)
    f64.bind("<Button-3>", f64r)
    f65= Button(hf, height=20, width=20, image=nichts)
    f65.bind("<Button-1>", f65l)
    f65.bind("<Button-3>", f65r)
    f66= Button(hf, height=20, width=20, image=nichts)
    f66.bind("<Button-1>", f66l)
    f66.bind("<Button-3>", f66r)
    f67= Button(hf, height=20, width=20, image=nichts)
    f67.bind("<Button-1>", f67l)
    f67.bind("<Button-3>", f67r)
    f70= Button(hf, height=20, width=20, image=nichts)
    f70.bind("<Button-1>", f70l)
    f70.bind("<Button-3>", f70r)
    f71= Button(hf, height=20, width=20, image=nichts)
    f71.bind("<Button-1>", f71l)
    f71.bind("<Button-3>", f71r)
    f72= Button(hf, height=20, width=20, image=nichts)
    f72.bind("<Button-1>", f72l)
    f72.bind("<Button-3>", f72r)
    f73= Button(hf, height=20, width=20, image=nichts)
    f73.bind("<Button-1>", f73l)
    f73.bind("<Button-3>", f73r)
    f74= Button(hf, height=20, width=20, image=nichts)
    f74.bind("<Button-1>", f74l)
    f74.bind("<Button-3>", f74r)
    f75= Button(hf, height=20, width=20, image=nichts)
    f75.bind("<Button-1>", f75l)
    f75.bind("<Button-3>", f75r)
    f76= Button(hf, height=20, width=20, image=nichts)
    f76.bind("<Button-1>", f76l)
    f76.bind("<Button-3>", f76r)
    f77= Button(hf, height=20, width=20, image=nichts)
    f77.bind("<Button-1>", f77l)
    f77.bind("<Button-3>", f77r)
    normaldesign() # Als Standard wird das normale Design gesetzt
    start(0) # Die Startfunktion wird aufgerufen, um das Spiel zu starten
    smiley.bind("<Button-1>", start)
    hf.mainloop()
