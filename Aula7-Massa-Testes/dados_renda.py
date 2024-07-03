"""
com idade maior que 40 anos
com renda maior de 5 mil
com renda maior de 15 mil
"""

import pandas as pd

dados = pd.read_csv('./dados_ficticios.csv')
df = pd.DataFrame(data=dados)

print("Pessoas com idade maior que 40 anos")
print(df[df['idade'] > 40])
print("\n\nPessoas com renda maior que R$ 5.000,00")
print(df[df['renda'] > 5000])
print("\n\nPessoas com renda maior que R$15.000,00")
print(df[df['renda'] > 15000])