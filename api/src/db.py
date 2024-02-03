from typing import Optional
from datetime import date
from sqlmodel import *


class User(SQLModel):
    id: Optional[int] = Field(default=None, primary_key=True)
    name:         str
    pass_hash:    str
    coins:        int
    dob:          date

    # owned_item:   item
    # equiped_item: item


class Game(SQLModel):
    game_id: int
    players: list
