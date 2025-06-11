# 🔴 РАЗРАБОТЧИК 2 - FRONTEND + INTEGRATION

## 🎯 ЗОНА ОТВЕТСТВЕННОСТИ

### Frontend Developer + Integration Specialist
- **React админ-панель** - интерфейс для управления студией
- **UI/UX компоненты** - дизайн-система и пользовательский опыт
- **API интеграция** - связь с backend сервисами
- **Деплой и финализация** - подготовка к продакшну

---

## 📚 ОБЯЗАТЕЛЬНОЕ ЧТЕНИЕ

### Перед КАЖДОЙ ИИ-сессией:
1. 📋 **`/dev2-frontend/cursor-rules.md`** - правила для ИИ
2. 🏗️ **`/dev2-frontend/architecture.md`** - frontend архитектура  
3. 🎯 **`/dev2-frontend/session-plan.md`** - план сессий
4. 📝 **Соответствующий шаблон из `/dev2-frontend/templates/`**

---

## 🚀 БЫСТРЫЙ СТАРТ

### 1. Настройка окружения
```bash
# Клонирование проекта
git clone <repo>
cd practiti

# Установка Node.js зависимостей
cd frontend
npm install

# Проверка TypeScript
npm run type-check
```

### 2. Конфигурация
```bash
# Копирование переменных окружения
cp .env.example .env.local

# Настройка обязательных переменных:
# REACT_APP_API_URL=http://localhost:8000
# REACT_APP_ENVIRONMENT=development
```

### 3. Первый запуск
```bash
# Запуск в dev режиме
npm start

# Запуск Storybook (компоненты)
npm run storybook

# Тестирование
npm test
```

---

## 📅 ПЛАН СЕССИЙ (13 сессий)

### 🏗️ ФАЗА 1: ФУНДАМЕНТ (4 сессии)
- **F1:** React проект и структура
- **F2:** UI Kit и дизайн-система
- **F3:** API клиент и типы
- **F4:** Layout и навигация

### 🎯 ФАЗА 2: ОСНОВНЫЕ КОМПОНЕНТЫ (5 сессий)
- **F5:** Поиск и список клиентов
- **F6:** Карточка клиента
- **F7:** Управление абонементами
- **F8:** Dashboard аналитика
- **F9:** Быстрые действия

### 💰 ФАЗА 3: ПРОДВИНУТЫЕ ФИЧИ (2 сессии)
- **F10:** Календарь и расписание
- **F11:** Отчеты и экспорт

### 🚀 ФАЗА 4: ФИНАЛИЗАЦИЯ (2 сессии)
- **F12:** UI/UX полировка
- **F13:** Деплой и документация

---

## 🔄 WORKFLOW С GIT

### Ежедневная работа:
```bash
# Начало дня
git checkout develop
git pull origin develop

# Новая фича
git checkout -b feature/session-F{N}-description

# Работа...

# Завершение сессии
git add .
git commit -m "feat(frontend): описание фичи

- Детальное описание изменений
- Добавленные компоненты/тесты
- Обновленная документация"

git push origin feature/session-F{N}-description
# Создать Pull Request в develop
```

### Синхронизация с Backend:
- **После F3:** API типы синхронизированы
- **После F5:** Интеграция с клиентскими API
- **После F7:** Интеграция с абонементными API
- **После F11:** Полная интеграция

---

## 🎯 КРИТЕРИИ КАЧЕСТВА

### ✅ Сессия готова, если:
- [ ] Компоненты типизированы (TypeScript)
- [ ] Responsive дизайн работает
- [ ] Тесты написаны и проходят
- [ ] ESLint проверки пройдены
- [ ] Storybook обновлен
- [ ] API интеграция работает

### 🚨 СТОП-ФАКТОРЫ:
- ❌ Компоненты больше 300 строк
- ❌ Inline стили
- ❌ Прямые API вызовы в компонентах
- ❌ Any типы в TypeScript
- ❌ Отсутствие accessibility

---

## 📊 СТЕК ТЕХНОЛОГИЙ

### Frontend Core
- **React 18** - основной фреймворк
- **TypeScript** - типизация
- **React Router** - роутинг
- **Material-UI** - UI библиотека
- **Emotion/styled-components** - стилизация

