from fastapi import APIRouter
from src.db import Session

router = APIRouter(prefix="/orders", tags=["orders"])

@router.get("/")
def sdfjskdf():
 return "hello"
@router.get("/goodbye")
def sdfjskdf():
 return "hello"
