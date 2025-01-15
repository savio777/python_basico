def response1():
    values = [10, 15, 20]
    return sum(values) / len(values)


def response2():
    note1 = int(input("Digite a primeira nota: "))
    note2 = int(input("Digite a segunda nota: "))

    weight1 = int(input("Digite o peso da primeira nota: "))
    weight2 = int(input("Digite o peso da segunda nota: "))

    if (weight1 + weight2) != 10:
        return "os pesos devem ter a soma igual a 10"

    return ((note1 * weight1) + (note2 * weight2)) / (weight1 + weight2)


def response3():
    values = (100.20, 34.90, 31.50, 18.95)

    return min(values)


def response4():
    number = int(input("Digite o número: "))

    return number % 2 == 0


def response5():
    values = (100.20, 34.90, 31.50, 18.95)

    return min(values) < 20


def response6():
    farenheit = float(input("Digite a temperatura em farenheit: "))

    return str(5 / 9 * farenheit - 32) + "ºC"


print("Exercícios 1\n\n")

print("1. calcule a média entre os números 10, 15, 20:")
print(response1())

print(
    "\n2. Peça para o usuário digitar duas notas de zero a dez e os pesos das notas e calcule a média ponderada entre elas.\nlembrando que a soma dos pesos precisa ser dez."
)
print(response2())

print(
    "\n3. qual o menor preço da lista?\npreços: R$ 100.20, R$ 34.90, R$ 31.50, R$ 18.95"
)
print(response3())

print("\n4. Avalie se o número digitado pelo usuário é par ou ímpar.")
print(response4())

print(
    "\n5. Verifique se o menor preço dessa lista é menor que R$ 20.00\npreços: R$ 100.20, R$ 34.90, R$ 31.50, R$ 18.95"
)
print(response5())

print(
    "\n6. Faça um programa que converta a temperatura em graus Farenheit fornecida pelo usuário em Celsius.\n(celsius = 5/9 * farenheit - 32)"
)
print(response6())
