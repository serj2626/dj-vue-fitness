FROM python:3.10-slim-bullseye

ENV PYTHONUNBUFFERED 1
# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONPATH=/app
# ENV VIRTUAL_ENV=/opt/venv

WORKDIR /app
COPY . /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]