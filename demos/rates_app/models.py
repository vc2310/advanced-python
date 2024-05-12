from sqlalchemy import Column, Integer, String, Float
from rates_app.databases import Base


class Currency(Base):
    __tablename__ = "currency"

    id = Column(Integer, primary_key=True)
    date = Column(String)
    currency_symbol = Column(String)
    currency_value = Column(Float)

    def __str__(self) -> str:
        return f"<Person Id={self.id} Date={self.date} currency_symbol={self.currency_symbol} currency_value={self.currency_value}>"
