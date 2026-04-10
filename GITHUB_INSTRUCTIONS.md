# 🚀 Instrucciones para Subir a GitHub

## Paso 1: Crear Repositorio en GitHub

1. Ve a https://github.com/new
2. **Repository name:** `agente-documentos`
3. **Description:** "Agente Local de Documentos - Analyze PDFs with AI"
4. **Visibility:** Public ✅
5. **NO inicialices con README** (ya tenemos uno)
6. Click "Create repository"

---

## Paso 2: Preparar el Proyecto Local

```powershell
# Ve a la carpeta principal del proyecto
cd c:\Users\julia\OneDrive\Documentos\agente-documentos

# Inicializa git (si no está hecho)
git init
git config user.name "Tu Nombre"
git config user.email "tu-email@ejemplo.com"
```

---

## Paso 3: Verificar .gitignore

✅ El `.gitignore` ya está configurado correctamente con:
- `.env` (credenciales)
- `.venv/` (entorno virtual)
- `__pycache__/`
- Archivos temporales

---

## Paso 4: Agregar Archivos y Hacer Commit

```powershell
# Copiar el README de GitHub a la raíz
Copy-Item agente-documentos\GITHUB_README.md README.md

# Agregar todos los archivos
git add .

# Ver qué se va a subir
git status

# Primer commit
git commit -m "feat: initial commit - Agente Local de Documentos v1.0"
```

---

## Paso 5: Conectar con GitHub

```powershell
# Reemplaza TU-USERNAME con tu usuario de GitHub
git remote add origin https://github.com/TU-USERNAME/agente-documentos.git

# Renombra rama a main (si es necesario)
git branch -M main

# Sube los cambios
git push -u origin main
```

---

## Paso 6: Personalizar el Repositorio

### En GitHub:

1. **Settings → General**
   - Description: "Agente Local de Documentos - Analyze PDFs with AI"
   - Website: (tu website si tienes)
   - Topics: `python`, `streamlit`, `llm`, `pdf`, `spanish`

2. **Settings → Pages**
   - Source: Deploy from a branch
   - Branch: main
   - Folder: / (root)
   - Click Save

3. **About (lado derecho)**
   - Click ⚙️ (gear icon)
   - Selecciona "Use your template repository"
   - Add topics: `pdf-analysis`, `ai`, `document-processing`, `spanish`

### Se Agrega Automáticamente:

✅ License badge (MIT)
✅ Issues templates (bug, feature)
✅ Pull Request template
✅ GitHub Actions workflows
✅ Dependabot para actualizaciones

---

## Paso 7: Verificar Todo

Cosas que deberías ver en GitHub:

- ✅ README.md con badges
- ✅ Carpeta `.github/` con workflows
- ✅ LICENSE file
- ✅ CONTRIBUTING.md
- ✅ SECURITY.md
- ✅ CHANGELOG.md
- ✅ Pestaña "Releases" (una vez que hagas tag)

---

## Paso 8: Crear Primera Release (Opcional pero Recomendado)

```powershell
# Crear un tag
git tag -a v1.0.0 -m "Release v1.0.0 - Initial release"

# Sube los tags
git push origin v1.0.0
```

Luego en GitHub:
1. Ve a "Releases"
2. Haz clic en "Draft a new release"
3. Selecciona el tag `v1.0.0`
4. Llena la descripción (puedes copiar del CHANGELOG.md)
5. Click "Publish release"

---

## Archivos Creados para GitHub

### Configuración de Proyecto
- ✅ `setup.py` - Configuración de instalación
- ✅ `setup.cfg` - Configuración adicional
- ✅ `pyproject.toml` - Estándar moderno
- ✅ `LICENSE` - MIT License

### Documentación
- ✅ `CONTRIBUTING.md` - Guía de contribución
- ✅ `CODE_OF_CONDUCT.md` - Código de conducta
- ✅ `SECURITY.md` - Política de seguridad
- ✅ `CHANGELOG.md` - Historial de cambios

### GitHub Specifics
- ✅ `.github/workflows/tests.yml` - CI/CD pipeline
- ✅ `.github/dependabot.yml` - Actualizaciones automáticas
- ✅ `.github/ISSUE_TEMPLATE/` - Plantillas de issues
- ✅ `.github/pull_request_template.md` - Plantilla de PR

### Mejoras
- ✅ `.gitignore` - Ampliado con más patrones
- ✅ `GITHUB_README.md` - README profesional para GitHub

---

## Comandos Rápidos

### Después de la Instalación Inicial

```powershell
# Actualizar código y subir cambios
git add .
git commit -m "feat: descripción de cambios"
git push origin main

# Crear rama para features
git checkout -b feature/nueva-feature
# ... realiza cambios ...
git add .
git commit -m "feat: nueva feature"
git push origin feature/nueva-feature
# Luego en GitHub: abre un Pull Request

# Ver estado
git status
git log --oneline
```

---

## Badges para el README

Puedes agregar estos badges a tu README:

```markdown
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![GitHub Issues](https://img.shields.io/github/issues/tu-usuario/agente-documentos)](../../issues)
[![GitHub Stars](https://img.shields.io/github/stars/tu-usuario/agente-documentos?style=social)](../../)
```

---

## Topics Recomendados

Agregar estos topics en GitHub (Settings → General → Topics):

```
python streamlit llm pdf spanish document-analysis ai nlp
```

---

## Próximos Pasos

1. ✅ Sube el proyecto a GitHub
2. ✅ Comparte el link en redes sociales
3. ✅ Invita a amigos a colaborar
4. ✅ Responde issues y PRs
5. ✅ Mantén el proyecto actualizado

---

## Recursos Útiles

- [GitHub Docs](https://docs.github.com)
- [Git Cheat Sheet](https://github.github.com/training-kit/)
- [Conventional Commits](https://www.conventionalcommits.org/es/)
- [Keep a Changelog](https://keepachangelog.com/es-ES/)

---

## ¿Necesitas Ayuda?

- 📖 Lee [CONTRIBUTING.md](agente-documentos/CONTRIBUTING.md)
- 🐛 Crea un issue en GitHub
- 💬 Abre una discussion
- 📧 Contacta a los mantenedores

---

**¡Tu proyecto está listo para GitHub! 🚀**

Reemplaza `TU-USERNAME` con tu username de GitHub y ¡sigue los pasos!
