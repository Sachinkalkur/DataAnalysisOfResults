from HttpClass import HttpSchemaClass
import urllib2
from bs4 import BeautifulSoup
import logging

class DataParser(HttpSchemaClass):
    def __init__(self, **kwargs):
        super(DataParser, self).__init__(kwargs['degree'], kwargs['reg'])
        self.namesError = None
        self.student = {}
        self.tables_result = ["FAILURE", "FAILURE", "FAILURE"]

    def get_data(self):
        request_data = urllib2.Request(self.url, self.postData, self.postHeaders)
        try:
            response_data = urllib2.urlopen(request_data)
            self.response = response_data.read()
        except urllib2.HTTPError, e:
            self.HttpError = e.fp.read()

    def parse_data(self):

        def extract_names(given_table):
            try:
                for row in given_table.findAll('tr'):
                    cells = row.findAll('td')
                    self.student[str(cells[0].find(text=True))] = str(cells[len(cells)-1].find(text=True)).lstrip()\
                        .rstrip()
                self.tables_result[1] = 'SUCCESS'
            except:
                self.namesError = "Something wrong with name table parsing for registration Number {}".format(self.reg)

        def extract_marks(given_table):
            try:
                for row in given_table.findAll('tr'):
                    cells = row.findAll('td')
                    if len(cells) > 2:
                        key = cells[0].find(text=True)
                        value = cells[len(cells)-1].find(text=True)
                        key = str(key.encode('ascii', 'ignore').decode('ascii'))
                        value = str(value.encode('ascii', 'ignore').decode('ascii'))
                        self.student[key] = value.lstrip().rstrip()
                self.tables_result[2] = "SUCCESS"
            except:
                self.namesError = "Something wrong with mark table parsing for registration Number {}".format(self.reg)

        try:
            assert (len(self.response) > 0), 'Empty results page, PU Board might have closed the page'
            soup_parsed = BeautifulSoup(self.response, 'html.parser')
            #soup_parsed = BeautifulSoup(open(r"C:\Users\kalkurs\PycharmProjects\untitled1\results.html"), 'html.parser')
            name_table = soup_parsed.find('table', {'class': "table"})
            assert (len(name_table) > 0), 'Unknown Entity found without Name'
            extract_names(name_table)
            assert(self.tables_result[1] is not 'FAILURE'), 'Unable to write the name to the file'
            for marksTable in soup_parsed.find('table').parent.find_next_siblings():
                if len(marksTable) > 0:
                    assert (len(marksTable) > 0), 'Marks of The student not found'
                    extract_marks(marksTable)
                    assert(self.tables_result[2] is not 'FAILURE'), 'Unable to write marks of student to the file'
            self.tables_result[0] = "SUCCESS"
            return self.tables_result[0]

        except urllib2.HTTPError, e:
            print e.fp.read()

# data = DataParser(degree='PU', reg='193158')
#
# data.get_data()
# if data.HttpError is not None:
#     print data.HttpError
# else:
#     print data.response
#
# result = data.parse_data()
# if result == "SUCCESS":
#     print data.student
# else:
#     print "its a failure \n"
