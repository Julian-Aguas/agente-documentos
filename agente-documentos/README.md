# 📄 Agente Local de Documentos

Una aplicación web moderna y fácil de usar para analizar documentos PDF usando Inteligencia Artificial. Extrae texto de PDFs y genera análisis estructurado en español con resumen ejecutivo, puntos clave, tareas accionables y riesgos identificados.

## ✨ Características Principales

- 📤 **Carga de PDFs**: Interfaz intuitiva para seleccionar archivos (hasta 50MB)
- 🤖 **Análisis con IA**: Integración con APIs LLM compatibles con OpenAI (OpenRouter, Azure OpenAI, etc.)
- 🇪🇸 **Completamente en Español**: Interfaz y respuestas 100% en español
- 📊 **Análisis Estructurado**: Genera automáticamente:
  - Resumen ejecutivo
  - Puntos clave
  - Tareas accionables
  - Riesgos y vacíos identificados
  - Conclusión final
- 💾 **Descarga de Resultados**: Exporta el análisis completo en formato TXT
- 📋 **Historial de Documentos**: Accede rápidamente a análisis anteriores
- ⚙️ **Configuración Flexible**: Compatible con múltiples proveedores de LLM
- 🔒 **Privado**: Los documentos se procesan en tiempo real sin almacenamiento permanente

## 🚀 Instalación Paso a Paso

### Requisitos Previos

- **Python 3.8+** instalado en tu computadora
- **Git** (opcional, para clonar el repositorio)
- Una **API Key** de un proveedor LLM (gratuito o de pago)

### Paso 1: Clonar el Repositorio

```bash
# Si usas Git
git clone <url-del-repositorio>
cd agente-documentos

# O descarga el ZIP y extrae la carpeta
```

### Paso 2: Crear un Entorno Virtual

```bash
# En Windows
python -m venv .venv
.venv\Scripts\activate

# En macOS/Linux
python3 -m venv .venv
source .venv/bin/activate
```

Deberías ver `(.venv)` al inicio de tu línea de comandos indicando que el entorno está activo.

### Paso 3: Instalar Dependencias

```bash
pip install -r requirements.txt
```

Esto puede tomar 1-2 minutos según tu conexión.

### Paso 4: Configurar el API

#### Opción A: OpenRouter (RECOMENDADO - Gratuito)

