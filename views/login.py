from models.employees import login as m_login
import hashlib


# Convertir password a hash 256.
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


# Inicio de sesión.
def login_view(user, password):
    result = m_login(user, hash_password(password))

    if isinstance(result[0], tuple) and len(result[0]) == 0:
        return result[1]
    elif result[0] is None:
        return 'El usuario no existe.'
    else:
        return result[0]
