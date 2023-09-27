import psycopg

from store.utils.patient_info import PatientInfo
from store.utils.patient_report import ReportInfo


class Store:
    _DNS: str = "postgres://postgres:postgres@localhost:5432/haemo_store"

    def __init__(self) -> None:
        self.initialize_schema()
        return None

    @classmethod
    def db(cls):
        return psycopg.connect(cls._DNS)

    @classmethod
    def initialize_schema(cls):
        with cls.db() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    CREATE TABLE IF NOT EXISTS Patients(
                            id serial PRIMARY KEY,
                            name varchar(70)
                    );
                            
                    CREATE TABLE IF NOT EXISTS Reports(
                            id serial PRIMARY KEY,
                            time timestamp,
                            patient_id integer NOT NULL REFERENCES Patients
                    );      
                            
                    CREATE TABLE IF NOT EXISTS Parameters(
                            id serial UNIQUE NOT NULL,
                            name varchar(70) PRIMARY KEY,
                            min_value real,
                            max_value real
                    );      
                            
                    CREATE TABLE IF NOT EXISTS Reads(
                            id serial PRIMARY KEY,
                            time time NOT NULL,
                            report_id integer NOT NULL REFERENCES Reports,
                            parameter_name varchar(70) NOT NULL REFERENCES Parameters,
                            value real NOT NULL
                    );      
                """
                )
        return cls

    @classmethod
    def create_patient(cls, patient_name: str) -> PatientInfo:
        with cls.db() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    INSERT INTO patients (name)
                    VALUES (%s)
                    RETURNING id;
                """,
                    ["_".join(patient_name.upper().strip().split())],
                )

                return PatientInfo(cur.fetchone()[0], patient_name)

    @classmethod
    def create_report(cls, time: str, patient_id: int) -> ReportInfo:
        with cls.db() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    INSERT INTO reports (patient_id)
                    VALUES (%s)
                    RETURNING id, time, patient_id;
                """,
                    [patient_id],
                )
                res = cur.fetchone()
                print(res)
                return ReportInfo(res[0], res[1], res[2])

    @classmethod
    def find_patient(cls, name: str):
        with cls.db() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    SELECT id FROM patients WHERE name = %s;
                """,
                    ["_".join(name.upper().strip().split())],
                )
                res = cur.fetchone()
                return res if res == None else PatientInfo(res[0], name)