1. Accede a [https://openrouter.ai/keys](https://openrouter.ai/keys)
2. Crea una cuenta gratuita (con GitHub, Google, etc.)
3. Copia tu API Key
4. Crea un archivo `.env` en la carpeta del proyecto:

```bash
# En Windows (Command Prompt)
copy .env.example .env

# En Windows (PowerShell)
Copy-Item .env.example .env

# En macOS/Linux
cp .env.example .env
```

5. Abre el archivo `.env` con un editor de texto y pega tu API Key:

```
LLM_API_URL=https://openrouter.ai/api/v1/chat/completions
LLM_API_KEY=sk-or-xxx-xxxxxxxxxxxxxxx
LLM_MODEL=mistralai/mistral-7b-instruct:free
```

#### Opción B: OpenAI (Con Costo)

1. Accede a [https://platform.openai.com/api-keys](https://platform.openai.com/api-keys)
2. Crea una API Key
3. Configura el `.env`:

```
LLM_API_URL=https://api.openai.com/v1/chat/completions
LLM_API_KEY=sk-...
LLM_MODEL=gpt-3.5-turbo
```

#### Opción C: Otro Proveedor Compatible

Si usas Azure OpenAI, LM Studio local, o cualquier otro proveedor compatible con OpenAI:

```
LLM_API_URL=https://tu-url-del-api/v1/chat/completions
LLM_API_KEY=tu-clave-api
LLM_MODEL=tu-modelo
```

## 📖 Cómo Usar la Aplicación

### Ejecución

```bash
streamlit run app.py
```

Se abrirá automáticamente en tu navegador (por defecto: `http://localhost:8501`)

### Flujo de Uso

1. **Carga un PDF**
   - Haz clic en "Selecciona un archivo PDF"
   - Selecciona tu documento (máximo 50MB)
   - Verifica que el archivo sea válido

2. **Analiza el Documento**
   - Haz clic en el botón azul "🚀 Analizar Documento"
   - Espera 1-2 minutos mientras se procesa (depende del tamaño y del API)
   - Verás una barra de progreso indicando el estado

3. **Revisa los Resultados**
   - El análisis aparecerá en la derecha en secciones expandibles
   - Lee el resumen ejecutivo, puntos clave, etc.
   - Todas las secciones están en español

4. **Descarga el Análisis**
   - Haz clic en "⬇️ Descargar Análisis (TXT)"
   - Se descargará un archivo con el análisis completo formateado

5. **Accede al Historial**
   - Revisa análisis anteriores en el panel izquierdo
   - Haz clic en cualquier documento del historial para verse nuevamente

## ⚙️ Configuración Avanzada

### Variables de Entorno

El archivo `.env` soporta estas configuraciones:

```
# URL del API (requerido)
LLM_API_URL=https://openrouter.ai/api/v1/chat/completions

# Clave de autenticación (requerido)
LLM_API_KEY=tu-clave-aqui

# Modelo a utilizar (opcional, default: mistralai/mistral-7b-instruct:free)
LLM_MODEL=mistralai/mistral-7b-instruct:free
```

### Cambiar Modelos en OpenRouter

Algunos modelos disponibles en OpenRouter (todos gratuitos o muy económicos):

```
# Gratuito pero lento
mistralai/mistral-7b-instruct:free

# Rápido y económico (requiere crédito)
openai/gpt-3.5-turbo
meta-llama/llama-2-70b-chat
anthropic/claude-2

# Premium
openai/gpt-4
```

Cambia el valor de `LLM_MODEL` en el `.env` para probar diferentes modelos.

### Limpieza de Historial

El historial se almacena en la sesión (se reinicia al actualizar la página). Para limpiar:

1. Recarga la página (F5 en el navegador)
2. El historial se borrará automáticamente

## 🔍 Estructura del Proyecto

```
agente-documentos/
├── app.py              # Aplicación principal (interfaz Streamlit)
├── agent.py            # Integración con LLM API
├── pdf_utils.py        # Extracción de texto de PDFs
├── prompts.py          # Prompts en español y parseo de respuestas
├── utils.py            # Funciones auxiliares (formato, timestamps, etc.)
├── requirements.txt    # Dependencias Python
├── .env.example        # Plantilla de configuración
├── .env                # Configuración actual (crear copiando .env.example)
├── README.md           # Este archivo
└── samples/            # Documentos de prueba (opcional)
    └── sample_document.pdf
```

### Descripción de Módulos

- **app.py**: Interfaz Streamlit, gestión de estado, carga de archivos, botones
- **agent.py**: Conexión al API LLM, reintentos automáticos, manejo de errores
- **pdf_utils.py**: Extracción de texto con PyMuPDF, truncado, validación
- **prompts.py**: Prompts del sistema, parseo de JSON, formateo
- **utils.py**: Funciones auxiliares (timestamps, descarga de archivos, etc.)

## � Documentación Adicional

Para profundizar en aspectos técnicos del proyecto:

- **[ARCHITECTURE.md](ARCHITECTURE.md)** - Arquitectura del sistema, patrones de diseño, flujos de datos, decisiones técnicas
- **[TECH_STACK.md](TECH_STACK.md)** - Stack tecnológico completo, versiones de librerías, skills demonstrados, benchmarks
- **[DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)** - Guía de despliegue en producción, cloud hosting, Docker
- **[QUICK_START.md](QUICK_START.md)** - Setup rápido en 5 minutos

## �🐛 Solución de Problemas

### "Error: API Key NO CONFIGURADA"

**Solución:**
1. Verifica que existe un archivo `.env` en la carpeta del proyecto
2. Asegúrate de que contiene `LLM_API_KEY=tu-clave-actual`
3. Reinicia la aplicación: `streamlit run app.py`

### "Error: Timeout. El servidor tardó demasiado en responder."

**Causa:** El API tardó más de 60 segundos en responder.

**Soluciones:**
1. Intenta con un documento más pequeño
2. Cambia a un modelo más rápido (ej: mistral-7b)
3. Verifica tu conexión a internet
4. Intenta más tarde si es un API con alta carga

### "Error: El PDF está protegido con contraseña"

**Solución:** Usa un lector de PDFs para remover la protección:
1. Abre el PDF en Adobe Reader o similar
2. Guarda sin protección
3. Luego carga en la aplicación

### "Error: El PDF no contiene texto extraíble"

**Causa:** El PDF es una imagen escaneada sin OCR.

**Soluciones:**
- Usa un software de OCR como ABBYY, Adobe, o [iLovePDF](https://www.ilovepdf.com/)
- Genera el PDF desde el documento original

### "ImportError: No se encuentra el módulo..."

**Solución:** Asegúrate de activar el entorno virtual:

```bash
# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate
```

Luego reinstala las dependencias:
```bash
pip install -r requirements.txt
```

### La aplicación se ve cortada en el navegador

**Solución:** Streamlit usa el ancho completo. Intenta:
1. Maximizar la ventana del navegador
2. Ajustar el zoom (Ctrl+- en Windows, Cmd+- en Mac)
3. Usar un monitor más grande

## 📊 Modelos Recomendados

Para diferentes casos de uso:

| Caso | Modelo | Velocidad | Costo |
|------|--------|-----------|-------|
| Documentos cortos | mistralai/mistral-7b | ⚡ Rápido | 💰 Gratis |
| Documentos medianos | meta-llama/llama-2 | ⚡⚡ Normal | 💰 Muy bajo |
| Documentos complejos | openai/gpt-3.5-turbo | ⚡⚡ Normal | 💰💰 Bajo |
| Máxima calidad | openai/gpt-4 | ⚡ Lento | 💰💰💰 Medio |

## 🔐 Consideraciones de Privacidad y Seguridad

- Los documentos se envían al API LLM para procesamiento
- No se almacenan permanentemente en tu computadora después del análisis
- La API Key se almacena localmente en `.env` (NUNCA versionarla en Git)
- Verifica las políticas de privacidad de tu proveedor LLM

### Proteger tu API Key

⚠️ **Importante**: NO compartas tu `.env` ni tu API Key

```
# Archivo .gitignore (para Git)
.env
.venv
__pycache__
*.pyc
```

## 📈 Limitaciones Conocidas

- ✋ Máximo 50MB por archivo PDF
- ✋ Documentos muy grandes se truncan a 60KB de texto (~15K tokens)
- ✋ PDFs protegidos con contraseña no se procesan automáticamente
- ✋ PDFs scaneados sin OCR no tienen texto extraíble

## 🎯 Roadmap Futuro

- [ ] Soporte para OCR en documentos escaneados
- [ ] Análisis comparativo de múltiples documentos
- [ ] Base de datos SQLite para historial persistente
- [ ] Exportación a PDF, Word, Google Docs
- [ ] Configuración de prompts personalizados
- [ ] API REST para integración con otras aplicaciones
- [ ] Soporte para múltiples idiomas

## 📞 Soporte y Contribuciones

Si encuentras bugs o tienes sugerencias:

1. Revisa la sección de [Solución de Problemas](#-solución-de-problemas)
2. Consulta la documentación de [Streamlit](https://docs.streamlit.io/)
3. Revisa los reportes de error del API: [OpenRouter Docs](https://openrouter.ai/docs)

## 📄 Licencia

Este proyecto se proporciona como está para uso personal y educativo.

## 🙌 Créditos

- **Streamlit**: por la fantástica framework web
- **PyMuPDF (fitz)**: para extracción de PDFs
- **OpenRouter**: por proporcionar acceso a múltiples LLMs
- **Comunidad Open Source**: por las librerías excelentes

---

**Versión:** 1.0  
**Última actualización:** Abril 2024  
**Made with ❤️ for document analysis**

Para más ayuda, consulta la interfaz integrada de la aplicación (botón "💡 Ayuda" en el panel lateral).
