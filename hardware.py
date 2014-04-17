from sqlalchemy import Column, Integer, String, Enum, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

disk_sizes = Enum('2.5in', '3.5in', name='disk_sizes')
disk_interfaces = Enum('SCSI', 'SAS', 'IDE', 'SATA', 'FC', name='disk_interfaces')
host_interfaces = Enum('SCSI', 'SAS', 'FC', 'iSCSI', 'FCoE', name='host_interfaces')

class Enclosure_Disk_Association(Base):
	__tablename__ = 'enclosures_disks_association'
	enclosure_id = Column(Integer, ForeignKey('enclosures.id'), primary_key=True)
	disk_id = Column(Integer, ForeignKey('disks.id'), primary_key=True)
	bay = Column(Integer)
	disk = relationship('Disk', backref="enclosure_association")

class Enclosure(Base):
	__tablename__ = 'enclosures'
	
	id = Column(Integer, primary_key=True)
	name = Column(String)
	make = Column(String)
	model = Column(String)
	disk_interface = Column(disk_interfaces)
	host_interface = Column(host_interfaces)
	baysize = Column(disk_sizes)
	bays = Column(Integer)
	disks = relationship("Enclosure_Disk_Association", backref="enclosure")

class Disk(Base):
	__tablename__ = 'disks'

	id = Column(Integer, primary_key=True)
	make = Column(String)
	model = Column(String)
	interface = Column(disk_interfaces)
	baysize = Column(disk_sizes)
	capacity = Column(Integer)
	serial = Column(String)
	wwn = Column(String)
	vdev_id = Column(Integer, ForeignKey('vdev.id'))
