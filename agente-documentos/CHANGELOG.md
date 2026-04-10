# 📜 Changelog

Todos los cambios notables en este proyecto serán documentados en este archivo.

El formato se basa en [Keep a Changelog](https://keepachangelog.com/es-ES/1.0.0/) y este proyecto adhiere a [Semantic Versioning](https://semver.org/lang/es/).

---

## [1.0.0] - 2026-04-10

### ✨ Agregado
- Interfaz Streamlit completa en español
- Carga y procesamiento de archivos PDF
- Extracción de texto con PyMuPDF
- Integración con APIs LLM compatibles con OpenAI (OpenRouter, Azure OpenAI, etc.)
- Análisis estructurado de documentos con 5 secciones:
  - Resumen Ejecutivo
  - Puntos Clave
  - Tareas Accionables
  - Riesgos o Vacíos
  - Conclusión Final
- Exportación de análisis a archivos TXT formateados
- Historial de documentos en sesión
- Lógica de reintentos automáticos para llamadas a API
- Manejo comprehensivo de errores
- Validación de archivos PDF
- Truncado automático de documentos grandes
- Documentación completa en español
- Guías de instalación paso a paso
- Ejemplos de configuración para múltiples proveedores LLM

### 📁 Inclusiones
- `app.py` - Aplicación principal Streamlit
- `agent.py` - Integración LLM con requests
- `pdf_utils.py` - Procesamiento de PDFs
- `prompts.py` - Prompts en español
- `utils.py` - Funciones auxiliares
- `requirements.txt` - Dependencias del proyecto
- `.env.example` - Plantilla de configuración
- `README.md` - Documentación completa
- `QUICK_START.md` - Guía rápida
- `DEPLOYMENT_GUIDE.md` - Guía de despliegue
- `generate_sample_pdf.py` - Generador de PDFs de prueba
- `samples/sample_document.pdf` - Documento de ejemplo

---

## [Próximas Versiones]

### 🔄 Planificado para v1.1
- [ ] Soporte para OCR en documentos escaneados
- [ ] Exportación a múltiples formatos (PDF, DOCX, XLSX)
- [ ] Caché de respuestas por documento
- [ ] Interfaz web mejorada con dark mode
- [ ] Más idiomas de interfaz

### 🔄 Planificado para v2.0
- [ ] Base de datos SQLite para historial persistente
- [ ] API REST para integración con terceros
- [ ] Soporte para análisis comparativo multidocumento
- [ ] Configuración personalizable de prompts
- [ ] Monitoreo de uso y estadísticas
- [ ] Despliegue en Docker
- [ ] Tests automatizados

### 🔄 Roadmap Largo Plazo
- [ ] Soporte para múltiples archivos simultáneamente
- [ ] Integración con Google Drive, OneDrive
- [ ] Análisis de imágenes
- [ ] Webhooks y notificaciones
- [ ] Panel de administración

---

## Contribuciones

Si tienes ideas para nuevas características o mejoras, por favor abre un issue o un Pull Request.

Lee [CONTRIBUTING.md](CONTRIBUTING.md) para más detalles sobre cómo contribuir.

---

## Versionado

Este proyecto sigue [Semantic Versioning](https://semver.org/lang/es/):
- **MAJOR**: cambios incompatibles
- **MINOR**: nuevas características compatibles
- **PATCH**: correcciones de bugs

---

**Última actualización:** Abril 10, 2026
