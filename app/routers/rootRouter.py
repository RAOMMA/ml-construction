from fastapi import APIRouter
import os
# from helpers.preprocess import process
from app.helpers.preprocess import process


router = APIRouter()


@router.post("/predict")
async def preprocess_data(data: dict):
    # Add your data preprocessing logic here
    print(data)
    data1 = data['data']
    date = data['currentdate']
    print(data1)
    print(date)
    price = process(data1 , date)
    return price

