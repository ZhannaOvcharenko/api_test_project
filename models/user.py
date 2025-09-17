from typing import List
from pydantic import BaseModel, EmailStr, HttpUrl


# =======================
# Ответы API
# =======================
class UserData(BaseModel):
    id: int
    email: EmailStr
    first_name: str
    last_name: str
    avatar: HttpUrl


class UserListResponse(BaseModel):
    page: int
    per_page: int
    total: int
    total_pages: int
    data: List[UserData]


class UserResponse(BaseModel):
    id: str
    name: str
    job: str
    createdAt: str


class LoginResponse(BaseModel):
    token: str


class ErrorResponse(BaseModel):
    error: str


# =======================
# Запросы API
# =======================
class UserCreate(BaseModel):
    name: str
    job: str


class LoginRequest(BaseModel):
    email: EmailStr
    password: str
