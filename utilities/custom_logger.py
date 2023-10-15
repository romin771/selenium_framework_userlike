import inspect
import logging
import os


def customLogger(logLevel=logging.DEBUG): #defult value is DEBUG, so if we dont privide it from outside, we want everything gonna be log
    # Gets the name of the class / method from where this method is called
    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)
    # By default, log all messages
    logger.setLevel(logging.DEBUG)

    if not os.path.exists('reports'):
        os.makedirs('reports')

    # Specify the log file path inside the 'reports' directory
    log_file_path = os.path.join('reports', 'automation.log')

    fileHandler = logging.FileHandler(log_file_path, mode='w')
    fileHandler.setLevel(logLevel)





    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)

    return logger
