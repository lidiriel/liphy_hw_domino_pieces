from pydantic import BaseModel, Field, ConfigDict
from domino.models import OutputModifierModel, OutputModifierItemType
from typing import List, Union
from datetime import date as dt_date, datetime as dt_datetime, time as dt_time
from enum import Enum

class BioreactorId(str, Enum):
    option_1 = "BioRe_1"
    option_2 = "BioRe_2"
    option_3 = "BioRe_3"
    option_4 = "BioRe_4"
    option_5 = "BioRe_5"
    option_6 = "BioRe_6"
    option_7 = "BioRe_7"
    option_8 = "BioRe_8"
    option_9 = "BioRe_9"
    option_10 = "BioRe_10"
    
class InputModel(BaseModel):
    """
    Bioreactor Piece Input Model
    """
    incubator_uid: str = Field(
        default="orange_incubator",
        description='Incubator identifier (string).'
    )
    
    bioreactors: List[BioreactorId] = Field(
        default=[],
        description="Selection of Bioreactor"
    )

class OutputModel(BaseModel):
    """
    Bioreactor Piece Output Model
    """
    bioreactors: List[BioreactorId] = Field(
        description="Bioreactor(s) used"
    )

