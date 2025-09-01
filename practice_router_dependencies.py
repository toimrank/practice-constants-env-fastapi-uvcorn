from fastapi import FastAPI, APIRouter, Depends, HTTPException
from routers import person

app = FastAPI()

# Include person router
app.include_router(person.router)
