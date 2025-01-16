print("Exercicios for")


def response1():
    number = int(input("Digite o número da tablea que deseja: "))

    for item in range(21):
        print(item * number, end=" ")


def response2():
    # ajuda do chatgpt kkkkk
    number = int(input("Digite o enésimo para calcular a sequência de Fibonacci: "))

    if number <= 0:
        return []
    elif number == 1:
        return [0]
    elif number == 2:
        return [0, 1]

    listFibonacci = [0, 1]

    for i in range(2, number):
        listFibonacci.append(listFibonacci[-1] + listFibonacci[-2])
    print("\n", listFibonacci)


print(
    "1. faça um programa que gere uma tabela de multiplicação, a famosa tabuada. O programa deverá perguntar ao usuário qual tabuada ele quer e até qual valor a tabuada será mostrada, sempre começando pelo zero até o 20."
)
response1()

print(
    "\n\n2. Faça um programa que calcule o enésimo da série de Fibonacci. Lembrando que a série começa da seguinte forma 1,1,2,3,5,8..."
)
response2()
