from dotenv import load_dotenv

import os

load_dotenv()

FLASK_HOST = os.getenv('FLASK_HOST')
FLASK_PORT = os.getenv('PORT')
FLASK_DEBUG = os.getenv('DEBUG')

ROUTE_CREDENTIALS = os.getenv('ROUTE_CREDENTIALS')
DATABASE_URL = os.getenv('DATABASE_URL')

JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY ')