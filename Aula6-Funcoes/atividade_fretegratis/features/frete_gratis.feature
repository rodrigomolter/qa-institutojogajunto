Funcionalidade: Frete Gratis para as regiões Norte e Nordeste

  Como um cliente da Loja do Joga Junto,
  Eu quero saber se sou elegível para a promoção de frete grátis,
  Para que eu possa poder aproveitar as promoções da Loja do Joga Junto


  Contexto: Cliente na página de carrinho
    Dado que o cliente esta na página de carrinho

  Cenário: CEP válido da região Norte
    Quando ele inserir o CEP da região norte "69050063"
    Então o cliente deve ver a mensagem "Parabéns, você ganhou frete grátis!"

  Cenário: CEP válido da região Nordeste
    Quando ele inserir o CEP da região nordeste "40010000"
    Então o cliente deve ver a mensagem "Parabéns, você ganhou frete grátis!"

  Cenário: CEP válido da região sul
    Quando ele inserir o CEP da região sul "04870470"
    Então o cliente deve ver a mensagem "O valor do frete para 04870470 é R$19,90!"

  Cenário: Teste de CEP com mais de 8 digitos
    Quando ele inserir o CEP invalido "004870470"
    Então o cliente deve ver a mensagem "CEP 004870470 não é um CEP válido. Informe 08 dígitos e utilize apenas números"

  Cenário: Teste de CEP vazio
    Quando ele inserir um CEP vazio
    Então o cliente deve ver a mensagem "CEP  não é um CEP válido. Informe 08 dígitos e utilize apenas números"

  Cenário: Teste de CEP não numérico
    Quando ele inserir o CEP alfanumérico "95010A10"
    Então o cliente deve ver a mensagem "CEP não é um CEP válido. Informe 08 dígitos e utilize apenas números"

  Cenário: Teste de CEP válido mas inexistente
    Quando ele inserir o CEP com a validação válida mas inexistente "00000000"
    Então o cliente deve ver a mensagem "Houve um problema ao consultar o CEP. Certifique-se que o CEP foi digitado corretamente"
