from enum import Enum

class SourceType(Enum):
    """ Power source type enumerations """
    SOLAR = 1
    WIND = 2
    HYDRO = 3
    BATTERY = 4
    OTHER = 5

