def isPar(numero: int) -> bool:
  return numero % 2 == 0

print("BEM VINDO A OLIMPIADA DO CONHECIMENTO")
matricula = int(input("Digite a sua matricula: "))

if isPar(matricula):
  print("VOCÊ ESTÁ NO TIME AZUL")
else:
  print("VOCÊ ESTÁ NO TIME AMARELO")