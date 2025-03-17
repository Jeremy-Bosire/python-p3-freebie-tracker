#!/usr/bin/env python3

# Script goes here!
from models import Base, Dev, Company, Freebie
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///freebies.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

company1 = Company(name="Google", founding_year=1998)
company2 = Company(name="Microsoft", founding_year=1975)
session.add_all([company1, company2])
session.commit()

dev1 = Dev(name="Alice")
dev2 = Dev(name="Bob")
session.add_all([dev1, dev2])
session.commit()

freebie1 = Freebie(item_name="Laptop", value=1500, company=company1, dev=dev1)
freebie2 = Freebie(item_name="Mouse", value=50, company=company1, dev=dev2)
freebie3 = Freebie(item_name="Headphones", value=200, company=company2, dev=dev1)

session.add_all([freebie1, freebie2, freebie3])
session.commit()

print(dev1.companies)  
print(dev1.received_one("Laptop"))  
print(freebie1.print_details()) 
print(Company.oldest_company(session))  

dev1.give_away(dev2, freebie1)
session.commit()

print(freebie1.print_details())