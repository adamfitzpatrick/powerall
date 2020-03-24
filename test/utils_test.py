import unittest2
import helpers.utils as utils

class UtilsTestSuite(unittest2.TestCase):
    def setUp(self):
        self.data = [133, 181]
        self.decimal = 34229
        self.twosCompDecimal = -31307

    def test_generate_16bit_from_8bit_array(self):
        self.assertEqual(self.decimal, utils.generate_16bit_from_8bit_array(self.data))

    def test_convert_twos_complement_to_decimal(self):
        self.assertEqual(self.twosCompDecimal, utils.convert_twos_complement_to_decimal(self.decimal, 16))

    def test_convert_local_iso_time_to_utc(self):
        self.assertEqual('2020-03-24T20:47:42.179834', utils.convert_local_iso_time_to_utc('2020-03-24T13:47:42.179834'))

if __name__ == '__main__':
    unittest2.main()
