from fastapi import APIRouter

router = APIRouter(prefix="/api/v1", tags=["Products"])

@router.get("/product")
def getProduct():
    return {"productID" : "product_123"}