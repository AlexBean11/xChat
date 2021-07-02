import socket
import random
import platform
from threading import Thread
import threading
from datetime import datetime
import os
import sys
from time import sleep
from os import close
from tkinter import Entry, PhotoImage, messagebox
import webbrowser
import pybitz
import tkinter as tk
from tkinter.font import *
import webbrowser
from tkinter import ttk

theme = 'nativ'

pybitz.clear()

#Init:

def stop():
    sys.exit()

try:
    pybitz.rbank(7378)
except:
    pybitz.sbank('False', 7378)

#####################################################################
# Terminal Thread
#####################################################################
def terminal_thread_function():
    print('xChat Terminal Version: v1.0 Protocol: 1')
    print('Enter "stop" or "terminate" to exit the program.')
    while True:
        termcommand = input('xChat> ')
        if termcommand == 'stop':
            print("xChat closed (code:9)")
            os._exit(0)
        elif termcommand == 'terminate':
            print("xChat closed (code:9)")
            os._exit(0)
        elif termcommand == 'killterm':
            print("Terminal thread shutdown (code:5)")
            exit()
        elif termcommand == '':
            pass
        else:
            print("Unkown command!")

def terminal():
    terminalthread = threading.Thread(target=terminal_thread_function)
    terminalthread.daemon = False
    terminalthread.start()

#terminal()

#####################################################################
# Misc Def
#####################################################################

def changetheme(cttheme):
    if cttheme == 'dark':
        theme = 'dark'
    elif cttheme == 'native':
        theme = 'native'

def github():
    webbrowser.open('https://github.com/8bitz0/xChat')

def nextenter():
    nextbutton['background'] = '#424242'

def nextleave():
    nextbutton['background'] = '#353535'

#####################################################################
# Welcome 1
#####################################################################

def welcome():
    def nextenter():
        nextbutton['background'] = '#424242'

    def nextleave():
        nextbutton['background'] = '#353535'
    #pybitz.sbank("(:<", 5495637)
    if theme == 'native':
        welcomewin = tk.Tk()
        welcomewin.geometry('230x70')
        welcomewin.resizable(False, False)
        welcomewin.overrideredirect(True)
        welcomewin.eval('tk::PlaceWindow . center')
        welcomewin.title('Welcome!')
        welcomewin.iconbitmap('assets/window/images/icon.ico')
        #welcomewin.style.theme_use('xpnative')
        welcomewin.focus()
    else:
        welcomewin = tk.Tk()
        welcomewin.geometry('230x70')
        welcomewin.resizable(False, False)
        welcomewin.overrideredirect(True)
        welcomewin.eval('tk::PlaceWindow . center')
        welcomewin.title('Welcome!')
        welcomewin.iconbitmap('assets/window/images/icon.ico')
        welcomewin.configure(bg='#222')
        welcomewin.focus()

    style = ttk.Style(welcomewin)

    if theme == 'native':
        wecometext = ttk.Label(
            welcomewin,
            text="Welcome to xChat!",
        ).place(x=58, y=6)
    else:
        wecometext = tk.Label(
            welcomewin,
            text="Welcome to xChat!",
            fg='white',
            bg='#222'
        ).place(x=58, y=6)

    #backbutton = tk.Button(
    #    welcomewin,
    #    text='Back',
    #    fg='white',
    #    bg='#353535',
    #    borderwidth='0',
    #    width='8',
    #    activeforeground='white',
    #    activebackground='#444',
    #    command=welcomewin.destroy
    #).place(x=40, y=35)

    if theme == 'native':
        nextbutton = ttk.Button(
            welcomewin,
            text='Next >',
            width='8',
            cursor='hand2',
            command=lambda:[welcomewin.destroy(), welcome2()]
        )
    else:
        nextbutton = tk.Button(
            welcomewin,
            text='Next >',
            fg='white',
            bg='#353535',
            borderwidth='0',
            width='8',
            cursor='hand2',
            activeforeground='white',
            activebackground='#4f4f4f',
            command=lambda:[welcomewin.destroy(), welcome2()]
        )

    if theme == 'native':
        pass
    else:
        nextbutton.bind("<Enter>", lambda event:nextenter())
        nextbutton.bind("<Leave>", lambda event:nextleave())

    nextbutton.place(x=160, y=40)

    welcomewin.mainloop()

