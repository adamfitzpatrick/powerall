from datetime import datetime, time, timedelta
from tinydb import TinyDB, Query, where
from lib.utils import convert_local_iso_time_to_utc
from lib.sourcetypeenum import SourceType
from lib.ina260measurement import Ina260Measurement

MEASUREMENTS_TABLE_NAME = 'measurements'

class Persistence:
    """
    Library module which provides convenience methods to persist power data

    Data is persisted to a JSON file using TinyDB for simplicity.  This class
    provides access to data in a specific file provided during class initialization.
    The assumption is that data includes voltage & current readings for one solar
    or wind power sources for each moment in time.

    Schema matches the structure of Ina260Measurement
    """
    def __init__(self, path):
        self.db = TinyDB(path)
        self.table = self.db.table(MEASUREMENTS_TABLE_NAME)

    def save(self, ina260Measurement):
        self.table.insert(ina260Measurement.get_json())

    def upsert(self, ina260Measurement):
        query = Query()
        self.table.upsert(ina260Measurement.get_json(), query.timestamp == ina260Measurement.timestamp)

    def get_all(self):
        results = self.table.search(where('timestamp').exists())
        return [ self.__generate_measurement(data) for data in results ]

    def get_latest(self):
        data = self.table.get(doc_id=len(self.table))
        return self.__generate_measurement(data)

    def get_date(self, date):
        start = datetime.combine(date, time())
        end = datetime.combine(date + timedelta(1), time())
        return self.get_date_range(start, end)

    def get_date_range(self, startDate, endDate):
        if (endDate < startDate):
            raise TypeError('end date is before start date')

        startUtc = convert_local_iso_time_to_utc(startDate.isoformat())
        endUtc = convert_local_iso_time_to_utc(endDate.isoformat())
        Measurement = Query()
        results = self.table.search((Measurement.timestamp >= startUtc) & (Measurement.timestamp < endUtc))
        return [ self.__generate_measurement(data) for data in results ]

    def __generate_measurement(self, data):
        return Ina260Measurement(
            data['source_name'],
            SourceType(data['source_type']),
            data['voltage_measurement'],
            data['current_measurement'],
            data['timestamp']
        )

