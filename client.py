from threading import Thread
import socket


class Client():
    def __init__(self, gui):
        self.udp_socket = socket.socket(
            family=socket.AF_INET, type=socket.SOCK_DGRAM)
        
        self.gui = gui

    def receive(self):
        while True:
            received_message, received_adds = self.udp_socket.recvfrom(1024)
            received_message = received_message.decode("utf-8")
            print(f"Received ---> {received_message}")
            try:
                x = 0
            except:
                self.gui.receive_and_show(received_message)
                self.informations(received_message)

    # to-do: get the other user's data to pass as argument in line 19
    def send(self, *message):
        if len(message) > 0:
            if isinstance(message[0], str):
                self.udp_socket.sendto(bytes(message[0], 'utf-8'), self.info)
            else:
                self.udp_socket.sendto((message[0], 'utf-8'), self.info)

    def connect(self):
        sender = Thread(target=self.send)
        receiver = Thread(target=self.receive)

        self.udp_socket.sendto(
            bytes('Connected', 'utf-8'), ('localhost', 29996))

        sender.start()
        receiver.start()

    def informations(self, *info):
        info = info[0].strip()
        if info[0] == "(":
            info = eval(info)
            self.info = info