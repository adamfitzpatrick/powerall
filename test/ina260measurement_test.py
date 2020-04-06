import unittest
from lib.ina260measurement import Ina260Measurement
from lib.sourcetypeenum import SourceType

class Ina250MeasurementTestSuite(unittest.TestCase):
    def setUp(self):
        self.data = [133, 181]
        self.decimal = 34229
        self.twosDecimal = -31307
        self.measurement = Ina260Measurement('solar', SourceType.SOLAR, self.data, self.data)

    def test_init(self):
        self.assertIsNotNone(self.measurement)
        self.assertIsNotNone(self.measurement.timestamp)
        self.assertEqual(self.measurement.source_name, 'solar')
        self.assertEqual(self.measurement.source_type, 'SOLAR')
        self.assertEqual(self.data, self.measurement.voltage_measurement)
        self.assertEqual(self.data, self.measurement.current_measurement)

    def test_init_with_timestamp(self):
        measurement = Ina260Measurement('solar', SourceType.SOLAR, self.data, self.data, 'timestamp')
        self.assertEqual(measurement.timestamp, 'timestamp')

    def test_voltage(self):
        self.assertAlmostEqual(self.decimal * 0.00125, self.measurement.voltage)

    def test_current(self):
        self.assertAlmostEqual(self.twosDecimal * 0.00125, self.measurement.current)

    def test_source_type_enum(self):
        self.assertEqual(self.measurement.source_type_enum, SourceType.SOLAR)

    def test_get_json(self):
        json = self.measurement.get_json()
        self.assertIsNotNone(json['timestamp'])
        self.assertEqual(json['source_name'], 'solar')
        self.assertEqual(json['source_type'], 'SOLAR')
        self.assertEqual(json['voltage_measurement'], self.data)
        self.assertEqual(json['current_measurement'], self.data)

    def test_get_converted_json(self):
        json = self.measurement.get_converted_json()
        self.assertAlmostEqual(json['voltage'], self.measurement.voltage)
        self.assertAlmostEqual(json['current'], self.measurement.current)

if __name__ == '__main__':
    unittest.main()
