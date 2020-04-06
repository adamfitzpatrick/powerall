import falcon
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
        self.persistence = Persistence(filename)

    def on_get(self, req, res):
        results = self.persistence.get_all()
        res.media = [ data.get_converted_json() for data in results ]
        res.status = falcon.HTTP_200

app = falcon.API(middleware=[
    CorsResponse()
])

all_data = AllDataResource('./data.json')
app.add_route("/", all_data)

if (__name__ == "__main__"):
    resource = AllDataResource('./data.json')
    resource.on_get('', '')
