// Frontend para To-Do List com categorias
// Faz CRUD de categorias e tarefas, agrupando tarefas por categoria

document.addEventListener('DOMContentLoaded', () => {
    // Elementos do DOM
    const taskForm = document.getElementById('task-form');
    const taskInput = document.getElementById('task-input');
    const taskListGrouped = document.getElementById('tasks-grouped');
    const categoryForm = document.getElementById('category-form');
    const categoryInput = document.getElementById('category-input');
    const categorySelect = document.getElementById('category-select');
    const apiTasks = '/api/tasks/';
    const apiCategories = '/api/categories/';

    // Carrega categorias e popula o select
    function loadCategories(selectedId = "") {
        fetch(apiCategories)
            .then(res => res.json())
            .then(categories => {
                categorySelect.innerHTML = '<option value="">Sem categoria</option>';
                categories.forEach(cat => {
                    const opt = document.createElement('option');
                    opt.value = cat.id;
                    opt.textContent = cat.name;
                    if (cat.id === selectedId) opt.selected = true;
                    categorySelect.appendChild(opt);
                });
            });
    }

    // Renderiza tarefas agrupadas por categoria
    function renderTasksGrouped(tasks, categories) {
        taskListGrouped.innerHTML = '';
        // Agrupa tarefas por categoriaId
        const grouped = {};
        tasks.forEach(task => {
            const catId = task.category_id || '';
            if (!grouped[catId]) grouped[catId] = [];
            grouped[catId].push(task);
        });
        // Renderiza cada grupo
        categories.forEach(cat => {
            const div = document.createElement('div');
            div.style.marginBottom = '18px';
            const h2 = document.createElement('h2');
            h2.textContent = cat.name;
            h2.style.fontSize = '1.1em';
            h2.style.margin = '12px 0 6px 0';
            div.appendChild(h2);
            const ul = document.createElement('ul');
            ul.style.paddingLeft = '0';
            (grouped[cat.id] || []).forEach(task => ul.appendChild(renderTaskItem(task)));
            if (ul.children.length === 0) {
                const li = document.createElement('li');
                li.textContent = 'Nenhuma tarefa.';
                li.style.color = '#888';
                ul.appendChild(li);
            }
            div.appendChild(ul);
            taskListGrouped.appendChild(div);
        });
        // Tarefas sem categoria
        if (grouped['']) {
            const div = document.createElement('div');
            div.style.marginBottom = '18px';
            const h2 = document.createElement('h2');
            h2.textContent = 'Sem categoria';
            h2.style.fontSize = '1.1em';
            h2.style.margin = '12px 0 6px 0';
            div.appendChild(h2);
            const ul = document.createElement('ul');
            ul.style.paddingLeft = '0';
            grouped[''].forEach(task => ul.appendChild(renderTaskItem(task)));
            div.appendChild(ul);
            taskListGrouped.appendChild(div);
        }
    }

    // Cria um elemento de tarefa
    function renderTaskItem(task) {
        const li = document.createElement('li');
        li.className = 'task-item' + (task.completed ? ' completed' : '');
        li.dataset.id = task.id;
        const checkbox = document.createElement('input');
        checkbox.type = 'checkbox';
        checkbox.checked = task.completed;
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
        return li;
    }

    // Carrega tarefas e categorias e exibe agrupado
    function loadAll() {
        Promise.all([
            fetch(apiTasks).then(res => res.json()),
            fetch(apiCategories).then(res => res.json())
        ]).then(([tasks, categories]) => {
            renderTasksGrouped(tasks, categories);
            loadCategories();
        });
    }

    // Adiciona uma nova tarefa via API
    function addTask(title, categoryId) {
        fetch(apiTasks, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ title, category_id: categoryId || null })
        })
        .then(res => res.ok ? res.json() : res.json().then(e => Promise.reject(e)))
        .then(() => {
            taskInput.value = '';
            loadAll();
        })
        .catch(err => alert(err.error || 'Erro ao adicionar tarefa.'));
    }

    // Alterna status de conclusão da tarefa
    function toggleTask(id, completed) {
        fetch(apiTasks + id, {
            method: 'PATCH',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ completed })
        })
        .then(res => res.ok ? res.json() : res.json().then(e => Promise.reject(e)))
        .then(loadAll)
        .catch(err => alert(err.error || 'Erro ao atualizar tarefa.'));
    }

    // Remove uma tarefa via API
    function deleteTask(id) {
        if (!confirm('Excluir esta tarefa?')) return;
        fetch(apiTasks + id, { method: 'DELETE' })
            .then(res => {
                if (res.status === 204) loadAll();
                else return res.json().then(e => Promise.reject(e));
            })
            .catch(err => alert(err.error || 'Erro ao excluir tarefa.'));
    }

    // Adiciona uma nova categoria via API
    function addCategory(name) {
        fetch(apiCategories, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ name })
        })
        .then(res => res.ok ? res.json() : res.json().then(e => Promise.reject(e)))
        .then(() => {
            categoryInput.value = '';
            loadAll();
        })
        .catch(err => alert(err.error || 'Erro ao adicionar categoria.'));
    }

    // Evento de submit do formulário de tarefa
    taskForm.addEventListener('submit', e => {
        e.preventDefault();
        const title = taskInput.value.trim();
        const categoryId = categorySelect.value;
        if (!title) return;
        addTask(title, categoryId);
    });

    // Evento de submit do formulário de categoria
    categoryForm.addEventListener('submit', e => {
        e.preventDefault();
        const name = categoryInput.value.trim();
        if (!name) return;
        addCategory(name);
    });

    // Inicializa carregando tudo
    loadAll();
});
