# LLM Agent for interacting with OpenAI-compatible APIs

import os
import requests
import time
import json
from typing import Optional


class LLMAgent:
    """
    Agent for interacting with OpenAI-compatible LLM APIs.
    Supports OpenRouter, Azure OpenAI, and other compatible endpoints.
    """
    
    def __init__(self):
        """Initialize the LLM agent with configuration from environment variables."""
        self.api_url = os.getenv(
            'LLM_API_URL',
            'https://openrouter.ai/api/v1/chat/completions'
        )
        self.api_key = os.getenv('LLM_API_KEY')
        self.model = os.getenv('LLM_MODEL', 'mistralai/mistral-7b-instruct:free')
        self.timeout = 60
        self.max_retries = 3
        self.retry_delay = 2  # seconds
    
    def is_configured(self) -> bool:
        """Check if the agent is properly configured with an API key."""
        return bool(self.api_key and self.api_url)
    
    def get_config_info(self) -> dict:
        """Returns configuration information (masking the API key)."""
        return {
            'api_url': self.api_url,
            'model': self.model,
            'has_api_key': bool(self.api_key),
            'api_key_preview': f"{self.api_key[:10]}...{self.api_key[-5:]}" if self.api_key else "No configurada"
        }
    
    def call_llm(self, system_prompt: str, user_message: str) -> tuple[bool, str]:
        """
        Makes a request to the LLM API with retry logic.
        
        Args:
            system_prompt: The system/assistant role prompt
            user_message: The user's message/prompt
            
        Returns:
            A tuple (success: bool, response: str)
            - If successful: (True, response_text)
            - If failed: (False, error_message)
        """
        
        if not self.is_configured():
            return False, "Error: API KEY no configurada. Configure LLM_API_KEY en las variables de entorno."
        
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.api_key}'
        }
        
        payload = {
            'model': self.model,
            'messages': [
                {'role': 'system', 'content': system_prompt},
                {'role': 'user', 'content': user_message}
            ],
            'temperature': 0.7,
            'max_tokens': 2000
        }
        
        last_error = None
        
        for attempt in range(self.max_retries):
            try:
                response = requests.post(
                    self.api_url,
                    json=payload,
                    headers=headers,
                    timeout=self.timeout
                )
                
                # Handle different status codes
                if response.status_code == 200:
                    response_data = response.json()
                    
                    # Extract the message content
                    if 'choices' in response_data and len(response_data['choices']) > 0:
                        message_content = response_data['choices'][0]['message']['content']
                        return True, message_content
                    else:
                        return False, "Error: Respuesta inválida del LLM (formato no esperado)"
                
                elif response.status_code == 401:
                    return False, "Error: API KEY inválida. Verifica que LLM_API_KEY sea correcta."
                
                elif response.status_code == 429:
                    last_error = "Error: Limite de velocidad excedido. Reintentando..."
                    if attempt < self.max_retries - 1:
                        time.sleep(self.retry_delay ** (attempt + 1))
                        continue
                
                elif response.status_code >= 500:
                    last_error = f"Error del servidor: {response.status_code}"
                    if attempt < self.max_retries - 1:
                        time.sleep(self.retry_delay ** (attempt + 1))
                        continue
                
                else:
                    error_detail = response.text[:200]
                    return False, f"Error del API: {response.status_code} - {error_detail}"
            
            except requests.exceptions.Timeout:
                last_error = "Error: Timeout. El servidor tardó demasiado en responder."
                if attempt < self.max_retries - 1:
                    time.sleep(self.retry_delay ** (attempt + 1))
                    continue
            
            except requests.exceptions.ConnectionError:
                last_error = "Error: No se pudo conectar al API. Verifica tu conexión a internet."
                if attempt < self.max_retries - 1:
                    time.sleep(self.retry_delay ** (attempt + 1))
                    continue
            
            except requests.exceptions.RequestException as e:
                last_error = f"Error de solicitud: {str(e)[:100]}"
                if attempt < self.max_retries - 1:
                    time.sleep(self.retry_delay ** (attempt + 1))
                    continue
            
            except json.JSONDecodeError:
                return False, "Error: Respuesta inválida del API (JSON mal formado)"
            
            except Exception as e:
                return False, f"Error inesperado: {str(e)[:100]}"
        
        # If all retries failed
        return False, last_error or "Error: No se pudo completar la solicitud al LLM después de varios intentos."


def analyze_document(document_text: str, system_prompt: str, user_prompt: str) -> tuple[bool, str]:
    """
    Convenience function to analyze a document using the LLM agent.
    
    Args:
        document_text: The extracted document text
        system_prompt: The system prompt
        user_prompt: The user/analysis prompt
        
    Returns:
        A tuple (success: bool, response: str)
    """
    agent = LLMAgent()
    return agent.call_llm(system_prompt, user_prompt)
