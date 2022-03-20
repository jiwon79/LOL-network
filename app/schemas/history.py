from typing import List
from pydantic import BaseModel

class History(BaseModel):
    team_list: List[str]
    end_time: str