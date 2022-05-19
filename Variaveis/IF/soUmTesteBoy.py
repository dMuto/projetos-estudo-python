resposta = "SIM"
while resposta == "SIM":
    nivel = input("Digite o nivel de acesso: ").upper()

    if nivel == "ADM" or nivel == "USR":
        genero = input("Digite o seu genero: ").upper()
        if nivel == "ADM":
            if genero == "FEMININO":

                print("Olá administradora")

            else:
                print("Ola administador")

    elif nivel == "GUEST":

        print("Olá visitante")

    else:

        print("Ola desconhecido(a)")

    resposta = input("Digite SIM para continuar: ").upper()