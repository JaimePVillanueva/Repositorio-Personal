"""logic.py — Orquestación: validar, clasificar y responder.

Qué hace este módulo:
  - Fase 1: `clasificar_consulta()` — validar → prompt → Gemini → parsear JSON.
  - Fase 2: `responder_chat()` — prompt con contexto → Gemini → actualizar state.
  - Helpers `respuesta_ok()` y `respuesta_error()` (ya implementados).

Para qué sirve:
  - Es el «cerebro» que conecta validators, prompts, context, state y gemini_client.
  - `main.py` solo llama funciones de aquí; no duplica reglas.

Reglas importantes:
  - No uses `print` en este archivo (la salida la hace main.py).
  - Importa `llamar_gemini_json` / `safe_generate_texto` dentro de las funciones.

Funciones a implementar:
  - Fase 1: `parsear_clasificacion`, `clasificar_consulta`
  - Fase 2: `demo_seleccion_faq`, `responder_chat`
"""

from pathlib import Path

from validators import validar_consulta

import json


def respuesta_ok(mensaje: str, data: dict | None = None) -> dict:
    return {"status": "ok", "mensaje": mensaje, "data": data or {}}


def respuesta_error(mensaje: str, errores: list[str]) -> dict:
    return {"status": "error", "mensaje": mensaje, "data": {"errores": errores}}


def parsear_clasificacion(raw: str) -> dict:

    try:
        dicc = json.loads(raw)
    except json.JSONDecodeError:
        raise ValueError("JSON Inválido")
    
    if "category" and "priority" and "summary" not in dicc:
        raise ValueError("El JSON no cuenta con las claves adecuadas")
    if dicc.get("category").lower() not in ("academico", "tecnico", "administrativo", "otro"):
        raise ValueError("La categoría no es válida")
    if dicc.get("priority").lower() not in ("baja, media, alta"):
        raise ValueError("La prioridad no es válida")
    
    """TODO: clasificación — json.loads + whitelist de category y priority.

    Entrada: '{"category": "tecnico", "priority": "media", "summary": "..."}'
    Salida: dict con esas tres claves validadas.
    Lanza ValueError si el JSON es inválido o las claves no están en config.

    Ver README FASE 1, Tarea 3.
    """


def clasificar_consulta(datos: dict) -> dict:
    """TODO: clasificación — orquesta validar → prompt → Gemini → parsear.

    Entrada: dict como en consultas_ejemplo.json.
    Salida OK: {"status": "ok", "mensaje": "...", "data": {category, priority, summary}}
    Salida error: {"status": "error", "mensaje": "...", "data": {"errores": [...]}}

    Sin print. Ver README FASE 1, Tarea 4.
    """
    raise NotImplementedError("Implementa clasificar_consulta()")


def responder_chat(
    state: dict,
    pregunta: str,
    faq_entries: list[dict],
) -> dict:
    """TODO: contexto y chat — prompt con perfil, FAQ filtrado e historial.

    Entrada: state (inicializar_estado), pregunta del alumno, faq_entries de seleccionar_faq.
    Salida OK: respuesta del modelo + metricas (elapsed_ms, tokens).
    Actualiza state con append_user/append_model tras respuesta OK.

    Ver README FASE 2, Tarea 4.
    """
    raise NotImplementedError("Implementa responder_chat()")


def demo_seleccion_faq(faq_path: Path, consulta: str) -> dict:
    """TODO: contexto y chat — prueba seleccionar_faq sin chat completo.

    Entrada: ruta a faq.json y texto de consulta.
    Salida OK: {"status": "ok", "data": {"topic_id": "...", "entry": {...}}}

    Ver README FASE 2, Tarea 4.
    """
    raise NotImplementedError("Implementa demo_seleccion_faq()")
