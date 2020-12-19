#Cliente UDP
import socket;

HOST = '127.0.0.1';  # Endereco IP do Servidor
PORT = 5000;            # Porta que o Servidor esta
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM); # Criar socket
dest = (HOST, PORT); # destino de ip e porta do servidor
while True:
    msg = input(); # pegar valor digitado
    udp.sendto(msg.encode('utf-8'),dest); # enviar msg atraves do socket
    servidor, resp = udp.recvfrom(1024); # receber  informação enviada pelo servidor
    print(servidor, resp);
udp.close(); # encerrar conexão

