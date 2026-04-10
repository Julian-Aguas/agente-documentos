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

## 🚀 Quick Start

```bash
# Clonar repositorio
git clone https://github.com/Julian-Aguas/agente-documentos.git
cd agente-documentos/agente-documentos

# Crear entorno virtual
python -m venv .venv
.venv\Scripts\activate  # Windows
# source .venv/bin/activate  # macOS/Linux

# Instalar dependencias
pip install -r requirements.txt

# Configurar API (copiar .env.example a .env y agregar tu API key)
copy .env.example .env
# Edita el archivo .env con tu API key

# Ejecutar aplicación
streamlit run app.py
```

Se abrirá automáticamente en `http://localhost:8501`

## 📚 Documentación Completa

Para más detalles sobre instalación, uso y configuración, consulta los archivos de documentación en la carpeta `agente-documentos/`:

- **[📖 README Completo](agente-documentos/README.md)** - Guía completa de instalación y uso
- **[⚡ Quick Start](agente-documentos/QUICK_START.md)** - Setup en 5 minutos
- **[🚀 Deployment Guide](agente-documentos/DEPLOYMENT_GUIDE.md)** - Despliegue en producción
- **[📐 Architecture](agente-documentos/ARCHITECTURE.md)** - Arquitectura del sistema y patrones de diseño
- **[🛠️ Tech Stack](agente-documentos/TECH_STACK.md)** - Stack tecnológico y skills demonstrados

## 📂 Estructura del Proyecto

```
agente-documentos/
├── agente-documentos/           # Código fuente principal
│   ├── app.py                   # Aplicación principal Streamlit
│   ├── agent.py                 # Integración con LLM API
│   ├── pdf_utils.py             # Utilidades para PDF
│   ├── prompts.py               # Prompts y parseo
│   ├── utils.py                 # Funciones auxiliares
│   ├── requirements.txt         # Dependencias Python
│   ├── .env.example             # Plantilla de configuración
│   └── README.md                # Documentación detallada
├── .github/
│   ├── workflows/               # GitHub Actions CI/CD
│   ├── ISSUE_TEMPLATE/          # Plantillas de issues
│   └── pull_request_template.md # Plantilla de PRs
├── LICENSE                      # Licencia MIT
├── README.md                    # Este archivo
└── .gitignore
```

## 🎯 Características Técnicas

- **Backend**: Python 3.8+
- **Frontend**: Streamlit 1.28.1
- **PDF Processing**: PyMuPDF 1.23.8
- **LLM Integration**: requests + OpenAI-compatible APIs
- **Configuration**: python-dotenv
- **CI/CD**: GitHub Actions
- **Testing**: pytest (setup ready)

## 💡 Uso Básico

1. **Carga un PDF** - Selecciona tu documento (máximo 50MB)
2. **Analiza** - Haz clic en "🚀 Analizar Documento"
3. **Revisa resultados** - 5 secciones expandibles con análisis en español
4. **Descarga** - Exporta el análisis a archivo TXT

## ⚙️ Configuración

### Paso 1: Obtener API Key

**Opción A: OpenRouter (RECOMENDADO - Gratuito)**
1. Crea cuenta en [openrouter.ai](https://openrouter.ai)
2. Copia tu API Key desde la sección de "Keys"

**Opción B: OpenAI**
1. Crea cuenta en [platform.openai.com](https://platform.openai.com)
2. Genera una API Key

### Paso 2: Configurar .env

```bash
copy .env.example .env
# Edita con tu editor favorito
```

```
LLM_API_URL=https://openrouter.ai/api/v1/chat/completions
LLM_API_KEY=sk-or-xxxxxxxxxxxx
LLM_MODEL=mistralai/mistral-7b-instruct:free
```

## 🔐 Privacidad y Seguridad

⚠️ **IMPORTANTE**: 
- NUNCA compartas tu `.env` ni tu API Key
- El archivo `.env` está en `.gitignore` (no se sube a Git)
- Los documentos se procesan en tiempo real sin almacenamiento permanente
- Verifica las políticas de privacidad de tu proveedor LLM

## 📊 Indicadores de Rendimiento

- ⚡ **Velocidad**: 1-2 minutos por documento
- 💰 **Costo**: En OpenRouter muchos modelos son GRATIS
- 📄 **Capacidad**: Hasta 50MB por archivo
- 🔄 **Historial**: Sesión en memoria (se limpia al recargar)

## 🐛 Solución de Problemas

### "API Key NO CONFIGURADA"
```bash
# Verifica que existe .env con tu API key
# Reinicia la aplicación
streamlit run app.py
```

### "Timeout - El servidor tardó demasiado"
- Usa un documento más pequeño
- Cambia a un modelo más rápido (mistral-7b)
- Verifica tu conexión a internet

### "PDF no contiene texto extraíble"
- Usa OCR en [iLovePDF](https://www.ilovepdf.com/)
- Convierte desde documento original

Consulta [README.md](agente-documentos/README.md) para más soluciones.

## 🎯 Casos de Uso

✅ Análisis de reportes  
✅ Resumen de documentos largos  
✅ Extracción de puntos clave  
✅ Identificación de tareas  
✅ Evaluación de riesgos  

## 🔄 CI/CD Pipeline

Este proyecto usa **GitHub Actions** para:
- ✅ Ejecutar tests automáticamente
- ✅ Verificar código con linters
- ✅ Verificar dependencias
- ✅ Actualizar dependencias con Dependabot

## 📈 Roadmap

- [ ] Soporte OCR para documentos escaneados
- [ ] Base de datos SQLite para historial persistente
- [ ] REST API
- [ ] Docker containerization
- [ ] Análisis de múltiples documentos
- [ ] Exportación a PDF/Word
- [ ] Soporte para múltiples idiomas

## 👨‍💻 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Fork el repositorio
2. Crea una rama (`git checkout -b feature/amazing-feature`)
3. Commit tus cambios (`git commit -m 'Add amazing feature'`)
4. Push a la rama (`git push origin feature/amazing-feature`)
5. Abre un Pull Request

Consulta [CONTRIBUTING.md](agente-documentos/CONTRIBUTING.md) para más detalles.

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver [LICENSE](LICENSE) para detalles.

## 📞 Contacto y Soporte

- 📧 Issues: [GitHub Issues](https://github.com/Julian-Aguas/agente-documentos/issues)
- 🐛 Bugs: Abre un issue con el tag `bug`
- 💡 Features: Abre un issue con el tag `enhancement`

## 🙌 Créditos

- **Streamlit** - Fantástica framework web
- **PyMuPDF** - Extracción de PDFs
- **OpenRouter** - Acceso a múltiples LLMs
- **Open Source Community** - Librerías excelentes

---

**Versión:** 1.0.0  
**Status:** ✅ Production-Ready  
**Última actualización:** Abril 2026  

**Made with ❤️ for document analysis**

[⭐ Danos una estrella si te resulta útil!](https://github.com/Julian-Aguas/agente-documentos)
