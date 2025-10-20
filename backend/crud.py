from sqlalchemy.orm import Session
from . import models, schemas

def get_all_products(db: Session):
    return db.query(models.Product).all()

# Create operation
def create_product(db: Session, product: schemas.ProductCreate):
    db_product = models.Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)

    return db_product

# Read operation
def get_product(db: Session, product_id: int):
    return db.query(models.Product).filter(models.Product.id == product_id).first()

# Update operation
def update_produdct(db: Session, product_id: int, updated_data: schemas.ProductCreate):
    db_product = get_product(db, product_id)

    if not db_product:
        return None
    
    for key, value in updated_data.dict().items():
        setattr(db_product, key, value)

    db.commit()
    db.refresh(db_product)

    return db_product

# Delete operation
def delete_product(db: Session, product_id: int):
    db_product = get_product(db, product_id)
    
    if not db_product:
        return None
    
    db.delete(db_product)
    db.commit()

    return True