#language: pt

Funcionalidade: Envio de dados ao formulário
    Cenário: Envio de dados com assunto quero ser facilitador

        Dado que estou na página do instituto joga junto
        Quando preencho o formulário de contato
        E aperto o botão de enviar
        Então os dados são recebidos com sucesso