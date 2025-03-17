from sqlalchemy import ForeignKey, Column, Integer, String
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    founding_year = Column(Integer())

    freebies = relationship('Freebie', backref='company')
    devs = relationship('Dev', secondary='freebies', back_populates='companies')

    def give_freebie(self, dev, item_name, value):
        """Create a new Freebie associated with this company and a given dev."""
        return Freebie(item_name=item_name, value=value, company=self, dev=dev)

    @classmethod
    def oldest_company(cls, session):
        """Return the oldest company by founding year."""
        return session.query(cls).order_by(cls.founding_year).first()

    def __repr__(self):
        return f'<Company {self.name}>'

class Dev(Base):
    __tablename__ = 'devs'

    id = Column(Integer(), primary_key=True)
    name = Column(String())

    freebies = relationship('Freebie', backref='dev')
    companies = relationship('Company', secondary='freebies', back_populates='devs')

    def received_one(self, item_name):
        """Check if the dev has received a freebie with a specific name."""
        return any(freebie.item_name == item_name for freebie in self.freebies)

    def give_away(self, dev, freebie):
        """Transfer a freebie to another dev if it belongs to this dev."""
        if freebie in self.freebies:
            freebie.dev = dev

    def __repr__(self):
        return f'<Dev {self.name}>'

class Freebie(Base):
    __tablename__ = 'freebies'

    id = Column(Integer(), primary_key=True)
    item_name = Column(String(), nullable=False)
    value = Column(Integer(), nullable=False)
    dev_id = Column(Integer(), ForeignKey('devs.id'), nullable=False)
    company_id = Column(Integer(), ForeignKey('companies.id'), nullable=False)

    def print_details(self):
        """Return a formatted string describing the freebie."""
        return f'{self.dev.name} owns a {self.item_name} from {self.company.name}'

    def __repr__(self):
        return f'<Freebie {self.item_name}>'