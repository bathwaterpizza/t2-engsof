// Frontend básico para o To-Do List (apenas tarefas)
// Faz requisições para a API Flask e manipula o DOM

document.addEventListener('DOMContentLoaded', () => {
    // Elementos do formulário e lista
    const taskForm = document.getElementById('task-form');
    const taskInput = document.getElementById('task-input');
    const taskList = document.getElementById('tasks');
    const apiUrl = '/api/tasks/';

    // Renderiza uma tarefa na lista
    function renderTask(task) {
        const li = document.createElement('li');
        li.className = 'task-item' + (task.completed ? ' completed' : '');
        li.dataset.id = task.id;

        const checkbox = document.createElement('input');
        checkbox.type = 'checkbox';
        checkbox.checked = task.completed;
        // Alterna status da tarefa
        checkbox.addEventListener('change', () => toggleTask(task.id, !task.completed));

        const label = document.createElement('label');
        label.textContent = task.title;

        const deleteBtn = document.createElement('button');
        deleteBtn.className = 'delete-btn';
        deleteBtn.innerHTML = '🗑️';
        deleteBtn.title = 'Excluir';
        deleteBtn.onclick = () => deleteTask(task.id);

        li.appendChild(checkbox);
        li.appendChild(label);
        li.appendChild(deleteBtn);
        taskList.appendChild(li);
    }

    // Limpa a lista de tarefas
    function clearTasks() {
        taskList.innerHTML = '';
    }

    // Carrega tarefas da API e exibe
    function loadTasks() {
        fetch(apiUrl)
            .then(res => res.json())
            .then(tasks => {
                clearTasks();
                if (tasks.length === 0) {
                    const empty = document.createElement('li');
                    empty.textContent = 'Nenhuma tarefa cadastrada.';
                    empty.style.color = '#888';
                    taskList.appendChild(empty);
                } else {
                    tasks.forEach(renderTask);
                }
            });
    }

    // Adiciona uma nova tarefa via API
    function addTask(title) {
        fetch(apiUrl, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ title })
        })
        .then(res => res.ok ? res.json() : res.json().then(e => Promise.reject(e)))
        .then(() => {
            taskInput.value = '';
            loadTasks();
        })
        .catch(err => alert(err.error || 'Erro ao adicionar tarefa.'));
    }

    // Alterna status de conclusão da tarefa
    function toggleTask(id, completed) {
        fetch(apiUrl + id, {
            method: 'PATCH',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ completed })
        })
        .then(res => res.ok ? res.json() : res.json().then(e => Promise.reject(e)))
        .then(loadTasks)
        .catch(err => alert(err.error || 'Erro ao atualizar tarefa.'));
    }

    // Remove uma tarefa via API
    function deleteTask(id) {
        if (!confirm('Excluir esta tarefa?')) return;
        fetch(apiUrl + id, { method: 'DELETE' })
            .then(res => {
                if (res.status === 204) loadTasks();
                else return res.json().then(e => Promise.reject(e));
            })
            .catch(err => alert(err.error || 'Erro ao excluir tarefa.'));
    }

    // Evento de submit do formulário
    taskForm.addEventListener('submit', e => {
        e.preventDefault();
        const title = taskInput.value.trim();
        if (!title) return;
        addTask(title);
    });

    // Carrega tarefas ao iniciar
    loadTasks();
});
