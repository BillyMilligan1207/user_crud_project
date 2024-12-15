# Базовый образ для Python
FROM python:3.10-slim

# Устанавливаем системные зависимости для PostgreSQL
RUN apt-get update && apt-get install -y \
    libpq-dev gcc

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем файлы проекта в контейнер
COPY . /app

# Устанавливаем зависимости Python
RUN pip install --no-cache-dir -r /app/requirements.txt

# Устанавливаем порт для сервера
EXPOSE 8000

# Команда для запуска сервера
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
