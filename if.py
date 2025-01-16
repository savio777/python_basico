print("Instrução If")

number = 10

if number == 10:
    print("igual a 10")


if number > 10:
    print("maior que 10")
elif number < 10:
    print("menor que 10")
else:
    print("igual a 10")

if number >= 10:
    print("maior ou igual a 10")
elif number <= 10:
    print("menor ou igual a 10")

print("Instrução If exercícios\n")

note1 = int(input("Digite a primira nota: "))

note2 = int(input("Digite a segunda nota: "))

averageNotes = (note1 + note2) / 2

if averageNotes >= 7:
    print("Você está aprovado. Parabéns", averageNotes)
elif averageNotes >= 5:
    print("Você está de exame", averageNotes)
else:
    print("Você não está aprovado", averageNotes)

print("\n", True if "H" in "Hello World" else False)
