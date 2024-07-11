from sqlalchemy import String, DateTime, ForeignKey
from sqlalchemy.orm import DeclarativeBase
from .config import get_db_ingine
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

engine = get_db_ingine()


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"
    id: Mapped[str] = mapped_column(String(90), primary_key=True)
    firstname: Mapped[str] = mapped_column(String(90))
    lastname: Mapped[str] = mapped_column(String(90))

    def __repr__(self) -> str:
        value = f"User(id={self.id!r}, \
            firstname={self.firstname!r}, \
            lastname={self.lastname!r})"
        return value


class Request(Base):
    __tablename__ = "requests"
    id: Mapped[str] = mapped_column(String(90), primary_key=True)
    message_timestamp = mapped_column(DateTime)
    username: Mapped[str] = mapped_column(String(90),
                                          ForeignKey('users.id'))
    command: Mapped[str] = mapped_column(String(90))

    def __repr__(self) -> str:
        value = f"Request(id={self.id!r}, \
            message_timestamp={self.message_timestamp!r}, \
            user={self.user!r}, \
            command={self.command!r})"
        return value


Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
