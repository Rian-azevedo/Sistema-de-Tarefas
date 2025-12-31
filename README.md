# Sistema de Gerenciamento de Tarefas

Este projeto é um sistema de gerenciamento de tarefas desenvolvido com Django, com o objetivo de facilitar a organização e o acompanhamento de tarefas.
A aplicação permite cadastrar tarefas, definir seu status e acompanhar quando foram criadas.

 Projeto criado com foco em aprendizado, boas práticas e uso do Django ORM.

# Funcionalidades

  Criar tarefas com título e descrição
  Definir status da tarefa (Pendente ou Concluída)
  Listar tarefas cadastradas
  Registro automático da data de criação
  Organização dos dados utilizando Modelos do Django

# Tecnologias Utilizadas

  Python,
  Django,
  SQLite (banco de dados padrão do Django),
  Django ORM.

# Estrutura do Modelo Principal

O projeto utiliza um modelo chamado Tarefa, responsável por armazenar as informações das tarefas:
  
  Título,
  Descrição,
  Status,
  Data de criação.

O status da tarefa pode ser:
  PENDENTE,
  CONCLUIDA.
