from fileinput import filename
from http import client
from time import time
from tkinter import *
from tkinter import filedialog
from MessageHelper import MessageHelper
from TypeFile import Extension
from miniaturePic import MiniaturePic
from client import Client
import os
import sys

nickname = input("Escolha um nome de usuário: ")


class GUI:
    def __init__(self, width, height):
        self.window = Tk()
        self.window.title(f"Chat P2P de {nickname}")

        # Bind the Enter Key to Call an event
        self.window.bind('<Return>', self.send)

        self.canva = Canvas(self.window, width=width, height=height)
        self.canva.grid(columnspan=4)

        self.createAssets()

        self.client = Client(self, nickname)
        self.client.connect()

        self.video_counter = 0
        self.audio_counter = 0

    def createAssets(self):
        self.text_area = Text(self.canva, border=1, bg="#fadce6")
        self.image = MiniaturePic(self.text_area)

        self.text_field = Entry(self.canva, width=80, border=1, bg='white')

        self.add_file = Button(
            self.canva, text='Enviar Arquivo', padx=30, command=self.put_file)
        self.send_button = Button(
            self.canva, text='Enviar mensagem', padx=30, command=self.send)
        self.video_button = Button(
            self.canva, text='Play Video', padx=30, command=self.play_video)
        self.audio_button = Button(
            self.canva, text='Play Audio', padx=30, command=self.play_audio)
        self.clear_button = Button(
            self.canva, text='Limpar', padx=30, command=self.clear_all)

        self.list_audio = Listbox(selectmode=SINGLE, width=20)
        self.list_video = Listbox(selectmode=SINGLE, width=20)
        
        self.list_audio_count = 0
        self.list_video_count = 0

        
        self.list_video.grid(column=2, row=0, columnspan=2)
        self.list_audio.grid(column=3, row=0, columnspan=2)
        self.send_button.grid(column=2, row=2)
        self.clear_button.grid(column=3, row=2)
        self.add_file.grid(column=4, row=2)
        self.video_button.grid(column=5, row=2)
        self.audio_button.grid(column=6, row=2)
        self.text_area.grid(column=0, row=0)
        self.text_field.grid(column=0, row=2)

    def start(self):
        self.window.mainloop()

    def print_on_screen(self, message):
        self.text_area.insert(END, f'{message}\n')
        self.text_field.delete(0, END)

    def send(self, event=None):
        message = self.text_field.get()

        should_send = MessageHelper.is_valid_to_send(message)

        if should_send:
            messageToSend = MessageHelper.create_message(
                message, nickname)

            self.print_on_screen(messageToSend)
            self.client.send(message)
        else:
            self.print_on_screen(MessageHelper.INVALID_MESSAGE)

    def show_received(self, message, nickname):
        self.print_on_screen(MessageHelper.create_message(message, nickname))

    def send_file(self, name_of_file):
        changed_name = name_of_file.split('/')[-1]
        init = f"{changed_name}:file"

        self.client.send(init)
        file = open(name_of_file, 'rb')
        bool_ = True
        while bool_:
            bool_ = file.read(1024)
            self.client.send(bool_)
        file.close()

    def put_file(self):
        name_of_file = filedialog.askopenfilename()
        exten = Extension().which_ext(name_of_file)

        # add image pic 

        if exten == 2:
            self.list_audio.insert(self.list_audio_count, name_of_file)
            self.list_audio_count += 1

        if exten == 3:
            self.list_video.insert(self.list_video_count, name_of_file)
            self.list_video_count += 1

        self.send_file(name_of_file)

    def show_file(self, name_of_file):
        type_of_exten = Extension().which_ext(name_of_file)
        self.image.add_image(type_of_exten, name_of_file)

        if type_of_exten == 2:
            self.list_audio.insert(self.list_audio_count, name_of_file)
            self.list_audio_count += 1

        if type_of_exten == 3:
            self.list_video.insert(self.list_video_count, name_of_file)
            self.list_video_count += 1

    def to_play_stuff(self, name_of_file):
        os = sys.platform
        if os in ['linux', 'linux2']:
            name_of_file = name_of_file.replace(" ", "\ ")
            return f'xdg-open {name_of_file}'
        elif os in ['win32', 'win64']:
            return f'"{name_of_file}"'
        else:
            return f'open {name_of_file}'

    def clear_all(self):
        self.text_area.delete('1.0', END)

    def play_video(self):
        pass

    def play_audio(self):
        pass

if __name__ == '__main__':
    interface = GUI(800, 600).start()
