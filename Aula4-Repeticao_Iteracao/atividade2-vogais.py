print("Bem vindo a calculadora de vogais da Squad 4!")
palavra = input("Qual a palavra que você quer contar as vogais: ")

qtde_de_vogais = 0 
vogais = ('a', 'e', 'i', 'o', 'u')

qtde_de_vogais = sum(1 for letra in palavra.lower() if letra in vogais)

print(f"O número de vogais na palavra é {qtde_de_vogais}")



