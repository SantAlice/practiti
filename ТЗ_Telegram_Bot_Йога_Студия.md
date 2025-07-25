# ТЕХНИЧЕСКОЕ ЗАДАНИЕ
## Telegram-бот для йога студии "Пракрити"

### 1. ОБЩЕЕ ОПИСАНИЕ ПРОЕКТА

**Цель проекта:** Автоматизация процесса записи новичков на занятия и управления абонементами в йога студии через Telegram-бот.

**Основные задачи:**
- Обработка заявок с сайта и запись новичков на занятия
- Управление онлайн-абонементами
- Уведомления и напоминания клиентам
- Административная панель для преподавателей и администраторов

### 2. ФУНКЦИОНАЛЬНЫЕ ТРЕБОВАНИЯ

#### 2.1 Модуль записи на занятия

**Пользовательский сценарий:**
1. Пользователь переходит с сайта в Telegram-бот по кнопке
2. Проходит анкетирование:
   - Имя и номер телефона
   - Занимались раньше йогой? (Да/Нет)
   - Хотите поинтенсивней или поспокойней?
   - Когда рассматриваете занятия? (Будни утро/будни вечер/выходные/индивидуально)
3. Получает варианты доступных занятий
4. Выбирает подходящее время
5. Получает информационные материалы (адрес, FAQ, стоимость)

**Автоматические действия системы:**
- Сохранение данных в Google Таблицу
- Отправка уведомления администратору о новой записи
- Напоминание клиенту за день до занятия (утренние) или в день занятия (вечерние)
- После занятия: сообщение с предложением купить абонемент и ссылкой на канал

#### 2.2 Модуль управления абонементами

**Типы абонементов:**
- Пробное занятие — 500руб.
- Разовое занятие — 1100руб.
- Абонемент новичка (4 занятия) — 3200руб.
- Абонемент 4 занятия — 4000руб.
- Абонемент 8 занятий — 7000руб.
- Абонемент 12 занятий — 9000руб.
- Безлимит — 10800руб./месяц

**Срок действия:**
- Все абонементы (кроме безлимита) — 2 месяца
- Безлимит — 1 месяц

**Функционал:**
- Создание абонемента после подтверждения оплаты
- Отслеживание количества оставшихся занятий
- Контроль срока действия
- Напоминания после каждого занятия: "У вас осталось X занятий из Y, абонемент действует до [дата]"
- Напоминание за неделю до окончания срока действия
- Возможность продления абонемента (индивидуально или массово)
- Возможность добавления занятий в подарок

#### 2.3 Информационный модуль

**FAQ и справочная информация:**

**Адрес:**
```
Сокольнический вал 1Б
Ледовый дворец, сектор Б
Огибаете здание слева, вход с торца, лифт справа, как вошли
5 этаж, из лифта направо, дверь с надписью «Облачные врата»
```

**Что взять с собой:**
- Удобная форма одежды (легинсы, футболка/майка)
- Занимаемся босиком
- Все оборудование есть в зале

**Оплата:**
- После урока наличными или переводом
- Ссылка для оплаты: https://www.sberbank.com/sms/pbpn?requisiteNumber=79162565675
- Для других банков: перевод по номеру телефона

**Дополнительно:**
- Ссылка на Telegram-канал: https://t.me/sokolnikiyoga
- Ссылка на сайт: https://prakriti-yoga.ru/
- Кнопка "Связаться с администратором" с переходом в личные сообщения

### 3. АДМИНИСТРАТИВНАЯ ПАНЕЛЬ (ВЕБ-ИНТЕРФЕЙС)

**Функционал для преподавателей и администраторов:**

#### 3.1 Поиск клиентов
- Поиск по имени или номеру телефона
- Просмотр информации о клиенте
- Проверка статуса абонемента

#### 3.2 Управление абонементами
- Регистрация нового абонемента
- Подтверждение оплаты
- Продление абонемента
- Добавление занятий в подарок
- Массовое продление абонементов (для праздников/каникул)

#### 3.3 Управление записями
- Просмотр записей на занятия
- Добавление клиентов с минимальными данными (для разовых посещений)

### 4. ТЕХНИЧЕСКАЯ АРХИТЕКТУРА

#### 4.1 Хранение данных
**Google Таблица со следующими полями:**
- Фамилия, имя
- Номер телефона
- Telegram ID
- Дата первого занятия
- Опыт занятий йогой
- Предпочтения по интенсивности
- Удобное время
- Тип абонемента
- Количество занятий (всего/использовано/осталось)
- Дата покупки абонемента
- Срок действия абонемента
- Комментарии
- Статус (активный/неактивный)

#### 4.2 Интеграции
- Telegram Bot API
- Google Sheets API
- Веб-интерфейс для административной панели

#### 4.3 Уведомления
- Уведомления администратору о новых записях
- Напоминания клиентам о занятиях
- Напоминания об остатке занятий и сроке действия
- Возможность отправки спонтанных сообщений об акциях

### 5. ПОЛЬЗОВАТЕЛЬСКИЕ СЦЕНАРИИ

#### 5.1 Новичок записывается на занятие
1. Переход с сайта → анкетирование → выбор времени → сохранение в таблицу
2. Уведомление админу
3. Напоминание перед занятием
4. После занятия: предложение абонемента + ссылка на канал

#### 5.2 Покупка абонемента
1. Клиент оплачивает у преподавателя
2. Преподаватель/админ подтверждает через веб-панель
3. Создается онлайн-абонемент
4. Начинаются автоматические напоминания

#### 5.3 Проверка абонемента
1. Преподаватель ищет клиента в веб-панели
2. Проверяет статус и остаток занятий
3. Подтверждает или ограничивает доступ

### 6. ДОПОЛНИТЕЛЬНЫЕ ТРЕБОВАНИЯ

#### 6.1 Миграция существующих клиентов
- Возможность добавления существующих клиентов с частично использованными абонементами
- Ручной ввод данных о текущих абонементах

#### 6.2 Тон общения
- Дружелюбный и теплый тон сообщений
- Соответствие духу йога студии
- Детальная проработка текстов сообщений

#### 6.3 Безопасность
- Доступ к административной панели по ссылке (без авторизации на первом этапе)
- В будущем: разграничение ролей администратор/преподаватель

### 7. ОГРАНИЧЕНИЯ ПЕРВОЙ ВЕРСИИ (MVP)

**Не включается в первую версию:**
- ИИ-функционал
- Сложная система авторизации
- Прямое общение администратора через бота
- Автоматическое распознавание чеков
- Интеграция с платежными системами

**Планируется в будущих версиях:**
- Расширенный функционал для постоянных клиентов
- Система лояльности
- Автоматизированные платежи
- Более сложная логика уведомлений

### 8. КРИТЕРИИ ПРИЕМКИ

1. Бот корректно обрабатывает переходы с сайта
2. Анкетирование работает без ошибок
3. Данные корректно сохраняются в Google Таблицу
4. Административная панель позволяет управлять абонементами
5. Уведомления отправляются в нужное время
6. Все информационные материалы отображаются корректно
7. Кнопка связи с администратором работает
8. Возможность миграции существующих клиентов

### 9. КОНТАКТНАЯ ИНФОРМАЦИЯ

**Заказчик:** Йога студия "Пракрити"
**Сайт:** https://prakriti-yoga.ru/
**Telegram-канал:** https://t.me/sokolnikiyoga
**Администратор:** @prakriti_yoga 