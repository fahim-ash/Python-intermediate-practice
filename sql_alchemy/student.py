from sqlalchemy.orm import sessionmaker,declarative_base

from sqlalchemy import *
import os


#sqlite3 path
Base_dir=os.path.dirname(os.path.realpath(__file__))
print(Base_dir)
connection_string="sqlite:///"+os.path.join(Base_dir,'site.db')
print(connection_string)
#session
engine = create_engine(connection_string,echo=False)
Session=sessionmaker(bind=engine)
session=Session()

Base = declarative_base()

class Struden(Base):
    __tablename__= 'student'
    id= Column (Integer,primary_key=True)
    name= Column (String(50))
    age= Column (Integer)
    grade= Column (String(50))

Base.metadata.create_all(engine)