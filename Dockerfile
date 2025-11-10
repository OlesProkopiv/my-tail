# Використовуємо офіційний Python образ
FROM python:3.9-slim

# Створюємо робочу директорію
WORKDIR /app

# Копіюємо все в контейнер
COPY . .

# Встановлюємо пакет у editable режимі
RUN pip install --no-cache-dir -e .

# Запуск за замовчуванням: команда my-tail
ENTRYPOINT ["my-tail"]
