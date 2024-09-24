from pydantic import BaseModel, Field, ConfigDict
from domino.models import OutputModifierModel, OutputModifierItemType
from typing import List, Union
from datetime import date as dt_date, datetime as dt_datetime, time as dt_time
from enum import Enum
    
class InputModel(BaseModel):
    """
    Incubator Heating Piece Input Model
    """
    incubator_uid: str = Field(
        default="orange_incubator",
        description='Incubator identifier (string).'
    )
    
    temperature_target: float = Field(
        default=37.0,
        description='Target temperature (float)'
    )
    
    temperature_heating: bool = Field(
        default=False,
        description='Heating activation'
    )


class OutputModel(BaseModel):
    """
    Incubator Heating Piece Output Model
    """
    message: str = Field(
        description="Incubator command executed"
    )

