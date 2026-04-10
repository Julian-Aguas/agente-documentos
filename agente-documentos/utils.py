# Utility functions for the Local Document Agent

from datetime import datetime
import os


def format_timestamp_spanish(dt: datetime = None) -> str:
    """
    Formats a datetime object to Spanish format.
    
    Args:
        dt: datetime object (defaults to now)
        
    Returns:
        Formatted datetime string in Spanish
    """
    if dt is None:
        dt = datetime.now()
    
    months = {
        1: 'enero', 2: 'febrero', 3: 'marzo', 4: 'abril',
        5: 'mayo', 6: 'junio', 7: 'julio', 8: 'agosto',
        9: 'septiembre', 10: 'octubre', 11: 'noviembre', 12: 'diciembre'
    }
    
    return f"{dt.day} de {months[dt.month]} de {dt.year} a las {dt.strftime('%H:%M:%S')}"


def format_analysis_to_text(analysis: dict, filename: str, timestamp: str) -> str:
    """
    Formats the analysis dictionary into a readable text document.
    
    Args:
        analysis: The analysis dictionary with all sections
        filename: The original PDF filename
        timestamp: Formatted timestamp string
        
    Returns:
        Formatted text document
    """
    
    if "error" in analysis:
        return f"""REPORTE DE ANÁLISIS DE DOCUMENTO
================================

Archivo: {filename}
Fecha de análisis: {timestamp}

ERROR EN EL ANÁLISIS:
{analysis.get('error', 'Error desconocido')}

Respuesta del LLM (primeros 500 caracteres):
{analysis.get('raw_response', 'No disponible')[:500]}
"""
    
    text_output = f"""╔════════════════════════════════════════════════════════════╗
║       REPORTE DE ANÁLISIS DE DOCUMENTO - AGENTE LOCAL      ║
╚════════════════════════════════════════════════════════════╝

INFORMACIÓN DEL DOCUMENTO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Archivo:            {filename}
Fecha de análisis:  {timestamp}
Modelo LLM:         {os.getenv('LLM_MODEL', 'mistralai/mistral-7b-instruct:free')}

╔════════════════════════════════════════════════════════════╗
║ RESUMEN EJECUTIVO
╚════════════════════════════════════════════════════════════╝

{analysis.get('resumen_ejecutivo', 'N/A')}


╔════════════════════════════════════════════════════════════╗
║ PUNTOS CLAVE
╚════════════════════════════════════════════════════════════╝

"""
    
    puntos_clave = analysis.get('puntos_clave', [])
    if isinstance(puntos_clave, list):
        for i, punto in enumerate(puntos_clave, 1):
            text_output += f"{i}. {punto}\n"
    else:
        text_output += str(puntos_clave) + "\n"
    
    text_output += f"""

╔════════════════════════════════════════════════════════════╗
║ TAREAS ACCIONABLES
╚════════════════════════════════════════════════════════════╝

"""
    
    tareas = analysis.get('tareas_accionables', [])
    if isinstance(tareas, list):
        for i, tarea in enumerate(tareas, 1):
            text_output += f"☐ {i}. {tarea}\n"
    else:
        text_output += str(tareas) + "\n"
    
    text_output += f"""

╔════════════════════════════════════════════════════════════╗
║ RIESGOS O VACÍOS IDENTIFICADOS
╚════════════════════════════════════════════════════════════╝

"""
    
    riesgos = analysis.get('riesgos_o_vacios', [])
    if isinstance(riesgos, list):
        for i, riesgo in enumerate(riesgos, 1):
            text_output += f"⚠ {i}. {riesgo}\n"
    else:
        text_output += str(riesgos) + "\n"
    
    text_output += f"""

╔════════════════════════════════════════════════════════════╗
║ CONCLUSIÓN FINAL
╚════════════════════════════════════════════════════════════╝

{analysis.get('conclusion', 'N/A')}


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Documento generado por: Agente Local de Documentos
═══════════════════════════════════════════════════════════════
"""
    
    return text_output


def generate_filename_for_download(original_filename: str) -> str:
    """
    Generates a filename for the downloaded analysis.
    
    Args:
        original_filename: The original PDF filename
        
    Returns:
        Formatted filename for the analysis output
    """
    base_name = original_filename.replace('.pdf', '').replace('.PDF', '')
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    return f"analisis_{base_name}_{timestamp}.txt"


def truncate_filename(filename: str, max_length: int = 50) -> str:
    """
    Truncates a filename to a maximum length for display.
    
    Args:
        filename: The filename to truncate
        max_length: Maximum display length
        
    Returns:
        Truncated filename with ellipsis if needed
    """
    if len(filename) <= max_length:
        return filename
    
    # Keep extension
    if '.' in filename:
        name, ext = filename.rsplit('.', 1)
        available = max_length - len(ext) - 2  # Account for dot and space
        return f"{name[:available]}...{ext}"
    else:
        return filename[:max_length - 3] + "..."


def get_environment_status() -> dict:
    """
    Returns the current environment configuration status.
    
    Returns:
        Dictionary with configuration status
    """
    api_url = os.getenv('LLM_API_URL')
    api_key = os.getenv('LLM_API_KEY')
    model = os.getenv('LLM_MODEL')
    
    return {
        'api_url_set': bool(api_url),
        'api_key_set': bool(api_key),
        'model_set': bool(model),
        'api_url': api_url or '(No configurada)',
        'model': model or 'mistralai/mistral-7b-instruct:free',
        'api_key_preview': f"{api_key[:8]}..." if api_key else "(No configurada)"
    }
