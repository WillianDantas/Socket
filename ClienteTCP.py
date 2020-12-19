# Clinte TCP
import socket;
HOST = '127.0.0.1';     # Endereco IP do Servidor
PORT = 5000;            # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM); #Criar socket tcp
dest = (HOST, PORT); # destino tcp
tcp.connect(dest);  # abre conexão tcp

while True:
    msg = input(); # recebe valor
    tcp.send(msg.encode('utf-8')); # enviar mensagem para servidor
    msg = tcp.recv(1024);   # receber mensagem do servidor
    print(msg); # impime mensagem na tela
tcp.close();