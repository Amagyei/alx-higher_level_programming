#!/usr/bin/python3
"""
    script that lists all State objects from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy import asc
from sqlalchemy import func


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format
                           (sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    start = sessionmaker()
    start.configure(bind=engine)
    session = start()
    # count = session.query(func.count()).select_from(State).scalar()
    stmt = session.query(State).order_by(asc(State.id)).first()
    # if count != 0:
    if stmt:
        print("{:d}: {:s}".format(stmt.id, stmt.name))
    else:
        print("Nothing")
    session.close()
