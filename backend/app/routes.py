from fastapi import APIRouter
from app.db import SessionLocal
from app.models import Sales
from pydantic import BaseModel


class SaleIn(BaseModel):
    date: str
    grossSales: float
    returnAmount: float
    salesTax: float
    gasSales: float
    creditCardAmount: float
    cashAmount: float


router = APIRouter()


@router.post("/sales")
def create_sales(sales: SaleIn):
    with SessionLocal() as db:
        db_sale = Sales(
            date=sales.date,
            grossSales=sales.grossSales,
            returnAmount=sales.returnAmount,
            salesTax=sales.salesTax,
            gasSales=sales.gasSales,
            creditCardAmount=sales.creditCardAmount,
            cashAmount=sales.cashAmount,
        )
        db.add(db_sale)
        db.commit()
        db.refresh(db_sale)
        return db_sale


@router.get("/sales/summary")
def get_sales_summary():
    with SessionLocal() as db:
        rows = db.query(Sales).all()

        summaries = []

        for sale in rows:
            print("Sale-data", sale)
            date = sale.date
            gross = sale.grossSales
            ret = sale.returnAmount
            tax = sale.salesTax
            gas = sale.gasSales
            cc = sale.creditCardAmount
            cash = sale.cashAmount

            # compute
            netSales = gross - ret
            totalSales = netSales + tax + gas
            totalAmountCollected = cc + cash
            amountDifference = totalAmountCollected - totalSales

            summaries.append(
                {
                    "date": date,
                    "netSales": netSales,
                    "totalSales": totalSales,
                    "totalAmountCollected": totalAmountCollected,
                    "amountDifference": amountDifference,
                }
            )
        return summaries
