from threading import Thread
import socket


class Client():
    def __init__(self, gui, nickname):
        self.gui = gui
        self.nickname = nickname
        self.infoFulanoNickname = "Fulano"

        self.udp_socket = socket.socket(
            family=socket.AF_INET, type=socket.SOCK_DGRAM)

    def receive(self):
        count = 0
        while True:
            received_message, received_adds = self.udp_socket.recvfrom(1024)
            received_message = received_message.decode("utf-8")

            self.gui.show_received(received_message)

            data_about_sender = received_message.strip()

            if count == 0:
                infos = data_about_sender.split(" - ")
                self.infoAddr = infos[0]
                turningToTuple = self.infoAddr.split(', ')
                
                tuple1 = turningToTuple[0]
                tuple1 = tuple1.replace("(", "")
                tuple1 = tuple1.replace("'", "")

                tuple2 = turningToTuple[1].replace(")", "")
                tuple2 = int(tuple2)
                
                self.infoAddr = (tuple1, tuple2)
                self.infoFulanoNickname = infos[1]

                count += 1

    def send(self, *message):
        if len(message) > 0:
            if isinstance(message[0], str):
                self.udp_socket.sendto(bytes(message[0], 'utf-8'), self.infoAddr)
            else:
                self.udp_socket.sendto((message[0], 'utf-8'), self.infoAddr)

    def connect(self):
        sender = Thread(target=self.send)
        receiver = Thread(target=self.receive)

        self.udp_socket.sendto(
            bytes(f'Connected - {self.nickname}', 'utf-8'), ('localhost', 29996))

        sender.start()
        receiver.start()

    def giveFulanoName(self):
        return self.infoFulanoNickname