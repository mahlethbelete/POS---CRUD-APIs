from fastapi import FastAPI
import models
from database import Base, engine 
from routers import (
    product,
    category,
    supplier,
    customer,
    user,
    sale,
    payments,
    receipt,
    sale_item,
)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Pos API", version="1")

app.include_router(product.router)
app.include_router(category.router)
app.include_router(supplier.router)
app.include_router(customer.router)
app.include_router(user.router)
app.include_router(sale.router)
app.include_router(payments.router)
app.include_router(receipt.router)
app.include_router(sale_item.router)
