from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field


class ProductBase(BaseModel):
    name: str
    description: str | None = None

    unit_price: Decimal = Field(max_digits=10, decimal_places=2)
    cost_price: Decimal | None = Field(
        default=None,
        max_digits=10,
        decimal_places=2,
    )
    quantity_in_stock: int = 0
    reorder_level: int | None = None
    category_id: int
    supplier_id: int | None = None


class ProductCreate(ProductBase):
    pass


class ProductUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    unit_price: Decimal | None = None
    cost_price: Decimal | None = None
    quantity_in_stock: int | None = None
    reorder_level: int | None = None
    category_id: int | None = None
    supplier_id: int | None = None


class ProductRead(ProductBase):
    model_config = ConfigDict(from_attributes=True)

    product_id: int
