# 🏗️ Architecture & Design - Agente Local de Documentos

Documentación de la arquitectura, patrones de diseño y decisiones técnicas del proyecto.

---

## 📐 System Architecture

```
┌────────────────────────────────────────────────────────────────┐
│                      STREAMLIT UI LAYER                        │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────────┐    │
│  │ File Upload  │  │ Sidebar      │  │ Results Display  │    │
│  │ Button       │  │ Config       │  │ Export/History   │    │
│  │ Widgets      │  │ Status       │  │ Formatting       │    │
│  └──────────────┘  └──────────────┘  └──────────────────┘    │
└────────────┬───────────────────────────────────────────────────┘
             │ Session State
             ▼
┌────────────────────────────────────────────────────────────────┐
│                    APPLICATION LOGIC LAYER                     │
│ ┌──────────────────────────────────────────────────────────┐  │
│ │  app.py - Main orchestration & state management         │  │
│ │  ├─ Handle file uploads                                 │  │
│ │  ├─ Manage session state                                │  │
│ │  ├─ Coordinate between modules                          │  │
│ │  └─ Display results & history                           │  │
│ └──────────────────────────────────────────────────────────┘  │
└────────┬────────────────────────────────────────────────────────┘
         │
    ┌────┴─────┬──────────────┬──────────────┐
    ▼          ▼              ▼              ▼
┌────────┐ ┌────────────┐ ┌──────────┐ ┌────────┐
│PDF    │ │LLM         │ │Prompts & │ │Utils   │
│Utils  │ │Agent       │ │Formatting│ │Helpers │
├────────┤ ├────────────┤ ├──────────┤ ├────────┤
│Extract │ │• API calls │ │• Spanish │ │• Tokens│
│Validate│ │• Retry     │ │• Prompts │ │• Format│
│Truncate│ │• Error     │ │• Parse   │ │• Dates │
│        │ │  handling  │ │• Validate│ │• Files │
└────────┘ └────────────┘ └──────────┘ └────────┘
    │          │              │            │
    └──────────┴──────────────┴────────────┘
             │
             ▼
┌────────────────────────────────────────────────────────────────┐
│                    EXTERNAL SERVICES LAYER                     │
│ ┌──────────────────┐  ┌──────────────────┐                   │
│ │ PDF Files        │  │ LLM API          │                   │
│ │ (User Upload)    │  │ (OpenAI-compat)  │                   │
│ └──────────────────┘  └──────────────────┘                   │
└────────────────────────────────────────────────────────────────┘
```

---

## 📦 Module Structure

### **app.py - Main Application**

**Responsibilities:**
- Streamlit page configuration
- File upload handling
- Session state management
- Results display
- History tracking
- Download functionality

**Key Functions:**
```python
# Page setup
st.set_page_config()
st.markdown(custom_css)

# Sidebar
with st.sidebar:
    environment_status()
    upload_history()
    help_section()

# Main content
with col_main:
    upload_widget()
    analysis_button()
with col_display:
    display_results()
    download_button()
```

**Session State:**
```python
st.session_state.upload_history      # List of uploads
st.session_state.current_analysis    # Latest analysis
st.session_state.current_filename    # File name
st.session_state.current_timestamp   # Analysis time
```

---

### **agent.py - LLM Integration**

**Responsibilities:**
- API configuration
- Request formatting
- Response parsing
- Error handling
- Retry logic

**Key Class:**
```python
class LLMAgent:
    def __init__(self):
        self.api_url = os.getenv('LLM_API_URL')
        self.api_key = os.getenv('LLM_API_KEY')
        self.model = os.getenv('LLM_MODEL')
        self.timeout = 60
        self.max_retries = 3
        self.retry_delay = 2
    
    def is_configured(self) -> bool
    def get_config_info(self) -> dict
    def call_llm(self, system_prompt, user_message) -> tuple[bool, str]
```

**Error Handling Strategy:**
```
Request
  ├─ Success (200) → Return response
  ├─ Auth Error (401) → Fail immediately, return error
  ├─ Rate Limit (429) → Retry with exponential backoff
  ├─ Server Error (500+) → Retry with exponential backoff
  ├─ Timeout → Retry with exponential backoff
  └─ Connection Error → Retry with exponential backoff
```

---

### **pdf_utils.py - PDF Processing**

**Responsibilities:**
- File validation
- Text extraction
- Content truncation
- Error handling

**Key Functions:**
```python
def validate_pdf_file(file_obj) -> tuple[bool, str]
    # Checks: format, size, emptiness
    
def extract_text_from_pdf(pdf_bytes) -> dict
    # PyMuPDF extraction
    # Returns: success, text, page_count, error
    
def truncate_text(text, max_length=60000) -> str
    # Preserves sentence boundaries
    # Adds truncation note
```

**Validation Pipeline:**
```
File Upload
  ├─ Format validation (.pdf)
  ├─ Size validation (< 50MB)
  ├─ Extract attempt
  ├─ Content validation (not empty)
  └─ Return text or error
```

---

### **prompts.py - LLM Prompts & Response Handling**

**Responsibilities:**
- Spanish prompts
- JSON response parsing
- Response validation
- Format conversion

**Key Functions:**
```python
def get_system_prompt() -> str
    # Defines agent role and behavior
    # Requests JSON output with 5 sections
    
def get_analysis_prompt(document_text) -> str
    # User request with document content
    
def parse_analysis_response(response_text) -> dict
    # Parses JSON from response
    # Validates all 5 required fields
    # Returns structured dict or error
    
def format_analysis_for_display(analysis) -> dict
    # Ensures consistent display format
```

**Expected JSON Response:**
```json
{
  "resumen_ejecutivo": "string (1-3 sentences)",
  "puntos_clave": ["point 1", "point 2", ...],
  "tareas_accionables": ["task 1", "task 2", ...],
  "riesgos_o_vacios": ["risk 1", "risk 2", ...],
  "conclusion": "string (1-2 sentences)"
}
```

---

### **utils.py - Helper Utilities**

**Responsibilities:**
- Formatting utilities
- File operations
- Environment status
- Display helpers

**Key Functions:**
```python
def format_timestamp_spanish(dt) -> str
    # Spanish date formatting
    
def format_analysis_to_text(analysis) -> str
    # Beautiful TXT output with borders
    
def generate_filename_for_download(original_filename) -> str
    # Auto-generates filename with timestamp
    
def get_environment_status() -> dict
    # Returns config status for display
```

---

## 🔄 Data Flow & Interaction

### **1. File Upload Flow**

```
User selects PDF
    ↓
Streamlit file_uploader widget captures file
    ↓
validate_pdf_file()
    ├─ Check file format
    ├─ Check file size
    └─ Check file exists
    ↓
Show file info: name, size, status
    ↓
Wait for "Analyze" button click
```

### **2. PDF Processing Flow**

```
extract_text_from_pdf(pdf_bytes)
    ├─ fitz.open(stream=pdf_bytes)
    ├─ For each page:
    │  └─ page.get_text()
    ├─ Join all text
    └─ Return: success, text, pages, error
    ↓
truncate_text(text)
    ├─ Check length
    ├─ If > 60KB:
    │  ├─ Find last sentence end
    │  ├─ Truncate at sentence
    │  └─ Add truncation note
    └─ Return truncated text
```

### **3. LLM Analysis Flow**

```
LLMAgent.call_llm(system_prompt, user_message)
    ├─ Check API key configured
    ├─ Format request
    │  ├─ Headers (auth)
    │  ├─ Payload (model, messages, temp, tokens)
    │  └─ URL & timeout
    ├─ For each retry (max 3):
    │  ├─ requests.post(...)
    │  ├─ Check status code
    │  ├─ Parse JSON
    │  ├─ On 429/5xx: wait & retry
    │  └─ On error: next retry or fail
    └─ Return: (success, response_text)
```

### **4. Response Processing Flow**

```
parse_analysis_response(response_text)
    ├─ Try JSON.parse()
    ├─ On error: try regex extraction
    ├─ Validate required fields:
    │  ├─ resumen_ejecutivo
    │  ├─ puntos_clave
    │  ├─ tareas_accionables
    │  ├─ riesgos_o_vacios
    │  └─ conclusion
    └─ Return: validated dict or error
```

### **5. Display & Export Flow**

```
format_analysis_for_display(analysis)
    └─ Return clean dict
    ↓
Display in UI
├─ Expander: Resumen Ejecutivo
├─ Expander: Puntos Clave
├─ Expander: Tareas Accionables
├─ Expander: Riesgos o Vacíos
└─ Expander: Conclusión
    ↓
format_analysis_to_text(analysis)
    └─ Create formatted TXT
    ↓
st.download_button()
    └─ User downloads TXT file
```

---

## 🎨 Design Patterns Used

### **1. Separation of Concerns**
Each module has a single responsibility:
- UI in `app.py`
- LLM in `agent.py`
- PDF in `pdf_utils.py`
- Prompts in `prompts.py`
- Utils in `utils.py`

### **2. Configuration Pattern**
```python
# Instead of hardcoded values
API_KEY = os.getenv('LLM_API_KEY')  # ✅ Good
API_KEY = "sk-xxx"                   # ❌ Bad
```

### **3. Dependency Injection**
```python
def call_llm(system_prompt, user_message):
    # Dependencies passed as parameters
    pass
```

### **4. Factory Pattern**
```python
agent = LLMAgent()  # Creates configured instance
```

### **5. Data Validation Pattern**
```python
def validate_pdf_file(file_obj) -> tuple[bool, str]:
    if not file_obj.name.lower().endswith('.pdf'):
        return False, "Error: File must be PDF"
    return True, "OK"
```

### **6. Error as Value**
```python
success, response = agent.call_llm(system_prompt, user_message)
if not success:
    st.error(f"❌ {response}")  # Response contains error message
```

### **7. Session State Pattern (Streamlit-specific)**
```python
if 'upload_history' not in st.session_state:
    st.session_state.upload_history = []
```

---

## 🔐 Security Architecture

### **Layer 1: Input Validation**
```
User Input
    ├─ File format check
    ├─ File size check
    └─ Content validation
```

### **Layer 2: Credential Protection**
```
.env file (local)
    ├─ In .gitignore (never committed)
    ├─ Loaded only in memory
    └─ Never logged or displayed
```

### **Layer 3: API Communication**
```
HTTPS + Bearer Token
    ├─ TLS/SSL encryption
    ├─ Authorization header
    └─ No credentials in URL
```

### **Layer 4: Error Handling**
```
API Errors
    ├─ Sanitize error messages
    ├─ No API details exposed
    └─ Generic user messages
```

---

## 📈 Performance Considerations

### **1. Document Truncation**
- **Why:** API timeouts, high costs, slow processing
- **How:** Limit to 60KB (~15K tokens)
- **Implementation:** `truncate_text()` preserves sentence boundaries

### **2. Session State Caching**
- **Why:** Avoid re-processing same files
- **How:** Store in `st.session_state`
- **Implementation:** Check filename before re-analysing

### **3. Retry Strategy**
- **Why:** Handle transient failures
- **How:** Exponential backoff (2, 4, 8 seconds)
- **Implementation:** `for attempt in range(max_retries)`

### **4. Timeout Protection**
- **Why:** Prevent hanging requests
- **How:** 60-second timeout on API calls
- **Implementation:** `requests.post(..., timeout=60)`

---

## 🧪 Testing Strategy (Future)

### **Unit Tests**
```python
# test_pdf_utils.py
def test_validate_pdf_file():
    assert validate_pdf_file(valid_file) == (True, "OK")
    assert validate_pdf_file(invalid_file) == (False, error_msg)

# test_agent.py
def test_llm_agent_configuration():
    agent = LLMAgent()
    assert agent.is_configured() == True
```

### **Integration Tests**
```python
# test_integration.py
def test_full_pdf_to_analysis_flow():
    # Upload PDF → Extract → Analyze → Validate
    pass
```

### **E2E Tests (Streamlit)**
```python
# Use pytester or streamlit testing
def test_ui_flow():
    # Simulate user interactions
    pass
```

---

## 📊 Deployment Architecture

### **Development**
```
Local Machine
├─ Python venv
├─ .env file
└─ Streamlit dev server (localhost:8501)
```

### **Production (Future)**
```
Docker Container
├─ Python 3.11
├─ Environment variables (Docker secrets)
├─ Streamlit production server
└─ Reverse proxy (Nginx)
```

### **Cloud Options**
- **Streamlit Cloud:** Easiest (Git-connected)
- **Heroku:** Good for small projects
- **AWS/GCP/Azure:** Enterprise option
- **Docker:** Any hosting platform

---

## 🔄 CI/CD Pipeline (GitHub Actions)

```
Push to GitHub
    ↓
GitHub Actions Workflow
├─ Lint (flake8)
├─ Format check (black)
├─ Type check (mypy)
├─ Test on Python 3.8-3.13
├─ Test on Ubuntu/Windows/macOS
└─ Update dependencies (Dependabot)
    ↓
Pass/Fail ✅/❌
```

---

## 📚 Code Quality Metrics

### **Current Status**
```
Readability:     Excellent (clear naming, docstrings)
Maintainability: High (modular, DRY principle)
Testability:     Good (pure functions, no globals)
Error Handling:  Comprehensive
Documentation:   Extensive (README, guides, code comments)
Security:        High (credential management, validation)
```

### **Targets**
- [x] Type hints > 80%
- [x] Docstrings on all functions
- [x] PEP 8 compliance
- [ ] Unit test coverage > 80%
- [ ] Integration tests
- [ ] Performance benchmarks

---

## 🎯 Architecture Evolution

### **v1.0 (Current)**
- Single document analysis
- Session-based history
- In-memory processing
- Local configuration

### **v2.0 (Planned)**
- [ ] Database (SQLite)
- [ ] Persistent history
- [ ] REST API
- [ ] User authentication

### **v3.0 (Roadmap)**
- [ ] Multi-document analysis
- [ ] Batch processing
- [ ] Docker deployment
- [ ] Cloud hosting
- [ ] Advanced analytics

---

## 📖 Architecture Decision Records (ADRs)

### **ADR-001: Use Streamlit for UI**
**Decision:** Use Streamlit instead of React/Vue
**Rationale:** Rapid development, Python-native, no JavaScript needed
**Trade-offs:** Less control over styling, limited to Streamlit features

### **ADR-002: Use requests instead of official SDKs**
**Decision:** Use `requests` library instead of OpenAI SDK
**Rationale:** Multi-provider compatibility, lightweight, custom retry logic
**Trade-offs:** Slightly more verbose, manual error handling

### **ADR-003: Truncate at 60KB**
**Decision:** Limit documents to 60KB text (~15K tokens)
**Rationale:** Balance between cost and coverage, prevent timeouts
**Trade-offs:** Very large documents partially processed

### **ADR-004: Store config in .env**
**Decision:** Use environment variables in .env file
**Rationale:** Security, flexibility, local development ease
**Trade-offs:** Manual setup required

---

## 🏆 Architecture Strengths

✅ **Modular:** Easy to test and maintain  
✅ **Scalable:** Can add new features easily  
✅ **Secure:** Credential management best practices  
✅ **Documented:** Every component explained  
✅ **Robust:** Comprehensive error handling  
✅ **Flexible:** Works with any OpenAI-compatible API  

---

## ⚠️ Known Limitations & Future Improvements

### **Current Limitations**
- Single document per session
- No persistent history (session-only)
- No user authentication
- Manual configuration required
- No OCR for scanned PDFs

### **Future Improvements**
- [ ] Database persistency
- [ ] User authentication
- [ ] Multi-document support
- [ ] OCR integration
- [ ] Advanced analytics
- [ ] REST API
- [ ] Batch processing
- [ ] Docker/Kubernetes

---

**Project Version:** 1.0.0  
**Last Updated:** April 10, 2026  
**Status:** Production-Ready ✅

This architecture is designed for clarity, maintainability, and extensibility while prioritizing security and performance.
