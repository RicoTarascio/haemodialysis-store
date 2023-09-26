"""
Data controller and converter, starts from patient JSON and saves to Store

"""

import json
import pprint


class DataController:
    def __init__(self) -> None:
        return None

    @classmethod
    def convert(cls, patient_json: str):
        return json.load(patient_json)
