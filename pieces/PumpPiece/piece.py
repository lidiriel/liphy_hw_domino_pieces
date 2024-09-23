from domino.base_piece import BasePiece
from .models import InputModel, OutputModel
import importlib.util


class PumpPiece(BasePiece):

    def piece_function(self, input_data: InputModel):
        # Log inputs
        self.logger.info(f"Pump id {input_data.uid} run speed {input_data.speed}")

        #TODO call pump with Thor command
        
        message = f"Pump piece executed successfully"


        # Return output
        return OutputModel(
            message=message,
        )