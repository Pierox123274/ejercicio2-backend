# Ejercicio2 Backend (FastAPI + Firebase)

API REST para CRUD de personas con Firebase Firestore.

## Produccion (Hugging Face, sin tarjeta)

```powershell
.\install.ps1
.\deploy.ps1
```

| Servicio | URL |
|----------|-----|
| API | https://pierox123274-ejercicio2-api.hf.space/api |
| Health | https://pierox123274-ejercicio2-api.hf.space/api/health |
| Docs | https://pierox123274-ejercicio2-api.hf.space/docs |

## Requisitos para desplegar

1. `firebase login` (usa tu sesion actual con Firestore)
2. Cuenta en https://huggingface.co/join
3. Token en https://huggingface.co/settings/tokens → guardar en `.hf-token`
4. Ejecutar `.\deploy.ps1`

Repositorio: https://github.com/Pierox123274/ejercicio2-backend

## Local

```powershell
.\install.ps1
.\.venv\Scripts\Activate.ps1
uvicorn main:app --reload --port 8001
```

## Endpoints

- `GET /api/health`
- `GET/POST /api/personas`
- `GET/PUT/DELETE /api/personas/{docIdentidad}`

## Firebase

- Proyecto: `ing-web-93d49`
- Coleccion: `personas`
