#!/usr/bin/python3
"""
    script that lists all State objects from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy import asc


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format
                           (sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    start = sessionmaker()
    start.configure(bind=engine)
    session = start()
    stmt = session.query(State).order_by(
        asc(State.id)).filter(State.name.ilike('%a%'))

    print("{:d}: {:s}".format(stmt.id, stmt.name))

    session.close()
