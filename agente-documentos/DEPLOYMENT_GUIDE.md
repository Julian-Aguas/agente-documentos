# 🎯 DEPLOYMENT GUIDE - Local Document Agent

## ✅ PROJECT COMPLETE

Your **Agente Local de Documentos** project is fully implemented, tested, and ready to use!

---

## 📍 Project Location

```
c:\Users\julia\OneDrive\Documentos\agente-documentos\agente-documentos\
```

---

## 📦 What's Included

### ✅ Core Files
- `app.py` — Main Streamlit application
- `agent.py` — LLM API integration
- `pdf_utils.py` — PDF processing
- `prompts.py` — Spanish prompts and response parsing
- `utils.py` — Helper functions
- `.env.example` — Configuration template
- `.gitignore` — Git ignore rules

### ✅ Documentation
- `README.md` — Complete guide (Spanish)
- `QUICK_START.md` — 5-minute quick start (Spanish)
- `DEPLOYMENT_GUIDE.md` — This file

### ✅ Development Files
- `requirements.txt` — All dependencies
- `generate_sample_pdf.py` — Sample PDF generator
- `samples/sample_document.pdf` — Test document

### ✅ Environment
- `.venv/` — Virtual environment with all packages installed

---

## 🚀 QUICK START (Copy & Paste)

### 1. Create Configuration File

**Windows (PowerShell):**
```powershell
cd 'c:\Users\julia\OneDrive\Documentos\agente-documentos\agente-documentos'
Copy-Item .env.example .env
# Open .env with Notepad and add your API key
notepad .env
```

**Windows (Command Prompt):**
```cmd
cd c:\Users\julia\OneDrive\Documentos\agente-documentos\agente-documentos
copy .env.example .env
# Open .env with Notepad and add your API key
notepad .env
```

### 2. Activate Virtual Environment

**PowerShell:**
```powershell
cd 'c:\Users\julia\OneDrive\Documentos\agente-documentos'
. .\.venv\Scripts\Activate.ps1
```

**Command Prompt:**
```cmd
cd c:\Users\julia\OneDrive\Documentos\agente-documentos
.venv\Scripts\activate
```

### 3. Run the Application

```bash
streamlit run agente-documentos/app.py
```

**Result:** Browser automatically opens to `http://localhost:8501`

---

## 🔑 Getting Your API Key (Choose One)

### Option 1: OpenRouter (RECOMMENDED - FREE)

1. Go to: https://openrouter.ai/keys
2. Sign up (GitHub, Google, Discord)
3. Click "Create Key"
4. Copy the key
5. Paste into `.env`:
   ```
   LLM_API_KEY=sk-or-xxx-your-key-here
   ```

### Option 2: OpenAI (PAID)

1. Go to: https://platform.openai.com/api-keys
2. Sign in with OpenAI account
3. Click "Create new secret key"
4. Copy the key
5. Update `.env`:
   ```
   LLM_API_URL=https://api.openai.com/v1/chat/completions
   LLM_API_KEY=sk-your-key-here
   LLM_MODEL=gpt-3.5-turbo
   ```

### Option 3: Other Providers

Update `.env` with your provider's details:
```
LLM_API_URL=https://your-provider/v1/chat/completions
LLM_API_KEY=your-api-key
LLM_MODEL=your-model-name
```

---

## 📝 Configuration File (.env)

Create this file and fill in your API key:

```env
# REQUIRED: Your API key from OpenRouter, OpenAI, or other provider
LLM_API_KEY=sk-or-xxx-your-key-here

# OPTIONAL: API endpoint (default: OpenRouter)
LLM_API_URL=https://openrouter.ai/api/v1/chat/completions

# OPTIONAL: Model to use (default: free Mistral)
LLM_MODEL=mistralai/mistral-7b-instruct:free
```

---

## 📖 How to Use

1. **Load PDF**
   - Click "Selecciona un archivo PDF"
   - Choose a PDF file (max 50MB)
   - System extracts text automatically

2. **Analyze**
   - Click "🚀 Analizar Documento"
   - Wait for AI analysis (1-2 minutes)
   - Results appear on the right side

3. **View Results**
   - **Resumen Ejecutivo** - Executive summary
   - **Puntos Clave** - Key points
   - **Tareas Accionables** - What to do
   - **Riesgos o Vacíos** - Issues identified
   - **Conclusión** - Final conclusion

4. **Download**
   - Click "⬇️ Descargar Análisis (TXT)"
   - Save the formatted report

5. **History**
   - Left sidebar shows recent documents
   - Click any document to view previous analysis

---

## ✅ Testing Your Setup

### Test 1: Check Python Environment
```bash
python --version
```
Should show Python 3.8+

### Test 2: Check Virtual Environment
You should see `(.venv)` at the start of your terminal prompt

### Test 3: Test with Sample PDF
1. Run the app: `streamlit run agente-documentos/app.py`
2. Use sample file: `samples/sample_document.pdf`
3. Click "Analizar Documento"
4. Should complete in 1-2 minutes

### Test 4: Test Download
1. After analysis completes
2. Click "⬇️ Descargar Análisis (TXT)"
3. File should download with timestamp in filename

