idade = int(input("Boa noite senhor, qual a sua idade? "))

if idade > 18:
  print("Indivíduo possui idade mínima para dirigir")
elif idade >= 17:
  print("Indivíduo tem entre 17 e 18 anos e ainda NÃO está apto para dirigir")
else:
  print("Indivíduo NÃO possui idade mínima para dirigir")
