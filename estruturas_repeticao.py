print("Estrutura de repetição while")

number = 0

while number <= 10:
    print(number)
    number += 1

print("\n")

while number > -1:
    print(number)
    number -= 1

print(number)

days = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]

print("\nEstrutura de repetição for")

for day in days:
    print(day)

for item in range(10):
    print(item, end=" ")

print("\n")

for item in range(7, 21):
    print(item, end=" ")

print("\n")

for item in range(5, 21, 5):
    print(item, end=" ")


print("\n")

for item in range(4, 21, 5):
    print(item, end=" ")

print("\nEstrutura de repetição map")


def getLenghtWords(word):
    return len(word)


listLenghtWords = list(map(getLenghtWords, days))

print(listLenghtWords)

print(sum(map(lambda x: x, range(30))))
