from tinydb import TinyDB

class Persistence:
    """
    Library module which provides convenience methods to persist power data
    
    Data is persisted to a JSON file using TinyDB for simplicity.  This class
    provides access to data in a specific file provided during class initialization.
    The assumption is that data includes voltage & current readings for one or more
    solar or wind power sources for each moment in time, however it is possible to
    leave readings empty for any given timestamp.

    Schema:
        timestamp:    string UTC ISO time for the measurements
        measurements: array of voltage and current measurements and associated metadata
            name:     string indicating name of power source
            type:     string indicating power type (e.g., SOLAR)
            voltage:  float voltage reading
            current:  float current reading
        

