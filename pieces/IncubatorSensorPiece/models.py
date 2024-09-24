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
    
class OutputModel(BaseModel):
    """
    Incubator Sensor Piece Output Model
    """
    message: str = Field(
        description="Incubator command executed"
    )
    
    temperature_target: float = Field(
        description='Target temperature'
    )
    
    temperature_sensor1: float = Field(
        description='Temperature sensor 1'
    )
    
    temperature_sensor2: float = Field(
        description='Temperature sensor 2'
    )

