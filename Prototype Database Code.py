from typing import Optional
from sqlmodel import Field, SQLModel, create_engine
import datetime as dt

class User(SQLModel, table=True):
    ID: Optional[int] = Field(default=None, primary_key=True)
    username: str
    password: str
    BuffyCoins: Optional[int] = Field(default=1000)

sqlite_file_name = "Prototype.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)

SQLModel.metadata.create_all(engine)

