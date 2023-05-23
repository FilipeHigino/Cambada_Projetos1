import geocoder

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

    return caranguejo


def exibir_item_exclusivo(caranguejo):
    if "item_exclusivo" in caranguejo:
        print("Parabéns! Você ganhou um", caranguejo["item_exclusivo"] + "!")
        print("Este item representa sua visita a uma localização especial.")
        print("Use-o com orgulho em seu caranguejo virtual!")

caranguejo_personalizado = personalizar_caranguejo()

exibir_item_exclusivo(caranguejo_personalizado)

print(caranguejo_personalizado)