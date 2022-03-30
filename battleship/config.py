import os


class Config:
    SECRET_KEY = 'SuperSecret'
    db_password = os.environ.get('POSTGRES_PASSWORD', 'Passw0rd')
    db_username = os.environ.get('POSTGRES_USER', 'postgres')
    db_name = os.environ.get('POSTGRES_DB', 'battleship')
    db_host = os.environ.get('POSTGRES_HOST', '127.0.0.1')
    SQLALCHEMY_DATABASE_URI = f"postgresql://{db_username}:{db_password}@{db_host}/{db_name}"
