const API_URL = "http://127.0.0.1:8000/api/v1/articles/";

async function fetchArticles() {
    try {
        const response = await fetch(API_URL);
        const data = await response.json();
        renderTable(data);
    } catch (error) {
        console.error("Ошибка при получении:", error);
    }
}

async function putArticle(id) {
    const newTitle = prompt("Введите НОВЫЙ заголовок статьи:");
    const newContent = prompt("Введите НОВЫЙ контент статьи:");

    if (newTitle === null || newContent === null) return;

    const payload = {
        title: newTitle,
        content: newContent,
    };

    try {
        const response = await fetch(`${API_URL}${id}/`, {
            method: "PUT",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(payload)
        });

        if (response.ok) {
            alert("Статья полностью обновлена!");
            fetchArticles();
        } else {
            const errorData = await response.json();
            console.error("Ошибка от сервера:", errorData);
            alert("Ошибка! Проверь консоль (возможно, не все поля заполнены)");
        }
    } catch (error) {
        console.error("Ошибка PUT запроса:", error);
    }
}

function renderTable(articles) {
    const tbody = document.getElementById("articlesTable");
    tbody.innerHTML = "";

    articles.forEach(article => {
            const row = `
                <tr>
                    <td>${article.id}</td>
                    <td>${article.title}</td>
                    <td>${article.content}</td>
                    <td>${new Date(article.created_at).toLocaleDateString()}</td>
                    <td>
                        <button class="edit" onclick="putArticle(${article.id})">PUT (Заменить всё)</button>
                        <button class="delete" onclick="deleteArticle(${article.id})">Удалить</button>
                    </td>
                </tr>
            `;
        tbody.innerHTML += row;
    });
}

document.getElementById("articleForm").addEventListener("submit", async (e) => {
    e.preventDefault();
    const payload = {
        title: document.getElementById("title").value,
        content: document.getElementById("content").value,
    };

    const response = await fetch(API_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload)
    });

    if (response.ok) {
        e.target.reset();
        fetchArticles();
    }
});

async function deleteArticle(id) {
    if (confirm("Удалить статью?")) {
        const response = await fetch(`${API_URL}${id}/`, { method: "DELETE" });
        if (response.ok) fetchArticles();
    }
}

fetchArticles();

