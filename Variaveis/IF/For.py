tabuada = int(input("Digite um numero para exibir a tabuada: "))
print("Tabuada do numero ", tabuada)

    # O primeiro numero (1) é onde inicia * vai iniciar a contagem com o contador = 1 *
    # O segundo numero (11) é o range final * vai parar quando chegar em 11 *
    # O terceiro numero (1) é a quantia q vai concatenar * contador =+ 1 *

for valor in range(1, 11, 1):
    print(str(tabuada) + " x " + str(valor) + " = " + str((tabuada * valor)))

num = 8
i = 0
somaTotal = 0
while i <= num:
    somaTotal = somaTotal + i
    i = i + 1

print("aaaaa: " ,somaTotal)
print("Soma total 2 = ", sum(range(num + 1)))