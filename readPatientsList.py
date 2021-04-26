import datetime

import numpy as np
import pandas as pd
import logging
import shortuuid
from patientInfo import PatientInfo
from connectMongoDB import ConnectMongoDB

"""
class ReadPatientsList

Methods:

constructor -->
    param patients_list_file

    call from --> Main Method
------------------------------------------------
get_patients_list -->
    param no params

    call from --> Main Method
------------------------------------------------
Functions

generate_paitent_id -->
    param no params

    call from --> get_patients_list method
    
    return int 10 length 
"""


# Generate New ID for each patient with 10 numeric number
def generate_paitent_id():
    return int(shortuuid.ShortUUID(alphabet="0123456789").random(length=10))


class ReadPatientsList:
    """
    define the patient list file
    define the dataframe for the patient list file skip the first row beacuse have non valuable replace the Nan Number
    to empty string
    create object from class PatientInfo named patient_info as None
    define patient that we will have for each patient as None
    create object from class ConnectMongoDB named connection
    """

    def __init__(self, patients_list_file):
        self.patients_list_file = patients_list_file
        # self.patients_list_file_dataframe = pd.read_excel(self.patients_list_file,
        #                                                   sheet_name="Updates_New_Patients",
        #                                                   skiprows=1).replace(np.nan, '', regex=True)

        self.patients_list_file_dataframe = pd.read_excel(self.patients_list_file,
                                                          sheet_name="PatientsList_03162021",
                                                          skiprows=1).replace(np.nan, '', regex=True)
        self.patient = None
        self.patient_info = None
        self.date = datetime.datetime.now().date().strftime("%Y%m%d")
        self.time = datetime.datetime.now().time().strftime("%H:%M:%S")
        self.connection = ConnectMongoDB()

    """
    read rows in dr afroza patient list excel sheet 
    initialize the object of class PatientInfo
    define patient information by extracting the patient data from excel sheet columns using object patient_info     
    connect to patient collection in monogdb using the object connection      
    """

    def get_patients_list(self):
        self.connection.connect_to_patient_collection()
        try:
            for count, row in self.patients_list_file_dataframe.iterrows():
                patient_data = self.patients_list_file_dataframe.loc[count]
                self.patient_info = PatientInfo(patient_data)
                self.patient = {
                    "header_section": {
                        "document_id": generate_paitent_id(),
                        "date_created": {
                            "date": self.date,
                            "time": self.time
                        },
                        "current_status": {
                            "status": self.patient_info.get_patient_status(),
                            "date": {
                                "date": self.date,
                                "time": self.time
                            },
                        },
                        "status_history": [self.patient_info.get_current_status()],
                    },
                    "patient_info": {
                        "office_ally_id": self.patient_info.get_patient_office_ally_id(),
                        "patient_id": generate_paitent_id(),
                        "patient_name": {
                            "last": self.patient_info.get_patient_last_name(),
                            "first": self.patient_info.get_patient_first_name(),
                            "middle": self.patient_info.get_patient_middle_name()
                        },
                        "date_of_birth": self.patient_info.get_patient_date_of_birth(),
                        "gender": self.patient_info.get_patient_gender(),
                        "address": {
                            "street_address": self.patient_info.get_patient_street_address(),
                            "city": self.patient_info.get_patient_city(),
                            "state": self.patient_info.get_patient_state(),
                            "zip": self.patient_info.get_patient_zip()
                        },
                        "patient_contact": {
                            "cell_phone_number": self.patient_info.get_patient_cell_phone_number(),
                            "home_phone_number": self.patient_info.get_patient_home_phone_number(),
                            "email": self.patient_info.get_patient_email(),
                        },
                        "account_type": self.patient_info.get_patient_account_type(),
                        "status": self.patient_info.get_patient_status(),
                        "dx_codes": self.patient_info.get_patient_dx_codes()
                    },
                    "primary_insurance": self.patient_info.get_patient_primary_insurance_array(),
                    "home_plan_insurance": self.patient_info.get_patient_home_plan_info(),
                    "plan_admin": self.patient_info.get_patient_plan_admin_info(),
                    "secondary_insurance": self.patient_info.get_patient_secondary_insurance_array(),
                    "tertiary_insurance": self.patient_info.get_patient_tertiary_insurance_array(),
                }
                print(self.patient)
                # self.connection.insert_to_patients_collection(self.patient)
        except ValueError:
            print("get_patients_list Method:", ValueError)
            logging.error("get_patients_list:         Error While Reading Data")
