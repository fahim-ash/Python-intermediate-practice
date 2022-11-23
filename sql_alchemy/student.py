#--------crearting the schema--------#
from sqlalchemy.orm import sessionmaker,declarative_base
from sqlalchemy import *
import os
from jsondata import obj
import sqlite3



# sqlite3 path
Base_dir=os.path.dirname(os.path.realpath(__file__))
connection_string="sqlite:///"+os.path.join(Base_dir,'site.db')

#session
engine = create_engine(connection_string,echo=False)
Session=sessionmaker(bind=engine)
session=Session()

Base = declarative_base()

class Student(Base):
    __tablename__= 'student'
    id= Column (Integer,primary_key=True,autoincrement=True)
    name= Column (String(50))
    age= Column (Integer)
    grade= Column (String(50))

Base.metadata.create_all(engine)

#------ insert into database--------#
# for info in obj:
#     print(info)
#     user=Student(name=info['name'],age=info['age'],grade=info['grade'])
#     session.add(user)
#     session.commit()

# traverse sql

check=student.select()