#####################################################################
# Welcome 2
#####################################################################

def welcome2():
    def nextenter():
        nextbutton['background'] = '#424242'

    def nextleave():
        nextbutton['background'] = '#353535'

    if theme == 'native':
        welcomewin = tk.Tk()
        welcomewin.geometry('280x150')
        welcomewin.resizable(False, False)
        welcomewin.overrideredirect(True)
        welcomewin.eval('tk::PlaceWindow . center')
        welcomewin.title('xChat - Welcome!')
        welcomewin.iconbitmap('assets/window/images/icon.ico')
        welcomewin.focus()
    else:
        welcomewin = tk.Tk()
        welcomewin.geometry('280x150')
        welcomewin.resizable(False, False)
        welcomewin.overrideredirect(True)
        welcomewin.eval('tk::PlaceWindow . center')
        welcomewin.title('xChat - Welcome!')
        welcomewin.iconbitmap('assets/window/images/icon.ico')
        welcomewin.configure(bg='#222')
        welcomewin.focus()

    if theme == 'native':
        wecometext = ttk.Label(
            welcomewin,
            text="What should your username be?"
        ).place(x=55, y=6)
    else:
        wecometext = tk.Label(
            welcomewin,
            text="What should your username be?",
            fg='white',
            bg='#222'
        ).place(x=55, y=6)

    if theme == 'native':
        usernameinput = ttk.Entry(
            welcomewin
        )
    else:
        usernameinput = tk.Entry(
            welcomewin,
            bg='#454545',
            fg='white',
            borderwidth='0'
        )

    if theme == 'native':
        nextbutton = ttk.Button(
            welcomewin,
            text='Next >',
            width='8',
            cursor='hand2',
            command=lambda:[pybitz.sbank(usernameinput.get(), id=3213), welcomewin.destroy(), welcome3()]
        )
    else:
        nextbutton = tk.Button(
            welcomewin,
            text='Next >',
            fg='white',
            bg='#353535',
            borderwidth='0',
            width='8',
            cursor='hand2',
            activeforeground='white',
            activebackground='#444',
            command=lambda:[pybitz.sbank(usernameinput.get(), id=3213), welcomewin.destroy(), welcome3()]
        )

    usernameinput.place(x=81, y=40)

    #def verifyusername():
    #    usernamepre = usernameinput.get()
    #    if usernamepre == '':
    #        usernameverified = False
    #    else:
    #        usernameverified = True
    #        welcome3()
    #    pybitz.sbank(usernameinput.get(), id=3213)
    
    if theme == 'native':
        pass
    else:
        nextbutton.bind("<Enter>", lambda event:nextenter())
        nextbutton.bind("<Leave>", lambda event:nextleave())

    nextbutton.place(x=210, y=120)

    welcomewin.mainloop()

#####################################################################
# Welcome 3
#####################################################################

