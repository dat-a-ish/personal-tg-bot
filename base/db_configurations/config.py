from sqlalchemy import create_engine
import os


engine_str = os.environ['engine_str']


def get_db_ingine():
    engine = create_engine(engine_str,
                           echo=True)
    return engine
