from sqlalchemy.orm import Session
import schemas, models
from fastapi import HTTPException

def create_order(db: Session, order: schemas.OrderCreate):
    db_order = models.Order(
        symbol=order.symbol,
        order_type=order.order_type,
        quantity=order.quantity,
        price=order.price,
        timestamp=order.timestamp
    )
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

def read_orders(db: Session):
    return db.query(models.Order).all()
