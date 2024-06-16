import sys

"""
Faça um programa que capture o nome do usuário, altura em metros, idade e imprima esses dados na tela!
"""

print("Bem vindo ao programa do Squad 4 da Comunidade !\n")

nome = input("Qual o seu nome? ")
try:
  altura = float(input("Qual a sua altura? (em metros) "))
  idade = int(input("Qual a sua idade? "))
  nota_um = int(input("Qual nota você tirou no PRIMEIRO teste? "))
  nota_dois = int(input("E por último, qual nota você tirou no SEGUNDO teste? "))
  total = nota_um + nota_dois
  media = total/2
except ValueError:
  print("Por favor, utilize apenas números!")
  sys.exit()



print(f"\nBoa noite, {nome.capitalize()}! Você possui {idade} anos e sua altura é de {altura}m.")
print(f"Suas notas sommadas dão um total de {total} pontos e uma media de {media}")