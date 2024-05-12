from sqlalchemy.orm import Session

from ..data import engine, Actor


def all() -> list[Actor]:
    with Session(engine) as session:
        return session.query(Actor).all()


def one(id: int) -> Actor:
    with Session(engine) as session:
        return session.query(Actor).get(id)


def append(actor: Actor) -> Actor:
    with Session(engine) as session:
        session.add(actor)
        session.commit()
        session.refresh(actor)
        return actor


def replace(id: int, actor: Actor) -> Actor:
    with Session(engine) as session:
        actor.id = id
        session.merge(actor)
        session.commit()
        session.refresh(actor)
        return actor


def remove(id: int) -> Actor:
    with Session(engine) as session:
        actor = session.query(Actor).get(id)
        session.delete(actor)
        session.commit()
        return actor
