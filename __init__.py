import store
from store.utils.patient_info import PatientInfo

store.db.create_patient(PatientInfo("Mario Rossi", "2000-01-01"))
