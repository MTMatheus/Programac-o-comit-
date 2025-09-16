numero = int(input("Informe um número -> "))
fat = 1

for n in range(1, numero + 1):
    fat *= n
    print(fat)
