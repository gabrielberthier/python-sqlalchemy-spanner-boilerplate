from unittest import TestCase, main, mock
import os
from sqlalchemy.engine.base import Engine
from sqlalchemy.orm.session import Session
from app.infrastructure.database.database_manager import DatabaseManager
from app.infrastructure.database.db import Base


class DatabaseTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.env_patcher = mock.patch.dict(os.environ, {"MODE": "test"})
        cls.env_patcher.start()

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        cls.env_patcher.stop()

    def setUp(self) -> None:
        os.environ["MODE"] = "test"
        self._db_manager = DatabaseManager(force_memory_database=True)
        Base.metadata.create_all(bind=self.engine)

    def tearDown(self) -> None:
        Base.metadata.drop_all(self.engine)

    @property
    def engine(self) -> Engine:
        return self._db_manager.engine

    @property
    def session(self) -> Session:
        return self._db_manager.create_session()
