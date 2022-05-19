nome = input("Digite um nome: ")

idade = int(input("Digite a idade: "))

doencaInfectocontagiosa = input("Suspeita de doneça infecto-contagiosa? ").upper()

if idade >= 65 and doencaInfectocontagiosa == "SIM":

    print("O paciente será direcionado para sala AMARELA - COM prioridade")

elif idade < 65 and doencaInfectocontagiosa == "SIM":

    print("O paciente será direcionado para a sala AMARELA - SEM prioridade")

elif idade >= 65 and doencaInfectocontagiosa == "NAO":

    print("O paciente será direcionado a sala BRANCA - COM prioridade")

elif idade < 65 and doencaInfectocontagiosa == "NAO":

    print("O paciente será direcionado para a sala BRANCA - SEM prioridade")

else:

    print("Responda a suspeita de doença infecto-contagiosa com SIM ou NAO")