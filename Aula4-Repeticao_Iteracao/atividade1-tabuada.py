"""
Crie a estrutura de uma tabuada para um valor inserido. O resultado deverá ser printado do valor multiplicado de 1 a 10. 
"""
valor = float(input("Tabuada de: "))

for i in range(1,11):
  print(f"{i} x {valor} = {valor * i}")

  