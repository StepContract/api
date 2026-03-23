from datetime import datetime, timedelta
from typing import List, Optional, TypeVar, Type
import bcrypt
import pytest
from app.database.base import SessionLocal
from app.database.models.activities.run import Run
from app.database.models.activities.walk import Walk
from app.database.models.activities.workout import Workout
from app.database.models.activity import Activity
from app.database.models.user import User
from app.schemas.activity import ActivityTypes
from app.schemas.user import UserRole

ModelType = TypeVar("ModelType")


class TestDatabase:
    @pytest.fixture(autouse=True)
    def setup(self):
        with SessionLocal() as session:
            session.query(Workout).delete()
            session.query(Run).delete()
            session.query(Walk).delete()
            session.query(Activity).delete()
            session.query(User).delete()
            session.commit()

    @staticmethod
    def insert_resources(
        resource_type: Type[ModelType],
        resource_properties: dict,
        start_id: int = 1,
        length: int = 1,
    ) -> List[ModelType]:
        if start_id < 1:
            raise ValueError("start_id must be greater than 0")

        with SessionLocal() as session:
            resources: List[ModelType] = [
                resource_type(
                    id=resource_id,
                    created_at=datetime.now() - timedelta(minutes=10),
                    **{
                        key: (
                            value.replace("{id}", str(resource_id))
                            if type(value) is str
                            else value
                        )
                        for key, value in resource_properties.items()
                    },
                )
                for resource_id in range(start_id, length + start_id)
            ]

            session.add_all(resources)
            session.commit()
            return resources

    @staticmethod
    def get_resources(
        resource_type: Type[ModelType],
    ) -> List[ModelType]:
        with SessionLocal() as session:
            return session.query(resource_type).all()

    @staticmethod
    def get_resource_by_id(
        resource_type: Type[ModelType], resource_id: int
    ) -> ModelType:
        with SessionLocal() as session:
            return session.get(resource_type, resource_id)
