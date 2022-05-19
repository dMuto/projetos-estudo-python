nome = input("Digite um nomezinho ^^ : ")
idade = int(input("Digite a sua idade: "))
doencaInfecciosa = input("Suspeita de doença infecciosa? ").upper()

if idade >= 65:

    print("Paciente COM prioridade")

    if doencaInfecciosa == "SIM":

        print("Encaminhe o paciente para sala AMARELA")

    elif doencaInfecciosa == "NAO":

        print("Encaminhe o paciente para a sala BRANCA")

    else:

        print("Responda a suspeita de doença infecciosa com SIM ou NAO")

else:

    print("Paciente SEM prioridade")

    if doencaInfecciosa == "SIM":

        print("Encaminhe o paciente para sala AMARELA")

    elif doencaInfecciosa == "NAO":

        print("Encaminhe o paciente para sala BRANCA")

    else:

        print("Responda a suspeita de doença infecciosa com SIM ou NAO")
