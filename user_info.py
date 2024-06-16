import sys

"""
Faça um programa que capture o nome do usuário, altura em metros, idade e imprima esses dados na tela!
"""

print("Bem vindo ao programa do Squad 4 da Comunidade !\n")

nome = input("Qual o seu nome? ")

altura = input("Qual a sua altura? (em metros) ")
try:
  altura = float(altura)
except ValueError:
  print("Por favor, insira a altura em metros!")
  sys.exit()

idade = (input("E por último, qual a sua idade? "))
try:
  idade = int(idade)
except ValueError:
  print("Por favor, informe a idade utilizando apenas números")
  sys.exit()


print(f" Boa noite, {nome.capitalize()}! Você possui {idade} anos e sua altura é de {altura}m.")