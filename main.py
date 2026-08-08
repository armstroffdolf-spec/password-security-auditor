"""
Auditor de Seguridad de Contraseñas (Password Security Auditor)
Descripción: Herramienta en Python puro para evaluar la fortaleza de una clave
basándose en criterios de ciberseguridad.
"""

def evaluar_contrasena(password: str) -> tuple[int, list[str]]:
    puntos = 0
    fallos = []

    # 1. Regla: Longitud mínima
    if len(password) >= 8:
        puntos += 1
    else:
        fallos.append("Tiene menos de 8 caracteres (muy corta).")

    # 2. Regla: Uso de mayúsculas
    if any(caracter.isupper() for caracter in password):
        puntos += 1
    else:
        fallos.append("Le faltan letras mayúsculas (ej. A, B, C).")

    # 3. Regla: Uso de números
    if any(caracter.isdigit() for caracter in password):
        puntos += 1
    else:
        fallos.append("No contiene números (ej. 1, 2, 3).")

    # 4. Regla: Uso de caracteres especiales
    if any(not caracter.isalnum() for caracter in password):
        puntos += 1
    else:
        fallos.append("No tiene símbolos especiales (ej. @, #, $, !).")

    return puntos, fallos


def mostrar_reporte(puntos: int, fallos: list[str]) -> None:
    print("\n" + "=" * 40)
    print("📊 REPORTE DE ANÁLISIS DE SEGURIDAD")
    print("=" * 40)

    if puntos == 4:
        print("🟢 ¡Excelente! Es una contraseña muy fuerte. (4/4)")
    elif puntos == 3:
        print("🟡 Aceptable, pero puede mejorar. (3/4)")
    else:
        print(f"🔴 ¡Cuidado! Es una contraseña débil. ({puntos}/4)")

    if fallos:
        print("\n💡 Recomendaciones para mejorarla:")
        for fallo in fallos:
            print(f"  ❌ {fallo}")
    print("=" * 40 + "\n")


def main():
    print("🛡️  BIENVENIDO AL AUDITOR DE CONTRASEÑAS  🛡️")
    clave = input("🔑 Ingresa una contraseña para auditar: ")
    
    puntos, fallos = evaluar_contrasena(clave)
    mostrar_reporte(puntos, fallos)


if __name__ == "__main__":
    main()
