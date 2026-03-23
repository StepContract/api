from typing import Optional
from sqlalchemy import Integer, Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from app.database.models.activity import Activity
from app.schemas.activity import ActivityTypes


class Run(Activity):
    __tablename__ = "runs"

    id: Mapped[int] = mapped_column(
        Integer, ForeignKey("activities.id"), primary_key=True
    )
    kilometers: Mapped[float] = mapped_column(Float, nullable=False)
    steps: Mapped[int] = mapped_column(Integer, nullable=True)

    __mapper_args__ = {
        "polymorphic_identity": ActivityTypes.RUN,
    }

    @property
    def walk_speed(self) -> Optional[str]:
        if self.steps is None:
            return None

        return f"{int(self.steps / (self.duration.seconds // 60))} steps/min"

    @property
    def speed(self) -> str:
        speed = self.duration.seconds / self.kilometers
        return f"{int(speed // 60)}'{int(speed % 60)}/km"
