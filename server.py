import socket


class Server:
    def __init__(self):
        self.udp_socket = socket.socket(
            family=socket.AF_INET, type=socket.SOCK_DGRAM)
        self.udp_socket.bind(('localhost', 29996))
        self.connected_users = []
        print("UDP Server online")

    def start(self):
        while True:
            msg, addr = self.udp_socket.recvfrom(1024)

            self.connected_users.append(addr)
            print(f"Connection made with ---> {addr}")

            if (len(self.connected_users) == 2):
                firstUser, secondUser = self.connected_users[0], self.connected_users[1]

                self.udp_socket.sendto(
                    bytes(f"{firstUser}", "utf-8"), secondUser)
                self.udp_socket.sendto(
                    bytes(f"{secondUser}", "utf-8"), firstUser)

                connected_users = []
                print("UDP Server ready for two more users")


if __name__ == "__main__":
    server = Server()
    server.start()
