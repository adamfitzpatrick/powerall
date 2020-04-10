import sys
import getopt
import falcon
import json
from dateutil import parser

from lib.persistence import Persistence

class CorsResponse(object):
    """
    Adds standard CORS headers to the outgoing response so that browsers
    will block the incoming data.
    """
    def process_response(self, req, res, resource, req_suceeded):
        res.set_header('access-control-allow-origin', '*')
        res.set_header('access-control-allow-headers', 'content-type')
        res.set_header('access-control-allow-methods', 'GET')
        res.set_header('access-control-max-age', 86400)
        res.set_header('vary', 'Origin')

class AllDataResource(object):
    """
    Class to retrieve all measurement data currently stored in the database.
    """

    def __init__(self, filename):
        self.filename = filename

    def on_get(self, req, res):
        persistence = Persistence(self.filename)
        results = persistence.get_all()
        res.media = [ data.get_converted_json() for data in results ]
        res.status = falcon.HTTP_200

class DateRangeDataResource(object):
    """
    Class to retrieve a subset of available data based on an inclusive start datetime
    and end datetime.
    """

    def __init__(self, filename):
        self.filename = filename

    def on_post(self, req, res):
        persistence = Persistence(self.filename)
        body = json.loads(req.stream.read(req.content_length or 0).decode('utf-8'))
        start = parser.parse(body['startDate'])
        end = parser.parse(body['endDate'])
        results = persistence.get_date_range(start, end)
        res.media = [ data.get_converted_json() for data in results ]
        res.status = falcon.HTTP_200

app = falcon.API(middleware=[
    CorsResponse()
])

with open('config.json') as config_file:
    data = json.load(config_file)

db_location = data['dbPath'] + data['dbFile']

all_data = AllDataResource(db_location)
app.add_route("/", all_data)

data_range_data = DateRangeDataResource(db_location)
app.add_route("/dates", data_range_data)

