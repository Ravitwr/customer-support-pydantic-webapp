from datetime import datetime
from sqlalchemy import (
    Column, Integer, String, Text, Date, DateTime, 
    Numeric, ForeignKey
)
from app.models.base_entity import Base

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    phone = Column(String(20))
    address = Column(Text)
    date_of_birth = Column(Date)
    ssn = Column(String(11))
    credit_score = Column(Integer)
    balance = Column(Numeric(15, 2), default=0.00)
    status = Column(String(20), default='ACTIVE')
    created_at = Column(DateTime, nullable=False, default=lambda: datetime.now(datetime.UTC))
    updated_at = Column(DateTime, nullable=False, default=lambda: datetime.now(datetime.UTC))


class Loan(Base):
    __tablename__ = 'loans'

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
    loan_type = Column(String(50), nullable=False)
    amount = Column(Numeric(15, 2), nullable=False)
    interest_rate = Column(Numeric(5, 2), nullable=False)
    term_months = Column(Integer, nullable=False)
    balance = Column(Numeric(15, 2), nullable=False)
    status = Column(String(20), nullable=False, default='PENDING')
    origination_fee = Column(Numeric(15, 2))
    disbursement_date = Column(Date)
    first_payment_date = Column(Date)
    last_payment_date = Column(Date)
    created_at = Column(DateTime, nullable=False, default=lambda: datetime.now(datetime.UTC))
    updated_at = Column(DateTime, nullable=False, default=lambda: datetime.now(datetime.UTC))

class LoanPayment(Base):
    __tablename__ = 'loan_payments'

    id = Column(Integer, primary_key=True)
    loan_id = Column(Integer, ForeignKey('loans.id'), nullable=False)
    amount = Column(Numeric(15, 2), nullable=False)
    payment_type = Column(String(20), nullable=False)
    principal_amount = Column(Numeric(15, 2), nullable=False)
    interest_amount = Column(Numeric(15, 2), nullable=False)
    payment_date = Column(DateTime, nullable=False, default=lambda: datetime.now(datetime.UTC))
    status = Column(String(20), nullable=False, default='PENDING')
    created_at = Column(DateTime, nullable=False, default=lambda: datetime.now(datetime.UTC))

class PaymentSchedule(Base):
    __tablename__ = 'payment_schedule'

    id = Column(Integer, primary_key=True)
    loan_id = Column(Integer, ForeignKey('loans.id'), nullable=False)
    due_date = Column(Date, nullable=False)
    payment_amount = Column(Numeric(15, 2), nullable=False)
    principal_amount = Column(Numeric(15, 2), nullable=False)
    interest_amount = Column(Numeric(15, 2), nullable=False)
    status = Column(String(20), nullable=False, default='PENDING')
    created_at = Column(DateTime, nullable=False, default=lambda: datetime.now(datetime.UTC))

class LoanDocument(Base):
    __tablename__ = 'loan_documents'

    id = Column(Integer, primary_key=True)
    loan_id = Column(Integer, ForeignKey('loans.id'), nullable=False)
    document_type = Column(String(50), nullable=False)
    document_url = Column(Text, nullable=False)
    uploaded_at = Column(DateTime, nullable=False, default=lambda: datetime.now(datetime.UTC))
    status = Column(String(20), nullable=False, default='PENDING')
    created_at = Column(DateTime, nullable=False, default=lambda: datetime.now(datetime.UTC))