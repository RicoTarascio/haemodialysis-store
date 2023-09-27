class ReportInfo:
    id: int
    time: str
    patient_id: int

    def __init__(self, id: int, time: str, patient_id: int) -> None:
        self.id, self.time, self.patient_id = id, time, patient_id
        pass
