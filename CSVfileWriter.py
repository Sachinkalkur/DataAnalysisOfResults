from HttpRetreival import DataParser
import LoggerModule
import csv
import time
import os


class CsvFileWriter(object):
    def __init__(self):
        path = os.getcwd()
        LoggerModule.flush_logs()
        self.data_logger = LoggerModule.csv_loggers(path)
        self.field_values = []
        self.field_names = ["Name", "Reg. No.",
                            "KANNADA", "ENGLISH", "SANSKRIT", "HINDI",
                            "PHYSICS", "CHEMISTRY", "MATHEMATICS", "BIOLOGY", "ELECTRONICS",
                            "COMPUTER SCIENCE", "HOME SCIENCE", "GEOLOGY"]

        self.data_logger.debug("Logging Has been Initiated")
        self.studentData = None

    def get_data_parser(self, reg_num):
        data = DataParser.DataParser(degree='PU', reg=reg_num)
        data.get_data(self.data_logger)
        if data.HttpError is None:
            data.parse_data(self.data_logger)
            if data.tables_result[0] is 'SUCCESS':
                self.studentData = data.student

    def collect_data_csv(self):
        with open(r"C:\Users\kalkurs\Documents\GitHub\DataAnalysisOfResults\Studentmarks.csv", "wb") as out_file:
            writer = csv.DictWriter(out_file, delimiter=',', fieldnames=self.field_names)
            writer.writeheader()
            for row in self.field_values:
                writer.writerow(row)


my_csv = CsvFileWriter()
for register_num in range(173000, 194000):
    my_csv.get_data_parser(register_num)
    print "Got data for student with register number {}".format(register_num)
    if my_csv.studentData is not None:

        for student_keys in my_csv.studentData:
            my_csv.studentType = "Science"
            if not (student_keys in my_csv.field_names):
                my_csv.studentType = "Other"
                my_csv.data_logger.debug("The student with register number {} is a non-science student"
                                         .format(register_num))
                break

        if my_csv.studentType == "Science":
            my_csv.data_logger.debug("The student with register number {} is a science student".format(register_num))
            for student_keys in my_csv.field_names:
                if not (student_keys in my_csv.studentData):
                    my_csv.studentData[student_keys] = 0
            my_csv.data_logger.debug("================================================================================")
            my_csv.data_logger.debug("Corresponding data of the student is %s", my_csv.studentData)
            my_csv.data_logger.debug("================================================================================")
            my_csv.field_values.append(my_csv.studentData)

        time.sleep(20)

my_csv.data_logger.debug("Data Collection is complete and total number of science students is {}"
                         .format(my_csv.field_values.__len__()))
my_csv.collect_data_csv()
my_csv.data_logger.debug("Data has been written into the CSV file")

print "Completed"
