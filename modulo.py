import time
import geocoder

lat_mz = -8.062980
lon_mz = -34.871030
coord_marco_zero = {"lat":lat_mz,"lon":lon_mz}

lat_memorial = -8.066983497265666
lon_memorial = -34.87885283350753
coord_memorial = {"lat":lat_memorial,"lon":lon_memorial}

coordenadas = {}


def missões_jogo():
    def missao_marco_zero():
        print("Executando Missão Marco Zero...")
        if coord_marco_zero == coordenadas:
            print("Parabéns por ter cumprido a missão de ir até o Marco Zero!")
        else:
            print("Missão fracassada, tente novamente mais tarde!")

    def missao_memorial():
        print("Executando Missão Memorial...")
        if coord_memorial == coordenadas:
            print("Parabéns por ter cumprido a missão de ir até o Memorial!")
        else:
            print("Missão fracassada, tente novamente mais tarde!")

    def exibir_menu_missoes():
        print("Bem-vindo ao simulador de missões!")
        print("Escolha uma missão:")
        print("1. Missão Marco Zero")
        print("2. Missão Memorial")

    while True:
        exibir_menu_missoes()
        escolha = input("Digite o número da missão que deseja executar (ou 'q' para voltar para o menu principal): ")

        try:
            if escolha == '1':
                missao_marco_zero()
                break
            elif escolha == '2':
                missao_memorial()
                break
            elif escolha.lower() == 'q':
                print("Saindo do programa...")
                break
            else:
                raise ValueError("Opção inválida. Por favor, escolha uma opção válida.")
        except ValueError as error:
            print(str(error))
            continue
        except Exception as exception:
            print("Ocorreu um erro inesperado:", str(exception))
            continue

def esta_autenticado():
    with open("usuarios.txt", "r") as arquivo:
        linhas = arquivo.readlines()
        return len(linhas) > 1

def alimentar():
    total = 100
    while True:
        acao = input("Aumentando fome... Alimentar? [0 - NÃO / 1 - SIM] (ou 'q' para sair): ")
        
        if acao.lower() == 'q':
            menu_jogo()
            break
        
        if acao == '1':
            try:
                opcao = int(input("""Digite a opção desejada:
                    [1] - Cuscuz (+10)
                    [2] - Tapioca (+25)
                    [3] - Bolo de Rolo (+50)
                """))
            except ValueError:
                print("Opção inválida. Digite um número válido.")
                continue
            
            if opcao == 1:
                print("Cuscuz diminui 10 de fome")
                try:
                    cuscuz = int(input("Deseja dar Cuscuz? [0 - NÃO / 1 - SIM]: "))
                except ValueError:
                    print("Entrada inválida. Digite 0 para NÃO ou 1 para SIM.")
                    continue
                    
                if cuscuz == 1:
                    total += 10
                else:
                    continue
            elif opcao == 2:
                print("Tapioca diminui 25 de fome")
                try:
                    tapioca = int(input("Deseja dar Tapioca? [0 - NÃO / 1 - SIM]: "))
                except ValueError:
                    print("Entrada inválida. Digite 0 para NÃO ou 1 para SIM.")
                    continue
                    
                if tapioca == 1:
                    total += 25
                else:
                    continue
            elif opcao == 3:
                print("Bolo de rolo diminui 50 de fome")
                try:
                    bolo = int(input("Deseja dar cuscuz? [0 - NÃO / 1 - SIM]: "))
                except ValueError:
                    print("Entrada inválida. Digite 0 para NÃO ou 1 para SIM.")
                    continue
                    
                if bolo == 1:
                    total += 50
                else:
                    continue
        else:
            print("Não alimentando...")
        
        time.sleep(2)
        decorrer = total - 5
        if decorrer < total:
            total = decorrer
            if total >= 100:
                total = 100
                decorrer = total
        print(total)
        
        if total == 0:
            print("\nSem... Forças....")
            time.sleep(2)
            print("\nMude o mundo, minha ultima mensagem... Adeus.")
            time.sleep(2)
            print("\nBichinho morreu.")
            break









    usuario = input("Digite o seu nome de usuário: ")
    senha = input("Digite a sua senha: ")

    try:
        with open("usuarios.txt", "r") as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                usuario = linha.strip().split(":")
                usuario_login = usuario[0]
                if len(usuario) > 1:
                    usuario_senha = usuario[1]
                else:
                    usuario_senha = ""

                if usuario == usuario_login and senha == usuario_senha:
                    print("Login bem-sucedido!")
                    return

        print("Login ou senha incorretos!")
    except Exception as e:
        print("Ocorreu um erro durante o login:", str(e))

