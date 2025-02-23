from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from typing import List, Literal, Annotated
from sqlalchemy.orm import Session
from datetime import datetime

import crud.order
from database import engine, SessionLocal
import models, crud, schemas

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
db_dependency = Annotated[Session, Depends(get_db)]

@app.get("/")
async def root():
    return {"message": "Hello World"}

# Order endpoints

@app.post("/orders", response_model=schemas.OrderResponse)
async def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    return crud.order.create_order(db, order)

@app.get("/orders/{portfolio_id}", response_model=List[schemas.OrderResponse])
async def get_orders(db: Session = Depends(get_db)):
    return crud.order.read_orders(db)
