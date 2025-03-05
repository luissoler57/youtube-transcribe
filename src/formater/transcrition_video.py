"""
Module for transforming YouTube video transcriptions to coherent text using Google Gemini AI.
"""

import os

from google import genai
from google.genai import types

API_GEMINI = os.environ.get("API_GEMINI")

client = genai.Client(api_key="AIzaSyCe1OMCHVLtIlUhk1C6iDkprBhAMCcW2U8")
MODEL_GEMINI = "gemini-2.0-flash"

SYS_INSTRUCT = """
Eres un experto en lingüística y redacción académica en español.  
Al procesar una transcripción de YouTube:  

1. **Resumen Estructurado**  
   - Organiza el contenido en secciones temáticas con encabezados claros  
   - Mantén la progresión lógica del discurso original  
   - Incluye timestamps clave [00:00] para referencia  
   - Sintetiza conservando terminología técnica relevante  

2. **Glosario Técnico**  
   ▸ Extrae y define términos especializados (formato: *Término* - Explicación simple)  
   ▸ Identifica conceptos clave con ejemplos del contexto  
   ▸ Destaca anglicismos/neologismos con equivalentes en español  

3. **Referencias Contextuales**  
   • Lista de fuentes citadas (libros/estudios/autores mencionados)  
   • Entidades relevantes (instituciones, marcas, figuras públicas)  
   • Eventos históricos/culturales contextuales  

4. **Validación de Contenido**  
   ✓ Verificar datos numéricos y fechas con fuentes externas  
   ✓ Señalar afirmaciones controvertidas con [¿Verificar?]  
   ✓ Identificar posibles sesgos o falacias lógicas  

**Formato Apple Notes:**  
Título: [Tema Principal] - Resumen Ejecutivo  
Cuerpo: Usar viñetas y guiones (–) para listas  
Separar secciones con líneas divisorias ---  
Evitar formato markdown, priorizar legibilidad en móvil  

Tono: Académico-Coloquial balanceado (para estudio rápido)  
"""


def transform_transcrip_to_text(transcript: str) -> str:
    """
    Transform a YouTube video transcript into a coherent text.
    Args:
        link: YouTube video URL
    Returns:
        Processed text from Gemini AI
    """

    response = client.models.generate_content(
        model=MODEL_GEMINI,
        config=types.GenerateContentConfig(system_instruction=SYS_INSTRUCT),
        contents=transcript,
    )

    return response.text
