from domino.base_piece import BasePiece
from .models import InputModel, OutputModel
import importlib.util


class FilterwheelPiece(BasePiece):
    
    def piece_function(self, input_data: InputModel):
        # The Piece's input arguments are passed in the 'input_data' argument
        # print(f"Inpu argument 1: {input_data.in_argument_1}")
        # print(f"Inpu argument 2: {input_data.in_argument_2}")
        # print(f"Inpu argument 3: {input_data.in_argument_3}")

        # The Piece's secrets are passed in the 'secrets_data' argument
        # print(f"Secret variable: {secrets_data.SECRET_VAR}
        
        # If you want to save files in a shared storage, to be used by other Pieces,
        # you should save them under self.results_path
        # msg = "This is a text to be saved in a shared storage, to be read by other Pieces!"
        # file_path = str(Path(self.results_path)/"msg.txt")
        # with open(file_path, "w") as f:
        #     f.write(msg)

        # If you want to display results directly in the Domino GUI,
        # you should set the attribute self.display_result
        # self.display_result = {
        #     "file_type": "txt",
        #     "file_path": file_path
        # }

        # Log inputs
        self.logger.info(f"Filterwheel id {input_data.uid} set position tp {input_data.position}")

        #TODO call Filterwheel with Thor command
        
        message = f"Filterwheel piece executed successfully"

        # You should return the results using the Output model
        return OutputModel(
            message=message,
        )