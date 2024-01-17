import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('Server Socket created')

host = 'localhost'
port = 5432

s.bind((host, port))
message = 'Server: Hey there Client, I am Server UDP'

while 1:
    data, end = s.recvfrom(4096)

    if data:
        print("Server sending Message...")
        s.sendto(data + (message.encode()), end)
