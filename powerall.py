from threading import Thread
from time import sleep
import json

from lib.sourcetypeenum import SourceType
from lib.i2c import I2C
from lib.ina260measurement import Ina260Measurement
from lib.persistence import Persistence

class CollectData:
    """
    Primary class to collect samples from a specific solar source at specified intervals.
    Collects voltage and current information at each point in time and persists the data
    to using the persistence library.
    """

    def __init__(self, data_name, sample_interval, source_type, db_filename):
        self.data_name = data_name
        self.sample_interval = sample_interval
        self.source_type = SourceType[source_type]
        self.persistence = Persistence(db_filename)
        self.i2c = I2C(Ina260Measurement.DEVICE_ADDRESS)

    def _collect_sample(self):
        sample = Ina260Measurement(
            self.data_name,
            self.source_type,
            self.i2c.read_word(Ina260Measurement.VOLTAGE_REGISTER),
            self.i2c.read_word(Ina260Measurement.CURRENT_REGISTER)
        )
        self.persistence.save(sample)

    def _sample_loop(self):
        while True:
            self._collect_sample()
            sleep(self.sample_interval)

    def start(self):
        print("Starting collection:", self.data_name)
        self.thread = Thread(target=self._sample_loop)
        self.thread.start()

def startSamplers(sample):
    collector = CollectData(sample['name'], sample['interval'], sample['sourceType'], db_location)
    collector.start()

if __name__ == "__main__":
    with open('config.json') as config_file:
        data = json.load(config_file)

    db_location = data['dbPath'] + data['dbFile']
    sample_sets = data['sampleSets']

    [ startSamplers(sample) for sample in sample_sets ]