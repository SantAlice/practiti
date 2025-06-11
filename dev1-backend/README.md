# 🔵 РАЗРАБОТЧИК 1 - BACKEND + TELEGRAM BOT

## 🎯 ЗОНА ОТВЕТСТВЕННОСТИ

### - Backend Developer + Bot Specialist
- **Backend API сервисы** - бизнес-логика приложения
- **Telegram Bot** - анкетирование, уведомления, информация
- **Google Sheets интеграция** - хранение и управление данными
- **Система напоминаний** - автоматические уведомления клиентам

---

## 📚 ОБЯЗАТЕЛЬНОЕ ЧТЕНИЕ

### Перед КАЖДОЙ ИИ-сессией:
1. 📋 **`/dev1-backend/cursor-rules.md`** - правила для ИИ
2. 🏗️ **`/dev1-backend/architecture.md`** - backend архитектура  
3. 🎯 **`/dev1-backend/session-plan.md`** - план сессий
4. 📝 **Соответствующий шаблон из `/dev1-backend/templates/`**

---

## 🚀 БЫСТРЫЙ СТАРТ

### 1. Настройка окружения
```bash
# Клонирование проекта
git clone <repo>
cd practiti

# Создание виртуального окружения
python -m venv backend_env
source backend_env/bin/activate  # Linux/Mac
# backend_env\Scripts\activate   # Windows

# Установка зависимостей
cd backend
pip install -r requirements.txt
```

### 2. Конфигурация
```bash
# Копирование переменных окружения
cp .env.example .env

# Настройка обязательных переменных:
# TELEGRAM_BOT_TOKEN=your_bot_token
# GOOGLE_SHEETS_ID=your_sheet_id
# GOOGLE_CREDENTIALS_PATH=path_to_credentials.json
```

### 3. Первый запуск
```bash
# Тестирование Google Sheets подключения
python scripts/test_sheets_connection.py

# Запуск бота (для тестирования)
python src/main.py
```

---

## 📅 ПЛАН СЕССИЙ (12 сессий)

### 🏗️ ФАЗА 1: ФУНДАМЕНТ (4 сессии)
- **B1:** Настройка проекта и модели данных
- **B2:** Google Sheets репозиторий 
- **B3:** ClientService бизнес-логика
- **B4:** Базовый Telegram Bot

### 🎯 ФАЗА 2: ОСНОВНАЯ ЛОГИКА (5 сессий)
- **B5:** Анкетирование новичков (State Machine)
- **B6:** SubscriptionService (абонементы)
- **B7:** NotificationService (уведомления)
- **B8:** Информационные команды бота
- **B9:** REST API endpoints

### 💰 ФАЗА 3: АВТОМАТИЗАЦИЯ (2 сессии)
- **B10:** Система напоминаний (APScheduler)
- **B11:** Post-class автоматизация

### 🚀 ФАЗА 4: ФИНАЛИЗАЦИЯ (1 сессия)
- **B12:** Тестирование и оптимизация

---

## 🔄 WORKFLOW С GIT

### Ежедневная работа:
```bash
# Начало дня
git checkout develop
git pull origin develop

# Новая фича
git checkout -b feature/session-B{N}-description

# Работа...

# Завершение сессии
git add .
git commit -m "feat(backend): описание фичи

- Подробное описание изменений
- Добавленные тесты
- Обновленная документация"

git push origin feature/session-B{N}-description
# Создать Pull Request в develop
```

### Синхронизация с Frontend:
- **После B4:** Базовая интеграция проверена
- **После B9:** API готово для фронтенда
- **После B11:** Финальная интеграция

---

## 🎯 КРИТЕРИИ КАЧЕСТВА

### ✅ Сессия готова, если:
- [ ] Код соответствует архитектуре
- [ ] Все тесты написаны и проходят
- [ ] Логирование настроено
- [ ] Обработка ошибок реализована
- [ ] API документация обновлена
- [ ] Type hints добавлены

### 🚨 СТОП-ФАКТОРЫ:
- ❌ Нарушение слоевой архитектуры
- ❌ Отсутствие тестов
- ❌ Хардкод конфигурации
- ❌ Прямые импорты репозиториев в handlers

---

## 📊 СТЕК ТЕХНОЛОГИЙ

### Backend
- **Python 3.9+** - основной язык
- **FastAPI** - REST API фреймворк
- **python-telegram-bot** - Telegram API
- **Pydantic** - валидация данных
- **APScheduler** - планировщик задач

### Интеграции
- **Google Sheets API** - основное хранилище
- **Telegram Bot API** - интерфейс пользователя

### Тестирование
- **pytest** - unit и integration тесты
- **pytest-asyncio** - тестирование async кода
- **unittest.mock** - мокирование зависимостей

---

## 🔧 ПОЛЕЗНЫЕ КОМАНДЫ

```bash
# Форматирование кода
black src/
isort src/

# Проверка типов
mypy src/

# Линтер
flake8 src/

# Тесты
pytest tests/ -v
pytest tests/ --cov=src

# Запуск бота в dev режиме
python src/main.py --dev

# Генерация API документации
python scripts/generate_api_docs.py
```

---

## 📞 ПОДДЕРЖКА

### При возникновении проблем:
1. Проверить файлы в `/dev1-backend/troubleshooting/`
2. Просмотреть логи в `logs/backend.log`
3. Проверить статус интеграций с Google Sheets
4. Связаться с вторым разработчиком для координации

### Полезные ресурсы:
- [python-telegram-bot документация](https://python-telegram-bot.readthedocs.io/)
- [FastAPI документация](https://fastapi.tiangolo.com/)
- [Google Sheets API](https://developers.google.com/sheets/api)

---

**Принцип: Каждая ИИ-сессия должна завершиться рабочим, протестированным кодом!** 