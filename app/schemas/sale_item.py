from pydantic import BaseModel, ConfigDict


class SaleItemBase(BaseModel):
    sale_id: int
    product_id: int
    quantity: int


class SaleItemCreate(SaleItemBase):
    pass


class SaleItemUpdate(BaseModel):
    sale_id: int | None = None
    product_id: int | None = None
    quantity: int | None = None


class SaleItemRead(SaleItemBase):
    model_config = ConfigDict(from_attributes=True)

    sale_item_id: int