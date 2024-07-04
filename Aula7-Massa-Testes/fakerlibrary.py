"""
Uma função para criar personas, contendo nome, cidade, idade. 
Salve os dados dessas personas em um arquivo CSV.
Suba todos os arquivos para seu repositório.
"""

from faker import Faker
import json

faker = Faker('pt_BR')

persona = {
  "nome" : faker.name(),
  "idade" : faker.random_int(min=18, max=99),
  "cidade" : faker.city()
}

print(persona)

with open('persona.csv', 'w') as file:
  json.dump(persona, file)