# 🚀 Guía Rápida - Comienza en 5 Minutos

## Paso 1: Configurar la API Key (30 segundos)

### Opción A: OpenRouter (GRATUITO - Recomendado)

1. Ve a: https://openrouter.ai/keys
2. Crea una cuenta (GitHub, Google, etc.)
3. Copia tu API Key
4. En la carpeta del proyecto, crea un archivo `.env`:

```
LLM_API_URL=https://openrouter.ai/api/v1/chat/completions
LLM_API_KEY=sk-or-xxx-xxxxxxxxxxxxxxx
LLM_MODEL=mistralai/mistral-7b-instruct:free
```

### Opción B: OpenAI (Con costo)

```
LLM_API_URL=https://api.openai.com/v1/chat/completions
LLM_API_KEY=sk-...
LLM_MODEL=gpt-3.5-turbo
```

---

## Paso 2: Ejecutar la Aplicación (2 minutos)

### Windows - Command Prompt
```bash
cd c:\Users\julia\OneDrive\Documentos\agente-documentos
.venv\Scripts\activate
streamlit run agente-documentos/app.py
```

### Windows - PowerShell
```bash
cd 'c:\Users\julia\OneDrive\Documentos\agente-documentos'
. .\.venv\Scripts\Activate.ps1
streamlit run agente-documentos/app.py
```

### macOS/Linux
```bash
cd ~/tu-carpeta/agente-documentos
source .venv/bin/activate
streamlit run app.py
```

**Se abrirá automáticamente en tu navegador:** http://localhost:8501

---

## Paso 3: Usar la Aplicación (2 minutos)

1. **Carga un PDF**
   - Haz clic en "Selecciona un archivo PDF"
   - Usa el archivo de ejemplo: `samples/sample_document.pdf`

2. **Analiza**
   - Haz clic en "🚀 Analizar Documento"
   - Espera 1-2 minutos

3. **Descarga Resultados**
   - Haz clic en "⬇️ Descargar Análisis (TXT)"

---

## ✅ Verificar que Todo Funciona

Debería ver:
- ✅ Título: "Agente Local de Documentos"
- ✅ Panel de carga de archivos
- ✅ Botón azul "Analizar Documento"
- ✅ Historial en la barra lateral izquierda

---

## 🔧 Troubleshooting Rápido

| Problema | Solución |
|----------|----------|
| "streamlit: command not found" | Activa venv: `.venv\Scripts\activate` |
| "API Key NO CONFIGURADA" | Crea `.env` con tu API Key |
| "Timeout" | Intenta con PDF más pequeño o modelo más rápido |
| Navegador no abre | Abre manualmente: http://localhost:8501 |

---

## 📚 Siguiente Paso

Lee `README.md` para documentación completa, configuración avanzada y características.

**¡Listo! Ya está todo funcionando 🎉**
