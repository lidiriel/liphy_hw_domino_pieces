from pydantic import BaseModel, Field, ConfigDict
from domino.models import OutputModifierModel, OutputModifierItemType
from typing import List, Union
from datetime import date as dt_date, datetime as dt_datetime, time as dt_time


class InputModel(BaseModel):
    """
    Filterwheel Piece Input Model
    """
    uid: str = Field(
        default="FWA",
        description='Filterwheel identifier (string).'
    )
    
    position: int = Field(
        default=0,
        description="Filterwheel position",
    )


class OutputModel(BaseModel):
    """
    Filterwheel Piece Output Model
    """
    message: str = Field(
        description="Filterwheel command executed"
    )