def welcome3():
    def nextenter():
        nextbutton['background'] = '#424242'

    def nextleave():
        nextbutton['background'] = '#353535'

    def yesenter():
        yesbutton['background'] = '#D00000'

    def yesleave():
        yesbutton['background'] = '#C30000'

    def noenter():
        nobutton['background'] = '#424242'

    def noleave():
        nobutton['background'] = '#353535'

    if theme == 'native':
        welcomewin = tk.Tk()
        welcomewin.geometry('280x150')
        welcomewin.resizable(False, False)
        welcomewin.overrideredirect(True)
        welcomewin.eval('tk::PlaceWindow . center')
        welcomewin.title('xChat - Welcome!')
        welcomewin.iconbitmap('assets/window/images/icon.ico')
        welcomewin.focus()
    else:
        welcomewin = tk.Tk()
        welcomewin.geometry('280x150')
        welcomewin.resizable(False, False)
        welcomewin.overrideredirect(True)
        welcomewin.eval('tk::PlaceWindow . center')
        welcomewin.title('xChat - Welcome!')
        welcomewin.iconbitmap('assets/window/images/icon.ico')
        welcomewin.configure(bg='#222')
        welcomewin.focus()

    if theme == 'native':
        wecometext = ttk.Label(
            welcomewin,
            text="Would you like to show extended info?"
        ).place(x=38, y=6)
    else:
        wecometext = tk.Label(
            welcomewin,
            text="Would you like to show extended info?",
            fg='white',
            bg='#222'
        ).place(x=38, y=6)

    if theme == 'native':
        yesbutton = ttk.Button(
            welcomewin,
            text='Yes',
            width='8',
            cursor='hand2',
            command=lambda:[pybitz.sbank('True', 8577), welcomewin.destroy(), welcome4()]
        )
    else:
        yesbutton = tk.Button(
            welcomewin,
            text='Yes',
            fg='white',
            bg='#C30000',
            borderwidth='0',
            width='8',
            cursor='hand2',
            activeforeground='white',
            activebackground='#E00000',
            command=lambda:[pybitz.sbank('True', 8577), welcomewin.destroy(), welcome4()]
        )

    if theme == 'native':
        pass
    else:
        yesbutton.bind("<Enter>", lambda event:yesenter())
        yesbutton.bind("<Leave>", lambda event:yesleave())

    yesbutton.place(x=82, y=45)

    if theme == 'native':
        nobutton = ttk.Button(
            welcomewin,
            text='No',
            width='8',
            cursor='hand2',
            command=lambda:[pybitz.sbank('False', 8577), welcomewin.destroy(), welcome4()]
        )
    else:
        nobutton = tk.Button(
            welcomewin,
            text='No',
            fg='white',
            bg='#353535',
            borderwidth='0',
            width='8',
            cursor='hand2',
            activeforeground='white',
            activebackground='#444',
            command=lambda:[pybitz.sbank('False', 8577), welcome4()]
        )

    if theme == 'native':
        pass
    else:
        nobutton.bind("<Enter>", lambda event:noenter())
        nobutton.bind("<Leave>", lambda event:noleave())

    if theme == 'native':
        jsyntext = ttk.Label(
            welcomewin,
            text="Only enable this if you\n know what you are doing!"
        ).place(x=72, y=73)
    else:
        jsyntext = tk.Label(
            welcomewin,
            text="Only enable this if you\n know what you are doing!",
            fg='white',
            bg='#222'
        ).place(x=72, y=73)

    nobutton.place(x=152, y=45)

    welcomewin.mainloop()

#####################################################################
# Welcome 4
#####################################################################

def welcome4():
    def nextenter():
        nextbutton['background'] = '#424242'

    def nextleave():
        nextbutton['background'] = '#353535'

    if theme == 'native':
        welcomewin = tk.Tk()
        welcomewin.geometry('280x150')
        welcomewin.resizable(False, False)
        welcomewin.overrideredirect(True)
        welcomewin.eval('tk::PlaceWindow . center')
        welcomewin.title('xChat - Welcome!')
        welcomewin.iconbitmap('assets/window/images/icon.ico')
        welcomewin.focus()
    else:
        welcomewin = tk.Tk()
        welcomewin.geometry('280x150')
        welcomewin.resizable(False, False)
        welcomewin.overrideredirect(True)
        welcomewin.eval('tk::PlaceWindow . center')
        welcomewin.title('xChat - Welcome!')
        welcomewin.iconbitmap('assets/window/images/icon.ico')
        welcomewin.configure(bg='#222')
        welcomewin.focus()

    if theme == 'native':
        wecometext = ttk.Label(
            welcomewin,
            text="Setup is complete!"
        ).place(x=38, y=6)
    else:
        wecometext = tk.Label(
            welcomewin,
            text="Setup is complete!",
            fg='white',
            bg='#222'
        ).place(x=38, y=6)
        
    if theme == 'native':
        nextbutton = ttk.Button(
            welcomewin,
            text='Finish',
            width='8',
            cursor='hand2',
            command=lambda:[welcomewin.destroy()]
        )
    else:
        nextbutton = tk.Button(
            welcomewin,
            text='Finish',
            fg='white',
            bg='#353535',
            borderwidth='0',
            width='8',
            cursor='hand2',
            activeforeground='white',
            activebackground='#444',
            command=lambda:[welcomewin.destroy()]
        )
    
    if theme == 'native':
        pass
    else:
        nextbutton.bind("<Enter>", lambda event:nextenter())
        nextbutton.bind("<Leave>", lambda event:nextleave())

    nextbutton.place(x=210, y=120)

    welcomewin.mainloop()

try:
    pybitz.rbank(5913)
