from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas, database

router = APIRouter(prefix="/products", tags=["Products"])

# Conseguir DB
def get_db():
    db = database.SessionLocal()
    
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[schemas.Product])
def read_product(db: Session = Depends(get_db)):
    return crud.get_product(db)


@router.post("/", response_model=schemas.Product)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return crud.create_product(db, product)

@router.get("/{product_id}", response_model=schemas.Product)
def read_product(product_id: int, db: Session = Depends(get_db)):
    db_product = crud.get_product(db, product_id)

    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    return db_product

@router.put("/{product_id}", response_model=schemas.Product)
def update_product(product_id: int, product: schemas.ProductCreate, db: Session = Depends(get_db)):
    updated = crud.update_produdct(db, product_id, product)

    if not updated:
        raise HTTPException(status_code=404, detail="Product not found")
    
    return updated

@router.delete("/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_product(db, product_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return {"message": "Producto eliminado"}