### State Management
- **React Query** - серверное состояние
- **Zustand** - локальное состояние
- **React Hook Form** - формы

### Development Tools
- **Vite** - bundler
- **Storybook** - разработка компонентов
- **Jest + Testing Library** - тестирование
- **ESLint + Prettier** - линтинг

### API & Integration
- **Axios** - HTTP клиент
- **React Query** - кеширование API
- **MSW** - мокирование API для тестов

---

## 🔧 ПОЛЕЗНЫЕ КОМАНДЫ

```bash
# Разработка
npm start              # Dev сервер
npm run storybook      # Storybook
npm run type-check     # TypeScript проверка

# Тестирование
npm test               # Unit тесты
npm run test:coverage  # Покрытие тестами
npm run test:e2e       # E2E тесты

# Качество кода
npm run lint           # ESLint
npm run lint:fix       # Автофикс ESLint
npm run format         # Prettier

# Сборка
npm run build          # Production сборка
npm run preview        # Превью production

# Анализ
npm run analyze        # Анализ bundle
npm run lighthouse     # Performance audit
```

---

## 🎨 ДИЗАЙН-СИСТЕМА

### Цветовая палитра:
```css
:root {
  /* Primary - йога тематика */
  --color-primary: #4A90E2;
  --color-primary-light: #6FA8EA;
  --color-primary-dark: #357ABD;
  
  /* Secondary - теплые тона */
  --color-secondary: #F5A623;
  --color-secondary-light: #F7B955;
  --color-secondary-dark: #E69500;
  
  /* Neutral */
  --color-neutral-50: #F9FAFB;
  --color-neutral-100: #F3F4F6;
  --color-neutral-500: #6B7280;
  --color-neutral-900: #111827;
  
  /* Status */
  --color-success: #10B981;
  --color-warning: #F59E0B;
  --color-error: #EF4444;
}
```

### Typography:
```css
/* Заголовки */
--font-heading: 'Inter', sans-serif;
--font-body: 'Inter', sans-serif;

/* Размеры */
--text-xs: 0.75rem;
--text-sm: 0.875rem;
--text-base: 1rem;
--text-lg: 1.125rem;
--text-xl: 1.25rem;
--text-2xl: 1.5rem;
```

### Spacing:
```css
--space-1: 0.25rem;  /* 4px */
--space-2: 0.5rem;   /* 8px */
--space-4: 1rem;     /* 16px */
--space-6: 1.5rem;   /* 24px */
--space-8: 2rem;     /* 32px */
--space-12: 3rem;    /* 48px */
```

---

## 📱 RESPONSIVE DESIGN

### Breakpoints:
```css
/* Mobile First подход */
--breakpoint-sm: 640px;   /* Планшет portrait */
--breakpoint-md: 768px;   /* Планшет landscape */
--breakpoint-lg: 1024px;  /* Desktop */
--breakpoint-xl: 1280px;  /* Large desktop */
```

### Grid система:
```css
.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 1rem;
}

@media (min-width: 640px) {
  .container { padding: 0 2rem; }
}
```

---

## 🧪 ТЕСТИРОВАНИЕ

### Уровни тестирования:
1. **Unit тесты** - компоненты изолированно
2. **Integration тесты** - взаимодействие компонентов
3. **E2E тесты** - пользовательские сценарии
4. **Visual тесты** - скриншоты компонентов

### Покрытие:
- **Компоненты:** >90%
- **Хуки:** >95%
- **Утилиты:** >100%
- **API слой:** >85%

---

## 📞 ПОДДЕРЖКА

### При возникновении проблем:
1. Проверить файлы в `/dev2-frontend/troubleshooting/`
2. Просмотреть логи в браузере (DevTools)
3. Проверить статус API endpoints
4. Связаться с backend разработчиком

### Полезные ресурсы:
- [React 18 документация](https://react.dev/)
- [Material-UI компоненты](https://mui.com/)
- [React Query](https://tanstack.com/query)
- [TypeScript handbook](https://www.typescriptlang.org/)

---

**Принцип: Каждый компонент должен быть переиспользуемым и доступным!** 