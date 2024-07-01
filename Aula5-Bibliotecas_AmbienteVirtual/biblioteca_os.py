import os
import requests
import json

nome_cep_integrantes = {
  "Rodrigo":"93800156",
  "Julia":"03206020",
  "Diogo":"30110001",
  "George": "40010000",
  "Isadora": "40010000",
  "Vitória": "03206020"
}

squad = {}
for nome, cep in nome_cep_integrantes.items():
  response = requests.get(f"https://viacep.com.br/ws/{cep}/json")
  consulta = response.json()
  print(f"{nome} mora em {consulta['localidade']}")
  squad[nome] = {
    "CEP": cep,
    "CIDADE": consulta['localidade'],
    "ESTADO": consulta['uf'],
    "DDD": consulta['ddd']
  }

os.makedirs("fixtures", exist_ok=True)
with open('fixtures/squad.json', 'w') as file:
  json.dump(squad, file, ensure_ascii=True)