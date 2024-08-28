FROM python:3.9

# Установите рабочую директорию
WORKDIR /home/app

# Копируйте зависимости
COPY requirements.txt .
RUN pip install -r requirements.txt

# Копируйте проект
COPY . .

# Копируйте и сделайте исполняемым сценарий
COPY entrypoint.sh /home/app/entrypoint.sh
RUN chmod +x /home/app/entrypoint.sh

# Установите точку входа
ENTRYPOINT ["entrypoint.sh"]
