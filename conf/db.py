from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

URI = "sqlite:///home_work.sqlite"

engine = create_engine(URI, echo=True)
DBSession = sessionmaker(bind=engine)
session = DBSession()