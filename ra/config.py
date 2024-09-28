# config.py
import os

class Config:
    DATABASE_NAME = os.getenv('POSTGRES_DB')
    DATABASE_USER = os.getenv('POSTGRES_USER')
    DATABASE_PASSWORD = os.getenv('POSTGRES_PASSWORD')
    DATABASE_HOST = 'postgres'  # Docker service name
    DATABASE_PORT = '5432'