---

## 🔧 Troubleshooting

### Problem: "No module named 'streamlit'"
**Solution:** Activate virtual environment
```bash
# Windows PowerShell
. .\.venv\Scripts\Activate.ps1

# Windows Command Prompt
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate
```

### Problem: "API Key NO CONFIGURADA"
**Solution:** Create `.env` file with API key
1. Copy: `cp .env.example .env`
2. Edit: Open `.env` in text editor
3. Add your API key: `LLM_API_KEY=sk-...`
4. Save and restart Streamlit

### Problem: "Timeout" or slow responses
**Solution:** 
- Use a smaller PDF
- Try a faster model (e.g., mistral-7b)
- Check internet connection
- Increase timeout if needed

### Problem: "Cannot extract text from PDF"
**Solution:**
- PDF might be scanned image (no OCR)
- Try extracting text in Adobe Reader first
- Use different PDF file

### Problem: "Port 8501 already in use"
**Solution:** 
```bash
streamlit run agente-documentos/app.py --server.port 8502
```

---

## 📊 File Structure

```
agente-documentos/
├── .venv/                      # Virtual environment (ready to use)
├── agente-documentos/
│   ├── app.py                  # Main Streamlit app
│   ├── agent.py                # LLM integration
│   ├── pdf_utils.py            # PDF processing
│   ├── prompts.py              # Spanish prompts
│   ├── utils.py                # Helper functions
│   ├── requirements.txt         # Dependencies list
│   ├── .env.example            # Config template
│   ├── .gitignore              # Git ignore rules
│   ├── README.md               # Full documentation
│   ├── QUICK_START.md          # Quick guide
│   ├── DEPLOYMENT_GUIDE.md     # This file
│   ├── generate_sample_pdf.py  # Sample generator
│   └── samples/
│       └── sample_document.pdf # Test document
└── .venv/                      # (Parent level)
```

---

## 🌍 Environment Variables Explained

| Variable | Purpose | Default | Example |
|----------|---------|---------|---------|
| `LLM_API_KEY` | Your API authentication key | None (REQUIRED) | `sk-or-xxxxx` |
| `LLM_API_URL` | API endpoint URL | OpenRouter | `https://openrouter.ai/api/v1/chat/completions` |
| `LLM_MODEL` | Which AI model to use | Mistral 7B | `gpt-3.5-turbo` |

---

## 🎓 Available Models on OpenRouter

| Model | Speed | Cost | Best For |
|-------|-------|------|----------|
| `mistralai/mistral-7b-instruct:free` | ⚡ Fast | 💰 Free | Quick tests |
| `meta-llama/llama-2-70b` | ⚡⚡ Normal | 💰 Medium | Balanced |
| `openai/gpt-3.5-turbo` | ⚡⚡ Normal | 💰$ | Best quality |
| `openai/gpt-4` | 🐢 Slow | 💰$$ | Premium quality |

---

## 🔒 Security Notes

⚠️ **IMPORTANT:**

1. **Never commit `.env` file** - Add to `.gitignore` (already done)
2. **Keep API key private** - Don't share or publish
3. **Use `.env` for credentials** - Not in code
4. **Rotate keys regularly** - For security

---

## 📈 Performance Tips

1. **Use smaller PDFs** for faster processing (< 5MB)
2. **Choose faster models** for quick responses (mistral-7b)
3. **Batch analysis** — Process multiple documents sequentially
4. **Monitor API usage** if using paid models

---

## 🚀 Deployment Options (Advanced)

### Local Machine
✅ Already set up - Ready to use

### Docker
Add this Dockerfile to project root:
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install -r agente-documentos/requirements.txt
CMD ["streamlit", "run", "agente-documentos/app.py"]
```

### Cloud (Streamlit Cloud)
1. Push to GitHub
2. Deploy at: https://streamlit.io/cloud
3. Connect repository
4. Set environment variables in dashboard

---

## 📞 Support

### Documentation
- Full guide: [README.md](./README.md)
- Quick start: [QUICK_START.md](./QUICK_START.md)
- This guide: DEPLOYMENT_GUIDE.md

### API Providers
- OpenRouter: https://openrouter.ai/docs
- OpenAI: https://platform.openai.com/docs
- Streamlit: https://docs.streamlit.io

---

## ✨ Next Steps

### Immediate (Next 5 minutes)
1. ✅ Create `.env` file with API key
2. ✅ Run: `streamlit run agente-documentos/app.py`
3. ✅ Upload `samples/sample_document.pdf`
4. ✅ Click "Analizar Documento"

### Future Enhancements
- Add OCR support for scanned PDFs
- Implement persistent database
- Add multiple LLM comparison
- Export to Word/PDF format
- Build REST API

---

## 🎉 You're Ready!

Everything is set up and ready to use. Just add your API key and run:

```bash
streamlit run agente-documentos/app.py
```

**Enjoy analyzing your documents! 📄✨**

---

**Project Version:** 1.0  
**Created:** April 2026  
**Language:** Spanish UI & LLM responses  
**Status:** Production Ready ✅
