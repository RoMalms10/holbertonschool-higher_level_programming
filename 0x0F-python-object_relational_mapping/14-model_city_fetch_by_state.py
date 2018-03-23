#!/usr/bin/python3
""" This module queries 2 classes using SQLAlchemy """


if __name__ == "__main__":
    from sys import argv
    from model_state import Base, State
    from model_city import City
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                           argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    for row in session.query(State, City).order_by(City.id).\
            filter(City.state_id == State.id).all():
        print("{}: ({}) {}".format(row[0].name, row[1].id, row[1].name))
    session.close()
