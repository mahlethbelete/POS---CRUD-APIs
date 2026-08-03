from pydantic import BaseModel, ConfigDict


class UserBase(BaseModel):
    first_name: str
    last_name: str
    email: str
    username: str | None = None
    role: str | None = None


class UserCreate(UserBase):
    password_hash: str  

class UserUpdate(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    email: str | None = None
    role: str | None = None
    password: str | None = None


class UserRead(UserBase):
    model_config = ConfigDict(from_attributes=True)

    user_id: int