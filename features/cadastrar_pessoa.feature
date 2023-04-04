#language: pt
Funcionalidade: Cadastrar Pessoa
    '''
    Eu como usuario quero acessar a pagina de pessoas
    e realizar o cadastro de uma nova pessoa
    '''

    Cenario: Cadastrar pessoa
    Dado acesso a pagina inicial do Moodle
    Quando faço login no sistema
    E clico no menu Pessoas
    E clico no botão novo
    E insiro dados de uma nova pessoa
    E clico em salvar
    E clico em voltar
    Então A pessoa cadastrada deve ser apresentada no primeiro registro da consulta.