import requests

ENDPOINT = "https://viacep.com.br/ws"
FORMATO_RETORNO_API = "json"

def main():
  cep = input("Informe seu CEP: ")
  if is_cep_valid(cep):
    if tem_frete_gratis(cep):
      print("Parabéns, você ganhou frete grátis!")
    else:
      print(f"O valor do frete para {cep} é R$19,90")
  else:
    print("CEP INVALIDO")

def tem_frete_gratis(cep: str) -> bool:
  dados = consulta_cep(cep)
  return is_norte_nordeste(dados['uf'])

def consulta_cep(cep: str) -> dict:
  response = requests.get(f"{ENDPOINT}/{cep}/{FORMATO_RETORNO_API}")
  return response.json()

def is_norte_nordeste(uf: str) -> bool:
  UF_NORTE_NORDESTE = ("AC", "AP", "AM", "PA", "RO", "RR", "TO", "AL", "BA", "CE", "MA", "PB", "PE", "PI", "RN", "SE")
  return uf.upper() in UF_NORTE_NORDESTE

def is_cep_valid(cep):
  return len(cep) == 8

if __name__ == "__main__":
  main()