except:
    pybitz.sbank('', 5913)
    welcome()

try:
    pybitz.rbank(3213)
except:
    welcome()

try:
    pybitz.rbank(8577)
except:
    welcome()

#####################################################################
# Settings
#####################################################################

def settings():
    

    mainwin.iconify()

    def backenter():
        backbutton['background'] = '#424242'

    def backleave():
        backbutton['background'] = '#353535'

    if theme == 'native':
        settingswin = tk.Tk()
        settingswin.bind('<Escape>',lambda:os._exit(0))
        settingswin.resizable(False, False)
        settingswin.geometry('500x300')
        settingswin.eval('tk::PlaceWindow . center')
        settingswin.title('xChat - Settings')
        settingswin.iconbitmap('assets/window/images/icon.ico')
    else:
        settingswin = tk.Tk()
        settingswin.configure(bg='#222')
        settingswin.bind('<Escape>',lambda:os._exit(0))
        settingswin.resizable(False, False)
        settingswin.geometry('500x300')
        settingswin.eval('tk::PlaceWindow . center')
        settingswin.title('xChat - Settings')
        settingswin.iconbitmap('assets/window/images/icon.ico')

    titleStyle = Font(family="Lucida Grande", size=20)

    if theme == 'native':
        titletext = tk.Label(
            settingswin,
            text="Settings:",
            font=titleStyle
        ).place(x=15, y=15)
    else:
        titletext = tk.Label(
            settingswin,
            text="Settings:",
            fg='white',
            bg='#222',
            font=titleStyle
        ).place(x=15, y=15)

    if theme == 'native':
        versiontext = tk.Label(
        settingswin,
        text="v1.0",
    ).place(x=5, y=276)
    else:
        versiontext = tk.Label(
            settingswin,
            text="v1.0",
            fg='white',
            bg='#222'
        ).place(x=5, y=276)

    if theme == 'native':
        githubbutton = ttk.Button(
            settingswin,
            text='Github',
            width='6',
            cursor='hand2',
            command=github
        )

    else:
        githubbutton = tk.Button(
            settingswin,
            text='Github',
            fg='white',
            bg='#353535',
            borderwidth='0',
            width='6',
            cursor='hand2',
            activeforeground='white',
            activebackground='#444',
            command=github
        )

    #closeimage = PhotoImage(
    #    file='assets/button/images/close.png'
    #)

    if theme == 'native':
        backbutton = ttk.Button(
            settingswin,
            text='< Back',
            width='6',
            cursor='hand2',
            command=lambda:[settingswin.destroy(), mainwin.deiconify()]
        )
    else:
        backbutton = tk.Button(
            settingswin,
            text='< Back',
            fg='white',
            bg='#353535',
            borderwidth='0',
            width='6',
            cursor='hand2',
            activeforeground='white',
            activebackground='#444',
            command=lambda:[settingswin.destroy(), mainwin.deiconify()]
        )

    if theme == 'native':
            pass
    else:
        backbutton.bind("<Enter>", lambda event:backenter())
        backbutton.bind("<Leave>", lambda event:backleave())
        
        backbutton.place(x=448, y=273)

    mainwin.mainloop()
    
#####################################################################
# Main
#####################################################################

def gitenter():
    githubbutton['background'] = '#424242'

def gitleave():
    githubbutton['background'] = '#353535'
    
def closeenter():
    closebutton['background'] = '#424242'

def closeleave():
    closebutton['background'] = '#353535'
    
def settingsenter():
    settingsbutton['background'] = '#424242'

def settingsleave():
    settingsbutton['background'] = '#353535'
    
def connectenter():
    connectbutton['background'] = '#424242'

def connectleave():
    connectbutton['background'] = '#353535'
    
def hostenter():
    hostbutton['background'] = '#424242'

def hostleave():
    hostbutton['background'] = '#353535'

if theme == 'native':
    mainwin = tk.Tk()
    mainwin.bind('<Escape>',lambda:os._exit(0))
    mainwin.bind('<Insert>',lambda event:terminal())
    mainwin.resizable(False, False)
    mainwin.geometry('500x300')
    mainwin.eval('tk::PlaceWindow . center')
    mainwin.title('xChat')
    mainwin.iconbitmap('assets/window/images/icon.ico')
