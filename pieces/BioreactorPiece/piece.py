from domino.base_piece import BasePiece
from .models import InputModel, OutputModel
import importlib.util


class BioreactorPiece(BasePiece):

    def piece_function(self, input_data: InputModel):
        # Log inputs
        self.logger.info(f"Bioreactor selected {input_data.bioreactors} from incubator {input_data.incubator_uid}")

        # Return output
        return OutputModel(
            bioreactors=input_data.bioreactors,
        )