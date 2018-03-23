#!/usr/bin/python3
""" This module will connect to a database and access a table"""

if __name__ == "__main__":
    from sys import argv
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                           argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    delete_states = session.query(State).filter(State.name.ilike("%a%")).all()
    for state in delete_states:
        session.delete(state)
    session.commit()
    session.close()
