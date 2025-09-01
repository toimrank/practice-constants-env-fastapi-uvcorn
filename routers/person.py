from fastapi import APIRouter, Depends, Header, HTTPException
from typing import Optional

router = APIRouter(prefix="/api", tags=["User"])

def check_token_header(practice_token: str = Header(...), token : str = Header(...)):
    print(practice_token + " = " + token)
    if practice_token != "david" and token != "12345":
        raise HTTPException(status_code=403, detail="Token Values Not Found")

# Create router and include prefix, tags and dependencies.
router = APIRouter(
    prefix="/token/v1",
    tags=["Token"],
    dependencies=[Depends(check_token_header)]
)

@router.get("/person")
def getUser():
    return {"message" : "practice-token and token are found!"}

