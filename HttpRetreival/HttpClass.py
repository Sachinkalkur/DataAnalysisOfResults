import urllib2
import urllib


class HttpClass(object):

    def __init__(self, degree='PU', register_number=193150):
        base_url = "http://www.karresults.nic.in/"
        self.postHeaders = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                            'Content-Type': 'application/x-www-form-urlencoded'}
        if degree == 'PU':
            degree_url = "resPUC_2016.asp"
        self.url = base_url + degree_url
        self.postData = urllib.urlencode({'frmpuc_tokens': '0.4622766', 'reg': str(register_number)})
        self.response = None
        self.HttpError = None

    def get_data(self):
        request_data = urllib2.Request(self.url, self.postData, self.postHeaders)
        try:
            response_data = urllib2.urlopen(request_data)
            self.response = response_data.read()
        except urllib2.HTTPError, e:
            self.HttpError = e.fp.read()
