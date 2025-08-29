import socket
import threading

# Datos compartidos del "mundo del juego"
players = {}  # {addr: {"x": 0, "y": 0}}

def handle_client(conn, addr):
    print(f"[NUEVA CONEXION] {addr}")
    players[addr] = {"x": 0, "y": 0}  # estado inicial del jugador

    try:
        while True:
            data = conn.recv(1024).decode("utf-8")
            if not data:
                break

            print(f"[{addr}] -> {data}")

            # Procesamos acción: mover jugador
            if data == "UP":
                players[addr]["y"] += 1
            elif data == "DOWN":
                players[addr]["y"] -= 1
            elif data == "LEFT":
                players[addr]["x"] -= 1
            elif data == "RIGHT":
                players[addr]["x"] += 1

            # Enviar el estado actualizado a este jugador
            conn.sendall(str(players[addr]).encode("utf-8"))

    except ConnectionResetError:
        print(f"[DESCONECTADO] {addr}")
    finally:
        conn.close()
        del players[addr]

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("192.168.1.75", 5000))  # Cambia la IP por la de tu servidor real
    server.listen()

    print("[SERVIDOR] Esperando conexiones...")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

start_server()
