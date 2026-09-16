from fastapi import APIRouter, Depends
from pydantic import BaseModel

def check_access():
    print("Access checked")

class PrductResponse(BaseModel):
    name: str 
    id: int
  

router = APIRouter(prefix="/products",tags=["Products"],dependencies=[Depends(check_access)])

def get_category(category: str | None = None):
    return category

@router.get("/",response_model=list[PrductResponse])
def get_products():
    return [PrductResponse(id=1, name="Product 1")]

@router.get("/")
def get_category(category: str = Depends(get_category)):
    return [{"category": category}]

@router.get("/{product_id}")
def get_product(product_id: int):
    return {"id": product_id}