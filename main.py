import logging
from readPatientsList import ReadPatientsList
# ? formatting the logging file  
logging_format = "%(asctime)s =>  %(message)s"
logging.basicConfig(filename="PatientsList.log", filemode="w", format=logging_format, level=logging.INFO,
                    datefmt="%H:%M:%S")

# ? add paitnets file name 
EXCEL_FILE_NAME_DR_AFROZA_PATIENTS_LIST = "Dr.Afroza_PatientList_03162021.xls"

"""

Main Method
create object from class ReadPatientsList named read_patients_list
call method get_patients_list

@:exception File Maybe not exist
"""
if __name__ == '__main__':
    try:
        logging.info("Main Method:          Open DR_AfrozaAhmed excel sheet to read patients data")
        read_patients_list = ReadPatientsList(EXCEL_FILE_NAME_DR_AFROZA_PATIENTS_LIST)
        read_patients_list.get_patients_list()
    except FileNotFoundError:
        print("Main Method:", FileNotFoundError)
        logging.error("Main Method:         DR_AfrozaAhmed patient excel file doesn't exist")
