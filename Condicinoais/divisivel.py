numero = int(input("Qual o seu nuúmero -> "))
if (numero % 2) == 0 and (numero % 3) == 0:
    print("Seu número é divicivel")
else:
    print ("O número não é divicivel por 2 nem 3")

idade = int(input("Qual sua idade -> "))
if idade < 18:
    print("Vocẽ é menor de idade -> ")
else:
    print("Vocẽ é maior de idade -> ")

numero_1 = int(input("Qual seu número -> "))
numero_2 = int(input("Qual o seu segundo número -> "))
if numero_1 + numero_2 > 100:
    print("È maior que cem")
else:
    print("Não é maior que cem")

lado_1 = int(input("Dê seu primeiro lado -> "))
lado_2 = int(input("Dê seu segundo número -> "))
lado_3 = int(input("Dê seu terceiro número -> "))
if lado_1 + lado_2 > lado_3:
    print("`È maior que o terceiro")
if lado_1 == lado_2 == lado_3:
    print("Equilátero")
if lado_1 == lado_2 != lado_3:
    print("Isósceles")
if lado_1 != lado_2 != lado_3:
    print("Escaleno")
else:
    print("Nenhum")

