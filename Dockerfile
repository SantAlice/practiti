FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY yoga_bot.py ./
COPY .env ./

CMD ["python", "yoga_bot.py"] 