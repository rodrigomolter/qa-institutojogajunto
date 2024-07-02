import pandas as pd

pessoas = {
  "nome": ["Michael", "Pam", "Jim", "Dwight", "Kevin", "Andy", "Kelly"],
  "idade": [41, 26, 26, 37, 36, 32, 26],
  "cidade": ["Salvador", "Recife", "Recife", "Recife", "Salvador", "São Paulo", "Manaus"]
}

df = pd.DataFrame(data=pessoas)

print(df[df["cidade"] == "Recife"])