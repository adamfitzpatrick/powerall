import unittest
from unittest.mock import Mock, patch
from smbus2 import SMBus
from lib.i2c import I2C

@patch('lib.i2c.SMBus')
class I2cTestSuite(unittest.TestCase):
    def test_read_word(self, SMBusMock):
        busMock = Mock()
        busMock.read_i2c_block_data.return_value = [1, 2]
        SMBusMock.return_value = busMock
        i2c = I2C(0x00)
        self.assertEqual(i2c.read_word(0x01), [1, 2])
        busMock.read_i2c_block_data.assert_called_once_with(0x00, 0x01, 2)

if __name__ == '__main__':
    unittest.main()