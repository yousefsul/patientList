from pymongo import *
import logging

MONGO_CLIENT = "mongodb://yousef:Ys2021xch@209.151.150.58:63327/?authSource=admin&readPreference=primary&appname" \
               "=MongoDB%20Compass&ssl=false"
"""
class ConnectMongoDB

Methods:

constructor  --> 
    param no params
    
    call from --> get_patients_list method in ReadPatientsList class
---------------------------------------------------------------------------------
connect_to_patient_list_collection
    param no params
    
    call from --> get_patients_list method in ReadPatientsList class
----------------------------------------------------------------------------------
insert_to_patients_collection
    param result 
    
    call from --> get_patients_list method in ReadPatientsList class
----------------------------------------------------------------------------------

"""


class ConnectMongoDB:
    """
    connect to Mongodb
    initalze the database of dr_aforza ahmed
    define the paitnets_collection
    """
    def __init__(self):
        try:
            self.mongo_client = MongoClient(MONGO_CLIENT)
            self.client_db = self.mongo_client.client_2731928905_DB
            self.paitnets_collection = None
        except ConnectionError:
            logging.error("constructor Method:         Error while connecting to mongoDB")
            print("ConnectMongoDB Constructor:", ConnectionError)

    """
    create connection to paitnets collection 
    """
    def connect_to_patient_collection(self):
        self.paitnets_collection = self.client_db.patientsColl

    """
    insert the patinet data into mongodb under patientsColl collection
    """

    def insert_to_patients_collection(self, result):
        try:
            self.paitnets_collection.insert(result)
            logging.warning("insert_to_patients_collection Method:         Insert paitent data to patients collection")
        except Exception as e:
            logging.warning("insert_to_patients_collection Method:         Error While inserting records to patients "
                            "collection")
            print("An exception have occurred while inserting to mongodb", e)
