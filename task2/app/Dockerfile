# Используйте официальный образ Python в качестве базового образа
FROM python:3.11-slim-buster

# Устанавливаем системные зависимости
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Установка зависимостей Python
COPY requirements.txt /app/
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt

# Копирование исходного кода
COPY server.py /app

# Установка переменной окружения для работы внутри контейнера
ENV PYTHONUNBUFFERED=1

# Устанавливаем рабочую директорию
WORKDIR /app

# Открываем порт 8000 для обращения к приложению
EXPOSE 8000

# Запуск приложения
CMD ["python", "server.py"]