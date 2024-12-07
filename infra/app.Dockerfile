FROM python:3.11.9-alpine3.20
RUN apk update && apk upgrade && apk add bash
RUN mkdir findtoplaydjango
WORKDIR /findtoplaydjango
COPY . /findtoplaydjango

RUN pip install uv

RUN uv venv .venv
RUN uv pip install -r requirements.txt


RUN uv run manage.py makemigrations
RUN uv run manage.py migrate
RUN uv run manage.py createsuperuser
CMD ["uv", "run", "manage.py", "runserver"]