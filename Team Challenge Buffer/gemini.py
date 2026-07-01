import os
import getpass
from google import genai

if not os.getenv("GEMINI_API_KEY"):
    os.environ["GEMINI_API_KEY"] = getpass.getpass(
        "Pega aquí tu GEMINI_API_KEY (input oculto): "
    )

print("GEMINI_API_KEY configurada:", "sí" if os.getenv("GEMINI_API_KEY") else "no")

client = genai.Client()
MODEL = "gemini-3-flash-preview"

def summarize_overview_es(overview, title=""):
    overview = overview.strip()
    if not overview:
        raise ValueError("Cadena vacía")
    else:
        return client.models.generate_content(
            model=MODEL,
            contents=f"Resume el siguiente texto en un máximo de 2 frases:\n{overview}"
        )
    

