from HttpClass import HttpClass
from bs4 import BeautifulSoup
import re
import csv


class DataParser(HttpClass):
    def __init__(self):
        super(DataParser, self).__init__()
        self.get_data()
        if self.HttpError is not None:
            print self.HttpError

data = DataParser()
