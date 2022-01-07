from fastapi import FastAPI
from app.infrastructure.database.database_manager import DatabaseManager
from app.infrastructure.database.db import Base
import os
from app.framework.main.setup import setup

engine = DatabaseManager().engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="API Product", version="v0.1")

setup(app)

print(os.getenv("MODE"))

print("Started products API")
