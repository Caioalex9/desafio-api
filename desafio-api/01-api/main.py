from fastapi import FastAPI, Query, HTTPException, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Atleta, Base
from fastapi_pagination import Page, add_pagination, paginate

# Criar tabelas no banco de dados
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"Hello": "World"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
