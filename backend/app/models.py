from app.db import Base
from sqlalchemy import Column, Integer, Date, Float


class Sales(Base):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, nullable=False)
    grossSales = Column(Float, nullable=False)
    returnAmount = Column(Float, nullable=False)
    salesTax = Column(Float, nullable=False)
    gasSales = Column(Float, nullable=False)
    creditCardAmount = Column(Float, nullable=False)
    cashAmount = Column(Float, nullable=False)
