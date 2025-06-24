#!/bin/bash
echo "=== run todo list ==="

# Verificar se o virtual environment existe
if [ ! -d "venv" ]; then
    echo "Virtual environment não encontrado!"
    echo "Execute primeiro: ./setup.sh"
    exit 1
fi

# Ativar virtual environment
echo "Ativando virtual environment..."
source venv/bin/activate

# Verificar se as dependências estão instaladas
if ! python -c "import flask" 2>/dev/null; then
    echo "Dependências não instaladas!"
    echo "Execute primeiro: ./setup.sh"
    exit 1
fi

echo "Iniciando aplicação Flask..."
echo "Acesse: http://127.0.0.1:5000"
echo "Para parar: Ctrl+C"
echo ""

# Executar aplicação
python app.py
