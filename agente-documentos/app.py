"""
Agente Local de Documentos - Streamlit Application

A production-quality web app for analyzing PDF documents using LLM APIs.
Extracts text from PDFs and provides structured analysis in Spanish.
"""

import streamlit as st
import os
from datetime import datetime
from dotenv import load_dotenv

# Import local modules
from pdf_utils import extract_text_from_pdf, truncate_text, validate_pdf_file
from agent import LLMAgent
from prompts import (
    get_system_prompt,
    get_analysis_prompt,
    parse_analysis_response,
    format_analysis_for_display
)
from utils import (
    format_timestamp_spanish,
    format_analysis_to_text,
    generate_filename_for_download,
    truncate_filename,
    get_environment_status
)

# Load environment variables from .env file
load_dotenv()

# ============================================================================
# PAGE CONFIGURATION
# ============================================================================

st.set_page_config(
    page_title="Agente Local de Documentos",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown("""
<style>
    .main {
        padding-top: 2rem;
    }
    .stButton > button {
        width: 100%;
        border-radius: 0.5rem;
        font-weight: bold;
    }
    .analysis-section {
        background-color: #f0f2f6;
        padding: 1.5rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
    }
    .success-box {
        background-color: #d1e7dd;
        color: #0f5132;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #198754;
        margin: 1rem 0;
    }
    .error-box {
        background-color: #f8d7da;
        color: #842029;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #dc3545;
        margin: 1rem 0;
    }
    .info-box {
        background-color: #cfe2ff;
        color: #084298;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #0d6efd;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# ============================================================================
# SESSION STATE INITIALIZATION
# ============================================================================

if 'upload_history' not in st.session_state:
    st.session_state.upload_history = []

if 'current_analysis' not in st.session_state:
    st.session_state.current_analysis = None

if 'current_filename' not in st.session_state:
    st.session_state.current_filename = None

if 'current_timestamp' not in st.session_state:
    st.session_state.current_timestamp = None

# ============================================================================
# SIDEBAR - CONFIGURATION & HISTORY
# ============================================================================

with st.sidebar:
    st.title("⚙️ Configuración")
    
    # Environment Status
    st.markdown("### Estado del API")
    env_status = get_environment_status()
    
    if env_status['api_key_set']:
        st.markdown(
            f'<div class="info-box">✅ API Key configurada: {env_status["api_key_preview"]}</div>',
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            '<div class="error-box">❌ API Key NO CONFIGURADA</div>',
            unsafe_allow_html=True
        )
    
    st.markdown(f"**URL del API:** {env_status['api_url']}")
    st.markdown(f"**Modelo:** {env_status['model']}")
    
    st.divider()
    
    # Upload History
    st.markdown("### 📋 Historial de Documentos")
    
    if st.session_state.upload_history:
        for i, history_item in enumerate(reversed(st.session_state.upload_history)):
            col1, col2 = st.columns([3, 1])
            
            with col1:
                display_name = truncate_filename(history_item['filename'], max_length=25)
                if st.button(
                    f"📄 {display_name}",
                    key=f"history_{i}",
                    use_container_width=True
                ):
                    st.session_state.current_filename = history_item['filename']
                    st.session_state.current_timestamp = history_item['timestamp']
                    st.session_state.current_analysis = history_item['analysis']
                    st.rerun()
            
            with col2:
                st.caption(history_item['timestamp'].split(" ")[0])
    else:
        st.info("No hay documentos analizados aún.")
    
    st.divider()
    
    # Help Section
    st.markdown("### 💡 Ayuda")
    with st.expander("Cómo usar la aplicación"):
        st.markdown("""
1. **Carga un PDF** usando el área de carga
2. **Haz clic en "Analizar documento"**
3. **Espera los resultados** (puede tomar 1-2 minutos)
4. **Descarga el análisis** si lo necesitas
5. **Consulta el historial** para revisar análisis anteriores

### Limitaciones:
- Máximo 50MB por archivo
- PDF debe tener texto extraíble
- Se truncan documentos muy grandes (>60KB)
        """)
    
    st.markdown("### ⚙️ Variables de Entorno")
    with st.expander("Configuración necesaria"):
        st.markdown("""
Crea un archivo `.env` en la carpeta del proyecto:

```
LLM_API_URL=https://openrouter.ai/api/v1/chat/completions
LLM_API_KEY=tu_clave_api_aqui
LLM_MODEL=mistralai/mistral-7b-instruct:free
```

**Obtén una API Key:**
- [OpenRouter](https://openrouter.ai) (gratuito)
- [OpenAI](https://openai.com)
- [Another Provider]
        """)

# ============================================================================
# MAIN CONTENT AREA
# ============================================================================

# Header
st.title("📄 Agente Local de Documentos")
st.markdown("Analiza tus documentos PDF usando IA. Obtén resúmenes, puntos clave y tareas accionables.")

st.divider()

# Main Layout - Two Columns
col_main, col_display = st.columns([2, 3])

with col_main:
    # File Upload Section
    st.markdown("### 📤 Cargar Documento")
    
    uploaded_file = st.file_uploader(
        "Selecciona un archivo PDF",
        type=['pdf'],
        accept_multiple_files=False,
        label_visibility="collapsed"
    )
    
    # Analyze Button
    if uploaded_file is not None:
        is_valid, validation_message = validate_pdf_file(uploaded_file)
        
        if not is_valid:
            st.error(validation_message)
        else:
            st.success(f"✅ Archivo valid: {uploaded_file.name} ({uploaded_file.size / 1024:.1f}KB)")
            
            if st.button(
                "🚀 Analizar Documento",
                type="primary",
                use_container_width=True,
                key="analyze_button"
            ):
                # Create LLM Agent and check configuration
                agent = LLMAgent()
                
                if not agent.is_configured():
                    st.error("""
❌ **API Key no configurada**

Por favor, configura las siguientes variables de entorno:
- `LLM_API_KEY`: Tu clave de API
- `LLM_API_URL` (opcional): URL del API
- `LLM_MODEL` (opcional): Modelo a usar

Crea un archivo `.env` en la carpeta del proyecto con esta información.
                    """)
                else:
                    with st.spinner("⏳ Extrayendo texto del PDF..."):
                        # Extract text from PDF
                        pdf_bytes = uploaded_file.getvalue()
                        extraction_result = extract_text_from_pdf(pdf_bytes)
                        
                        if not extraction_result['success']:
                            st.error(extraction_result['error'])
                        else:
                            st.success(
                                f"✅ Extracción completada: {extraction_result['page_count']} páginas, "
                                f"{len(extraction_result['text'])} caracteres"
                            )
                            
                            # Truncate if necessary
                            document_text = truncate_text(extraction_result['text'])
                            
                            with st.spinner("🤔 Analizando documento con IA..."):
                                # Get prompts
                                system_prompt = get_system_prompt()
                                user_prompt = get_analysis_prompt(document_text)
                                
                                # Call LLM
                                success, response = agent.call_llm(system_prompt, user_prompt)
                                
                                if not success:
                                    st.error(f"❌ Error del API: {response}")
                                else:
                                    # Parse response
                                    analysis = parse_analysis_response(response)
                                    
                                    if "error" in analysis:
                                        st.error(f"Error al procesar respuesta: {analysis['error']}")
                                        st.info(f"Respuesta del LLM: {analysis.get('raw_response', '')[:300]}")
                                    else:
                                        # Format for display
                                        formatted_analysis = format_analysis_for_display(analysis)
                                        
                                        # Store in session
                                        timestamp = format_timestamp_spanish()
                                        st.session_state.current_analysis = formatted_analysis
                                        st.session_state.current_filename = uploaded_file.name
                                        st.session_state.current_timestamp = timestamp
                                        
                                        # Add to history
                                        history_entry = {
                                            'filename': uploaded_file.name,
                                            'timestamp': timestamp,
                                            'analysis': formatted_analysis
                                        }
                                        
                                        # Avoid duplicates
                                        if not any(h['filename'] == uploaded_file.name and h['timestamp'] == timestamp 
                                                 for h in st.session_state.upload_history):
                                            st.session_state.upload_history.append(history_entry)
                                        
                                        st.success("✅ Análisis completado exitosamente")
                                        st.rerun()

# Display Analysis Results
with col_display:
    if st.session_state.current_analysis is not None:
        st.markdown("### 📊 Resultados del Análisis")
        
        if "error" in st.session_state.current_analysis:
            st.error(st.session_state.current_analysis['error'])
        else:
            analysis = st.session_state.current_analysis
            
            # Resumen Ejecutivo
            with st.expander("📋 Resumen Ejecutivo", expanded=True):
                st.write(analysis.get('resumen_ejecutivo', 'N/A'))
            
            # Puntos Clave
            with st.expander("⭐ Puntos Clave", expanded=True):
                puntos = analysis.get('puntos_clave', [])
                if isinstance(puntos, list):
                    for i, punto in enumerate(puntos, 1):
                        st.markdown(f"**{i}.** {punto}")
                else:
                    st.write(puntos)
            
            # Tareas Accionables
            with st.expander("✅ Tareas Accionables", expanded=False):
                tareas = analysis.get('tareas_accionables', [])
                if isinstance(tareas, list):
                    for i, tarea in enumerate(tareas, 1):
                        st.markdown(f"☐ **{i}.** {tarea}")
                else:
                    st.write(tareas)
            
            # Riesgos o Vacíos
            with st.expander("⚠️ Riesgos o Vacíos", expanded=False):
                riesgos = analysis.get('riesgos_o_vacios', [])
                if isinstance(riesgos, list):
                    for i, riesgo in enumerate(riesgos, 1):
                        st.markdown(f"**{i}.** {riesgo}")
                else:
                    st.write(riesgos)
            
            # Conclusión
            with st.expander("🎯 Conclusión Final", expanded=False):
                st.write(analysis.get('conclusion', 'N/A'))
            
            st.divider()
            
            # Download Button
            analysis_text = format_analysis_to_text(
                analysis,
                st.session_state.current_filename,
                st.session_state.current_timestamp
            )
            
            download_filename = generate_filename_for_download(st.session_state.current_filename)
            
            st.download_button(
                label="⬇️ Descargar Análisis (TXT)",
                data=analysis_text,
                file_name=download_filename,
                mime="text/plain",
                use_container_width=True
            )
            
            # Copy to Clipboard Info
            st.info(
                f"📌 Documento: {st.session_state.current_filename}\n"
                f"📅 Análisis: {st.session_state.current_timestamp}"
            )
    else:
        st.info("👈 Carga un documento PDF en la izquierda para comenzar el análisis")

# ============================================================================
# FOOTER
# ============================================================================

st.divider()
st.markdown(
    """
    <div style='text-align: center; color: #888; font-size: 0.85rem; margin-top: 2rem;'>
    <p>Agente Local de Documentos v1.0 | Powered by Streamlit & OpenRouter</p>
    <p>Made with ❤️ for document analysis</p>
    </div>
    """,
    unsafe_allow_html=True
)
