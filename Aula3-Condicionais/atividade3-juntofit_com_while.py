"""
Na "JUNTOFIT", se um aluno tiver frequência de 21 vezes, sem interrupções, ele ganha um mês de aulas gratuitas para presentear um acompanhante.
Caso contrário, ele não se qualifica para o benefício.

Na catraca de acesso, haverá uma tela voltada para o cliente. Todos os dias, quando ele passar, deve aparecer a mensagem "VOCÊ ESTÁ PARTICIPANDO DA NOSSA PROMO TREINA JUNTO"

Quando ele completar 21 identificações seguidas, deve aparecer a mensagem "UHUU. AGORA VOCÊ PODE PRESENTEAR UM AMIGO OU AMIGA PARA TREINAR COM VOCÊ".

Caso o cliente tenha uma certa frequência, mas falte algum dia, quando retornar, deve aparecer "QUE BOM VER VOCÊ DE VOLTA. A PARTIR DE AGORA INICIAMOS MAIS UMA CONTAGEM DE 21 DIAS PARA A PROMO TREINA JUNTO."
"""

frequencia = 0

# Laço infinito para contabilizar as frequencias, ele se mantem dentro desse bloco de código até chegar em um break;
while True:
  presenca = input("Olá, bem vindo. Você confirma presença hoje? ").lower() #Verifica a presença

  # Se o usuário confirmar a preesnça
  if presenca == "sim":
    # Adiciono mais um dia a frequencia do usuário. Equivalente a frequencia = frequencia + 1
    frequencia +=1
    print("VOCÊ ESTÁ PARTICIPANDO DA NOSSA PROMO TREINA JUNTO")
    print(f"SUA FREQUENCIA É {frequencia}")

  # Se o faltar algum dia
  else:
    # Aqui verifico se ele tem alguma frequencia, equivalente a frequencia > 0
    if frequencia:
      print("QUE BOM VER VOCÊ DE VOLTA. A PARTIR DE AGORA INICIAMOS MAIS UMA CONTAGEM DE 21 DIAS PARA A PROMO TREINA JUNTO.")
    else:
      print("QUE PENA! :(")
    # Zero a sequencia de frequencias dele, pois ele teve uma falta
    frequencia = 0
  
  # Se ele atingir o total de 21 frequencias, então ganhou o bonus
  if frequencia >= 21:
    print("UHUU. AGORA VOCÊ PODE PRESENTEAR UM AMIGO OU AMIGA PARA TREINAR COM VOCÊ")
    # break é para sair do laço infinito, e por consequência encerra o programa
    break

  
