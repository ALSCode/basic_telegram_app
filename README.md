# Telegram Mini App - Echo Bot

Простое Telegram Mini App, которое повторяет введенное пользователем сообщение.

## Функциональность

- Ввод текстового сообщения
- Отображение введенного сообщения
- Отправка данных в Telegram бота
- Поддержка темы Telegram
- Адаптивный дизайн

## Использование

1. Разместите файлы на веб-сервере
2. Настройте бота через @BotFather:
   - Используйте команду /newapp
   - Укажите URL, где размещено приложение
   - Добавьте приложение в меню бота

## Структура проекта

- `index.html` - основной файл приложения с пользовательским интерфейсом
- `app.js` - JavaScript код для обработки взаимодействия с Telegram Web App API
- `README.md` - документация

## Технические детали

- Использует Telegram Web App API для интеграции с Telegram
- Поддерживает светлую и темную темы Telegram через CSS переменные
- Адаптивный дизайн для всех устройств
- Обработка отправки через кнопку и клавишу Enter
