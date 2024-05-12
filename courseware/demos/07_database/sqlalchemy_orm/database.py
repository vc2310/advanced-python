from typing import Any

from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base


DATABASE_USER = "postgres"
DATABASE_PASS = "dbPass123!"
DATABASE_HOST = "127.0.0.1"
DATABASE_PORT = "5441"
DATABASE_NAME = "dvdrental"

DATABASE_URI = (
    "postgresql+psycopg2://"
    f"{DATABASE_USER}:"
    f"{DATABASE_PASS}@"
    f"{DATABASE_HOST}:{DATABASE_PORT}/"
    f"{DATABASE_NAME}"
)

engine = create_engine(DATABASE_URI)

Base = automap_base()
Base.prepare(engine)


def to_dict(self: Any) -> dict[Any, Any]:
    return {c.name: getattr(self, c.name) for c in self.__table__.columns}


Category = Base.classes.category
Category.to_dict = to_dict

Actor = Base.classes.actor
Actor.to_dict = to_dict
