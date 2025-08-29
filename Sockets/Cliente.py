import socket

# Crear socket TCP/IP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectarse al servidor
client_socket.connect(("192.168.1.75", 5000))

print("Conectado al servidor.")

while True:
    mensaje = input("Cliente dice: ")
    client_socket.sendall(mensaje.encode("utf-8"))

    data = client_socket.recv(1024).decode("utf-8")
    print("Servidor responde:", data)

client_socket.close()
