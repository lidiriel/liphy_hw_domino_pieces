from pydantic import BaseModel, Field, ConfigDict
from domino.models import OutputModifierModel, OutputModifierItemType
from typing import List, Union
from datetime import date as dt_date, datetime as dt_datetime, time as dt_time


class InputModel(BaseModel):
    """
    Pump Piece Input Model
    """
    uid: int = Field(
        default=1,
        description='Pump identifier (integer).'
    )
    
    speed: float = Field(
        default=0,
        description="Pump speed",
    )


class OutputModel(BaseModel):
    """
    Pump Piece Output Model
    """
    message: str = Field(
        description="Pump command executed"
    )

