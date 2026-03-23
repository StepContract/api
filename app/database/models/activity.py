from datetime import datetime, timedelta
from sqlalchemy import Integer, DateTime, Enum
from sqlalchemy.orm import Mapped, mapped_column
from app.database.base import Base
from app.database.models.mixins import TimestampMixin
from app.schemas.activity import ActivityTypes


class Activity(TimestampMixin, Base):
    __tablename__ = "activities"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    ended_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    type: Mapped[ActivityTypes] = mapped_column(Enum(ActivityTypes), nullable=False)

    __mapper_args__ = {
        "polymorphic_identity": ActivityTypes.ACTIVITY,
        "polymorphic_on": type,
        "with_polymorphic": "*",
    }

    @property
    def duration(self) -> timedelta:
        return self.ended_at - self.created_at