else:
    mainwin = tk.Tk()
    mainwin.configure(bg='#222')
    mainwin.bind('<Escape>',lambda:os._exit(0))
    mainwin.bind('<Insert>',lambda event:terminal())
    mainwin.resizable(False, False)
    mainwin.geometry('500x300')
    mainwin.eval('tk::PlaceWindow . center')
    mainwin.title('xChat')
    mainwin.iconbitmap('assets/window/images/icon.ico')

titleStyle = Font(family="Lucida Grande", size=20)

if theme == 'native':
    titletext = tk.Label(
        mainwin,
        text="Hello, " + pybitz.rbank(3213) + "!",
        font=titleStyle
    ).place(x=15, y=15)
else:
    titletext = tk.Label(
        mainwin,
        text="Hello, " + pybitz.rbank(3213) + "!",
        fg='white',
        bg='#222',
        font=titleStyle
    ).place(x=15, y=15)

if theme == 'native':
    iptext = tk.Label(
        mainwin,
        text="IP:",
    ).place(x=15, y=87)
else:
    iptext = tk.Label(
        mainwin,
        text="IP:",
        fg='white',
        bg='#222',
    ).place(x=15, y=87)

if theme == 'native':
    ipinput = ttk.Entry(
        mainwin,
        width='20'
    )
else:
    ipinput = tk.Entry(
        mainwin,
        bg='#454545',
        fg='white',
        borderwidth='0',
        width='20'
    )
    
if theme == 'native':
    porttext = tk.Label(
        mainwin,
        text="Port:",
    ).place(x=15, y=112)
else:
    porttext = tk.Label(
        mainwin,
        text="Port:",
        fg='white',
        bg='#222',
    ).place(x=15, y=112)

if theme == 'native':
    portinput = ttk.Entry(
        mainwin,
        width='5'
    )
else:
    portinput = tk.Entry(
        mainwin,
        bg='#454545',
        fg='white',
        borderwidth='0',
        width='5'
    )

if theme == 'native':
    connectbutton = ttk.Button(
        mainwin,
        text='Connect',
        width='8',
        cursor='hand2',
        command=lambda:[connect()]
    )
else:
    connectbutton = tk.Button(
        mainwin,
        text='Connect',
        fg='white',
        bg='#353535',
        borderwidth='0',
        width='7',
        cursor='hand2',
        activeforeground='white',
        activebackground='#444',
        command=lambda:[connect()]
    )
    
if theme == 'native':
        pass
else:
    connectbutton.bind("<Enter>", lambda event:connectenter())
    connectbutton.bind("<Leave>", lambda event:connectleave())
    
#if theme == 'native':
#    ortext = tk.Label(
#        mainwin,
#        text="or",
#    ).place(x=76, y=145)
#else:
#    ortext = tk.Label(
#        mainwin,
#        text="or",
#        fg='white',
#        bg='#222',
#    ).place(x=76, y=145)
    
if theme == 'native':
    hostbutton = ttk.Button(
        mainwin,
        text='Host',
        width='7',
        cursor='hand2',
        command=lambda:[mainwin.iconify(), host()]
    )
else:
    hostbutton = tk.Button(
        mainwin,
        text='Host',
        fg='white',
        bg='#353535',
        borderwidth='0',
        width='7',
        cursor='hand2',
        activeforeground='white',
        activebackground='#444',
        command=lambda:[mainwin.iconify(), host()]
    )
    
if theme == 'native':
        pass
else:
    hostbutton.bind("<Enter>", lambda event:hostenter())
    hostbutton.bind("<Leave>", lambda event:hostleave())

#####################################################################
# Host
#####################################################################

