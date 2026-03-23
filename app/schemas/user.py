from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, EmailStr


class UserRole(Enum):
    MEMBER = "MEMBER"
    ADMIN = "ADMIN"


class UserSchema(BaseModel):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    avatar_url: Optional[str] = None
    bio: Optional[str] = None
    email: EmailStr
    username: str
    firstname: str
    lastname: str
    role: UserRole
    is_admin: bool
    is_active: bool
