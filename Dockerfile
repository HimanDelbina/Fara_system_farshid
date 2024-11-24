FROM python:3.11-slim

# نصب وابستگی‌های سیستمی
RUN apt-get update && apt-get install -y --no-install-recommends \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# تنظیم دایرکتوری کاری
WORKDIR /app

# کپی فایل requirements و نصب وابستگی‌ها
COPY requirements.txt /app/
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# کپی باقی کدهای برنامه
COPY . /app/

# دستور اجرای برنامه
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
