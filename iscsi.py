from sqlalchemy import Column, Integer, String, Enum, Boolean, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class iscsiTarget(Base):
	__tablename__ = 'iscsitargets'
	id = Column(Integer, primary_key=True)
	iqn = Column(String)

class iscsiLun(Base):
	__tablename__ = 'iscsiluns'
	id = Column(Integer, primary_key=True)
	name = Column(String)
	target = Column(Integer, ForeignKey('iscsitargets.id'))
	zvol = Column(Integer, ForeignKey('zvols.id'))
	number = Column(Integer)
	serial = Column(String)
