FROM python:3.11.9-alpine3.20
RUN apk update && apk upgrade && apk add bash
RUN mkdir findtoplaydjango
WORKDIR /findtoplaydjango
COPY . /findtoplaydjango



EXPOSE 5000

RUN pip install uv

RUN uv venv .venv
RUN uv python pin 3.11.9
RUN uv sync
RUN uv add gunicorn


# RUN uv run manage.py makemigrations
# RUN uv python manage.py migrate && \
#     uv python manage.py createsuperuser --noinput || true
CMD ["uv", "run", "manage.py", "runserver", "5000"]