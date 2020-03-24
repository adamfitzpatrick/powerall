from dateutil import parser

def generate_16bit_from_8bit_array(arr):
    return (arr[0] << 8) | arr[1]

def convert_twos_complement_to_decimal(val, bits):
    sign = val & (1 << (bits - 1))
    if (sign != 0):
        return val - (1 << bits)
    return val

def convert_local_iso_time_to_utc(localIsoTime):
    local = parser.parse(localIsoTime).astimezone()
    return (local - local.utcoffset()).isoformat()[:-6]
