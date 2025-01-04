let tg = window.Telegram.WebApp;

// Инициализация Telegram Web App
tg.expand();

// Функция для отправки сообщения
function sendMessage() {
    const messageInput = document.getElementById('messageInput');
    const resultDiv = document.getElementById('result');
    
    if (messageInput.value.trim() !== '') {
        // Показываем сообщение в результате
        resultDiv.innerHTML = `
            <strong>Ваше сообщение:</strong><br>
            ${messageInput.value}
        `;
        
        // Отправляем данные в Telegram
        tg.sendData(JSON.stringify({
            message: messageInput.value
        }));
        
        // Очищаем поле ввода
        messageInput.value = '';
    }
}

// Обработка нажатия Enter в поле ввода
document.getElementById('messageInput').addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        sendMessage();
    }
});

// Устанавливаем тему при загрузке
document.addEventListener('DOMContentLoaded', function() {
    tg.ready();
});
