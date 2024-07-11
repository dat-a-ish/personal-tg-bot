from sqlalchemy.orm import Session
from ..db_configurations.config import get_db_ingine


def load_objects(objects: list):
    with Session(get_db_ingine()) as session:
        session.add_all(objects)
        session.commit()
