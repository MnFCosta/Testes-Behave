#language: pt
Funcionalidade: Acessar o Youtube
    '''
    Eu como usuario quero acessar o Youtube e ver um video
    '''

    Cenario: Ver video no youtube
    Dado acesso a pagina inicial do Youtube
    Quando clico no campo de busca
    E clico no video
    Então retorno a página principal do Youtube