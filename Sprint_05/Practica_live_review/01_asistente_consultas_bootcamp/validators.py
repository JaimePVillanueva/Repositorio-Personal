"""validators.py — Validación de consultas en Python (Fase 1).

Qué hace este módulo:
  - Comprueba nombre, email y mensaje antes de llamar a Gemini.
  - Devuelve una lista de errores (vacía = consulta válida).

Para qué sirve:
  - Ahorrar tokens y evitar llamadas a la API con datos mal formados.
  - Es el primer paso del flujo en `clasificar_consulta()` (logic.py).

Función a implementar:
  - `validar_consulta(datos)` — ver README FASE 1, Tarea 1.
"""

from config import (
    MAX_CHARS_MENSAJE,
    MIN_CHARS_MENSAJE,
    PATRON_EMAIL,
)


def validar_consulta(datos: dict) -> list[str]:
    
    errores = []

    nombre = str(datos.get("nombre", "")).strip()
    if not nombre:
        errores.append("Nombre inválido: no puede estar vacío")
      
    email = str(datos.get("email", "")).strip()
    if not email:
        errores.append("Email inválido: no puede estar vacío")
    elif email.fullmatch(PATRON_EMAIL) is None:
        errores.append("Email inválido: formato incorrecto")

    mensaje = str(datos.get("mensaje", "")).strip()
    if len(mensaje) < MIN_CHARS_MENSAJE:
        errores.append("Mensaje inválido: demasiado corto")
    elif len(mensaje) > MAX_CHARS_MENSAJE:
        errores.append("Mensaje inválido: demsiado largo")

    return errores
    """TODO: clasificación — valida nombre, email y mensaje antes de llamar a Gemini.

    Entrada: {"nombre": "Ana", "email": "ana@ejemplo.com", "mensaje": "..."}
    Salida OK: []
    Salida error: ["Nombre inválido: ...", "Email inválido: ...", ...]

    Ver README FASE 1, Tarea 1 y config.py (MIN/MAX_CHARS, PATRON_EMAIL).
    """
    # TODO: clasificación — implementar validación
    raise NotImplementedError(
        "Completa validar_consulta() — revisa config.py y data/consultas_ejemplo.json"
    )
