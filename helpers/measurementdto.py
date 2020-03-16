from helpers.utils import generate_16bit_from_8bit_array, convert_twos_complement_to_decimal
from datetime import datetime

class MeasurementDTO:
    register_bit_size = 16
    voltage_multiplier = 0.00125
    current_multiplier = 0.00125
    """
    DTO for voltage and current measurements for a power source at a specific time

    Class is primarily intended for use with a TI INA260 precision power monitor.  Reading
    from the voltage and current measurement registers provide a binary representation of
    the desire value at a specific point in time.  In order to facilitate accurate collection
    of data and the possible need to revisit conversions into standard voltage or current
    values, the data collected from the INA260 is stored as raw values associated with
    a timestamp.

    timestamp: string ISO representation of UTC time when the measurement was recorded
    source_name: string descriptive name of power source
    source_type: SourceTypeEnum
    voltageMeasurement: 16 bit representation of voltage measurement
    currentMeasurement: 16 bit representation of current measurement
    """

    def __init__(self, source_name, source_type, voltage, current):
        """
        Initialize the class data

        Voltage and current are provided in a length 2 array of 8 bit values.
        """
        self.timestamp = datetime.utcnow().isoformat()
        self.source_name = source_name
        self.source_type = source_type
        self.voltageMeasurement = generate_16bit_from_8bit_array(voltage)
        self.currentMeasurement = generate_16bit_from_8bit_array(current)

    @property
    def voltage(self):
        """Returns a decimal representation of the measured voltage""
        return self.voltageMeasurement * self.voltage_multiplier

    @property
    def current(self):
        return convert_twos_complement_to_decimal(self.currentMeasurement, self.register_bit_size) * self.current_multiplier

