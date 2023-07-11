FROM python:3.9

COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt

COPY ../.. /app


CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]