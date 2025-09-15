
from __future__ import annotations
from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel, EmailStr, HttpUrl, Field

# ----- Request models -----

class CreateUserRequest(BaseModel):
    name: str
    job: str

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

# ----- Response models -----

class CreateUserResponse(BaseModel):
    name: str
    job: str
    id: str
    createdAt: datetime

class Support(BaseModel):
    url: HttpUrl
    text: str

class User(BaseModel):
    id: int
    email: EmailStr
    first_name: str
    last_name: str
    avatar: HttpUrl

class ListUsersResponse(BaseModel):
    page: int
    per_page: int
    total: int
    total_pages: int
    data: List[User]
    support: Support

class LoginResponse(BaseModel):
    token: str

class ErrorResponse(BaseModel):
    error: str