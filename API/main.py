import os
import sys
import django

# Add the parent directory to sys.path to allow imports from the project root
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "ecom"))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecom.settings')
django.setup()

from typing import List, Optional
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from django.db import transaction
from django.contrib.auth.models import User

from store.models import Product
from payment.models import Order as PaymentOrder, OrderItem

app = FastAPI()

def _order_to_dict(o: PaymentOrder) -> dict:
    return {
        "id": o.id,
        "user": o.user.username if o.user else None,
        "user_id": o.user.id if o.user else None,
        "full_name": o.full_name,
        "email": o.email,
        "shipping_address": o.shipping_address,
        "amount_paid": float(o.amount_paid),
        "date_ordered": o.date_ordered.isoformat() if o.date_ordered else None,
        "shipped": o.shipped,
        "date_shipped": o.date_shipped.isoformat() if o.date_shipped else None,
        "items": [
            {
                "product": item.product.name if item.product else None,
                "product_id": item.product.id if item.product else None,
                "quantity": item.quantity,
                "price": float(item.price),
            }
            for item in o.orderitem_set.all()
        ],
    }

class OrderCreate(BaseModel):
    product_id: int
    user_id: int
    quantity: Optional[int] = 1
    address: Optional[str] = ""
    status: Optional[bool] = False

class OrderUpdate(BaseModel):
    shipped: Optional[bool] = None
    address: Optional[str] = None

@app.get("/")
def welcome():
   return "HELLO WELCOME TO GAMESTOP FASTAPI is the best framework for building APIs"

@app.get("/orders")
def get_all_orders():
    qs = PaymentOrder.objects.select_related("user").prefetch_related("orderitem_set__product").all()
    return [_order_to_dict(o) for o in qs]

@app.get("/orders/{order_id}")
def get_order(order_id: int):
    try:
        o = PaymentOrder.objects.prefetch_related("orderitem_set__product").get(id=order_id)
    except PaymentOrder.DoesNotExist:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found")
    return _order_to_dict(o)

@app.post("/orders", status_code=status.HTTP_201_CREATED)
def create_order(payload: OrderCreate):
    try:
        product = Product.objects.get(id=payload.product_id)
    except Product.DoesNotExist:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Product not found")
    try:
        user = User.objects.get(id=payload.user_id)
    except User.DoesNotExist:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User not found")
    
    with transaction.atomic():
        payment_order = PaymentOrder.objects.create(
            user=user,
            full_name=user.get_full_name(),
            email=user.email,
            shipping_address=payload.address or "",
            amount_paid=product.price * (payload.quantity or 1),
        )

        OrderItem.objects.create(
            order=payment_order,
            product=product,
            user=user,
            quantity=payload.quantity or 1,
            price=product.price,
        )

    return _order_to_dict(payment_order)

@app.put("/orders/{order_id}")
def update_order(order_id: int, payload: OrderUpdate):
    try:
        o = PaymentOrder.objects.get(id=order_id)
    except PaymentOrder.DoesNotExist:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Order not found")
    
    if payload.shipped is not None:
        o.shipped = payload.shipped
    if payload.address is not None:
        o.shipping_address = payload.address
    o.save()

    return _order_to_dict(o)

@app.delete("/orders/{order_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_order(order_id: int):
    try:
        o = PaymentOrder.objects.get(id=order_id)
    except PaymentOrder.DoesNotExist:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Order not found")
    o.delete()
    return None

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)