# 🔒 Seguridad

## Reportar Vulnerabilidades

Si descubres una vulnerabilidad de seguridad, **por favor NO la publiques como issue pública**.

En su lugar:

1. **Envía un email a:** (configura tu email de seguridad)
2. **Incluye:**
   - Descripción de la vulnerabilidad
   - Pasos para reproducir
   - Posible impacto
   - Sugerencia de arreglo (si tienes)

Nos esforzaremos por confirmar y arreglar vulnerabilidades dentro de 48 horas.

---

## Prácticas de Seguridad

### API Keys & Credenciales

⚠️ **CRÍTICO:**

- **NUNCA** compartas tu `LLM_API_KEY`
- **NUNCA** commits `.env` con credenciales
- **SIEMPRE** usa `.env.example` como plantilla
- **SIEMPRE** agrega `.env` al `.gitignore`

### Para Contribuyentes

Cuando envíes un Pull Request:

1. ✅ Verifica que no haya `.env` con credenciales
2. ✅ No incluyas claves API en logs/debugs
3. ✅ No uses credenciales hardcodeadas
4. ✅ Valida, sanitiza y escapa inputs del usuario

### Datos de Documentos

- Los documentos se procesan en tiempo real
- **NO se almacenan** permanentemente en el servidor
- Se truncan a 60KB para limitar exposición
- Se limpian después de cada análisis

### Recomendaciones para Usuarios

1. **Usa una API Key dedicada** para este proyecto
2. **Limita permisos** si tu proveedor lo permite
3. **Rota keys regularmente** (cada 3 meses)
4. **Monitora usage** en tu proveedor LLM
5. **Usa HTTPS** si despliegas en la nube

---

## Dependencias Seguras

Verificamos regularmente:

- ✅ Vulnerabilidades en dependencias
- ✅ Actualizaciones de seguridad
- ✅ Compatibilidad de versiones

Para verificar localmente:

```bash
pip install safety
safety check
```

---

## Encriptación

- Las comunicaciones con el API LLM usan **HTTPS**
- Los `.env` locales NO están encriptados (usa contraseña del SO)
- Los documentos en transporte están protegidos por HTTPS

---

## Auditoría & Logging

- NO registramos API keys en logs
- NO almacenamos contenido de documentos
- Logs solo contienen estados de error (sin datos sensibles)

---

## Cumplimiento

- 🇪🇸 Cumple con RGPD (cuando es aplicable)
- 🇪🇸 Compatibles con leyes españolas de protección de datos
- 🇪🇸 No comparte datos con terceros

---

## Contacto de Seguridad

Para cualquier pregunta de seguridad, contacta a los mantenedores del proyecto.

**¡Gracias por ayudarnos a mantener este proyecto seguro! 🛡️**
