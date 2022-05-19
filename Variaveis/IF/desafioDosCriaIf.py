print("Ola, seja bem vindo ao desafio dos cria!")

acesso = input("Por favor, digite seu tipo de acesso(ADM, USR, GUEST): ").upper()
genero = input("Qual o seu genero? ").upper()

if genero == "FEMININO":

    if acesso == "ADM":

        print("Olá administradora")

    elif acesso == "USR":

        print("Olá usuária")

    elif acesso == "GUEST":

        print("Olá visitante")

    else:

        print("Olá desconhecida")

elif genero == "MASCULINO":

    if acesso == "ADM":

        print("Olá administrador")

    elif acesso == "USR":

        print("Olá usuário")

    elif acesso == "GUEST":

        print("Olá visitante")

    else:

        print("Ola desconhecido")

else:

    print("Olá helicóptero de combate")