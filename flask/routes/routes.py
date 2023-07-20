from flask import Blueprint

#Importar rutas
from user import users_bp

all_bp = []

all_bp.append(users_bp)