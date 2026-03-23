from sqlalchemy import Integer, ForeignKey, Enum
from sqlalchemy.orm import Mapped, mapped_column
from app.database.base import Base
from app.database.models.activity import Activity
from app.database.models.mixins import TimestampMixin
from app.schemas.activity import WorkoutTypes, ActivityTypes


class Workout(Activity):
    __tablename__ = "workouts"

    id: Mapped[int] = mapped_column(
        Integer, ForeignKey("activities.id"), primary_key=True
    )
    repetitions: Mapped[int] = mapped_column(Integer, nullable=False)
    workout_type: Mapped[WorkoutTypes] = mapped_column(
        Enum(WorkoutTypes), nullable=False
    )

    __mapper_args__ = {
        "polymorphic_identity": ActivityTypes.WORKOUT,
    }
