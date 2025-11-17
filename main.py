from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware # 1. Importer


app = FastAPI()


# 2. Définir les origines autorisées
origins = [
    "http://localhost:5500",
    "http://127.0.0.1:5500",
]


# 3. Ajouter le middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/api/status")
def get_api_status():
    return {"srv01": "En Ligne", "cam01": "Éteinte"}
