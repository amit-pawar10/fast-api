from fastapi import FastAPI
from pydantic import BaseModel, Field, HttpUrl
from typing import List, Set

class Profile(BaseModel):
    name: str 
    email: str
    age: int

class Image(BaseModel):
    url: HttpUrl
    name: str

class Product(BaseModel):
    name: str
    price: int = Field(title="Price of the item",
                       description="This would be the price of the item being added",
                       gt=0)
    discount: int
    discounted_price: float
    tags: Set[str] =[]
    image: List[Image]

    class Config:
        json_schema_extra = {
            "example": {
                "name": "Phone",
                "price": 1000,
                "discount": 100,
                "discounted_price": 0,
                "tags":["electronics", "computers"],
                "image":[
                    {"url":"www.google.com",
                     "name": "phone image"},
                     {"url":"www.google.com",
                     "name": "phone image side view"},
                ]
            }
        }


class Offer(BaseModel):
    name: str = Field(example="New Year Sale")
    description: str
    price: float
    products: List[Product]

app = FastAPI()


@app.get('/user/admin')
def admin():
    return {"This is admin page"}


@app.post('/addoffer')
def addoffer(offer: Offer):
    return {offer}


@app.post('/addproduct')
def addproduct(product: Product):
    product.discounted_price = product.price - (product.price * product.discount/100)
    return product


################ ADDING PATH & QUERY parameters to REQUEST
@app.post('/addproduct/{product_id}')
def addproduct_id(product: Product, product_id: int, category: str):
    product.discounted_price = product.price - (product.price * product.discount/100)
    return {"product_id":product_id, "product":product, "category":category}


@app.post('/adduser')
def adduser(profile: Profile):
    return profile