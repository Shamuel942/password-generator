import random
import string

def generar_contraseña(longitud=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña

if __name__ == "__main__":
    print("🔐 Generador de Contraseñas Seguras")
    longitud = int(input("Introduce la longitud de la contraseña (ej. 12): "))
    print("Tu contraseña segura es:")
    print(generar_contraseña(longitud))
