from smbus2 import SMBus

class I2C:
    """
    Utility class to provide simple methods for reading from the I2C bus given a
    specific device address.
    """

    _raspberry_pi_i2c_id = 1

    def __init__(self, device_address):
        self.device_address = device_address

    def read_word(self, register_address):
        bus = SMBus(self._raspberry_pi_i2c_id)
        data = bus.read_i2c_block_data(self.device_address, register_address, 2)
        bus.close()
        return data