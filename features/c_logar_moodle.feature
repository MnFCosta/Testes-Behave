#language: pt
Funcionalidade: Utilizar o Moodle
    '''
    Eu como usuario quero acessar a pagina de alguma
    matéria e marcar tarefas como concluidas
    '''

    Cenario: Fazer login no moodle e marcar tarefas como concluida
    Dado acesso a pagina inicial do Moodle
    Quando faço login no sistema
    E clico no menu Meus Cursos
    E entro na página da matéria Testes de Software
    E me desespero ao ver um trabalho para dia 05/4
    E clico na matéria para retornar a página
    E clico na checkmark para marcar a atividade como concluida
    E dou scroll para o topo da página novamente
    Então retorno a página principal