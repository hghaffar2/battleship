FROM python:3.9
COPY requirements.txt .
RUN apt-get update &&  \
    apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
    build-essential curl gnupg2 libpq-dev dos2unix tini postgresql-client gettext procps python3  \
    python3-pip python3-dev nano vim \
    && apt-get autoclean \
    && apt-get clean \
    && apt-get autoremove && pip install -r requirements.txt
ENV FLASK_RUN_HOST=0.0.0.0
WORKDIR /app
COPY . /app
EXPOSE 5000
CMD ["python", "app.py"]