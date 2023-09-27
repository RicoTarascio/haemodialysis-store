"""
Data controller and converter, starts from patient JSON and saves to Store

"""

from io import TextIOWrapper
import json
import pprint
import store

from store.utils.patient_info import PatientInfo


class Controller:
    patient_data: dict = dict()

    def __init__(self, data: dict) -> None:
        self.patient_data = data
        return None

    @classmethod
    def from_json(cls, patient_json: str | TextIOWrapper):
        if patient_json is str:
            return cls(json.loads(patient_json))
        return cls(json.load(patient_json))

    def store_data(self):
        patient_name = self.patient_data.get("patient", "")
        if patient_name == "":
            print("[WARNING] No name for patient")

        patient = store.db.find_patient(patient_name)
        if patient == None:
            patient = store.db.create_patient(patient_name)

        report = store.db.create_report("", patient.id)

        pprint.pprint(report)

        return
