from controller.controller import Controller
import store
from store.utils.patient_info import PatientInfo

f = open("sample.json")

Controller.from_json(f).store_data()

f.close()
