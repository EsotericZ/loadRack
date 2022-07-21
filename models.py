from sqlalchemy import Column, Integer, String, DateTime
from database import Base
from datetime import datetime

class Job(Base):
    __tablename__ = 'racks'

    id = Column(Integer, primary_key=True)
    rack = Column(String(50))
    row = Column(String(50))
    matl = Column(String(120))
    size = Column(String(50))
    note = Column(String(340))
    weight = Column(Integer)
    phidget = Column(Integer)

    def __init__(self, rack=None, row=None, matl=None, size=None, note=None, weight=None, phidget=None):
        self.rack = rack
        self.row = row
        self.matl = matl
        self.size = size
        self.note = note
        self.weight = weight
        self.phidget = phidget

    def __repr__(self):
        return '<Row %r>' % (self.row)
