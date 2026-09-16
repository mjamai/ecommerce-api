from fastapi import FastAPI
from pydantic import BaseModel,Field, field_validator, model_validator
from enum import Enum


app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello, fastapi!"}

class ProductStatus(str, Enum):
    active = "active"
    inactive = "inactive"
    out_of_stock = "out_of_stock"
    
class Product(BaseModel):
    name: str = Field(min_length=3,max_length=50)
    price: float = Field(ge=0)
    stock: int = Field(ge=0)
    active: bool = True
    status: ProductStatus
    category: str | None = Field(
        default=None,
        max_length=30
        )

    @field_validator("price")
    @classmethod
    def price_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError("Le prix doit être supérieur à 0")
        return v
    @model_validator(mode="after")
    def validate_product(self):
         if self.active and self.stock == 0:
            raise ValueError("Un produit actif doit avoir du stock")
         return self
    

@app.post("/products")
def create_product(product: Product):
    return product

class UserResponse(BaseModel):
    name: str = Field(min_length=3,max_length=50)
    email: str = Field(max_length=100)

@app.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int):
    return {"name": "John Doe", "email": "john.doe@example.com","password":"123456"}  # Example user data
