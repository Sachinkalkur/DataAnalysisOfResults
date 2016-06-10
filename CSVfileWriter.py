from HttpRetreival import DataParser
from collections import OrderedDict
import csv
import re


class CsvFileWriter(object):
    def __init__(self):
        self.data = DataParser.DataParser(degree='PU', reg=193158)
        self.data.get_data()
        if self.data.HttpError is not None:
            print self.data.HttpError
        else:
            print self.data.response
        result = self.data.parse_data()
        if result == "SUCCESS":
            print self.data.student
        else:
            print "its a failure \n"
        field_names = ['Name', "ECONOMICS", "KANNADA",  "LOGIC", "Reg. No.", "POLITICAL SCIENCE", "ENGLISH", "HISTORY"]
        #fieldvalues = [self.data.student[field] for field in fieldnames]
        #self.csvdict = dict(zip(fieldnames, fieldvalues))
        #print self.csvdict
        with open(r"C:\Users\kalkurs\Documents\GitHub\DataAnalysisOfResults\Studentmarks.csv", "wb") as out_file:
            writer = csv.DictWriter(out_file, delimiter=',', fieldnames=field_names)
            writer.writeheader()
            for row in self.data.student:
                print row
                writer.writerow(row)




my_csv = CsvFileWriter()
