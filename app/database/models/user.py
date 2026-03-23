from typing import Optional
from sqlalchemy import Enum, String, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from app.database.base import Base
from app.database.models.mixins import TimestampMixin
from app.schemas.user import UserRole


class User(TimestampMixin, Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    email: Mapped[str] = mapped_column(
        String(255), unique=True, index=True, nullable=False
    )
    username: Mapped[str] = mapped_column(
        String(50), unique=True, index=True, nullable=False
    )
    hashed_password: Mapped[str] = mapped_column(String(255), nullable=False)
    firstname: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    lastname: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    bio: Mapped[Optional[str]] = mapped_column(String(1000), nullable=True)
    avatar_url: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    role: Mapped[UserRole] = mapped_column(
        Enum(UserRole), nullable=False, default=UserRole.MEMBER.value
    )

    @property
    def is_admin(self) -> bool:
        return self.role.value == UserRole.ADMIN.value
