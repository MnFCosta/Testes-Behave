#language: pt
Funcionalidade: Cadastrar Procedimento
    '''
    Eu como usuario quero acessar a pagina de procedimentos
    e realizar o cadastro de um novo procedimento
    '''

    Cenario: Cadastrar procedimento
    Dado acesso a pagina inicial do sistema Florence Teste
    Quando Realizo o Login no sistema
    E clico no menu Procedimentos
    E clico no botão novo procedimento
    E insiro dados de um novo procedimento
    E clico em salvar procedimento
    E clico no botão novo item procedimento
    E insiro dados de um item de procedimento
    E clico em salvar item procedimento
    E clico em salvar procedimento novamente
    E clico em voltar para tela procedimento
    Então O procedimento cadastrado deve ser apresentada no primeiro registro da consulta.