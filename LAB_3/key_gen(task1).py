import tkinter as tk
from tkinter import messagebox
import random
import pygame
from PIL import Image
from tkinter.ttk import Progressbar
import time


KEY = '-------------------'
WINDOW_NAME = 'Hello Kitty Game Key Generator'
WINDOW_SIZE = '1024x768'
PHOTO_PATH = 'hellokitty_game.png'
FONT_PARAMETERS = ('Verdana', 24)
MUSIC_FILE = 'Soundtrack_HK.mp3'
GEN_BTN = 'Generate Key'
CANCEL_BTN = 'x'
FIELD_NAME = 'Your private key'
BTN_BG_COLOR = 'pink'
BTN_TEXT_COLOR = 'purple'
ALPHABET = 'QWERTYUIOPASDFGHJKLZXCVBNM'


def close():
    window.destroy()
    pygame.mixer.music.stop()


def key_gen():
    global KEY
    create_progressbar()
    KEY = ''
    for i in range(4):
        sub_key = ''
        count = 0
        category = random.randint(1, 2)
        while len(sub_key) != 4:
            if category == 1:
                sub_key += str(random.randint(0, 9))
                if count > 0: category = 1
                else: category = random.randint(1, 2)
            if category == 2:
                sub_key += random.choice(ALPHABET)
                count +=1
                category = 1
        if i > 2:
            KEY += sub_key
        else:
            KEY += sub_key + '-'
    key_lbl.configure(text=f'{FIELD_NAME}: {KEY}')
    return KEY


def create_progressbar():
    prog_bar=Progressbar(window,orient='horizontal',length=440,mode='determinate')
    prog_bar.place(x=290,y=700)
    for row in range(100):
        prog_bar['value']=row
        window.update_idletasks()
        time.sleep(0.01)
    prog_bar.destroy()


if __name__ == '__main__':
    window = tk.Tk()
    window.title(WINDOW_NAME)
    window.geometry(WINDOW_SIZE)
    bg_img = tk.PhotoImage(file=PHOTO_PATH)


    lbl_bg = tk.Label(window, image=bg_img)
    lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

    btn_gen = tk.Button(
                    window, 
                    text=GEN_BTN,
                    width=20,
                    command=key_gen,
                    bg=BTN_BG_COLOR, 
                    fg=BTN_TEXT_COLOR, 
                    font=FONT_PARAMETERS, bd=15
                    )
    btn_gen.place(relx=0.5, rely=0.85, anchor='center')

    btn_cl = tk.Button(
        window, 
        text=CANCEL_BTN, 
        width=2, 
        height=1, 
        command=close, 
        bg=BTN_BG_COLOR, 
        fg=BTN_TEXT_COLOR, 
        font=FONT_PARAMETERS, 
        bd=15
        )
    btn_cl.place(relx=0.75, rely=0.85, anchor='center')

    key_lbl = tk.Label(
        window, 
        text=f'{FIELD_NAME}: {KEY}', 
        font=FONT_PARAMETERS, 
        bg=BTN_BG_COLOR, 
        fg=BTN_TEXT_COLOR, 
        borderwidth= 10, 
        relief=tk.RAISED,
        )
    key_lbl.place(relx=0.5, rely=0.73, anchor='center')
    pygame.mixer.init()
    pygame.mixer.music.load(MUSIC_FILE)
    pygame.mixer.music.play() 
    window.mainloop()



