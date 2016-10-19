
import webbrowser
from tkinter import *
import tkinter as tk
from tkinter import ttk
import os
import subprocess
import sys
from win32api import GetSystemMetrics
import socket
import clientmodule
LARGE_FONT=("verdana",12)
NORM_FONT=("verdana",10)

#socketin asetukset

s = socket.socket()             # luodaan socket objekti
port = 60000                    # portin varaus

#Asetusten luonti
i=open("asetukset.txt","a")
i.close()
lehti = open("asetukset.txt","r").read()

#näytön resoluutio
WxH=str(GetSystemMetrics(0)) + "x" + str(GetSystemMetrics(1))
leveys=GetSystemMetrics(0)
korkeus=GetSystemMetrics(1)

#Asetus ikkuna

def poistu():
    quit

def asetukset():
    asetus = tk.Tk()
    asetus.wm_title("Asetukset")
    
    label = ttk.Label(asetus,text="Asetukset", font=LARGE_FONT)
    label.pack(side="top",fill="x",pady=10)
    info = ttk.Label(asetus, text="Anna käyttämäsi lehden kotisivu", font=NORM_FONT)
    info.pack()
    
    ent = Entry(asetus)
    ent.pack()

    buttok = ttk.Button(asetus , text="OK",command = lambda: tallenna())
    buttok.pack()

    def tallenna():
                teksti=ent.get()
                file = open("asetukset.txt","w")
                file.write(teksti)
                file.close()
                asetus.destroy()
    asetus.mainloop()

class EoAapp (tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.wm_title(self, "EoAapp")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=2,minsize=100)
        container.grid_columnconfigure(0, weight=2,minsize=100)
        

        #menu
        menubar=tk.Menu(container)
        filemenu=tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Asetukset", command = lambda: asetukset())
        filemenu.add_command(label="Exit",command=lambda: poistu())
        menubar.add_cascade(label="File", menu=filemenu)

        tk.Tk.config(self,menu=menubar)

        
        
        #ikkunan lataaminen
        self.frames = {}


        frame = StartPage(container, self)

        self.frames[StartPage] = frame

        frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self,cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):


    #nappulat ja otsikot
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        tk.Frame.configure(self,background='#7C8082')
        
        label = tk.Label(self, text="EoAapp", font=LARGE_FONT)
        label.configure(background='#7C8082')
        label.grid(row=1,column=0)

        tyhja = tk.Label(self, text="       ", font=LARGE_FONT)
        tyhja.configure(background='#7C8082')
        tyhja.grid(row=1,column=1)

        label2 = tk.Label(self, text="Puh. 050 55512343")
        label2.configure(background='#7C8082')
        label2.grid(row=1,column=2)

        butLasi = tk.Button(self, text="Suurennuslasi")
        butLasi.config(bg='#837E7C')
        butLasi["command"]=self.lasi
        butLasi.place(x=120,y=int(korkeus*0.95-110),height=100,width=100)

        butLehti = tk.Button(self, text="lehti")
        butLehti.config(bg='#837E7C')
        butLehti["command"]=self.lehti
        butLehti.place(x=10,y=int(korkeus*0.95-110),height=100,width=100)

        butSaa = tk.Button(self, text="Sää")
        butSaa.config(bg='#837E7C')
        butSaa["command"]=self.saa
        butSaa.place(x=230,y=int(korkeus*0.95-110),height=100,width=100)

        butRemote = tk.Button(self, text="TARVITSETKO APUA?")
        butRemote.config(bg='#837E7C')
        butRemote["command"] = self.kysely
        butRemote.place(x=10,y=int(korkeus/3),height=100,width=int(leveys/2-20))

    #nappuloiden funktiot
    def lasi(self):
            
            os.startfile("C:\Windows\System32\magnify.exe")


    def lehti(self):
            lehti = open("asetukset.txt","r").read()
            webbrowser.open(lehti)

    def saa (self):
            webbrowser.open("http://ilmatieteenlaitos.fi/saa")

    #etakaytton vahvistus ikkuna
    def kysely(StartPage):
        ikkuna = tk.Tk()

        ikkuna.wm_title("Tarvitsetko apua?")
        
        label = ttk.Label(ikkuna,text="Tarvitsetko apua?",font=LARGE_FONT)
        label.grid(row=0,column=0)
        
        label2 = ttk.Label(ikkuna,text="Puh. 050 55512343",font=LARGE_FONT)
        label2.grid(row=1,column=0)
        
        label3 = ttk.Label(ikkuna,text="Kuvaile lyhyesti ongelmaa.",font=NORM_FONT)
        #label3.grid(row=2,column=0)
        label3.place(x=10,y=int(korkeus/11))

        ent = Entry(ikkuna)
        ent.place(x=10,y=int(korkeus/8),height=100,width=int(leveys/4-20))

        butLaheta= ttk.Button(ikkuna,text="Lähetä",command=lambda: ok())
        butLaheta.place(x=10,y=int(korkeus/4),height=80,width=int(leveys/4-20))
      
        def ok():
                teksti=ent.get()
                file = open("vika.txt","w")
                file.write(teksti)
                file.close()
                ikkuna.destroy()
                clientmodule.laheta()
                    
                
            
            #geometriat    
        ikkuna.geometry("720x1060")
        ikkuna.maxsize(width=int(leveys/4), height=int(korkeus/3))
        ikkuna.minsize(width=int(leveys/4), height=int(korkeus/3))
        ikkuna.mainloop()





#ikkunan koko ja lukitus
app = EoAapp()
app.geometry("720x1060")
app.maxsize(width=int(leveys/2), height=int(korkeus*0.95))
app.minsize(width=int(leveys/2), height=int(korkeus*0.95))
app.mainloop()

