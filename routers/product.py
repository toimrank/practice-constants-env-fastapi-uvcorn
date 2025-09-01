from fastapi import APIRouter

router = APIRouter(prefix="/api", tags=["Products"])

@router.get("/product")
def getProduct():
    return {"productID", "product_123"}