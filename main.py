import glob
import logging
import os.path
from pathlib import Path

from readPatientsList import ReadPatientsList

# ? formatting the logging file
logging_format = "%(asctime)s =>  %(message)s"
logging.basicConfig(filename="PatientsList.log", filemode="w", format=logging_format, level=logging.INFO,
                    datefmt="%H:%M:%S")

# ? add paitnets file name 
# EXCEL_FILE_NAME_DR_AFROZA_PATIENTS_LIST = "request/Appointments_Report_03.29_to_04.03.2021.xlsx"
# EXCEL_FILE_NAME_DR_AFROZA_PATIENTS_LIST = "Dr.Afroza_PatientList_03162021.xls"

"""

Main Method
create object from class ReadPatientsList named read_patients_list
call method get_patients_list

@:exception File Maybe not exist
"""


def get_request_files():
    return glob.glob(pathname='request/*.*')


if __name__ == '__main__':
    Path("request").mkdir(parents=True, exist_ok=True)
    Path("completed").mkdir(parents=True, exist_ok=True)
    try:
        request_files = get_request_files()
        for file in request_files:
            print(os.path.basename(file))
            logging.info("Main Method:          Open DR_AfrozaAhmed excel sheet to read patients data")
            read_patients_list = ReadPatientsList(file)
            read_patients_list.get_patients_list()
    except FileNotFoundError:
        print("Main Method:", FileNotFoundError)
        logging.error("Main Method:         DR_AfrozaAhmed patient excel file doesn't exist")
