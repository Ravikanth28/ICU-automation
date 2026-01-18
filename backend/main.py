from fastapi import FastAPI
from backend.database import engine
from backend import models
from fastapi.middleware.cors import CORSMiddleware


from backend.routes import patients, resources, allocation

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Smart ICU Resource Allocation")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(patients.router)
app.include_router(resources.router)
app.include_router(allocation.router)

@app.get("/")
def health():
    return {"status": "ICU system running"}
