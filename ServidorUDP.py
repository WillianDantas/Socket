# Servidor UDP
import socket;

def quadrado(num): # Função que eleva quadrado
    num = num ** 2;
    return num;



HOST = 'localhost';              # Endereco IP do Servidor
PORT = 5000;            # Porta que o Servidor esta
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM); # Cria socket
orig = (HOST, PORT);  # origem do  servidor
udp.bind(orig); # abre conexao
while True:
    msg, cliente = udp.recvfrom(1024); # receber valor do cliente
    print(cliente, msg);
    msg = quadrado(int(msg));
    udp.sendto(str(msg).encode('utf-8'),cliente); #envia msg para cliente
udp.close();


