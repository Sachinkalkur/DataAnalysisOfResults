import logging
import os


class LogHandler(object):
    current_path = os.getcwd()
    format = '%(levelname)s: %(name)s: %(message)s'
    files = {
        'ERROR': current_path + '\LogFolder/\/' + 'errorAccumulator.log',
        'INFO': current_path + '\LogFolder/\/' + 'dataCollector.log',
        'DEBUG': current_path + '\LogFolder/\/' + 'dataParser.log',
    }

    def write(self, msg):
        msg_type = msg.split(':')
        try:
            with open(self.files.get(msg_type[0], 'log.log'), 'a') as f:
                f.write(msg)
        except IOError:
            with open(self.files.get(msg_type[0], 'log.log'), 'w+') as f:
                f.write("Log file : {} created".format(self.files.get(msg_type[0], 'log.log')))
                f.flush()
            self.write(msg)


def flush_logs():
    current_path = os.getcwd()
    files = {
        'ERROR': current_path + '\LogFolder/\/' + 'errorAccumulator.log',
        'INFO': current_path + '\LogFolder/\/' + 'dataCollector.log',
        'DEBUG': current_path + '\LogFolder/\/' + 'dataParser.log',
    }
    for key_d in files:
        try:
            with open(files.get(key_d, 'log.log'), 'w+') as f:
                f.flush()
        except IOError:
            pass


def csv_loggers(current_path):
        logging.basicConfig(format=LogHandler.format, stream=LogHandler(), level=logging.DEBUG)
        try:
            os.mkdir(current_path + '\LogFolder')
        except OSError:
            logger = logging.getLogger('DataScienceApplication')
        except:
            logging.error("Unable to create directory")

        return logger

if __name__ == '__main__':
    path = os.getcwd()
    flush_logs()
    log_instance = csv_loggers(path)
    log_instance.debug("This is debug message")
    log_instance.error("This is error message")
