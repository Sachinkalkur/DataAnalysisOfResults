import urllib
import logging

class HttpSchemaClass(object):

    def __init__(self, degree='PU', reg=193150):
        base_url = "http://www.karresults.nic.in/"
        self.postHeaders = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                            'Content-Type': 'application/x-www-form-urlencoded'}
        if degree == 'PU':
            degree_url = "resPUC_2016.asp"
        self.url = base_url + degree_url
        self.reg = reg
        self.postData = urllib.urlencode({'frmpuc_tokens': '0.4622766', 'reg': str(reg)})
        self.response = None
        self.HttpError = None


