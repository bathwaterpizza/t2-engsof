# To-Do List Application

## Descrição
Aplicação simples de lista de tarefas desenvolvida como trabalho da disciplina de Engenharia de Software.

## Arquitetura
Este projeto segue os princípios de Clean Architecture, SOLID e Clean Code, organizando o código em camadas bem definidas:

- **Domain**: Entidades e regras de negócio
- **Application**: Casos de uso (use cases)
- **Infrastructure**: Implementações de repositórios e acesso a dados
- **Presentation**: Controllers e rotas da API

## Tecnologias
- Backend: Flask (Python)
- Banco de dados: SQLite
- Frontend: HTML, CSS, JavaScript
- Testes: pytest

## Estrutura do Projeto
```
├── src/
│   ├── domain/          # Entidades e regras de negócio
│   ├── application/     # Casos de uso
│   ├── infrastructure/  # Repositórios e acesso a dados
│   └── presentation/    # Controllers e rotas
├── tests/               # Testes automatizados
├── static/              # Arquivos CSS e JavaScript
├── templates/           # Templates HTML
├── requirements.txt     # Dependências do projeto
├── setup.sh             # Script de setup do ambiente
├── run.sh               # Script para rodar a aplicação
└── app.py               # Ponto de entrada principal
```

## Como executar

### Setup inicial (primeira vez)
```bash
./setup.sh
```

### Executar aplicação
```bash
./run.sh
```

### Manualmente
```bash
source venv/bin/activate
python app.py
```

Acesse: http://127.0.0.1:5000

## Funcionalidades Implementadas

### ✅ Domain Layer (Domínio)
- **Entidade Task**: Modelo principal com validações, suporte a category_id
- **Entidade Category**: Modelo de categoria, com lista de tarefas associadas
- **Exceções customizadas**: TaskValidationError, TaskNotFoundError
- **Interface Database[T]**: Contrato genérico para repositórios

### ✅ Application Layer (Casos de Uso)
- **CreateTaskUseCase**: Criar novas tarefas (com ou sem categoria)
- **GetAllTasksUseCase**: Listar todas as tarefas
- **UpdateTaskUseCase**: Atualizar tarefas (título, descrição, status, categoria)
- **DeleteTaskUseCase**: Remover tarefas
- **CreateCategoryUseCase**: Criar categorias
- **GetAllCategoriesUseCase**: Listar categorias
- **UpdateCategoryUseCase**: Atualizar categorias
- **DeleteCategoryUseCase**: Remover categorias

### ✅ Infrastructure Layer (Infraestrutura)
- **SQLiteTaskDatabase**: Implementação SQLite do repositório de tarefas (persistência em banco de dados)
- **SQLiteCategoryDatabase**: Implementação SQLite do repositório de categorias (persistência em banco de dados)
- **SQLiteBase**: Classe base para gerenciar conexões SQLite
- **DictTaskDatabase**: Implementação em memória do repositório de tarefas (para testes)
- **DictCategoryDatabase**: Implementação em memória do repositório de categorias (para testes)

### ✅ Presentation Layer (API)
- **Rotas RESTful para tarefas**: CRUD completo, aceita e retorna category_id
- **Rotas RESTful para categorias**: CRUD completo

### ✅ Frontend
- **HTML/CSS/JS simples**: CRUD de tarefas e categorias
- **Seleção de categoria ao criar tarefa**
- **Exibição de tarefas agrupadas por categoria**

### ✅ Testes
- Testes unitários para entidade Task e Category
- Testes para todos os casos de uso de Task e Category
- Testes de integração para implementações SQLite
- Testes cobrem category_id e integração entre tarefas e categorias

## Como executar os testes
```bash
# Ativar ambiente virtual
source venv/bin/activate

# Executar todos os testes
pytest

# Executar testes específicos
pytest tests/test_task.py
pytest tests/test_task_use_cases.py
pytest tests/test_category.py
pytest tests/test_category_use_cases.py
pytest tests/test_sqlite_task_database.py
pytest tests/test_sqlite_category_database.py
```

## Documentação e Observações
- **Persistência**: O projeto agora utiliza SQLite para persistência de dados. O banco de dados é criado automaticamente na primeira execução.
- **Arquitetura**: Implementa Clean Architecture com separação clara de responsabilidades entre as camadas.
- **Testes**: Os casos de uso utilizam implementações em memória para isolamento, enquanto testes específicos validam a integração SQLite.
- Código revisado para PEP-8, com docstrings sucintas e comentários explicativos.
- Scripts de setup e execução documentados.
- README atualizado para refletir toda a arquitetura, funcionalidades, instruções de uso, testes e status do projeto.

## Autor
Trabalho desenvolvido para a disciplina de Engenharia de Software - 5º período
