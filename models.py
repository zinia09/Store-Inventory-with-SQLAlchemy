from sqlalchemy import create_engine, Column, String, Integer, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///inventory.db', echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Inventory(Base):
    __tablename__ = "inventory"

    product_id = Column(Integer, primary_key=True)
    product_name = Column("Product", String)
    product_quantity = Column("Quantity", Integer)
    product_price = Column("Price", Integer)
    date_updated = Column("Date updated", Date)

    def __repr__(self):
        return f"Id: {self.product_id} " \
               f"\nProduct: {self.product_name} " \
               f"\nQuantity: {self.product_quantity} " \
               f"\nPrice: {self.product_price} " \
               f"\nDate updated: {self.date_updated}"
