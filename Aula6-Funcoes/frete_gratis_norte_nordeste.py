import requests

ENDPOINT = "https://viacep.com.br/ws"
FORMATO_RETORNO_API = "json"

def main():
  cep: str = input("Informe seu CEP: ")
  if is_cep_valid(cep):
    if tem_frete_gratis(cep):
      print("Parabéns, você ganhou frete grátis!")
    else:
      print(f"O valor do frete para {cep} é R$19,90")
  else:
    print(f"CEP {cep} NÃO É UM CEP VALIDO")

def tem_frete_gratis(cep: str) -> bool:
  dados: dict = consulta_cep(cep)
  return is_norte_nordeste(dados['uf'])

def consulta_cep(cep: str) -> dict:
  response: requests.Response = requests.get(f"{ENDPOINT}/{cep}/{FORMATO_RETORNO_API}")
  return response.json()

def is_norte_nordeste(uf: str) -> bool:
  UF_NORTE_NORDESTE = ("AC", "AP", "AM", "PA", "RO", "RR", "TO", "AL", "BA", "CE", "MA", "PB", "PE", "PI", "RN", "SE")
  return uf.upper() in UF_NORTE_NORDESTE

def is_cep_valid(cep: str) -> bool:
  return len(cep) == 8 and cep.isdigit()

if __name__ == "__main__":
  main()