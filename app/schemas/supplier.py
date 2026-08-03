from pydantic import BaseModel, ConfigDict


class SupplierBase(BaseModel):
    name: str
    phone: str | None = None
    email: str | None = None


class SupplierCreate(SupplierBase):
    pass


class SupplierUpdate(BaseModel):
    name: str | None = None
    phone: str | None = None
    email: str | None = None


class SupplierRead(SupplierBase):
    model_config = ConfigDict(from_attributes=True)

    supplier_id: int