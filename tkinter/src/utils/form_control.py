import re

def control_name_and_lastname(value):
    patron = r'^[a-zA-Z\s]+$'
    if not re.match(patron, value):
        return True
    else:
        return False
    
def control_user(usuario):
    patron = r'^[a-zA-Z][a-zA-Z0-9]+$'
    
    if not re.match(patron, usuario):
        return True
    else:
        return False
    
def control_min_len(value):
    if len(value) < 4:
        return True
    else:
        return False

def control_max_len(value):
    if len(value) > 20:
        return True
    else:
        return False

def control_name_route(value):
    patron = r'^[a-zA-Z0-9\s]+$'
    if not re.match(patron, value):
        return True
    else:
        return False
