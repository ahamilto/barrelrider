from sqlalchemy import Column, Integer, String, Enum, Boolean, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

vdev_levels = Enum('stripe', 'mirror', 'raidz', 'raidz2', 'raidz3')

class ZPool(Base):
	__tablename__ = 'zpools'
	id = Column(Integer, primary_key=True)
	name = Column(String)
	guid = Column(Integer)
	dedup = Column(Boolean)
	vdevs = relationship('VDev', backref='zpool')
	zvols = relationship('ZVol', backref='zpool')

class VDev(Base):
	__tablename__ = 'vdevs'
	id = Column(Integer, primary_key=True)
	zpool_id = Column(Integer, ForeignKey('zpools.id'))
	level = Column(vdev_levels)
	disks = relationship('Disk', backref='vdev')

class ZVol(Base):
	__tablename__ = 'zvols'
	id = Column(Integer, primary_key=True)
	zpool_id = Column(Integer, ForeignKey('zpools.id'))
	name = Column(String)
	size = Column(Integer)
	compression = Column(Boolean)

class ZFileSystem(Base):
	__tablename__ = 'zfilesystems'
	id = Column(Integer, primary_key=True)
	zpool_id = Column(Integer, ForeignKey('zpools.id'))
	name = Column(String)
	quota = Column(Integer)
	compression = Column(Boolean)
