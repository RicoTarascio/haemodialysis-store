import psycopg

from store.utils.patient_info import PatientInfo


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
                            name varchar(70),
                            birth date
                    );
                            
                    CREATE TABLE IF NOT EXISTS Reports(
                            id serial PRIMARY KEY,
                            time time,
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
    def create_patient(cls, patient_info: PatientInfo):
        with cls.db() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    INSERT INTO patients (name, birth)
                    VALUES (%s, %s);
                """,
                    (patient_info.name, patient_info.birth),
                )
        return cls