def host():
    def backenter():
        backbutton['background'] = '#424242'

    def backleave():
        backbutton['background'] = '#353535'
        
    def hostserverenter():
        hostserverbutton['background'] = '#424242'

    def hostserverleave():
        hostserverbutton['background'] = '#353535'

    if theme == 'native':
        hostwin = tk.Tk()
        hostwin.bind('<Escape>',lambda:os._exit(0))
        hostwin.bind('<Insert>',lambda event:terminal())
        hostwin.resizable(False, False)
        hostwin.geometry('500x300')
        hostwin.eval('tk::PlaceWindow . center')
        hostwin.title('xChat - Host')
        hostwin.iconbitmap('assets/window/images/icon.ico')
    else:
        hostwin = tk.Tk()
        hostwin.configure(bg='#222')
        hostwin.bind('<Escape>',lambda:os._exit(0))
        hostwin.bind('<Insert>',lambda event:terminal())
        hostwin.resizable(False, False)
        hostwin.geometry('500x300')
        hostwin.eval('tk::PlaceWindow . center')
        hostwin.title('xChat - Host')
        hostwin.iconbitmap('assets/window/images/icon.ico')

    titleStyle = Font(hostwin, family="Lucida Grande", size=18)
    subStyle = Font(hostwin, family="Lucida Grande", size=12)

    if theme == 'native':
        hosttext = tk.Label(
            hostwin,
            text="Host:",
            font=titleStyle
        ).place(x=15, y=15)
    else:
        hosttext = tk.Label(
            hostwin,
            text="Host:",
            fg='white',
            bg='#222',
            font=titleStyle
        ).place(x=15, y=15)
      
    if theme == 'native':
        hostserverbutton = tk.Button(
            hostwin,
            text="Server",
            width='8',
            font=subStyle
        )
    else:
        hostserverbutton = tk.Button(
            hostwin,
            text="Server",
            fg='white',
            bg='#353535',
            width='8',
            borderwidth='0',
            cursor='hand2',
            activeforeground='white',
            activebackground='#444',
            font=subStyle
        )
        
    if theme == 'native':
        pass
    else:
        hostserverbutton.bind("<Enter>", lambda event:hostserverenter())
        hostserverbutton.bind("<Leave>", lambda event:hostserverleave())
        
    hostserverbutton.place(x=15, y=65)
        
    if theme == 'native':
        servertext = tk.Label(
            hostwin,
            text="A blank standard server."
        ).place(x=100, y=68)
    else:
        servertext = tk.Label(
            hostwin,
            text="A blank standard server.",
            fg='white',
            bg='#222'
        ).place(x=100, y=68)
        
    if theme == 'native':
        backbutton = ttk.Button(
            hostwin,
            text='< Back',
            width='6',
            cursor='hand2',
            command=lambda:[hostwin.destroy(), mainwin.deiconify()]
        )
    else:
        backbutton = tk.Button(
            hostwin,
            text='< Back',
            fg='white',
            bg='#353535',
            borderwidth='0',
            width='6',
            cursor='hand2',
            activeforeground='white',
            activebackground='#444',
            command=lambda:[hostwin.destroy(), mainwin.deiconify()]
        )
        
    if theme == 'native':
        pass
    else:
        backbutton.bind("<Enter>", lambda event:backenter())
        backbutton.bind("<Leave>", lambda event:backleave())
    
    backbutton.place(x=448, y=273)

#####################################################################
# Client
#####################################################################

