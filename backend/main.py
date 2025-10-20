from fastapi import FastAPI
#from fastapi.middleware.cors import CORSMiddleware
#from typing import Union
import products
from .database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(products.router)
#@app.get("/")
#def read_root():
    #return {"Hello": "World"}

#@app.get("/items/{item_id}")
##   return {"item_id": item_id, "q":q}