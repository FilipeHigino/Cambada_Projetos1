import geocoder

def solicitar_localizacao():
        resposta = input("Deseja permitir acesso à sua localização? (sim/não): ")
        if resposta.lower() == "sim":
            g = geocoder.ip('me')
            print("Sua localização é: ", g.latlng)
        elif resposta.lower() == "não" or resposta.lower() == "nao":
            print("Acesso à localização negado.")
        else:
            print("Ocorreu um erro durante a solicitação da localização:")

solicitar_localizacao()
