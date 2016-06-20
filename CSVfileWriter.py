from HttpRetreival import DataParser
import csv
import time
import logging


class CsvFileWriter(object):
    def __init__(self):

        logging.basicConfig(level=logging.DEBUG)
        self.data_logger = logging.getLogger(__name__)
        data_file_handler = logging.FileHandler('topLevel.log')
        data_file_handler.setLevel(logging.INFO)
        self.data_logger.addHandler(data_file_handler)

        self.field_values = []
        self.field_names = ["Name", "Reg. No.",
                            "KANNADA", "ENGLISH", "SANSKRIT", "HINDI",
                            "PHYSICS", "CHEMISTRY", "MATHEMATICS", "BIOLOGY", "ELECTRONICS",
                            "COMPUTER SCIENCE", "HOME SCIENCE", "GEOLOGY"]

        self.data_logger.info("Logging Has been Initiated")

    def get_data_parser(self, reg_num):
        data = DataParser.DataParser(degree='PU', reg=reg_num)
        data.get_data()
        data.parse_data()
        self.studentData  = data.student

    def collect_data_csv(self):
        with open(r"C:\Users\kalkurs\Documents\GitHub\DataAnalysisOfResults\Studentmarks.csv", "wb") as out_file:
            writer = csv.DictWriter(out_file, delimiter=',', fieldnames=self.field_names)
            writer.writeheader()
            for row in self.field_values:
                writer.writerow(row)


my_csv = CsvFileWriter()
for register_num in range(193140, 193152):
    my_csv.get_data_parser(register_num)

    for student_keys in my_csv.studentData:
        my_csv.studentType = "Science"
        if not (student_keys in my_csv.field_names):
            my_csv.studentType = "Other"
            my_csv.data_logger.info("The student with register number {} is a non-science student".format(register_num))
            break

    if my_csv.studentType == "Science":
        my_csv.data_logger.info("The student with register number {} is a science student".format(register_num))
        for student_keys in my_csv.field_names:
            if not (student_keys in my_csv.studentData):
                my_csv.studentData[student_keys] = 0
        my_csv.data_logger.info("====================================================================================")
        my_csv.data_logger.info("Corresponding data of the student is %s", my_csv.studentData)
        my_csv.data_logger.info("====================================================================================")
        my_csv.field_values.append(my_csv.studentData)

    time.sleep(20)

my_csv.data_logger.info("Data Collection is complete and total number of science students is {}"
                        .format(my_csv.field_values.__len__()))
my_csv.collect_data_csv()
my_csv.data_logger.info("Data has been written into the CSV file")

print "Completed"
