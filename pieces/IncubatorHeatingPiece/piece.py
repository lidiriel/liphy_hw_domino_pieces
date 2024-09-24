from domino.base_piece import BasePiece
from .models import InputModel, OutputModel
import importlib.util


class IncubatorHeatingPiece(BasePiece):

    def piece_function(self, input_data: InputModel):
        # Log inputs
        self.logger.info(f"Incubator id {input_data.uid} set target temperature to {input_data.target_temperature}")

        #TODO call pump with Thor command
        
        message = f"Incubator heating piece executed successfully"


        # Return output
        return OutputModel(
            message=message,
        )