"""
A dona de um PETSHOP quer criar um programa para calcular a idade dos cachorros de seus clientes em "anos de cachorro". Como os pets envelhecem de maneira diferente dos humanos - cada ano humano corresponde a 7 do Cachorro.

Desafio: Crie um programa Python que calcule a idade de cachorro com base na idade humana.

O que seu programa deve conter:

Solicitar ao usuário a idade humana do pet (um número inteiro).
Calcular a idade do pet, levando em consideração que cada ano da idade humana corresponde a 7.
Exibir a idade do pet ao usuário.
Além disso, ela deseja calcular, a cada 12 meses, o lucro obtido por banho e por cachorro. 

VALORES POR BANHO X CUSTO POR BANHO

Cachorro de grande porte: BANHO: R$75,00 | CUSTO: R$20,00
Cachorro de médio porte: BANHO: R$60,00 | CUSTO: 15,00
Cachorro de pequeno porte: BANHO: R$50,00 | CUSTO: R$5,00
Exemplo: Se um animal de grande porte tomar 10 banhos em 12 meses, no final, o programa deve imprimir a seguinte informação:

Olá, Tuco tem 35 anos e nos últimos 12 meses o lucro com este animal foi de R$550,00
"""

print("Olá, bem vindo ao PetShop Amor de Bicho")
nome = input("Qual o nome do pet? ").capitalize()
idade = int(input(f"Quantos anos o/a {nome} possui? "))
porte = input(f"Qual o porte do/da {nome} (Utilize P, M ou G)? ")
banhos = int(input(f"Quantos banhos o banho tomou nos últimos 12 meses? "))

valores = {
  "g": {
    "banho": 75,
    "custo": 20
  },
  "m": {
    "banho": 60,
    "custo": 15
  },
  "p": {
    "banho": 50,
    "custo": 5
  }
}

idade_cachorro = idade*7
valores_cachorro = valores[porte.lower()]
lucro = (valores_cachorro["banho"]*banhos) - (valores_cachorro["custo"]*banhos)

print(f"Olá, {nome} tem {idade_cachorro} anos e nos últimos 12 meses o lucro com este animal foi de R${lucro:.2f}")

