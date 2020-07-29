import os
import tkinter
from tkinter.filedialog import askdirectory

import pygame

window = tkinter.Tk()
window.geometry("350x160")

pygame.mixer.init()

listofsongs = []
index = 0

v = tkinter.StringVar()
songlabel = tkinter.Label(window, textvariable=v, width=35)


def start_stop():
    global index
    index = index + 1

    if index == 1:
        index += 1
        pygame.mixer.music.load(listofsongs[index])
        pygame.mixer.music.play(0)
        print("music started ")

    elif (index % 2) == 0:
        pygame.mixer.music.pause()
        print("paused ")

    elif (index % 2) != 0:
        pygame.mixer.music.unpause()
        pygame.mixer.music.play()
        print('unPaused')


def nextsong():
    global index
    index += 1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    # updatelabel()
    print('Next Song')


def prevsong():
    global index
    index -= 1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    # updatelabel()
    print('Previous Song')


def stopsong():
   pygame.mixer.music.stop()
   v.set("")
   print('Stop Song')


def updatelabel():
    global index
    v.set(listofsongs[index])


def directorychooser():
    """

    """
    directory = askdirectory()
    os.chdir(directory)

    for files in os.listdir(directory):
        if files.endswith(".mp3"):
            listofsongs.append(files)

    pygame.mixer.init()
    pygame.mixer.music.load(listofsongs[0])
    # pygame.mixer.music.play()


directorychooser()

l1 = tkinter.Label(window, text="MUSIC PLAYER", font="times 13")
l1.grid(row=1, column=2)

b2 = tkinter.Button(window, text='◄◄', width=14, command=prevsong)
b2.grid(row=14, column=1)

b3 = tkinter.Button(window, text='►/║║', width=12, command=start_stop)
b3.grid(row=14, column=2)

# b4 = tkinter.Button(window, text='■', width=7, command=stopsong)
# b4.grid(row=14, column=3)

b4 = tkinter.Button(window, text='►►', width=14, command=nextsong)
b4.grid(row=14, column=3)

songs_list = os.listdir()
songs_listbox = tkinter.StringVar(window)
songs_listbox.set("songs")
menu = tkinter.OptionMenu(window, songs_listbox, *songs_list)
menu.grid(row=16, column=1)

window.mainloop()
