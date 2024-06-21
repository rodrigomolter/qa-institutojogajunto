"""
Na "FashionStyle", para um cliente obter 10% de desconto em suas compras, a compra deve ser de pelo menos R$250,00 e para obter 30%, a compra deve ser acima de R$500,00.
Caso contrário, nenhum desconto é aplicado.

No caixa, haverá uma tela voltada para o cliente. Ao passar o produto, caso cumpra o requisito da promoção, aparecerá a mensagem:

Caso o cliente não cumpra o requisito, deve aparecer "POXA, FALTA POUCO PARA VOCÊ GANHAR 10% DE DESCONTO EM SUA COMPRA."

Caso o cliente faça uma compra acima de R$250,00 "PARABÉNS. VOCÊ GANHOU 10% DE DESCONTO, MAS PODE GANHAR 30% SE SUA COMPRA FOR ACIMA DE R$500,00"

Caso o cliente faça uma compra acima de R$500,00 "PARABÉNS. VOCÊ GANHOU SUPER DESCONTO DE 30%"
"""

# print("Bem vindo a FashionStyle")
# valor = int(input("Qual o valor da compra? "))
# desconto = 0
# if valor >= 500:
#   print("PARABÉNS. VOCÊ GANHOU SUPER DESCONTO DE 30%")
#   desconto = 0.3
#   print()
# elif valor >= 250:
#   desconto = 0.1
#   print("PARABÉNS. VOCÊ GANHOU 10% DE DESCONTO, MAS PODE GANHAR 30% SE SUA COMPRA FOR ACIMA DE R$500,00")
#   print(f"FALTA {500-valor} para ganhar 30% de desconto")
# else:
#   print("POXA, FALTA POUCO PARA VOCÊ GANHAR 10% DE DESCONTO EM SUA COMPRA.")
#   print(f"Adquire mais {250-valor}")

valor_compra = float(input("Informe o valor da sua compra para verificar elegibilidade para desconto: "))

if valor_compra > 500.00:
    desconto = valor_compra*0.3
    print("PARABÉNS. VOCÊ GANHOU SUPER DESCONTO DE 30%.")
    print(f"O SEU DESCONTO É DE R${desconto:.2f}")
elif valor_compra >= 250.00:
    desconto = valor_compra*0.1
    print("PARABÉNS. VOCÊ GANHOU 10% DE DESCONTO, MAS PODE GANHAR 30% SE SUA COMPRA FOR ACIMA DE R$500,00.")
    print(f"O SEU DESCONTO É DE R${desconto:.2f}")
else:
    desconto = 0
    print("POXA, FALTA POUCO PARA VOCÊ GANHAR 10% DE DESCONTO EM SUA COMPRA.")

print(f"O TOTAL DA COMPRA É R${(valor_compra-desconto):.2f}")