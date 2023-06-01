import os
import time
os.system("cls")

def alimentar():
    alimentar = open("alimentar.txt", "a+")
    #alimentar.seek(0)
    total = 100
    while True:
        alimentar.readline()
        time.sleep(2)
        decorrer = total - 25
        if decorrer < total:
            total = decorrer
            if total >= 100:
                total = 100
                decorrer = total
        alimentar.write(str(total))
        alimentar.seek(0)
        print(total)
        try:
            alimentar_input = int(input("Aumentando fome... Alimentar? [0 - NÃO / 1 - SIM]: "))
        except ValueError:
            print("Entrada inválida. Digite 0 para NÃO ou 1 para SIM.")
            continue
        
        if alimentar_input == 1:
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
            print("Nao alimentando...")
        
        if total == 0:
            print("\nSem... Forças....")
            time.sleep(2)
            print("\nMude o mundo, minha ultima mensagem... Adeus.")
            time.sleep(2)
            print("\nBichinho morreu.")
            break
    alimentar.close()

try:
    alimentar()
except Exception as e:
    print("Ocorreu um erro:", str(e))
