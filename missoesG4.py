import os; os.system ("cls")

def missao_marco_zero():
    print("Executando Missão Marco Zero...")
    #adicionar as missões aí

def missao_memorial():    
    print("Executando Missão Memorial...")
    #adicionar as missões aí

def exibir_menu():
    print("Bem-vindo ao simulador de missões!")
    print("Escolha uma missão:")
    print("1. Missão Marco Zero")
    print("2. Missão Memorial")

while True:
    exibir_menu()
    escolha = input("Digite o número da missão que deseja executar (ou 'q' para sair): ")

    if escolha == '1':
        missao_marco_zero()
    elif escolha == '2':
        missao_memorial()
    elif escolha.lower() == 'q':
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
