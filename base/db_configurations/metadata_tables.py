from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import DeclarativeBase
from .config import get_db_ingine


engine = get_db_ingine()


class Base(DeclarativeBase):
    pass


class Request(Base):
    __tablename__ = "requests"
    id = Column(String(90), primary_key=True)
    message_timestamp = Column(DateTime)
    username = Column(String(90))
    firstname = Column(String(90))
    lastname = Column(String(90))
    command = Column(String(90))

    def __repr__(self) -> str:
        value = f"Request(id={self.id!r}, \
            message_timestamp={self.message_timestamp!r}, \
            username={self.username!r}, \
            firstname={self.firstname!r}, \
            lastname={self.lastname!r}, \
            command={self.command!r})"
        return value


Base.metadata.create_all(engine)
