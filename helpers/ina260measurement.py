from datetime import datetime
from helpers.utils import generate_16bit_from_8bit_array, convert_twos_complement_to_decimal
from helpers.sourcetypeenum import SourceType

class Ina260Measurement:
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

    _register_bit_size = 16
    _voltage_multiplier = 0.00125
    _current_multiplier = 0.00125
    _json_fields = { 'timestamp', 'source_name', 'source_type', 'voltage_measurement', 'current_measurement' }

    def __init__(self, source_name, source_type, voltage_measurement, current_measurement):
        """
        Initialize the class data

        Voltage and current are provided in a length 2 array of 8 bit values.
        """
        self.timestamp = datetime.utcnow().isoformat()
        self.source_name = source_name
        self.source_type = source_type.value
        self.voltage_measurement = voltage_measurement
        self.current_measurement = current_measurement

    @property
    def voltage(self):
        """Returns a decimal representation of the measured voltage"""
        return generate_16bit_from_8bit_array(self.voltage_measurement) * self._voltage_multiplier

    @property
    def current(self):
        """Returns a decimal representation of the measured current"""
        return convert_twos_complement_to_decimal(
            generate_16bit_from_8bit_array(self.current_measurement), self._register_bit_size
        ) * self._current_multiplier

    @property
    def source_type_enum(self):
        """Returns a string representation of the source type"""
        return SourceType(self.source_type)

    def get_json(self):
        return { field: getattr(self, field) for field in self._json_fields }

