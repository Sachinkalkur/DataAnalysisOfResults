from HttpClass import HttpSchemaClass
import urllib2
from bs4 import BeautifulSoup
import time


class DataParser(HttpSchemaClass):
    def __init__(self, **kwargs):
        super(DataParser, self).__init__(kwargs['degree'], kwargs['reg'])
        self.namesError = None
        self.student = {}
        self.tables_result = ["FAILURE", "FAILURE", "FAILURE"]

    def get_data(self, logger):
        request_data = urllib2.Request(self.url, self.postData, self.postHeaders)
        try:
            response_data = urllib2.urlopen(request_data)
            self.response = response_data.read()
        except urllib2.HTTPError, e:
            logger.error("encountered error while getting result pages")
            logger.error(e.fp.read())
            self.HttpError = e.fp.read()
            time.sleep(120)

    def parse_data(self, logger):

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
                        self.student[key] = int(value.lstrip().rstrip()[:-1])
                self.tables_result[2] = "SUCCESS"
            except:
                self.namesError = "Something wrong with mark table parsing for registration Number {}".format(self.reg)

        try:
            if not len(self.response) > 0:
                self.namesError = 'Empty results page, PU Board might have closed the page'
                logger.error(self.namesError)
            else:
                soup_parsed = BeautifulSoup(self.response, 'html.parser')
                name_table = soup_parsed.find('table', {'class': "table"})
                if not len(name_table) > 0:
                    logger.error('Unknown Entity found without Name for the student')
                else:
                    extract_names(name_table)
                    if self.tables_result[1] is 'FAILURE':
                        logger.error('Unable to write the name to the file')
                        logger.error(self.namesError)
                    else:
                        for marksTable in soup_parsed.find('table').parent.find_next_siblings():
                            if len(marksTable) > 0:
                                extract_marks(marksTable)
                                if self.tables_result[2] is 'FAILURE':
                                    logger.error('Unable to write marks of student to the file')
                                    logger.error(self.namesError)
                        if self.tables_result[2] is 'SUCCESS':
                            self.tables_result[0] = "SUCCESS"

        except:
            print("Assertion Error raised and log has been written")
            pass

if __name__ == '__main':
    #soup_parsed = BeautifulSoup(open(r"C:\Users\kalkurs\PycharmProjects\untitled1\results.html"), 'html.parser')
    print "In the main function for testing"