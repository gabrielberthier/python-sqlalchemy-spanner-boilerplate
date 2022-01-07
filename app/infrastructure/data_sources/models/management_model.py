from datetime import datetime
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import DateTime, Integer, String
from app.infrastructure.database.db import Base


class ManagementModel(Base):
    __tablename__ = "management"
    id = Column(Integer, primary_key=True)
    restaurant_id = Column(ForeignKey("restaurant.id"))
    manager_id = Column(ForeignKey("person.id"))
    created_at = Column("last_updated", DateTime, default=datetime.now())

    manager = relationship("PersonModel", back_populates="restaurants")
