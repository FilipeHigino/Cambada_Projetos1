import geocoder

def solicitar_localizacao():
    resposta = input("Deseja permitir acesso à sua localização? (sim/não): ")
    if resposta.lower() == "sim":
        g = geocoder.ip('me')
        print("Sua localização é: ", g.latlng)
    else:
        print("Acesso à localização negado.")

solicitar_localizacao()
