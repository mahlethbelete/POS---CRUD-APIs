from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict


class SaleBase(BaseModel):
    customer_id: int | None = None
    user_id: int
    sale_date: datetime
    tax_amount: Decimal
    total: Decimal


class SaleCreate(SaleBase):
    pass


class SaleUpdate(BaseModel):
    customer_id: int | None = None
    user_id: int | None = None
    sale_date: datetime | None = None
    tax_amount: Decimal | None = None
    total: Decimal | None = None


class SaleRead(SaleBase):
    model_config = ConfigDict(from_attributes=True)

    sale_id: int