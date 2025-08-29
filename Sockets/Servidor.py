import socket

# Crear el socket TCP/IP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Asociar a una IP y puerto
server_socket.bind(("192.168.1.75", 5000))  # localhost:5000
server_socket.listen(1)  # Máximo 1 cliente en espera

print("Servidor esperando conexiones...")

# Esperar conexión
conn, addr = server_socket.accept()
print(f"Conectado con: {addr}")

while True:
    data = conn.recv(1024).decode("utf-8")  # Recibir mensaje (máx 1024 bytes)
    if not data:
        break
    print("Cliente dice:", data)

    respuesta = input("Servidor responde: ")
    conn.sendall(respuesta.encode("utf-8"))

conn.close()
server_socket.close()
