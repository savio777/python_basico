print("Exercicios while")


def response1():
    numberInput = int(input("Digite o número para calcular o fatorial: "))

    result = numberInput

    while numberInput > 0:
        numberInput -= 1
        if numberInput > 0:
            result *= numberInput

    return result


def response2():
    passwordDefault = "pass"

    attempts = 3

    while attempts > 0:
        attempts -= 1
        passwordInput = input("Digite a senha: ")

        if passwordInput == passwordDefault:
            print("Senha correta. Acesso concedido.")
            return
        else:
            print("Senha incorreta")


print(
    "1. faça um programa que calcule o fatorial de um numro, fornecido pelo usuário. (Ex: 5!= 5*4*3*2*1)"
)

print(response1())

print(
    "2. Vamos fazer um programa que simule um cofre. Ele tera uma senha predefinida e o usuário terá três tentativas para acertar a senha. A cada tentativa errada o programa deverá mostrar a mensagem: Senha incorreta. Se ele acertar a senha deverá mostar a mensagem: Senha correta. Acesso concedido."
)

response2()
