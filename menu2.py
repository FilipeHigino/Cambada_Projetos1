import os
os.system ("cls")

def menu():
    while True:
        print("=-" * 8)
        print("Menuzinho amigo")
        print("=-" * 8)
        print()
        print("[1] - Iniciar Jogo")
        print("[2] - Editar Personagem")
        print("[3] - Configurações")
        print("[4] - Encerrar o game")

        resp = int(input("Digite a opção que você deseja selecioanar: "))

        if resp == 1:
            print("Opção 1 selecionada, Jogo iniciado")
        elif resp == 2:
            print("Opçao 2 selecionada, editar personagem: ")
            print("O quê você quer editar no personagem ?")
            print()
            print("[1] - editar cor")
            print("[2]- editar tamanho")

            resp2 = int(input("Digite a opção desejada: "))

            if resp2 == 1:
                print("Qual a cor do personagem vc deseja a partir de agora? ")
                print("[1] - Laranja")
                print("[2] - Verde")
                print("[3] - Azul")
                cor = int(input("Digite a cor escolhida: "))
                if cor == 1:
                    print("Cor laranja selecionada")
                if cor == 2:
                    print("Cor verde selecionada")
                if cor == 3:
                    print("Cor azul selecionada")
                else:
                    print("Opção inválida, escolha outra cor")
            if resp2 == 2:
                print("Qual tamanho de personagem você deseja agora? ")
                print("[1] - Pequeno")
                print("[2] - Médio")
                print("[3] - Grande")
                tamanho = int(input("Digite qual tamanho de personagem você deseja: "))
                if tamanho == 1:
                    print("Tamanho pequeno slecionado")
                elif tamanho == 2:
                    print("Tamanho médio selecionado")
                elif tamanho == 3:
                    print("Tamanho grande selecionado")
                else:
                    print("Tamanh inválido, escolha novamente.")
        if resp == 3:
            print("Configurações selecionadas")
            print("Configurações: ")
            print("[1] - Áudio")
            print("[2] - Serviço de localização")
            print("[3] - Créditos")
            opcao = int(input("Selecione a opção: "))
            
            if opcao == 1:
                audio = int(input("Escolha o nível do áudio de 0 a 100: "))
                if audio >= 0 and audio <= 100:
                    print("O áudio foi alterado para: ", audio)
                else:
                    print("Audio inválido, tente novamente.")
            elif opcao == 2:
                loc = int(input(print("Deseja ativar[1] ou desativar[0] o serviço de localização ?")))
                if loc == 1:
                    print("Serviço de localização ativado.")
                elif loc ==0:
                    print("Serviço de localização desativado.")
                else:
                    print("Opção inválida, tente novamente.")
            elif opcao == 3:
                print("Créditos: ")
                print()
                print("Alunos de Cicência da Computação: \nÍcaro Barros \nFilipe \nLucas Rosati \nMalu Coimbra \nMirna Lustosa \nHenrique Lobo")
                print()
                print("Alunos de Desing: \nEduarda Marrocos \nBia Sampaio \nLetícia Crisstina \nIsabella \nLucas \nVitor")
                print()
                print()
                print("Obrigado!")
        if resp == 4:
            print("Jogo finalizado.")
            break
menu()
