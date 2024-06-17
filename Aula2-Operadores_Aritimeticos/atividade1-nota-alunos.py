"""
Desafio: Fazer um programa que some 4 notas e, no final, tenha a média aritmética dessas notas.

O que seu programa deve conter:

Um input onde cada interação tenha um texto.
No final, seu programa deverá ter o output:
“Olá, Caique! Sua média é: 10 pontos”
"""

import sys

nome = input("Qual o seu nome? ")
try:
  total_notas = int(input("Quantas notas você deseja somar? "))
except ValueError:
  print("Por favor, utilize apenas números!")
  sys.exit()

notas = []
try:
  for i in range(total_notas):
    notas.append(int(input(f"Qual a nota {i+1}? ")))
except ValueError:
  print("Por favor, utilize apenas números!")
  sys.exit()

total = 0
for nota in notas:
  total += nota

print(f"Olá {nome.capitalize()}, sua média é {total/total_notas}.")