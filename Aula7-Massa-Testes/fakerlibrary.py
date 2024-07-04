"""
Uma função para criar personas, contendo nome, cidade, idade. 
Salve os dados dessas personas em um arquivo CSV.
Suba todos os arquivos para seu repositório.
"""
from faker import Faker
import pandas as pd
import os

def main() -> None:
  df = pd.DataFrame(create_personas(3))
  save_to_csv('personas.csv', df)
  
def create_persona() -> dict:
  fake = Faker('pt_BR')
  data = {
    "nome": fake.name(),
    "cidade": fake.city(),
    "idade": fake.random_int(18, 100)
  }
  return data

def create_personas(number_of_personas: int) -> list:
    return [create_persona() for _ in range(number_of_personas)]

def save_to_csv(file_name: str, dataframe: pd.DataFrame) -> None:
  file_exists = os.path.isfile(file_name)
  dataframe.to_csv(file_name, index=False, mode='a', header=not file_exists)

main()