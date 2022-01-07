from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.orm import relationship
from app.infrastructure.database.db import Base


class PersonModel(Base):
    __tablename__ = "person"

    id = Column(Integer, primary_key=True)
    name = Column(String())
    email = Column(String())

    restaurants = relationship("ManagementModel", back_populates="manager")
