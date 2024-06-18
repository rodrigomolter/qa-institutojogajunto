"""
- Crie uma tupla com 5 dados
- Altere a tupla para uma lista
- Insira 2 dados extras a essa lista
- Remova o primeiro dado da lista
- Remova o último dado da lista
- Faça um print com o primeiro dado da lista
- Faça um print com a quantidade de dados da lista
- Crie um dicionário com os seguintes dados:
- Nome, Idade, Profissão
- Imprima somente o valor contido na chave Nome do dicionário
"""

# Crie uma tupla com 5 dados
tupla = ('Maça', 'Abacaxi', 'Pera', 'Pessego', 'Kiwi')
# Altere a tupla para uma lista
lista = list(tupla)

# Insira 2 dados extras a essa lista
lista.append('Melencia')
lista.append('Uva')

# Remova o primeiro dado da lista
lista.pop(0)
 # Remova o último dado da lista
lista.pop()

# Faça um print com o primeiro dado da lista
print(f"Primeiro elemento da lista: {lista[0]}")
 # Faça um print com a quantidade de dados da lista
print(f"Tamanho da lista: {len(lista)}")

# Crie um dicionário com os seguintes dados:
pessoa = {
  "nome": "Rodrigo",
  "idade": 29,
  "profissão": "QA"
}

# Imprima somente o valor contido na chave Nome do dicionário
print(f"Nome: {pessoa['nome']}")