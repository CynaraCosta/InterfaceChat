from http import client
from time import time
from tkinter import *
from tkinter import filedialog
from MessageHelper import MessageHelper
from client import Client

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

        self.client = Client(self)
        self.client.connect()

        self.video_counter = 0
        self.audio_counter = 0

    def createAssets(self):
        self.text_area = Text(self.canva, border=1, bg="#abd3eb")

        self.text_field = Entry(self.canva, width=80, border=1, bg='white')

        self.send_button = Button(
            self.canva, text='Send', padx=30, command=self.send)
        self.video_button = Button(
            self.canva, text='Play Video', padx=30, command=self.play_video)
        self.audio_button = Button(
            self.canva, text='Play Audio', padx=30, command=self.play_audio)
        self.clear_button = Button(
            self.canva, text='Clear', padx=30, command=self.clear_all)

        self.list_audio = Listbox(selectmode=SINGLE, width=20)
        self.list_video = Listbox(selectmode=SINGLE, width=20)

        self.list_video.grid(column=2, row=0, columnspan=2)
        self.list_audio.grid(column=3, row=0, columnspan=2)
        self.send_button.grid(column=2, row=2)
        self.clear_button.grid(column=3, row=2)
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

    def show_received(self, message):
        self.print_on_screen(MessageHelper.create_message(message, 'Fulano'))

    def clear_all(self):
        self.text_area.delete('1.0', END)

    def play_video(self):
        pass

    def play_audio(self):
        pass


if __name__ == '__main__':
    interface = GUI(800, 600).start()
