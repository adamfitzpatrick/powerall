from threading import Thread
from time import sleep

from lib.sourcetypeenum import SourceType
from lib.i2c import I2C
from lib.ina260measurement import Ina260Measurement
from lib.persistence import Persistence

class CollectSolarData:
    """
    Primary class to collect samples from a specific solar source at specified intervals.
    Collects voltage and current information at each point in time and persists the data
    to using the persistence library.
    """

    _source_type = SourceType.SOLAR

    def __init__(self, data_name, sample_interval, db_filename):
        self.data_name = data_name
        self.sample_interval = sample_interval
        self.persistence = Persistence(db_filename)
        self.i2c = I2C(Ina260Measurement.DEVICE_ADDRESS)

    def _collect_sample(self):
        sample = Ina260Measurement(
            self.data_name,
            self._source_type,
            self.i2c.read_word(Ina260Measurement.VOLTAGE_REGISTER),
            self.i2c.read_word(Ina260Measurement.CURRENT_REGISTER)
        )
        self.persistence.save(sample)

    def _sample_loop(self):
        while True:
            self._collect_sample()
            sleep(self.sample_interval)

    def start(self):
        print("Starting collection: %s", self.data_name)
        self.thread = Thread(target=self._sample_loop)
        self.thread.start()

if __name__ == "__main__":
    solar_collector = CollectSolarData('HQST 100W panel', 300, './data.json')
    solar_collector.start()