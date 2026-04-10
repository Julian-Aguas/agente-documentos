# 🤝 Guía de Contribución

¡Gracias por tu interés en contribuir a Agente Local de Documentos! 

## Cómo Contribuir

### 1. Fork del Repositorio
```bash
# Haz un fork en GitHub
# Luego clona tu fork
git clone https://github.com/TU-USERNAME/agente-documentos.git
cd agente-documentos
```

### 2. Crea una Rama
```bash
git checkout -b feature/tu-feature
# o
git checkout -b fix/tu-fix
```

### 3. Realiza tus Cambios
- Sigue el estilo de código existente
- Mantén commits claros y descriptivos
- Comenta código complejo
- Prueba localmente

### 4. Commit y Push
```bash
git add .
git commit -m "breve descripción del cambio"
git push origin tu-rama
```

### 5. Crea un Pull Request
- Describe claramente qué cambios hiciste
- Vincula issues relacionados
- Espera la revisión

---

## Estándares de Código

### Python
- Usa **PEP 8** (formatea con `black` si es posible)
- Escribe docstrings para funciones y clases
- Mantén líneas < 100 caracteres
- Comenta en inglés, UI en español

### Commits
```bash
# ✅ Bien
git commit -m "fix: corrige timeout en API calls"
git commit -m "feat: agrega soporte para OCR"
git commit -m "docs: actualiza README"

# ❌ Evita
git commit -m "cambios"
git commit -m "fix stuff"
```

### Tipos de Commits
- `feat:` Nueva característica
- `fix:` Corrección de bug
- `docs:` Cambios de documentación
- `style:` Formato, sin cambiar lógica
- `refactor:` Cambio de código sin nuevas features
- `test:` Agregar/actualizar tests
- `chore:` Cambios de build, dependencies, etc.

---

## Reportar Bugs

### Antes de Reportar
- Busca en issues existentes
- Prueba con la versión más reciente
- Reúne información del error

### Información Necesaria
```markdown
**Descripción del bug:**
[Breve descripción]

**Pasos para reproducir:**
1. ...
2. ...
3. ...

**Comportamiento esperado:**
[Qué debería pasar]

**Comportamiento actual:**
[Qué está pasando]

**Información del sistema:**
- OS: [Windows/macOS/Linux]
- Python version: [3.8/3.9/etc]
- Versión del app: [1.0]

**Logs/Errores:**
[Pega el error completo]
```

---

## Solicitar Nuevas Características

```markdown
**Descripción:**
[Qué quieres que haga]

**Caso de Uso:**
[Por qué lo necesitas]

**Solución Propuesta:**
[Cómo debería funcionar]

**Alternativas Consideradas:**
[Otras formas de resolver esto]
```

---

## Configuración Local

```bash
# Clona el repo
git clone https://github.com/TU-USERNAME/agente-documentos.git
cd agente-documentos

# Crea entorno virtual
python -m venv .venv

# Activa el entorno
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Instala dependencias
pip install -r agente-documentos/requirements.txt

# Copia .env.example a .env
cp agente-documentos/.env.example agente-documentos/.env
# Agrega tu API key

# Corre la app
streamlit run agente-documentos/app.py
```

---

## Testing

```bash
# Prueba el PDF parsing
python -c "from agente_documentos.pdf_utils import extract_text_from_pdf; print('✅ PDF parsing works')"

# Prueba la integración LLM
python -c "from agente_documentos.agent import LLMAgent; agent = LLMAgent(); print('✅ LLM agent works')"
```

---

## Áreas de Contribución Bienvenidas

- ✅ Traducción a otros idiomas
- ✅ Soporte para más formatos (DOCX, TXT, etc.)
- ✅ Mejoras de UI/UX
- ✅ Optimización de performance
- ✅ Documentación adicional
- ✅ Tests unitarios
- ✅ Soporte para OCR
- ✅ Exportación a múltiples formatos

---

## Respuesta de Mantenedores

- Se revisarán PRs en máximo 7 días
- Se etiquetarán issues por prioridad
- Se notificará si se necesitan cambios

---

## Código de Conducta

Lee [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) para las normas de la comunidad.

---

**¡Gracias por contribuir! 🙌**
