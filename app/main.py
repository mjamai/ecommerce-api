from fastapi import FastAPI
from pydantic import BaseModel,Field, field_validator, model_validator
from enum import Enum
from app.routers.products import router as products_router
from app.schemas.product import Product


app = FastAPI()
app.include_router(products_router)

@app.get("/")
def home():
    return {"message": "Hello, fastapi!"}

class ProductStatus(str, Enum):
    active = "active"
    inactive = "inactive"
    out_of_stock = "out_of_stock"



@app.post("/products")
def create_product(product: Product):
    return product

class UserResponse(BaseModel):
    name: str = Field(min_length=3,max_length=50)
    email: str = Field(max_length=100)

@app.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int):
    return {"name": "John Doe", "email": "john.doe@example.com","password":"123456"}  # Example user data
