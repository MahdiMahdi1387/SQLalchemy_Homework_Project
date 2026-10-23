from sqlalchemy import create_engine, FLOAT, INTEGER, Column, String
from sqlalchemy.orm import declarative_base, sessionmaker


engine = create_engine('sqlite:///Student.db')
engine.connect()

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    id = Column(INTEGER, primary_key=True, unique=True)
    name = Column(String, nullable=False)
    score = Column(FLOAT)

Base.metadata.create_all(engine)
################################################

Session = sessionmaker(bind=engine)
session_local = Session()
################################################

student1 = Student(name='Ali', score=20)
student2 = Student(name='Mahdi', score=19.75)
student3 = Student(name='Sina', score=12)

session_local.add_all([student1, student2, student3])
session_local.commit()
################################################

students = session_local.query(Student).all()
i = 1
for student in students:
    print(f'Student number {i}\'s info:\n\n')
    print(f'Id: {student.id}')
    print(f'Name: {student.name}')
    print(f'Score: {student.score}')
    print('-' * 30)
    i += 1
################################################

Mahdi = session_local.query(Student).filter_by(name='Mahdi').first()

Mahdi.score = 20
session_local.commit()

print(f'Mahdi\'s new score: {Mahdi.score}')
################################################

if Mahdi is not None:
    session_local.delete(Mahdi)
    session_local.commit()
    print(f'Mahdi successfully deleted from data base.')
