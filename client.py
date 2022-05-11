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
            # self.received_message = received_message.decode("utf-8")

            # if firstMessage:
            #     self.get_sender_info(self.received_message)
            #     firstMessage = False

            # try:
            #     self.receive_file(self.received_message)
            #     self.gui.show_file(self.name_of_file)
            # except:
            #     self.gui.show_received(
            #         self.received_message, self.senderName)
            #     self.get_sender_info(self.received_message)
            try:
                self.received_message = received_message.decode("utf-8")

                if firstMessage:
                    self.get_sender_info(self.received_message)
                    firstMessage = False

                self.gui.show_received(
                    self.received_message, self.senderName)

            except:
                self.receive_file(self.received_message)
                self.gui.show_file(self.name_of_file)

    def receive_file(self, data):
        self.name_of_file = f"binariesFiles/${data.split(':')[0]}"
        file = open(self.name_of_file, 'wb')
        while self.received_message:
            self.received_message, received_adds = self.udp_socket.recvfrom(
                1024)
            file.write(self.received_message)
        file.close()

    def send(self, *message):
        if len(message) > 0:
            if isinstance(message[0], str):
                self.udp_socket.sendto(
                    bytes(message[0], 'utf-8'), self.senderAddress)
            else:
                self.udp_socket.sendto(message[0], self.senderAddress)

    def connect(self):
        sender = Thread(target=self.send)
        receiver = Thread(target=self.receive)

        self.udp_socket.sendto(
            bytes(f'Connected - {self.nickname}', 'utf-8'), ('localhost', 29996))

        sender.start()
        receiver.start()

    def get_sender_info(self, message):
        data = message.split(" - ")
        if data[0][0] == '(':
            self.senderAddress = eval(data[0])
            self.senderName = data[1]
