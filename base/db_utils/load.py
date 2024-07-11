from sqlalchemy.orm import Session
from ..db_configurations.config import get_db_ingine


def load_objects(objects: list):
    with Session(get_db_ingine()) as session:
        session.add_all(objects)
        session.commit()


def merge_objects(object):
    with Session(get_db_ingine()) as session:
        session.merge(object)
        session.commit()


def merge_and_insert_objects(merge_objects, insert_objects):
    with Session(get_db_ingine()) as session:
        for merge_object in merge_objects:
            session.merge(merge_object)
        session.add_all(insert_objects)
        session.commit()
