from datetime import datetime, timedelta
from enum import Enum
from typing import Optional
from pydantic import BaseModel
from app.schemas.user import UserRole


class ActivityTypes(Enum):
    ACTIVITY = "activity"
    WALK = "walk"
    RUN = "run"
    WORKOUT = "workout"


class WorkoutTypes(Enum):
    PUMP = "pump"
    PULLUP = "pullup"


class ActivitySchema(BaseModel):
    id: int
    created_at: datetime
    ended_at: datetime
    type: ActivityTypes
    duration: timedelta

    model_config = {"from_attributes": True}


class WorkoutSchema(ActivitySchema):
    repetitions: int
    workout_type: WorkoutTypes


class RunSchema(ActivitySchema):
    steps: Optional[int] = None
    kilometers: float
    speed: str
    walk_speed: Optional[str] = None


class WalkSchema(ActivitySchema):
    kilometers: Optional[int] = None
    steps: float
    walk_speed: str
    speed: Optional[str] = None
