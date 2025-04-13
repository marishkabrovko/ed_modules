# Django-приложение "Образовательные модули".

Дипломный проект для управления образовательными модулями.

## Структура проекта

Проект состоит из приложения **education_modules**:
- **education_modules** — управление образовательными модулями.

## Состав проекта

- **Django** — веб-фреймворк.
- **Django Rest Framework** — для создания API.
- **PostgreSQL** — база данных.
- **Docker** — для контейнеризации приложения.
- **Swagger** — для автогенерации документации API.

## Установка и запуск

### 1. Клонировать репозиторий

```bash
git clone https://github.com/marishkabrovko/ed_modules.git
cd ed_modules
```

### 2. Собрать контейнер Docker
```bash
docker compose up --build
```

### 3. Доступ к серверу

- Вебприложение будет доступно по адресу [http://localhost:8000](http://localhost:8000)
- Swagger документация доступна по адресу [http://localhost:8000/swagger](http://localhost:8000/swagger)

### 4. Эндпойнты 

#### Образовательные модули
- GET /api/modules/ — Получить список образовательных модулей.
- POST /api/modules/ — Создать новый образовательный модуль.
- GET /api/modules/{id}/ — Получить информацию о модуле.
- PATCH /api/modules/{id}/ — Обновить образовательный модуль.
- DELETE /api/modules/{id}/ — Удалить образовательный модуль.

### 5. Тесты

Total coverage - 91%