from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey

Base = declarative_base()


class Machine(Base):

    __tablename__ = 'machine'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    ip = Column(String)
    hostname = Column(String)
    username = Column(String)


class RefTime(Base):

    __tablename__ = 'ref_time'

    id = Column(Integer, primary_key=True, autoincrement=True)
    time_ref = Column(DateTime)
    machine_id = Column(Integer)




class CpuUsage(Base):

    __tablename__ = 'cpu_usage'

    id = Column(Integer, primary_key=True)
    cpu = Column(String)
    value_percent = Column(String)
    ref_time_id = Column(Integer)
 

class DiskUsage(Base):

    __tablename__ = 'disk_usage'
    
    id = Column(Integer, primary_key=True)
    filesystem = Column(String)
    type = Column(String)
    size = Column(String)
    used = Column(String)
    mounted_on = Column(String)
    available = Column(String)
    use_percent = Column(Float)
    ref_time_id = Column(Integer)



class UsersConnected(Base):
    
    __tablename__ = 'users_connected'
    
    id = Column(Integer, primary_key=True)
    user = Column(String)
    tty =  Column(String)
    time = Column(String)
    from_s = Column(String)
    ref_time_id = Column(Integer)


class ProccessRunning(Base):

    __tablename__ = 'proccess_running'

    id = Column(Integer, primary_key=True)
    user = Column(String)
    pid = Column(String)
    vsz = Column(String)
    rss = Column(String)
    tty = Column(String)
    stat = Column(String)
    start = Column(String)
    time = Column(String)
    command = Column(String)
    cpu_percent = Column(String)
    men_percent = Column(String)
    ref_time_id = Column(Integer)


class MemUsage(Base):

    __tablename__ = 'mem_usage'

    id = Column(Integer, primary_key=True)
    mem_usage_percent = Column(Float)
    ref_time_id = Column(Integer)

class ConnectionActive(Base):

    __tablename__ = 'connection_active'

    id = Column(Integer, primary_key=True)
    connected = Column(String)
    ref_time_id = Column(Integer)


