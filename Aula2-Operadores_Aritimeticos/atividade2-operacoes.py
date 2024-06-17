"""
Imagine que você está em um processo se seleção para ocupar uma vaga de QA e, para testarem seus conhecimentos sobre OPERADORES, propõem o seguinte:

Desafio: Faça um código que permita, ao inserir um valor, o retorno de 5 outputs, sendo eles:

primeiro output: deve apresentar como resultado o dobro do valor inserido;
segundo output: deve apresentar como resultado o triplo do valor inserido;
terceiro output: deve apresentar como resultado o valor inserido ao quadrado;
quarto output: deve apresentar como resultado a raiz quadrada do valor inserido;
quinto output: deve apresentar como resultado a raíz cúbica do valor inserido.
"""

valor = float(input ("Insira um valor numérico: "))

print(f"Dobro de {valor}: {valor*2}")
print(f"Triplo de {valor}: {valor*3}")
print(f"Quadrado de {valor}: {valor**2}")
print(f"Raiz quadradada de {valor}: {(valor**(1/2)):.2f}")
print(f"Raiz cubica de {valor}: {valor**(1/3):.2f}")