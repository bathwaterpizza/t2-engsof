#!/bin/bash

# Script para configurar o ambiente do projeto To-Do List

echo "=== setup todo list ==="

# Criar virtual environment se não existir
if [ ! -d "venv" ]; then
    echo "Criando virtual environment..."
    python3 -m venv venv
fi

# Ativar virtual environment
echo "Ativando virtual environment..."
source venv/bin/activate

# Instalar dependências
echo "Instalando dependências..."
pip install -r requirements.txt

echo "✅ Setup concluído!"
echo ""
echo "Para executar o projeto:"
echo "  ./run.sh"
