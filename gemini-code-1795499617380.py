from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Permitir que el frontend (HTML/JS) se comunique con este backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class DatosCamara(BaseModel):
    estado: str
    detalles: str

@app.get("/")
def inicio():
    return {"mensaje": "API del Proyecto Fenómeno El Niño activa"}

@app.post("/analizar")
def analizar_datos(datos: DatosCamara):
    # AQUÍ VA TU LÓGICA (ej. guardar reporte de alerta, procesar imagen, etc.)
    respuesta = f"Reporte recibido: {datos.estado}. Protocolo de emergencia activado."
    return {"status": "ok", "resultado": respuesta}