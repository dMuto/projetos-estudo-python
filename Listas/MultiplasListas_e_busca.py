#Listas multiplas:  Inercao e busca

equipamentos = []
valores = []
seriais = []
departamentos = []
resposta = "S"

while resposta == "S":
    equipamentos.append(input("Equipamento: "))
    valores.append(float(input("valor: ")))
    seriais.append(int(input("serial: ")))
    departamentos.append(input("Departamento: "))
    resposta = input("Digite \"S\" para continuar: ").upper()

buscar = input("\nDigite o nome do equipamento que deseja buscar: ")
for indice in range(0, len(equipamentos)):
    if buscar == equipamentos[indice]:
        print("Valor..: ", valores[indice])
        print("Serial..: ", seriais[indice])