import os
import time
os.system("cls")

def alimentar():
    #arquivo = open("fome.txt","rt+") #, "UTF-8"
    total = 100
    while True:
        time.sleep(2)
        decorrer = total - 25
        if decorrer<total:
            total = decorrer
            if total >=100:
                total = 100
                decorrer = total
        print(total)
        alimentar = int(input("Aumentando fome... Alimentar? [0 - NÃO / 1 - SIM]:  "))
        if alimentar == 1:
            opcao = int(input("""Digite a opção desejada:
                    [1] - Cuscuz (+10)
                    [2] - Tapioca (+25)
                    [3] - Bolo de Rolo (+50)    
                """))
            if opcao == 1:
                print("Cuscuz diminui 10 de fome")
                cuscuz = int(input("Deseja dar Cuscuz? [0 - NÃO / 1 - SIM]: "))
                if cuscuz== 1:
                    total+=10
                else:
                    continue
            elif opcao == 2:
                print("Tapioca diminui 25 de fome")
                tapioca = int(input("Deseja dar Tapioca? [0 - NÃO / 1 - SIM]: "))
                if tapioca == 1:
                    total+=25
                else:
                    continue
            elif opcao == 3:
                print("Bolo de rolo diminui 50 de fome")
                bolo = int(input("Deseja dar cuscuz? [0 - NÃO / 1 - SIM]: "))
                if bolo == 1:
                    total+=50
                else:
                    continue
        else:
           print("Nao alimentando...")
           continue
        if total == 0:
            print("\nSem... Forças....")
            time.sleep(2)
            print("\nMude o mundo, minha ultima mensagem... Adeus.")
            time.sleep(2)
            print("\nBichinho morreu.")
            break
        
    #atual = arquivo.write(total)
    #decorrer = str(decorrer)
    #atual = arquivo.write(decorrer)
    #arquivo.close()

alimentar()