def connect():
    mainwin.iconify()
    quit = False
    
    def sayerror():
        print("An error has occurred! xChat cannot continue!")
    
    pybitz.clear()
    
    print("        _____ _           _   ")
    print("       / ____| |         | |  ")
    print(" __  _| |    | |__   __ _| |_ ")
    print(" \ \/ / |    | '_ \ / _` | __|")
    print("  >  <| |____| | | | (_| | |_ ")
    print(" /_/\_\\\_____|_| |_|\__,_|\__|\n")
    
    ip = ipinput.get()
    port = portinput.get()
    
    SERVER_HOST = ip
    try:
        SERVER_PORT = 0
        SERVER_PORT = int(port)
    except:
        sayerror()
        
    separator_token = "<SEP>"
    
    s = socket.socket()
    connected = False
    print("[*] Connecting to "+SERVER_HOST+":"+str(SERVER_PORT)+"...")
    try:
        s.connect((SERVER_HOST, SERVER_PORT))
    except Exception as e:
        print("\nUnable to connect to "+SERVER_HOST+":"+str(SERVER_PORT)+"! " + str(e))
        #input("Press enter to continue...")
        mainwin.deiconify()
        quit = True
    
    if quit == False:
        print("[+] Connected.")
        connected = True
        to_send = pybitz.rbank(3213) + " has connected!"
        try:
            to_send = to_send
            s.send(to_send.encode())
        except:
            print("Disconnected!")
        name = pybitz.rbank(3213)
        
        def listen_for_messages():
            while True:
                try:
                    message = s.recv(1024).decode()
                    print("\n" + message)
                except:
                    print("Disconnected!")
                    #mustquit = True
                    break
                
        t = Thread(target=listen_for_messages)
        t.daemon = True
        t.start()
        
        to_send = name +" has joined!"
        to_send = to_send
        
        
        pybitz.clear()
        print("        _____ _           _   ")
        print("       / ____| |         | |  ")
        print(" __  _| |    | |__   __ _| |_ ")
        print(" \ \/ / |    | '_ \ / _` | __|")
        print("  >  <| |____| | | | (_| | |_ ")
        print(" /_/\_\\\_____|_| |_|\__,_|\__|\n")
        print("Welcome " + name + "!")
    
    while True:
        cannotsend = False
        if quit == True:
            break
        to_send = input("\r")
        if to_send.lower() == 'exit':
            break
            mainwin.deiconify()
        if to_send.lower() == 'clear':
            pybitz.clear()
            print("        _____ _           _   ")
            print("       / ____| |         | |  ")
            print(" __  _| |    | |__   __ _| |_ ")
            print(" \ \/ / |    | '_ \ / _` | __|")
            print("  >  <| |____| | | | (_| | |_ ")
            print(" /_/\_\\\_____|_| |_|\__,_|\__|\n")
            cannotsend = True
        if to_send.lower() == '':
            cannotsend = True
        #if to_send.lower() == 'reconnect':
        #    cannotsend = True
        #    s.close()
        #    s = socket.socket()
        #    s.connect((SERVER_HOST, SERVER_PORT))
        try:
            date_now = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
            to_send = name + separator_token + to_send
            if cannotsend == False:
                s.send(to_send.encode())
        except:
            print("Disconnected!")
            break
        
    s.close()
    mainwin.deiconify()

ipinput.place(x=52, y=90)
portinput.place(x=52, y=115)
connectbutton.place(x=15, y=145)
hostbutton.place(x=440, y=5)

if theme == 'native':
    versiontext = tk.Label(
    mainwin,
    text="v1.0",
).place(x=5, y=276)
else:
    versiontext = tk.Label(
        mainwin,
        text="v1.0",
        fg='white',
        bg='#222'
    ).place(x=5, y=276)

if theme == 'native':
    githubbutton = ttk.Button(
        mainwin,
        text='Github',
        width='6',
        cursor='hand2',
        command=github
    )

else:
    githubbutton = tk.Button(
        mainwin,
        text='Github',
        fg='white',
        bg='#353535',
        borderwidth='0',
        width='6',
        cursor='hand2',
        activeforeground='white',
        activebackground='#444',
        command=github
    )

if theme == 'native':
        pass
else:
    githubbutton.bind("<Enter>", lambda event:gitenter())
    githubbutton.bind("<Leave>", lambda event:gitleave())

githubbutton.place(x=395, y=273)

if theme == 'native':
    settingsbutton = ttk.Button(
        mainwin,
        text='Settings',
        width='7',
        cursor='hand2',
        command=settings
    )
else:
    settingsbutton = tk.Button(
        mainwin,
        text='Settings',
        fg='white',
        bg='#353535',
        borderwidth='0',
        width='7',
        cursor='hand2',
        activeforeground='white',
        activebackground='#444',
        command=settings
    )

if theme == 'native':
        pass
else:
    settingsbutton.bind("<Enter>", lambda event:settingsenter())
    settingsbutton.bind("<Leave>", lambda event:settingsleave())
    
settingsbutton.place(x=335, y=273)

#closeimage = PhotoImage(
#    file='assets/button/images/close.png'
#)

if theme == 'native':
    closebutton = ttk.Button(
        mainwin,
        text='Quit',
        width='6',
        cursor='hand2',
        command=lambda:os._exit(0)
    )
else:
    closebutton = tk.Button(
        mainwin,
        text='Quit',
        fg='white',
        bg='#353535',
        borderwidth='0',
        width='6',
        cursor='hand2',
        activeforeground='white',
        activebackground='#444',
        command=lambda:os._exit(0)
    )

if theme == 'native':
        pass
else:
    closebutton.bind("<Enter>", lambda event:closeenter())
    closebutton.bind("<Leave>", lambda event:closeleave())

closebutton.place(x=448, y=273)

mainwin.mainloop()