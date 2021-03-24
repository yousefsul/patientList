import logging
from readPatientsList import ReadPatientsList
# ? formatting the logging file  
logging_format = "%(asctime)s =>  %(message)s"
logging.basicConfig(filename="PatientsList.log", filemode="w", format=logging_format, level=logging.INFO,
                    datefmt="%H:%M:%S")

# ? add paitnets file name 
EXCEL_FILE_NAME_DR_AFROZA_PATIENTS_LIST = "Dr.Afroza_PatientList_03162021.xls"

"""
* Main Method 
"""
if __name__ == '__main__':
    try:
        logging.info("Main Method:          Open DR_AfrozaAhmed excel sheet to read patients data")
    except FileNotFoundError:
        print("Main Method:", FileNotFoundError)
        logging.error("Main Method:         DR_AfrozaAhmed patient excel file doesn't exist")
