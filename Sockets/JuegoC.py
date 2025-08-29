import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("192.168.1.75", 5000))

print("Conectado al servidor. Usa comandos: UP, DOWN, LEFT, RIGHT")

try:
    while True:
        move = input("Movimiento: ")
        client.sendall(move.encode("utf-8"))

        # Recibir estado de mi jugador
        state = client.recv(1024).decode("utf-8")
        print("Tu posición:", state)

except KeyboardInterrupt:
    print("Saliendo...")
finally:
    client.close()
