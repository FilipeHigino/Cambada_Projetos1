import os
import time
os.system("cls")

def alimentar():
    #arquivo = open("fome.txt","rt+") #, "UTF-8"
    total = 100
    while True:
        time.sleep(2)
        decorrer = total - 5
        if decorrer<total:
            total = decorrer
        print(total)
        print("Aumentando fome...")
        if total == 75:
            print("\nComeçando a ficar com fome...")
            alimentar = int(input("Deseja alimentar o bichinho? [0 = NÃO e 1 = SIM]: "))
            if alimentar == 1:
                print("Huuum comida.")
                total+=25
            else:
                continue
        elif total == 50:
            print("\nBicho tem fome.")
            alimentar = int(input("Deseja alimentar o bichinho? [0 = NÃO e 1 = SIM]: "))
            if alimentar == 1:
                print("Huuum comida.")
                total + 50
            else:
                continue
        elif total == 25:
            print("\nME ALIMENTE!")
            alimentar = int(input("Deseja alimentar o bichinho? [0 = NÃO e 1 = SIM]: "))
            if alimentar == 1:
                print("Huuum comida.")
                total + 75
            else:
                continue
        if total == 0:
            print("\nSem... Forças....")
            time.sleep(2)
            print("\nMude o mundo, minha utlima mensagem... Adeus.")
            time.sleep(2)
            print("\nBichinho morreu.")
            break
        
    #atual = arquivo.write(total)
    #decorrer = str(decorrer)
    #atual = arquivo.write(decorrer)
    #arquivo.close()

alimentar()
