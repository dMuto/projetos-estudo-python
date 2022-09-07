import math

def find_average(numbers):
    # your code here
    pass
    return sum(numbers) / len(numbers) if numbers else 0

numeros = []
print("Media: ", find_average(numeros))#str((sum(numeros) / 2)))

tempo = 3
agua = 0.5
nn = tempo * agua
print(str(math.floor(nn)))

tempo = 3
agua = 0.5
nn = tempo * agua
print(str(math.ceil(nn)))

tempo = 3
agua = 0.5
nn = tempo * agua
print(str(nn))