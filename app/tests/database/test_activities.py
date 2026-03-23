from datetime import datetime, timedelta
from typing import Optional, List
from app.database.models.activities.run import Run
from app.database.models.activities.walk import Walk
from app.database.models.activities.workout import Workout
from app.database.models.activity import Activity
from app.schemas.activity import (
    ActivityTypes,
    WorkoutTypes,
    ActivitySchema,
    WalkSchema,
    RunSchema,
    WorkoutSchema,
)
from app.tests.database.base import TestDatabase


class TestActivities(TestDatabase):
    ENUM_MODEL_MAP = {
        ActivityTypes.ACTIVITY: Activity,
        ActivityTypes.WALK: Walk,
        ActivityTypes.RUN: Run,
        ActivityTypes.WORKOUT: Workout,
    }

    def __insert_activities(
        self,
        activity_type: ActivityTypes,
        start_id: int = 1,
        length: int = 1,
        ended_at: Optional[datetime] = datetime.now(),
        additional_properties: dict = {},
    ) -> List[Activity]:
        return self.insert_resources(
            resource_type=self.ENUM_MODEL_MAP[activity_type],
            start_id=start_id,
            length=length,
            resource_properties={
                "type": activity_type,
                "ended_at": ended_at,
                **additional_properties,
            },
        )

    def __test_workout_activities(self, workout_type: WorkoutTypes):
        self.__insert_activities(
            activity_type=ActivityTypes.WORKOUT,
            additional_properties={
                "repetitions": 100,
                "workout_type": workout_type,
            },
        )

        activity: List[Workout] = TestDatabase.get_resources(Workout)

        assert len(TestDatabase.get_resources(Activity)) == 1
        assert len(activity) == 1
        assert activity[0].workout_type == workout_type
        assert WorkoutSchema.model_validate(activity[0])

    def test_create_activity(self):
        self.__insert_activities(
            activity_type=ActivityTypes.WALK,
            additional_properties={"steps": 1000},
        )

        activity: List[Activity] = TestDatabase.get_resources(Walk)

        assert len(TestDatabase.get_resources(Activity)) == 1
        assert len(activity) == 1
        assert activity[0].duration == timedelta(minutes=10)
        assert ActivitySchema.model_validate(activity[0])

    def test_create_walk_activity(self):
        self.__insert_activities(
            activity_type=ActivityTypes.WALK,
            additional_properties={"steps": 1000},
        )

        activity: List[Walk] = TestDatabase.get_resources(Walk)

        assert len(TestDatabase.get_resources(Activity)) == 1
        assert len(activity) == 1
        assert activity[0].speed is None
        assert activity[0].walk_speed == "100 steps/min"
        assert WalkSchema.model_validate(activity[0])

    def test_create_run_activity(self):
        self.__insert_activities(
            activity_type=ActivityTypes.RUN,
            additional_properties={"kilometers": 2.1},
        )

        activity: List[Run] = TestDatabase.get_resources(Run)

        assert len(TestDatabase.get_resources(Activity)) == 1
        assert len(activity) == 1
        assert activity[0].speed == "4'45/km"
        assert activity[0].walk_speed is None
        assert RunSchema.model_validate(activity[0])

    def test_create_pullup_activity(self):
        self.__test_workout_activities(WorkoutTypes.PULLUP)

    def test_create_pump_activity(self):
        self.__test_workout_activities(WorkoutTypes.PUMP)
