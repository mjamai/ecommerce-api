from fastapi import FastAPI
from pydantic import BaseModel,Field, field_validator, model_validator

class Product(BaseModel):
    name: str = Field(min_length=3,max_length=50)
    price: float = Field(ge=0)
    stock: int = Field(ge=0)
    active: bool = True
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
    