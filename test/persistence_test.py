import unittest
from unittest.mock import patch, MagicMock
from hamcrest import assert_that, not_none, has_entries, instance_of
from datetime import datetime, timedelta
from helpers.persistence import Persistence
from helpers.ina260measurement import Ina260Measurement
from helpers.sourcetypeenum import SourceType

@patch('helpers.persistence.TinyDB')
class PersistenceTestSuite(unittest.TestCase):

    def setUp(self):
        self.measurement = Ina260Measurement('solar', SourceType.SOLAR, [5, 1], [6, 3])
        self.json_object_matcher = {
            'timestamp': not_none(),
            'source_name': 'solar',
            'source_type': 'SOLAR',
            'voltage_measurement': [5, 1],
            'current_measurement': [6, 3],
        }
        self.json_response = {
            'timestamp': 'time',
            'source_name': 'solar',
            'source_type': 'SOLAR',
            'voltage_measurement': [5, 1],
            'current_measurement': [6, 3],
        }

    def test_save_data(self, TinyDBMock):
        persistence = Persistence('path/to/db')
        persistence.save(self.measurement)
        assert_that(
            persistence.table.insert.call_args[0][0],
            has_entries(self.json_object_matcher)
        )

    def test_upsert(self, TinyDBMock):
        persistence = Persistence('path/to/db')
        persistence.upsert(self.measurement)
        self.assertEqual(len(persistence.table.upsert.call_args[0]), 2)
        assert_that(
            persistence.table.upsert.call_args[0][0],
            has_entries(self.json_object_matcher)
        )

    def test_get_latest(self, TinyDBMock):
        persistence = Persistence('path/to/db')
        persistence.table = MagicMock()
        persistence.table.__len__.return_value = 3
        persistence.table.get.return_value = self.json_response
        result = persistence.get_latest()
        assert_that(
            result,
            instance_of(Ina260Measurement)
        )
        persistence.table.get.assert_called_with(doc_id=3)

    def test_get_date(self, TinyDBMock):
        persistence = Persistence('path/to/db')
        persistence.table.search.return_value = [self.json_response]
        today = datetime.today()
        result = persistence.get_date(today)
        assert_that(
            result[0],
            instance_of(Ina260Measurement)
        )
        persistence.table.search.assert_called()

    def test_get_date_range(self, TinyDBMock):
        persistence = Persistence('path/to/db')
        persistence.table.search.return_value = [self.json_response]
        today = datetime.today()
        yesterday = today - timedelta(1)
        result = persistence.get_date_range(yesterday, today)
        assert_that(
            result[0],
            instance_of(Ina260Measurement)
        )
        persistence.table.search.assert_called()

    def test_get_date_range_bad_inputs(self, TinyDBMock):
        persistence = Persistence('path/to/db')
        persistence.table.search.return_value = [self.json_response]
        today = datetime.today()
        yesterday = today - timedelta(1)
        with self.assertRaises(Exception) as cm:
            persistence.get_date_range(today, yesterday)
        self.assertIn('end date is before', cm.exception.args[0])
        persistence.table.search.assert_not_called()


if __name__ == '__main__':
    unittest.main()
