class PatientInfo:
    name: str
    birth: str

    def __init__(self, name: str, birth: str) -> None:
        self.name, self.birth = name, birth
        pass
