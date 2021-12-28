from sqlalchemy import create_engine, MetaData, Table, Integer, String, \
    Column, DateTime, ForeignKey, Numeric, update
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects.mysql import insert
from datetime import datetime
from chalicelib.kms_decrypto import decrypto

Base = declarative_base()

username = 'admin'
password = decrypto('RDS_AUTH_PWD')
port = '3306'
host = 'auth.c1bu69q4moat.us-east-2.rds.amazonaws.com'
database = 'users'

engine = create_engine(
    f'mysql+pymysql://{username}:{password}@{host}:{port}/{database}')
DBsession = sessionmaker(bind=engine)
session = DBsession()


class User(Base):
    __tablename__ = 'users'
    id = Column(String(50), primary_key=True)
    email = Column(String(100))
    currency = Column(String(50))
    address = Column(String(200))
    default_payment_method = Column(String(50))
    name = Column(String(50))
    phone = Column(String(50))
    description = Column(String(200))
    invoice_prefix = Column(String(50))
    created = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now,
                        onupdate=datetime.now)


def create_table():
    return Base.metadata.create_all(engine)


def update_table(customers):
    for c in customers:
        print(c.email)
        # user = User(id=c.id, email=c.email, currency=c.currency,
        #             address=c.address, default_payment_method=c.invoice_settings.default_payment_method,
        #             name=c.name, phone=c.phone, description=c.description, invoice_prefix=c.invoice_prefix, created=c.created)
        insert_stmt = insert(User).values(id=c.id, email=c.email, currency=c.currency,
                                          address=c.address, default_payment_method=c.invoice_settings.default_payment_method,
                                          name=c.name, phone=c.phone, description=c.description, invoice_prefix=c.invoice_prefix, created=c.created)
        on_duplicate_key_stmt = insert_stmt.on_duplicate_key_update(email=c.email, currency=c.currency,
                                                                    address=c.address, default_payment_method=c.invoice_settings.default_payment_method,
                                                                    name=c.name, phone=c.phone, description=c.description, invoice_prefix=c.invoice_prefix, created=c.created)
        session.execute(on_duplicate_key_stmt)
    session.commit()

    return "update Success"

# def session_add(objs):
#     session.add_all(objs)
#     session.commit()
# class Post(Base):
#     __tablename__ = 'posts'
#     id = Column(Integer, primary_key=True)
#     description = Column(String(200), nullable=False)
#     slug = Column(String(100), nullable=False)
#     content = Column(String(50), nullable=False)
#     published = Column(String(200), nullable=False, unique=True)
#     created_on = Column(DateTime(), default=datetime.now)
#     updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)


# {
#     "address": null,
#     "balance": 0,
#     "created": 1631775324,
#     "currency": null,
#     "default_source": null,
#     "delinquent": false,
#     "description": "My First Test Customer (created for API docs)",
#     "discount": null,
#     "email": "henry@gmail.com",
#     "id": "cus_KEhvN9Rn024wCH",
#     "invoice_prefix": "558A43AE",
#     "invoice_settings": {
#           "custom_fields": null,
#           "default_payment_method": null,
#           "footer": null
#     },
#     "livemode": false,
#     "metadata": {},
#     "name": null,
#     "next_invoice_sequence": 1,
#     "object": "customer",
#     "phone": null,
#     "preferred_locales": [],
#     "shipping": null,
#     "tax_exempt": "none"
# }
