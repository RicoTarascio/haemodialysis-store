class PatientInfo:
    id: int
    name: str

    def __init__(self, id: int, name: str) -> None:
        self.id, self.name = id, name
        pass