def cadastrar_usuario():
    # with open('usuarios.txt', 'a') as arquivo:
    #     arquivo.write('usuario,senha\n')

    
    usuario = input("Digite o nome do usuário: ")
    senha = input("Digite a senha do usuário: ")

    
    with open("usuarios.txt", "r") as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas:
            if usuario in linha:
                print("Usuário já cadastrado.")
                return

   
    with open("usuarios.txt", "a") as arquivo:
        arquivo.write(f"{usuario}:{senha}\n")

    print("Usuário cadastrado com sucesso!")

def fazer_login():
    autenticado = False
    while not autenticado:
        usuario_login = input("Digite o seu nome de usuário: ")
        senha = input("Digite a sua senha: ")

        with open("usuarios.txt", "r") as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                usuario = linha.strip().split(":")
                usuario_usuario = usuario[0]
                if len(usuario) > 1:
                    usuario_senha = usuario[1]
                else:
                    usuario_senha = ""

                if usuario_login == usuario_usuario and senha == usuario_senha:
                    print("Login bem-sucedido!")
                    autenticado = True
                    break

        if not autenticado:
            print("Nome de usuário ou senha incorretos. Tente novamente.")

def main():
    opcao = int(input("Bem-vindo!\nDigite:\n[1] - Para realizar o cadastro\n[2] - Para fazer Login\nOpção: "))

    if opcao == 1:
        cadastrar_usuario()
    elif opcao == 2:
        fazer_login()
    else:
        print("Opção inválida.")

def personalizar_caranguejo():
    caranguejo = {}
    print("Escolha a espécie do caranguejo:")
    print("1. Caranguejo-Ermitão")
    print("2. Caranguejo-Verde")
    print("3. Caranguejo-Vermelho")
    especie_opcao = input("Digite o número da opção desejada: ")

    if especie_opcao == "1":
        tipo = "Caranguejo-Ermitão"
    elif especie_opcao == "2":
        tipo = "Caranguejo-Verde"
    elif especie_opcao == "3":
        tipo = "Caranguejo-Vermelho"
    else:
        print("Opção inválida. Espécie padrão definida.")
        tipo = "Caranguejo-Vermelho"

    print("Escolha a cor da casca:")
    print("1. Vermelha")
    print("2. Azul")
    print("3. Verde")
    cor_opcao = input("Digite o número da opção desejada: ")

    if cor_opcao == "1":
        cor = "Vermelha"
    elif cor_opcao == "2":
        cor = "Azul"
    elif cor_opcao == "3":
        cor = "Verde"
    else:
        print("Opção inválida. Cor padrão definida.")
        cor = "Vermelha"

    nome = input("Digite o nome do caranguejo: ")

    caranguejo["tipo"] = tipo
    caranguejo["cor"] = cor
    caranguejo["nome"] = nome
    caranguejo["caracteristicas"] = []

    try:
        g = geocoder.ip('me')
        latitude, longitude = g.latlng
        localizacoes = [
            "Paço do frevo",
            "Marco zero",
            "Casa dos bonecos gigantes",
            "Espaço ciência",
            "Museu do mamulengo",
            "Monumento a Chico Science",
            "Centro de artesanato de Pernambuco",
            "Parque de estruturas de Francisco Brennand",
            "Caixa cultural do recife",
            "Museu do homem do nordeste",
            "Museu cais do sertão",
            "Museu da cidade do recife",
            "Casa da cultura",
            "Pátio de são pedro",
            "Teatro santa isabel"
        ]

        if (latitude, longitude) in [
            (8.0657, -34.8711),    # Paço do frevo
            (8.0586, -34.8679),    # Marco zero
            (8.0597, -34.8747),    # Casa dos bonecos gigantes
            (8.0415, -34.8717),    # Espaço ciência
            (8.0515, -34.8614),    # Museu do mamulengo
            (8.0496, -34.8817),    # Monumento a Chico Science
            (8.0474, -34.8882),    # Centro de artesanato de Pernambuco
            (8.0716, -34.8999),    # Parque de estruturas de Francisco Brennand
            (8.0646, -34.8713),    # Caixa cultural do recife
            (8.0544, -34.8842),    # Museu do homem do nordeste
            (8.0603, -34.8781),    # Museu cais do sertão
            (8.0636, -34.8739),    # Museu da cidade do recife
            (8.0592, -34.8726),    # Casa da cultura
            (8.0640, -34.8720),    # Pátio de são pedro
            (8.0647, -34.8756)     # Teatro santa isabel
        ]:
            caranguejo["item_exclusivo"] = "Item Exclusivo"

    except Exception as e:
        print("Erro ao obter a localização:", str(e))
        latitude, longitude = None, None

    return caranguejo

def exibir_item_exclusivo(caranguejo):
    if "item_exclusivo" in caranguejo:
        print("Parabéns! Você ganhou um", caranguejo["item_exclusivo"] + "!")
        print("Este item representa sua visita a uma localização especial.")
        print("Use-o com orgulho em seu caranguejo virtual!")

