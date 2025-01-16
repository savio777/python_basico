print("Funções Exercícios")


def response1(number=5):
    result = number**2
    print(result)
    return result


def response2(temperatureCelsius=0):
    # (32 °C × 9/5) + 32 = 89,6 °F
    resultFahrenheit = (temperatureCelsius * 9 / 5) + 32
    print(f"{resultFahrenheit} ºF")
    return resultFahrenheit


# type: 'quadrado' | 'cubo'
# number: number
def response3(type="", number=0):
    if type == "quadrado":
        print(number**2)
        return number**2

    if type == "cubo":
        print(number**3)
        return number**3


print(
    "1. Escreva uma função que calcule o quadrado do número passado como parâmetro. Se nenhum número for passado use como padrão o número 5."
)
response1()

print(
    "\n2. Escreva uma função que receba como parâmetro uma temperatura em Celsius e converta para Fahrenheit."
)
response2()

print(
    "\n3. Escreva uma função que receba dois parâmetros. O primeiro será uma palavra, se ela for quadrado deverá calcular o quadrado do número passado como segundo parâmetro. Se a palavra for cubo deverá realizar o calculo do cubo do número passado."
)
response3("quadrado", 3)
response3("cubo", 3)
