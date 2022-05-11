from threading import Thread
import socket


class Client():
    def __init__(self, gui, nickname):
        self.gui = gui
        self.nickname = nickname

        self.udp_socket = socket.socket(
            family=socket.AF_INET, type=socket.SOCK_DGRAM)

    def receive(self):
        firstMessage = True
        while True:
            received_message, received_adds = self.udp_socket.recvfrom(1024)
            received_message = received_message.decode("utf-8")

            if firstMessage:
                self.get_sender_info(received_message)
                firstMessage = False

            self.gui.show_received(received_message, self.senderName)

    def send(self, *message):
        if len(message) > 0:
            if isinstance(message[0], str):
                self.udp_socket.sendto(
                    bytes(message[0], 'utf-8'), self.senderAddress)
            else:
                self.udp_socket.sendto(
                    (message[0], 'utf-8'), self.senderAddress)

    def connect(self):
        sender = Thread(target=self.send)
        receiver = Thread(target=self.receive)

        self.udp_socket.sendto(
            bytes(f'Connected - {self.nickname}', 'utf-8'), ('localhost', 29996))

        sender.start()
        receiver.start()

    def get_sender_info(self, message):
        data = message.split(" - ")
        self.senderAddress = eval(data[0])
        self.senderName = data[1]
