import requests

nome_cep_integrantes = {
  "Rodrigo":"93800156",
  "Julia":"03206020",
  "Diogo":"30110001",
  "George": "40010000",
  "Isadora": "40010000",
  "Vitória": "03206020"
}

for nome, cep in nome_cep_integrantes.items():
  response = requests.get(f"https://viacep.com.br/ws/{cep}/json")
  consulta = response.json()
  print(f"{nome} mora em {consulta['localidade']}")