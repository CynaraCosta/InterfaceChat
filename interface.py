from http import client
from time import time
from tkinter import *
from tkinter import filedialog
from check_message import *

nickname = input("Escolha um nome de usuário: ")

class GUI:
    def __init__(self, width, height):
        self.window = Tk()
        self.window.title(f"Chat P2P de {nickname}")
        
        #Bind the Enter Key to Call an event
        self.window.bind('<Return>', self.send)

        self.canva = Canvas(self.window, width=width, height=height)
        self.canva.grid(columnspan=4)

        # Check message ! 

        self.createAssets()

        # self.client = ClientUDP(28886, self)
        # self.client.listenning()

        self.video_counter = 0
        self.audio_counter = 0

    def createAssets(self):
        self.text_area = Text(self.canva, border=1, bg = "#abd3eb")

        self.text_field = Entry(self.canva, width=80, border=1, bg='white')
       
        self.send_button = Button(self.canva, text='Send', padx=30, command=self.send)
        self.video_button = Button(self.canva, text='Play Video', padx=30, command=self.play_video)
        self.audio_button = Button(self.canva, text='Play Audio', padx=30, command=self.play_audio)
        self.clear_button = Button(self.canva, text='Clear', padx=30, command=self.clear_all)

        self.list_audio = Listbox(selectmode = SINGLE, width = 20)
        self.list_video = Listbox(selectmode = SINGLE, width = 20)

        self.list_video.grid(column=2, row=0, columnspan=2)
        self.list_audio.grid(column=3, row=0, columnspan=2)
        self.send_button.grid(column=2, row=2)
        self.clear_button.grid(column=3, row=2)
        self.video_button.grid(column=5, row=2)
        self.audio_button.grid(column=6,row=2)
        self.text_area.grid(column=0, row=0)
        self.text_field.grid(column=0, row=2)

    def start(self):
        self.window.mainloop()

    def send(self, event=None):
        text = is_valid_to_send(self.text_field.get())
        
        # self.client.send_message(text) -> func do client pra mandar msg pra o outro client pelo server
        self.text_area.insert(END, f'{text}\n')
        self.text_field.delete(0, END)

    def received_show_text_area(self):
        pass
        # if client.received_message:
        #    message = message
        #else: 
        #    return

        #should_print = is_valid_to_print(message)
        #if should_print:
        #    self.text_area.insert(END, f'Outro usuário: {message}')
        #    self.text_field.delete(0, END)

    def clear_all(self):
        self.text_area.delete('1.0', END)

    def play_video(self):
        pass

    def play_audio(self):
        pass

if __name__ == '__main__':
    interface = GUI(800, 600).start()