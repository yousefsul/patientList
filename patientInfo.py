import datetime
import math
import pandas as pd

"""
class ReadPatientsList

Methods:

constructor -->
    param patient_info

    call from --> get_patients_list method in ReadPatientsList class
------------------------------------------------
getters for each paitent data 
------------------------------------------------
Functions
"""


class PatientInfo:
    """
    get the full name of the paitent and subscriber and manipulate it
    """

    def __init__(self, patient_info):
        self.patient_info = patient_info
        self.patient_full_name = self.patient_info.get("Patient Name (Last, First MI)").split(",")
        self.patient_middle_first_name = self.patient_full_name[1].split(" ")
        # self.patient_date_of_birth = str(self.patient_info.get("DOB")).split("/")
        # print(self.patient_info.get('DOB'),"    ",type(self.patient_info.get('DOB')))
        self.patient_date_of_birth = pd.to_datetime(str(self.patient_info.get('DOB')))
        self.patient_date_of_birth = self.patient_date_of_birth.strftime('%Y%m%d')
        self.primary_insurance_subscriber_full_name = self.patient_info.get("Subscriber Name").split(",")
        if self.patient_info.get("Secondary Subscriber Name") == "":
            self.subscriber_first_secondary_insurance = ""
            self.subscriber_last_secondary_insurance = ""
        else:
            self.subscriber_full_name_secondary_insurance = self.patient_info.get("Secondary Subscriber Name").split(
                ",")
            self.subscriber_first_secondary_insurance = self.subscriber_full_name_secondary_insurance[1].strip()
            self.subscriber_last_secondary_insurance = self.subscriber_full_name_secondary_insurance[0].strip()

    def get_patient_office_ally_id(self):
        return int(self.patient_info.get("Office Ally ID"))

    def get_patient_last_name(self):
        return self.patient_full_name[0].strip()

    def get_patient_first_name(self):
        return self.patient_middle_first_name[1].strip()

    def get_patient_middle_name(self):
        return self.patient_middle_first_name[2].strip()

    def get_patient_date_of_birth(self):
        return self.patient_date_of_birth
    #     return self.patient_date_of_birth[2] + self.patient_date_of_birth[0] + self.patient_date_of_birth[1]

    def get_patient_gender(self):
        return self.patient_info.get("Gender")

    def get_patient_street_address(self):
        return self.patient_info.get("Patient Address").strip()

    def get_patient_city(self):
        return self.patient_info.get("Patient City")

    def get_patient_state(self):
        return self.patient_info.get("Patient State")

    def get_patient_zip(self):
        return str(self.patient_info.get("Patient Zip"))

    def get_patient_home_phone_number(self):
        home_phone_number = self.patient_info.get("Patient Cell Phone Number").replace("-", "")
        return int(home_phone_number)

    def get_patient_cell_phone_number(self):
        cell_phone_number = self.patient_info.get("Patient Cell Phone Number").replace("-", "")
        return int(cell_phone_number)

    def get_patient_email(self):
        return self.patient_info.get("Email")

    def get_patient_account_type(self):
        return self.patient_info.get("Account Type")

    def get_patient_status(self):
        return self.patient_info.get("Status")

    def get_patient_dx_codes(self):
        dx_code_list = self.patient_info.get("DX Codes").split(",")
        dx_codes_list = [dx_code.strip(' ') for dx_code in dx_code_list]
        return dx_codes_list

    def get_patient_primary_insurance_last_name(self):
        return self.primary_insurance_subscriber_full_name[0].strip()

    def get_patient_primary_insurance_first_name(self):
        return self.primary_insurance_subscriber_full_name[1].strip()

    def get_patient_primary_insurance_subscriber_id(self):
        return self.patient_info.get("Subscriber ID")

    def get_patient_primary_insurance_name(self):
        return self.patient_info.get("Primary Insurance Name")

    def get_patient_primary_insurance_group_number(self):
        return self.patient_info.get("Group Number")

    def get_patient_primary_insurance_plan_name(self):
        return self.patient_info.get("Plan Name")

    def get_patient_primary_insurance_insurance_id(self):
        return int(9001654108)

    # return primary insurance as array
    def get_patient_primary_insurance_array(self):
        self.patient_primary_insurance = []
        primary_insurance = {
            "insurance_id": self.get_patient_primary_insurance_insurance_id(),
            "insurance_name": self.get_patient_primary_insurance_name(),
            "subscriber_id": self.get_patient_primary_insurance_subscriber_id(),
            "subscriber_name": {
                "last": self.get_patient_primary_insurance_last_name(),
                "first": self.get_patient_primary_insurance_first_name()
            },
            "group_number": self.get_patient_primary_insurance_group_number(),
            "plan_name": self.get_patient_primary_insurance_plan_name(),
            "accept_assignment": ""
        }
        self.patient_primary_insurance.append(primary_insurance)
        return self.patient_primary_insurance

    def get_patient_secondary_insurance_last_name(self):
        return self.subscriber_last_secondary_insurance

    def get_patient_secondary_insurance_first_name(self):
        return self.subscriber_first_secondary_insurance

    def get_patient_secondary_insurance_subscriber_id(self):
        return self.patient_info.get("Secondary Subscriber ID")

    def get_patient_secondary_insurance_name(self):
        return self.patient_info.get("Secondary Insurance Name")

    def get_patient_secondary_insurance_subscriber_group_number(self):
        return self.patient_info.get("Group Number")

    def get_patient_secondary_insurance_subscriber_plan_name(self):
        return self.patient_info.get("Plan Name")

    def get_patient_secondary_insurance_array(self):
        self.patient_secondary_insurance = []
        if self.get_patient_secondary_insurance_name() == "":
            return []
        else:
            secondary_insurance = {
                "subscriber_id": self.get_patient_secondary_insurance_subscriber_id(),
                "subscriber_name": {
                    "last": self.get_patient_secondary_insurance_last_name(),
                    "first": self.get_patient_secondary_insurance_first_name()
                },
                "group_number": self.get_patient_secondary_insurance_subscriber_group_number(),
                "plan_name": self.get_patient_secondary_insurance_subscriber_plan_name()
            }
            self.patient_secondary_insurance.append(secondary_insurance)
            return self.patient_secondary_insurance

    def get_patient_tertiary_insurance_array(self):
        self.patient_tertiary_insurance = []
        return self.patient_tertiary_insurance

    def get_patient_home_plan_info(self):
        if self.patient_info.get("Home Plan Insurance Name") == "":
            return {}
        else:
            return {
                "home_plan_payer_id": self.get_home_plan_payer_id(),
                "home_plan_name": self.get_home_plan_insurance_name(),
                "address": self.get_patient_home_plan_address(),
                # "phone_number": self.get_home_plan_phone_number()
            }

    # extract the home plan address coulmn
    def get_patient_home_plan_address(self):
        global home_plan_street_address, home_plan_city, home_plan_state, home_plan_zip
        if self.patient_info.get("Home Plan Address") != "":
            full_home_plan_address = self.patient_info.get("Home Plan Address").replace(",", "")
            full_home_plan_address_list = full_home_plan_address.split(" ")
            if len(full_home_plan_address_list) == 7:
                home_plan_street_address = full_home_plan_address_list[0] + " " + full_home_plan_address_list \
                    [1] + " " + full_home_plan_address_list[2]
                home_plan_city = full_home_plan_address_list[3] + " " + full_home_plan_address_list[4]
                home_plan_state = full_home_plan_address_list[5]
                home_plan_zip = full_home_plan_address_list[6]
            if len(full_home_plan_address_list) == 6:
                home_plan_street_address = full_home_plan_address_list[0] + " " + full_home_plan_address_list \
                    [1] + " " + full_home_plan_address_list[2]
                home_plan_city = full_home_plan_address_list[3]
                home_plan_state = full_home_plan_address_list[4]
                home_plan_zip = full_home_plan_address_list[5]
            return {
                "street_address": home_plan_street_address,
                "city": home_plan_city,
                "state": home_plan_state,
                "zip": home_plan_zip
            }
        else:
            return {}

    def get_home_plan_insurance_name(self):
        return self.patient_info.get("Home Plan Insurance Name")

    def get_home_plan_payer_id(self):
        return str(self.patient_info.get("Home Plan Payer ID"))

    # def get_home_plan_phone_number(self):
    #     return int(math.trunc(self.patient_info.get("Home Plan Phone Number")))

    def get_patient_plan_admin_info(self):
        if self.patient_info.get("Plan Admin Name") == "":
            return {}
        else:
            return {
                "plan_admin_payer_id": self.get_patient_plan_admin_payer_id(),
                "plan_admin_name": self.get_patient_plan_admin_insurance_name(),
                "address": self.get_patient_plan_admin_address(),
                "phone_number": self.get_patient_plan_admin_phone_number()
            }
    # extract the plan admin address
    def get_patient_plan_admin_address(self):
        global plan_admin_street_address, plan_admin_plan_city, plan_admin_state, plan_admin_zip
        if self.patient_info.get("Plan Admin Address") != "":
            full_plan_admin_address = self.patient_info.get("Plan Admin Address").replace(",", "")
            full_plan_admin_address_list = full_plan_admin_address.split(" ")
            if len(full_plan_admin_address_list) == 7:
                plan_admin_street_address = full_plan_admin_address_list[0] + " " + full_plan_admin_address_list \
                    [1] + " " + full_plan_admin_address_list[2]
                plan_admin_plan_city = full_plan_admin_address_list[3] + " " + full_plan_admin_address_list[4]
                plan_admin_state = full_plan_admin_address_list[5]
                plan_admin_zip = full_plan_admin_address_list[6]
            if len(full_plan_admin_address_list) == 6:
                plan_admin_street_address = full_plan_admin_address_list[0] + " " + full_plan_admin_address_list \
                    [1] + " " + full_plan_admin_address_list[2]
                plan_admin_plan_city = full_plan_admin_address_list[3]
                plan_admin_state = full_plan_admin_address_list[4]
                plan_admin_zip = full_plan_admin_address_list[5]
            return {
                "street_address": plan_admin_street_address,
                "city": plan_admin_plan_city,
                "state": plan_admin_state,
                "zip": plan_admin_zip
            }
        else:
            return {}

    def get_patient_plan_admin_insurance_name(self):
        return self.patient_info.get("Plan Admin Name")

    def get_patient_plan_admin_payer_id(self):
        return str(math.trunc(self.patient_info.get("Plan Admin Payer ID")))

    def get_patient_plan_admin_phone_number(self):
        return int(math.trunc(self.patient_info.get("Plan Admin Phone Number")))

    def get_current_status(self):
        current_status = {
            "status": self.get_patient_status(),
            "date": {
                "date": datetime.datetime.now().date().strftime("%Y%m%d"),
                "time": datetime.datetime.now().time().strftime("%H:%M:%S")
            }
        }
        return current_status