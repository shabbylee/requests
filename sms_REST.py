import requests
import httplib2
class HttpRequest(object):

    def __init__(self):

        self.url = None
        self.method = None
        self.body = None
        self.headers = None

    def sendRequest(self):

        if self.method == 'GET':

            resp = requests.get(self.url, self.body, self.headers)

            response = resp.json()

            status_code = resp.status_code

            return response

        elif self.method == 'PUT':

            resp = requests.put(self.url, self.body, self.headers)

            response = resp.text

            return response

        elif self.method == 'POST':

            resp = requests.post(self.url, self.body, self.headers)

            response = resp.text

            return response

        elif self.method == 'DELETE':

            resp = requests.delete(self.url, self.body, self.headers)

            response = resp.text

            return response