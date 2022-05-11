from threading import Thread
import socket


class Client():
    def __init__(self, gui):
        self.gui = gui

        self.udp_socket = socket.socket(
            family=socket.AF_INET, type=socket.SOCK_DGRAM)

    def receive(self):
        while True:
            received_message, received_adds = self.udp_socket.recvfrom(1024)
            received_message = received_message.decode("utf-8")

            self.gui.show_received(received_message)

            data_about_sender = received_message.strip()
            if data_about_sender[0] == "(":
                self.info = eval(data_about_sender)

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
