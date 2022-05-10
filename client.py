from threading import Thread
import socket


class Client():
    def __init__(self):
        self.udp_socket = socket.socket(
            family=socket.AF_INET, type=socket.SOCK_DGRAM)

    def receive(self):
        while True:
            received_message = self.udp_socket.recvfrom(1024)
            message = received_message[0].decode("utf-8")
            print(f"Received ---> {message}")

    # to-do: get the other user's data to pass as argument in line 19
    def send(self, *message):
        if len(message) > 0:
            self.udp_socket.sendto(bytes(message[0], 'utf-8'))

    def connect(self):
        sender = Thread(target=self.send)
        receiver = Thread(target=self.receive)

        self.udp_socket.sendto(
            bytes('Connected', 'utf-8'), ('localhost', 29996))

        sender.start()
        receiver.start()
