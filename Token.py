import random
import string

def generate_token(length):
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for i in range(length))

token = generate_token(30)  # Puedes ajustar el valor 10 al tamaño de token que necesites
print("Token de prueba generado:", token)