from sqlalchemy.orm import Session
import schemas, models
from fastapi import HTTPException

def create_order(db: Session, order: schemas.OrderCreate):
    # Check if the order already exists
    existing_order = db.query(models.Order).filter(
        models.Order.symbol == order.symbol,
        models.Order.order_type == order.order_type,
        models.Order.timestamp == order.timestamp
    ).first()
    if existing_order:
        raise HTTPException(
            status_code=400,
            detail="Order with this symbol, order type, and timestamp already exists"
        )

    # Validate quantity and price
    if order.quantity <= 0:
        raise HTTPException(
            status_code=400,
            detail="Quantity must be greater than zero"
        )
    if order.price <= 0:
        raise HTTPException(
            status_code=400,
            detail="Price must be greater than zero"
        )

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
