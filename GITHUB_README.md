# Agente Local de Documentos

<div align="center">

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![GitHub Issues](https://img.shields.io/github/issues/tu-usuario/agente-documentos)](https://github.com/tu-usuario/agente-documentos/issues)
[![GitHub Stars](https://img.shields.io/github/stars/tu-usuario/agente-documentos?style=social)](https://github.com/tu-usuario/agente-documentos)

**Analiza tus documentos PDF con IA. Resúmenes inteligentes en español.**

[Inicio Rápido](#-inicio-rápido) • [Características](#-características) • [Documentación](#-documentación) • [Contribuir](#-contribuir)

</div>

---

## 📄 Acerca de

**Agente Local de Documentos** es una aplicación web moderna que te permite:

- 📤 Cargar archivos PDF
- 🤖 Analizar con IA (LLM)
- 📊 Obtener análisis estructurado
- 💾 Descargar resultados
- 🇪🇸 Todo en español

Perfecta para:
- 📋 Análisis de propuestas y reportes
- 📑 Extracción de información clave
- ✅ Generación de tareas accionables
- ⚠️ Identificación de riesgos
- 🎯 Toma de decisiones rápida

---

## 🎯 Características Principales

| Característica | Descripción |
|---|---|
| **📤 Carga Fácil** | Interfaz drag-and-drop para PDFs |
| **🤖 IA Inteligente** | Usa OpenRouter, OpenAI o cualquier LLM compatible |
| **📊 Análisis Estructurado** | 5 secciones: resumen, puntos, tareas, riesgos, conclusión |
| **💾 Exportación** | Descarga resultados en formato TXT |
| **📋 Historial** | Acceso rápido a análisis anteriores |
| **🇪🇸 Español Completo** | UI y respuestas 100% en español |
| **🔒 Seguro** | Tus documentos no se almacenan |
| **⚡ Rápido** | Análisis en 1-2 minutos |

---

## 🚀 Inicio Rápido

### Requisitos
- Python 3.8+
- API Key (gratis en [OpenRouter](https://openrouter.ai/keys))

### Instalación en 3 pasos

```bash
# 1. Clona el repositorio
git clone https://github.com/tu-usuario/agente-documentos.git
cd agente-documentos

# 2. Instala dependencias
pip install -r agente-documentos/requirements.txt

# 3. Configura tu API Key
cp agente-documentos/.env.example agente-documentos/.env
# Edita .env y añade tu API Key de OpenRouter
```

### Ejecuta la App

```bash
cd agente-documentos
streamlit run app.py
```

Se abrirá en: **http://localhost:8501** 🎉

---

## 📖 Documentación

- **[README Completo](./agente-documentos/README.md)** - Documentación detallada
- **[Guía Rápida](./agente-documentos/QUICK_START.md)** - Inicio en 5 minutos
- **[Guía de Despliegue](./agente-documentos/DEPLOYMENT_GUIDE.md)** - Configuración avanzada
- **[Contribuir](./agente-documentos/CONTRIBUTING.md)** - Cómo contribuir al proyecto

---

## 📸 Screenshots

[Aquí van tus screenshots - añade capturas de pantalla de la interfaz]

---

## 🏗️ Estructura del Proyecto

```
agente-documentos/
├── app.py                 # Aplicación principal Streamlit
├── agent.py               # Integración LLM
├── pdf_utils.py           # Procesamiento de PDFs
├── prompts.py             # Prompts en español
├── utils.py               # Utilidades
├── requirements.txt       # Dependencias
├── README.md              # Documentación completa
├── QUICK_START.md         # Guía rápida
└── samples/
    └── sample_document.pdf # Documento de ejemplo
```

---

## 🔧 Configuración

### Variables de Entorno

```env
# Requerido - Tu API Key
LLM_API_KEY=sk-or-xxx-your-key

# Opcional - URL del API (default: OpenRouter)
LLM_API_URL=https://openrouter.ai/api/v1/chat/completions

# Opcional - Modelo a usar (default: Mistral 7B)
LLM_MODEL=openai/gpt-3.5-turbo
```

### Proveedores de LLM Soportados

| Proveedor | URL | Ventajas |
|---|---|---|
| **OpenRouter** ⭐ | https://openrouter.ai | Gratis, múltiples modelos |
| **OpenAI** | https://api.openai.com | Máxima calidad |
| **Azure OpenAI** | Azure Portal | Empresa |
| **Local** | http://localhost:8000 | Privacidad total |

---

## 🤝 Contribuir

¡Las contribuciones son bienvenidas! Lee [CONTRIBUTING.md](./agente-documentos/CONTRIBUTING.md)

### Areas en Busca de Help
- [ ] 🌍 Traducción a otros idiomas
- [ ] 📖 Documentación mejorada
- [ ] 🐛 Reporte y fixes de bugs
- [ ] ✨ Nuevas características
- [ ] 🧪 Tests unitarios
- [ ] 📚 Ejemplos y tutoriales

### Paso a Paso para Contribuir

```bash
# 1. Fork y clona
git clone https://github.com/TU-USERNAME/agente-documentos.git

# 2. Crea rama
git checkout -b feature/tu-feature

# 3. Realiza cambios
# ... edita archivos ...

# 4. Commit & Push
git add .
git commit -m "feat: tu cambio"
git push origin feature/tu-feature

# 5. Abre Pull Request
# En GitHub: crea un PR con descripción clara
```

---

## 📊 Roadmap

### ✅ Completado (v1.0)
- [x] Interfaz Streamlit completa
- [x] Integración LLM
- [x] Análisis de PDFs
- [x] Exportación a TXT
- [x] Historial de documentos

### 🔄 En Desarrollo (v1.1)
- [ ] Soporte para OCR
- [ ] Exportación a múltiples formatos
- [ ] Caché de respuestas
- [ ] Dark mode
- [ ] Más idiomas

### 📋 Planificado (v2.0)
- [ ] Base de datos persistente
- [ ] API REST
- [ ] Docker
- [ ] Tests automatizados
- [ ] Dashboard de analíticas

---

## 📝 Licencia

Este proyecto está bajo la licencia MIT. Ver [LICENSE](./agente-documentos/LICENSE) para detalles.

---

## ⭐ Agradecimientos

- [Streamlit](https://streamlit.io/) por la fantástica framework
- [OpenRouter](https://openrouter.ai/) por acceso a múltiples LLMs
- [PyMuPDF](https://pymupdf.readthedocs.io/) por extracción de PDFs
- Todos los [contribuyentes](https://github.com/tu-usuario/agente-documentos/graphs/contributors) ❤️

---

## 💬 Comunidad

- 📧 Email: [tu-email@ejemplo.com]
- 💬 Discussions: [GitHub Discussions](https://github.com/tu-usuario/agente-documentos/discussions)
- 🐛 Issues: [GitHub Issues](https://github.com/tu-usuario/agente-documentos/issues)
- 🌍 Discord: [Tu servidor Discord]

---

## 🔒 Seguridad

Para reportar vulnerabilidades, por favor lee [SECURITY.md](./agente-documentos/SECURITY.md)

---

<div align="center">

**[⬆ volver arriba](#agente-local-de-documentos)**

Hecho con ❤️ por [Tu Nombre]

</div>