def solicitar_localizacao():
    resposta = input("Deseja permitir acesso à sua localização? (sim/não): ")
    if resposta.lower() == "sim":
        g = geocoder.ip('me')
        print("Sua localização é: ", g.latlng)
        armazenar_localizacao()
    elif resposta.lower() == "não" or resposta.lower() == "nao":
        print("Acesso à localização negado.")
    else:
        print("Ocorreu um erro durante a solicitação da localização:")

def armazenar_localizacao():
    with open('localizacao_usuario.txt', 'r') as arquivo:
        linhas = arquivo.readlines()
    for linha in linhas:
        if "Latitude:" in linha:
            latitude = float(linha.split(":")[1])
            coordenadas["lat"] = latitude
        elif "Longitude:" in linha:
            longitude = float(linha.split(":")[1])
            coordenadas["lon"] = longitude

    print("Coordenadas armazenadas no dicionário:", coordenadas)

def menu_jogo():

    print("Bem-vindo ao jogo!")
    while True:
            opcao = input(f'''
        JOGO CAMBADA
        
        [A]: Alimentar
        [B]: Customização 
        [C]: Geolocalização
        [D]: Missões 
        [E]: Sair
        Selecione a opção:''').upper()

            if opcao == 'A':
                alimentar()
            elif opcao == 'B':
                personalizar_caranguejo()
            elif opcao == 'C':
                solicitar_localizacao()
            elif opcao == 'D':
                missões_jogo()
            elif opcao == 'E':
                print("Obrigado por jogar nosso jogo, volte sempre!")
                break
            else:
                print("Não foi escolhida uma opção válida")
def menu(): 
        while True:
            print(f"""            {"=-" * 32}
            {" "*24}Menu Principal
            {"=-" * 32}
            \n
            [1] - Iniciar Jogo
            [2] - Minha Conta
            [3] - Configurações
            [4] - Suporte
            [5] - Encerrar o game""")

            try:
                resp = int(input("Digite a opção que você deseja selecionar: "))

                if resp == 1:
                    print("Opção 1 selecionada. Jogo iniciado")
                    main()
                    menu_jogo()
                elif resp == 2:
                    print("Opção 2 selecionada. Minha Conta:")
                    print("O que você deseja fazer na sua conta?")
                    print()
                    print("[1] - Editar Perfil")
                    print("[2] - Alterar Senha")
                    print("[3] - Excluir Conta")

                    try:
                        resp2 = int(input("Digite a opção desejada: "))

                        if resp2 == 1:
                            print("Perfil editado.")
                        elif resp2 == 2:
                            print("Senha alterada.")
                        elif resp2 == 3:
                            print("Conta excluída.")
                        else:
                            print("Opção inválida, tente novamente.")
                    except ValueError:
                        print("Entrada inválida. Digite um número inteiro.")
                elif resp == 3:
                    print("Opção 3 selecionada. Configurações:")
                    print("O que você deseja configurar?")
                    print()
                    print("[1] - Áudio")
                    print("[2] - Serviço de Localização")
                    print("[3] - Idioma")

                    try:
                        resp3 = int(input("Digite a opção desejada: "))

                        if resp3 == 1:
                            audio = int(input("Escolha o nível do áudio de 0 a 100: "))

                            if 0 <= audio <= 100:
                                print("O áudio foi alterado para:", audio)
                            else:
                                print("Áudio inválido, tente novamente.")
                        elif resp3 == 2:
                            loc = int(input("Deseja ativar [1] ou desativar [0] o serviço de localização?"))

                            if loc == 1:
                                print("Serviço de localização ativado.")
                            elif loc == 0:
                                print("Serviço de localização desativado.")
                            else:
                                print("Opção inválida, tente novamente.")
                        elif resp3 == 3:
                            print("Idioma configurado.")
                        else:
                            print("Opção inválida, tente novamente.")
                    except ValueError:
                        print("Entrada inválida. Digite um número inteiro.")
                elif resp == 4:
                    print("Opção 4 selecionada. Suporte:")
                    print("Como posso ajudar?")
                    print()
                    print("[1] - Relatar um problema")
                    print("[2] - Perguntas frequentes")
                    print("[3] - Contatar suporte")

                    try:
                        resp4 = int(input("Digite a opção desejada: "))

                        if resp4 == 1:
                            print("Problema relatado.")
                        elif resp4 == 2:
                            print("Perguntas frequentes.")
                        elif resp4 == 3:
                            print("Suporte contatado.")
                        else:
                            print("Opção inválida, tente novamente.")
                    except ValueError:
                        print("Entrada inválida. Digite um número inteiro.")
                elif resp == 5:
                    print("Jogo finalizado.")
                    return
                else:
                    print("Opção inválida, tente novamente.")
            except ValueError:
                print("Entrada inválida. Digite um número inteiro.")
