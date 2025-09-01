from fastapi import APIRouter

router = APIRouter(prefix="/api", tags=["User"])

@router.get("/user")
def getUser():
    return {"userID", "user_123"}