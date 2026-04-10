# Spanish Prompts for Document Analysis

def get_system_prompt() -> str:
    """
    Returns the system prompt in Spanish that defines the agent's role and behavior.
    """
    return """Eres un agente experto en análisis de documentos. Tu tarea es leer documentos 
y proporcionar un análisis estructurado en español. Debes ser profesional, claro y conciso.

Analiza el documento proporcionado y devuelve un análisis en formato JSON con la siguiente estructura:
{
    "resumen_ejecutivo": "Un párrafo conciso (máximo 3 oraciones) que resuma los puntos principales del documento",
    "puntos_clave": ["Punto clave 1", "Punto clave 2", ...],
    "tareas_accionables": ["Tarea 1: descripción", "Tarea 2: descripción", ...],
    "riesgos_o_vacios": ["Riesgo/vacío 1", "Riesgo/vacío 2", ...],
    "conclusion": "Una conclusión final (máximo 2 oraciones) que sintetice el documento"
}

IMPORTANTE: 
- Responde SOLO con JSON válido, sin explicaciones adicionales
- Todos los textos deben estar en español
- Sé específico y evita generalidades
- Si el documento es muy corto o limitado, ajusta el análisis a la información disponible"""


def get_analysis_prompt(document_text: str) -> str:
    """
    Returns the user prompt in Spanish for analyzing a document.
    
    Args:
        document_text: The extracted text from the PDF document
        
    Returns:
        The formatted prompt requesting structured analysis
    """
    return f"""Por favor, analiza el siguiente documento y proporciona un análisis estructurado en JSON:

---
DOCUMENTO:
---
{document_text}

---
FIN DEL DOCUMENTO
---

Proporciona el análisis en el formato JSON especificado en tus instrucciones del sistema."""


def parse_analysis_response(response_text: str) -> dict:
    """
    Parses the LLM response and extracts the JSON structure.
    
    Args:
        response_text: The raw response from the LLM
        
    Returns:
        A dictionary containing the analysis or an error structure
    """
    import json
    
    try:
        # Try to parse the entire response as JSON
        analysis = json.loads(response_text)
        
        # Validate required fields
        required_fields = [
            "resumen_ejecutivo",
            "puntos_clave",
            "tareas_accionables",
            "riesgos_o_vacios",
            "conclusion"
        ]
        
        for field in required_fields:
            if field not in analysis:
                raise ValueError(f"Campo requerido faltante: {field}")
        
        return analysis
    
    except json.JSONDecodeError:
        # If JSON parsing fails, try to extract JSON from the response
        import re
        json_match = re.search(r'\{.*\}', response_text, re.DOTALL)
        if json_match:
            try:
                analysis = json.loads(json_match.group())
                return analysis
            except json.JSONDecodeError:
                pass
        
        # If all attempts fail, return error structure
        return {
            "error": "No se pudo analizar la respuesta del LLM",
            "raw_response": response_text[:500]
        }


def format_analysis_for_display(analysis: dict) -> dict:
    """
    Formats the analysis dictionary for display in Streamlit.
    
    Args:
        analysis: The analysis dictionary from parse_analysis_response
        
    Returns:
        The formatted analysis dictionary
    """
    if "error" in analysis:
        return analysis
    
    return {
        "resumen_ejecutivo": analysis.get("resumen_ejecutivo", "N/A"),
        "puntos_clave": analysis.get("puntos_clave", []),
        "tareas_accionables": analysis.get("tareas_accionables", []),
        "riesgos_o_vacios": analysis.get("riesgos_o_vacios", []),
        "conclusion": analysis.get("conclusion", "N/A")
    }
