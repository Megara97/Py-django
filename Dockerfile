FROM python:3.11.1

RUN mkdir /app
WORKDIR /app

COPY . /app/

RUN pip install Django==4.2.5

CMD ["bash", "-c", "cd Practica && python manage.py runserver 3000"]