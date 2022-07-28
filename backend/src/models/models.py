from sqlalchemy import Column, Integer, String, Numeric

from services.SQLiteConnector import Base


class Stock(Base):
    __tablename__ = "stocks"

    id = Column(Integer, primary_key=True, index=True)
    ticker = Column(String, unique=True, index=True)
    cnpj = Column(String)
    price_2021 = Column(Numeric(10,2))
    price_2022 = Column(Numeric(10,2))