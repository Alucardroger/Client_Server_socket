import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Client Socket created succesfully!")

host = 'localhost'
port = 5433
message = 'Hello Server, welcome to UDP Client!\n'

try:
    print('Client:' + message)
    s.sendto(message.encode(), (host, 5432))

    data, server = s.recvfrom(4096)
    data = data.decode()
    print("Client: " + data)
finally:
    print("Client closed")
    s.close()