def cadastrar_usuario():
    nome = input("Digite o nome do usuário: ")
    email = input("Digite o e-mail do usuário: ")
    senha = input("Digite a senha do usuário: ")

    
    with open("usuarios.txt", "r") as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas:
            if email in linha:
                print("Usuário já cadastrado.")
                return

   
    with open("usuarios.txt", "a") as arquivo:
        arquivo.write(f"{email}:{senha}\n")

    print("Usuário cadastrado com sucesso!")


def fazer_login():
    email = input("Digite o seu e-mail: ")
    senha = input("Digite a sua senha: ")


    with open("usuarios.txt", "r") as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas:
            usuario = linha.strip().split(":")
            usuario_email = usuario[0]
            if len(usuario) > 1:
                usuario_senha = usuario[1]
            else:
                usuario_senha = ""

            if email == usuario_email and senha == usuario_senha:
                print("Login bem-sucedido!")
                return

    print("E-mail ou senha incorretos!")



def main():
    opcao = int(input("Bem-vindo!\nDigite:\n[1] - Para realizar o cadastro\n[2] - Para fazer Login\nOpção: "))

    if opcao == 1:
        cadastrar_usuario()
    elif opcao == 2:
        fazer_login()
    else:
        print("Opção inválida.")



main()
