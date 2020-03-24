from enum import Enum

class SourceType(Enum):
    """ Power source type enumerations """
    SOLAR = 'SOLAR'
    WIND = 'WIND'
    HYDRO = 'HYDRO'
    BATTERY = 'BATTERY'
    OTHER = 'OTHER'

