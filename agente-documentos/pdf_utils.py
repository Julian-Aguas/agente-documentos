# PDF utilities for text extraction

import io
import fitz  # PyMuPDF


def extract_text_from_pdf(pdf_bytes: bytes, max_size_bytes: int = 52428800) -> dict:
    """
    Extracts text from a PDF file provided as bytes.
    
    Args:
        pdf_bytes: The PDF file content as bytes
        max_size_bytes: Maximum allowed PDF size (default 50MB)
        
    Returns:
        A dictionary containing:
        - 'success': bool indicating if extraction was successful
        - 'text': extracted text (empty string if failed)
        - 'page_count': number of pages in the PDF
        - 'error': error message (if any)
        - 'file_size': size of the PDF in bytes
    """
    
    result = {
        'success': False,
        'text': '',
        'page_count': 0,
        'error': None,
        'file_size': len(pdf_bytes) if pdf_bytes else 0
    }
    
    # Validate file size
    if result['file_size'] == 0:
        result['error'] = "Error: El archivo PDF está vacío."
        return result
    
    if result['file_size'] > max_size_bytes:
        result['error'] = f"Error: El archivo PDF es demasiado grande ({result['file_size'] / 1024 / 1024:.1f}MB). Máximo permitido: 50MB"
        return result
    
    try:
        # Open PDF from bytes
        pdf_document = fitz.open(stream=pdf_bytes, filetype="pdf")
        result['page_count'] = len(pdf_document)
        
        # Validate that PDF has content
        if result['page_count'] == 0:
            result['error'] = "Error: El PDF no contiene páginas."
            pdf_document.close()
            return result
        
        # Extract text from all pages
        extracted_text = []
        for page_num in range(result['page_count']):
            try:
                page = pdf_document[page_num]
                text = page.get_text()
                extracted_text.append(text)
            except Exception as page_error:
                result['error'] = f"Error al leer página {page_num + 1}: {str(page_error)}"
                pass
        
        pdf_document.close()
        
        # Join all text with page separators
        result['text'] = "\n\n--- Página siguiente ---\n\n".join(extracted_text)
        
        # Check if any text was extracted
        if not result['text'].strip():
            result['error'] = "Error: El PDF no contiene texto extraíble. Posiblemente sea una imagen escaneada."
            return result
        
        result['success'] = True
        
    except Exception as e:
        result['error'] = f"Error al procesar el PDF: {str(e)}"
        if "cannot open encrypted file" in str(e).lower():
            result['error'] = "Error: El PDF está protegido con contraseña. Por favor, use un PDF sin protección."
    
    return result


def truncate_text(text: str, max_length: int = 60000) -> str:
    """
    Truncates text to a maximum length while trying to preserve word boundaries.
    
    Args:
        text: The text to truncate
        max_length: Maximum number of characters (default 60KB ~ 15K tokens)
        
    Returns:
        The truncated text
    """
    if len(text) <= max_length:
        return text
    
    # Truncate and try to find the last complete sentence
    truncated = text[:max_length]
    
    # Find the last sentence-ending punctuation
    last_period = max(
        truncated.rfind('.'),
        truncated.rfind('!'),
        truncated.rfind('?')
    )
    
    if last_period > max_length * 0.8:  # Only use if it's reasonably close to the max
        truncated = truncated[:last_period + 1]
    
    truncated += "\n\n[Nota: Documento truncado debido a su tamaño. Solo se procesaron los primeros caracteres.]"
    
    return truncated


def validate_pdf_file(file_obj) -> tuple[bool, str]:
    """
    Validates if the uploaded file is a valid PDF.
    
    Args:
        file_obj: The uploaded file object from Streamlit
        
    Returns:
        A tuple (is_valid: bool, message: str)
    """
    if not file_obj:
        return False, "No se proporcionó ningún archivo."
    
    # Check file extension
    if not file_obj.name.lower().endswith('.pdf'):
        return False, "Error: El archivo debe ser un PDF. Extensión no válida."
    
    # Check file size
    file_size = len(file_obj.getvalue())
    if file_size == 0:
        return False, "Error: El archivo está vacío."
    
    if file_size > 52428800:  # 50MB
        return False, f"Error: El archivo es demasiado grande ({file_size / 1024 / 1024:.1f}MB). Máximo: 50MB"
    
    return True, "OK"
