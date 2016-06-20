from HttpRetreival import DataParser
import csv
import time
import re
import string


class CsvFileWriter(object):
    def __init__(self):
        self.field_values = []
        self.field_names = ["Name", "Reg. No.",
                            "KANNADA", "ENGLISH", "SANSKRIT", "HINDI",
                            "PHYSICS", "CHEMISTRY", "MATHEMATICS", "BIOLOGY", "ELECTRONICS",
                            "COMPUTER SCIENCE", "HOME SCIENCE", "GEOLOGY"]

    def get_data_parser(self, reg_num):
        data = DataParser.DataParser(degree='PU', reg=reg_num)
        data.get_data()
        data.parse_data()
        #print data.student
        self.studentData  = data.student
        #self.field_values.append(data.student)

    def collect_data_csv(self):
        with open(r"C:\Users\kalkurs\Documents\GitHub\DataAnalysisOfResults\Studentmarks.csv", "wb") as out_file:
            writer = csv.DictWriter(out_file, delimiter=',', fieldnames=self.field_names)
            writer.writeheader()
            for row in self.field_values:
                writer.writerow(row)


my_csv = CsvFileWriter()
for register_num in range(193000, 193152):
    my_csv.get_data_parser(register_num)

    for student_keys in my_csv.studentData:
        my_csv.studentType = "Science"
        if not (student_keys in my_csv.field_names):
            my_csv.studentType = "Other"
            break
    if my_csv.studentType == "Science":
        for student_keys in my_csv.field_names:
            if not (student_keys in my_csv.studentData):
                my_csv.studentData[student_keys] = 0
        my_csv.field_values.append(my_csv.studentData)

    print my_csv.field_values

    time.sleep(20)

my_csv.collect_data_csv()

#my_csv.collect_data_csv()
