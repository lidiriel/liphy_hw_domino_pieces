from domino.base_piece import BasePiece
from .models import InputModel, OutputModel
import importlib.util


class IncubatorSensorPiece(BasePiece):

    def piece_function(self, input_data: InputModel):
        # Log inputs
        self.logger.info(f"Get sensors values from incubator with id {input_data.uid}")

        #TODO call pump with Thor command
        
        message = f"Incubator sensor piece executed successfully"
        temperature_target = 37.5
        temperature_sensor1 = 36.0
        temperature_sensor2 = 33.0

        # Return output
        return OutputModel(
            message=message,
            temperature_target=temperature_target,
            temperature_sensor1=temperature_sensor1,
            temperature_sensor2=temperature_sensor2
        )