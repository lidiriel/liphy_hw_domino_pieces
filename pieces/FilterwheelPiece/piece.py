from domino.base_piece import BasePiece
from .models import InputModel, OutputModel
import importlib.util


class FilterwheelPiece(BasePiece):

    def piece_function(self, input_data: InputModel):
        # Log inputs
        self.logger.info(f"Filterwheel id {input_data.uid} set position tp {input_data.position}")

        #TODO call Filterwheel with Thor command
        
        message = f"Filterwheel piece executed successfully"


        # Return output
        return OutputModel(
            message=message,
        )