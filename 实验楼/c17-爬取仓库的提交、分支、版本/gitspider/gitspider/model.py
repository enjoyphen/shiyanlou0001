from sqlalchemy import Column, String, create_engine, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base


# connect sqldb
engine = create_engine('mysql+mysqldb://root:@localhost:3306/shiyanlougithub?charset=utf8')
#create the meta class
Base = declarative_base()

#def repositor class
class repositor(Base):
    __tablename__ = 'repositories'
    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    update_time = Column(DateTime)
    commits = Column(Integer)
    branches = Column(Integer)
    releases = Column(Integer)


if __name__ == '__main__':
    Base.metadata.create_all(engine)

    
