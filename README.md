# Auditor de Contraseñas en Python

Un script de consola para evaluar si una contraseña cumple con reglas básicas de seguridad (longitud, mayúsculas, números y caracteres especiales).

## ¿Por qué hice este proyecto?

Este es uno de mis primeros proyectos prácticos en Python. Lo construí para aplicar conceptos fundamentales sin depender de librerías externas:

- Organización del código con **funciones** (`def`).
- Uso de **Type Hints** para indicar tipos de datos.
- Manejo de condiciones (`if/elif/else`) y métodos de texto nativos como `.isupper()`, `.isdigit()` y `.isalnum()`.

## Ejemplo de funcionamiento

```text
🛡️ BIENVENIDO AL AUDITOR DE CONTRASEÑAS
🔑 Ingresa una contraseña para auditar: miClave123

========================================
📊 REPORTE DE ANÁLISIS DE SEGURIDAD
========================================
🟡 Aceptable, pero puede mejorar. (3/4)

💡 Recomendaciones para mejorarla:
  ❌ No tiene símbolos especiales (ej. @, #, $, !).
========================================
