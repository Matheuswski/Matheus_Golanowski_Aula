def get_nome():
    nome_usuario = input("Entre com seu nome: ")
    return nome_usuario
def print_Mensagem(nome_usuario):
    print("Ola Joven Padawan ", nome_usuario)

def main():
    nome_usuario = get_nome()
    print_Mensagem(nome_usuario)

main()        