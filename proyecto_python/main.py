from fastapi import FastAPI
import models
from database import engine
from routers import auth, mlmodels
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(lifespan=mlmodels.lifespan)

models.Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(mlmodels.router)

# Configuración de los orígenes permitidos
origins = [
    "http://localhost",
    "http://localhost:4200",  # Agrega aquí la URL de tu aplicación Angular
]

# Configuración del middleware de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

