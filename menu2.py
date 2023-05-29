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

        try:
            resp = int(input("Digite a opção que você deseja selecionar: "))

            if resp == 1:
                print("Opção 1 selecionada. Jogo iniciado")
            elif resp == 2:
                print("Opção 2 selecionada. Editar personagem:")
                print("O que você quer editar no personagem?")
                print()
                print("[1] - Editar cor")
                print("[2] - Editar tamanho")

                try:
                    resp2 = int(input("Digite a opção desejada: "))

                    if resp2 == 1:
                        print("Qual a cor do personagem você deseja a partir de agora?")
                        print("[1] - Laranja")
                        print("[2] - Verde")
                        print("[3] - Azul")
                        cor = int(input("Digite a cor escolhida: "))

                        if cor == 1:
                            print("Cor laranja selecionada")
                        elif cor == 2:
                            print("Cor verde selecionada")
                        elif cor == 3:
                            print("Cor azul selecionada")
                        else:
                            print("Opção inválida, escolha outra cor")
                    elif resp2 == 2:
                        print("Qual tamanho de personagem você deseja agora?")
                        print("[1] - Pequeno")
                        print("[2] - Médio")
                        print("[3] - Grande")
                        tamanho = int(input("Digite qual tamanho de personagem você deseja: "))

                        if tamanho == 1:
                            print("Tamanho pequeno selecionado")
                        elif tamanho == 2:
                            print("Tamanho médio selecionado")
                        elif tamanho == 3:
                            print("Tamanho grande selecionado")
                        else:
                            print("Tamanho inválido, escolha novamente.")
                    else:
                        print("Opção inválida, tente novamente.")
                except ValueError:
                    print("Entrada inválida. Digite um número inteiro.")
            elif resp == 3:
                print("Configurações selecionadas")
                print("Configurações:")
                print("[1] - Áudio")
                print("[2] - Serviço de localização")
                print("[3] - Créditos")

                try:
                    opcao = int(input("Selecione a opção: "))

                    if opcao == 1:
                        audio = int(input("Escolha o nível do áudio de 0 a 100: "))

                        if 0 <= audio <= 100:
                            print("O áudio foi alterado para:", audio)
                        else:
                            print("Áudio inválido, tente novamente.")
                    elif opcao == 2:
                        loc = int(input("Deseja ativar [1] ou desativar [0] o serviço de localização?"))

                        if loc == 1:
                            print("Serviço de localização ativado.")
                        elif loc == 0:
                            print("Serviço de localização desativado.")
                        else:
                            print("Opção inválida, tente novamente.")
                    elif opcao == 3:
                        print("Créditos:")
                        print()
                        print("Alunos de Ciência da Computação:")
                        print("Ícaro Barros")
                        print("Filipe")
                        print("Lucas Rosati")
                        print("Malu Coimbra")
                        print("Mirna Lustosa")
                        print("Henrique Lobo")
                        print()
                        print("Alunos de Design:")
                        print("Eduarda Marrocos")
                        print("Bia Sampaio")
                        print("Letícia Cristina")
                        print("Isabella")
                        print("Lucas")
                        print("Vitor")
                        print()
                        print("Obrigado!")
                    else:
                        print("Opção inválida, tente novamente.")
                except ValueError:
                    print("Entrada inválida. Digite um número inteiro.")
            elif resp == 4:
                print("Jogo finalizado.")
                break
            else:
                print("Opção inválida, tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")

menu()

