import socket

SERVER_HOST = '0.0.0.0'
SERVER_PORT = 8080

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(1)
print("Server is listening...")

connection, address = server_socket.accept()
print("Connected by", address)

image_data = bytearray()
while True:
    data = connection.recv(1024)
    if not data:
        break
    image_data.extend(data)

with open("image.jpg", "wb") as f:
    f.write(image_data)

print('Фотография сохранена в файле image.jpg')
connection.close()
