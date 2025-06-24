# Afazeres - Aplicação To-Do List

## Descrição
Aplicação simples de lista de tarefas desenvolvida como trabalho da disciplina de Engenharia de Software (INF1041) em 2025.1.

## Arquitetura
Este projeto segue os princípios de Clean Architecture, SOLID e Clean Code, organizando o código em camadas bem definidas:

- **Domain**: Entidades e regras de negócio
- **Application**: Casos de uso (use cases)
- **Infrastructure**: Implementações de repositórios e acesso a dados
- **Presentation**: Controllers e rotas da API

O código fonte segue o padrão PEP-8.

```
├── src/
│   ├── domain/          # Entidades e regras de negócio
│   ├── application/     # Casos de uso
│   ├── infrastructure/  # Persistência
│   └── presentation/    # Controllers e rotas
├── tests/               # Testes unitários
├── static/              # CSS/JS
├── templates/           # HTML
├── requirements.txt     # Dependências do projeto
├── setup.sh             # Script de setup do ambiente
├── run.sh               # Script para rodar a aplicação
└── app.py               # Main
```

## Tecnologias
- Backend: Flask (Python)
- Banco de dados: SQLite
- Frontend: HTML, CSS, JavaScript
- Testes: pytest

## Funcionalidades

- **Domínio**: Entidades Task e Category com validações, exceções customizadas e interface genérica para persistência.
- **Casos de uso**: CRUD completo para tarefas e categorias, incluindo associação de tarefas a categorias.
- **Infra**: Repositórios com implementações em SQLite ou dicionário em memória.
- **API**: Rotas para tarefas e categorias.
- **Frontend**: Interface simples em HTML, CSS e JavaScript para gerenciar tarefas e categorias, com seleção e exibição por categoria.
- **Testes**: Testes unitários para entidades e casos de uso

## Como executar a aplicação

### 1. Setup inicial
```bash
./setup.sh
```

### 2. Executar
```bash
./run.sh
```

### 3. Acessar http://127.0.0.1:5000

## Como executar os testes

### 1. Ativar venv

```bash
source venv/bin/activate
```

### 2. Executar todos os testes
```bash
pytest
```
