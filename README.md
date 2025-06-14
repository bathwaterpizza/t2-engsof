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
└── requirements.txt     # Dependências do projeto
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
- **Entidade Task**: Modelo principal com validações
- **Exceções customizadas**: TaskValidationError, TaskNotFoundError
- **Interface TaskDatabase**: Contrato para repositórios

### ✅ Application Layer (Casos de Uso)
- **CreateTaskUseCase**: Criar novas tarefas
- **GetAllTasksUseCase**: Listar todas as tarefas
- **UpdateTaskUseCase**: Atualizar tarefas (título, descrição, status)
- **DeleteTaskUseCase**: Remover tarefas

### ✅ Infrastructure Layer (Infraestrutura)
- **DictTaskDatabase**: Implementação em memória do repositório

### ✅ Testes
- Testes unitários para entidade Task
- Testes para todos os casos de uso

## Como executar os testes
```bash
# Ativar ambiente virtual
source venv/bin/activate

# Executar todos os testes
pytest

# Executar testes específicos
pytest tests/test_task.py
pytest tests/test_use_cases.py
```

## Autor
Trabalho desenvolvido para a disciplina de Engenharia de Software - 5º período
