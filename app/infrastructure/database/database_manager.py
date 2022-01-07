from sqlalchemy.engine import create_engine
from sqlalchemy.engine.base import Engine
from sqlalchemy.orm.session import Session, sessionmaker
from app.infrastructure.database.db_source import data_source_decider, connection_args


class DatabaseManager:
    def __init__(self, force_memory_database: bool = False) -> None:
        db_url = (
            "sqlite:///:memory:" if force_memory_database else data_source_decider()
        )

        print("Accessing databasae via: " + db_url)

        self._engine = create_engine(
            db_url, connect_args=connection_args()
        ).execution_options(isolation_level="SERIALIZABLE")

        self._session = sessionmaker(self.engine)

    @property
    def engine(self) -> Engine:
        return self._engine

    @engine.setter
    def engine(self, value: Engine):
        self._engine = value

    @property
    def session(self):
        return self._session

    @session.setter
    def session(self, value):
        self._session = value

    def create_session(self) -> Session:
        return self.session()
