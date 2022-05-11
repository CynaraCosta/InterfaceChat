import socket


class Server:
    def __init__(self):
        self.udp_socket = socket.socket(
            family=socket.AF_INET, type=socket.SOCK_DGRAM)
        self.udp_socket.bind(('localhost', 29996))
        self.connected_users = []
        self.nicknames_users = []
        print("UDP Server online")

    def start(self):
        while True:
            self.msg, self.addr = self.udp_socket.recvfrom(1024)

            self.nickname = self.msg[12:].decode("utf-8")
            self.nicknames_users.append(self.nickname)
            self.connected_users.append(self.addr)

            print(f"Connection made with ---> {self.addr}")

            if (len(self.connected_users) == 2):
                firstUser, secondUser = self.connected_users[0], self.connected_users[1]
                firstUserName, secondUserName = self.nicknames_users[0], self.nicknames_users[1]

                self.udp_socket.sendto(
                    bytes(f"{firstUser} - {firstUserName}", "utf-8"), secondUser)
                self.udp_socket.sendto(
                    bytes(f"{secondUser} - {secondUserName}", "utf-8"), firstUser)

                self.connected_users = []
                self.nicknames_users = []
                print("UDP Server ready for two more users")

if __name__ == "__main__":
    server = Server()
    server.start()
