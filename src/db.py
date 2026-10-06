from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase


engine = create_engine("sqlite:///test.db")

Session = sessionmaker(engine)


class Base(DeclarativeBase):
 ...
