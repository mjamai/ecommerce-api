from fastapi import APIRouter

router = APIRouter()

@router.get("/products")
def get_products():
    return [{"id": 1, "name": "Product 1"}]