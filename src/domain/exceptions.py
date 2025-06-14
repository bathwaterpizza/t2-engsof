"""
Exceções customizadas da camada de domínio
"""


class DomainError(Exception):
    """Exceção base para erros de domínio"""

    pass


class TaskValidationError(DomainError):
    """Erro de validação de tarefa"""

    pass


class TaskNotFoundError(DomainError):
    """Erro quando uma tarefa não é encontrada"""

    pass
