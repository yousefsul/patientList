import glob
import logging
import shutil
from pathlib import Path

import numpy as np
from pandas import unique

from readPatientsList import ReadPatientsList

# ? formatting the logging file
logging_format = "%(asctime)s =>  %(message)s"
logging.basicConfig(filename="PatientsList.log", filemode="w", format=logging_format, level=logging.INFO,
                    datefmt="%H:%M:%S")

"""

Main Method
create object from class ReadPatientsList named read_patients_list
call method get_patients_list

@:exception File Maybe not exist
"""


def get_request_files():
    return glob.glob(pathname='request/*.*')


def move_file(req_file):
    shutil.move(req_file, 'completed')


if __name__ == '__main__':
    Path("request").mkdir(parents=True, exist_ok=True)
    Path("completed").mkdir(parents=True, exist_ok=True)
    try:
        request_files = get_request_files()
        for file in request_files:
            logging.info("Main Method:          Open DR_AfrozaAhmed excel sheet to read patients data")
            read_patients_list = ReadPatientsList(file)
            read_patients_list.get_patients_list()
            move_file(file)
            print("Completed")
    except FileNotFoundError:
        print("Main Method:", FileNotFoundError)
        logging.error("Main Method:         DR_AfrozaAhmed patient excel file doesn't exist")
