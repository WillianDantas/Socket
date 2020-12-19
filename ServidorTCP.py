import socket;

def quadrado(num):
    num = num ** 2;
    return num;


HOST = '127.0.0.1';              # Endereco IP do Servidor
PORT = 5000;            # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM); # criar ssocket tcp
orig = (HOST, PORT); # origem tcp
tcp.bind(orig); # abrindo conexao
tcp.listen(1);
while True:
    con, cliente = tcp.accept(); #aceitando conexão
    print ('Concetado por', cliente);
    while True:
        msg = con.recv(1024) # recebendo mensagem
        if not msg: break;
        print (cliente, msg);
        msg = quadrado(int(msg));
        con.send(str(msg).encode('utf-8'));# enviando mensagem
    print ('Finalizando conexao do cliente', cliente);
    con.close(); # finalizando conexao