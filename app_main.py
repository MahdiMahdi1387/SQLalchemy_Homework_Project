from sqlalchemy import create_engine, INTEGER, Column, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship


def course_obj_info_printer(obj: object, i: int) -> None:
    '''Prints course object info: id, title, unit, student_id and has a number i to show'''
    print(f'Course number {i} info:\n\n')
    print(f'Id: {obj.id}')
    print(f'Title: {obj.title}')
    print(f'Unit: {obj.unit}')
    print(f'Student_id: {obj.student_id}')


def courses_info_printer(obj_list: list[object]) -> None:
    '''Prints a Whole list of courses objects info cleanly.'''
    for i, obj in enumerate(obj_list):
        if i == 0:
            print('=' * 30)
            course_obj_info_printer(obj, i)
            print('-' * 30)
        elif i + 1 < len(obj_list):
            print('-' * 30)
            course_obj_info_printer(obj, i)
            print('-' * 30)
        else:
            course_obj_info_printer(obj, i)
            print('=' * 30)


engine = create_engine('sqlite:///University.db', echo=True)
engine.connect()

Base = declarative_base()


class Student(Base):
    __tablename__ = 'students'

    id = Column(INTEGER, primary_key=True, autoincrement=True)
    name = Column(String)

    students = relationship('Course', back_populates='courses',
                             cascade='all, delete-orphan')


class Course(Base):
    __tablename__ = 'courses'

    id = Column(INTEGER, primary_key=True)
    title = Column(String)
    unit = Column(INTEGER)
    student_id = Column(INTEGER, ForeignKey('students.id', ondelete='CASCADE'))

    courses = relationship('Student', back_populates='students')

Base.metadata.create_all(engine)
#############################################################

Session = sessionmaker(bind=engine)

SessionLocal = Session()
#############################################################

student1 = Student(name='Ali')
student2 = Student(name='Mahdi')

SessionLocal.add_all([student1, student2])
SessionLocal.commit()
#############################################################

course1 = Course(id=1, title='Physics', unit=3, student_id=1)
course2 = Course(id=2, title='Mathmatics', unit=2, student_id=2)

SessionLocal.add_all([course1, course2])
SessionLocal.commit()
#############################################################

Mahdi = SessionLocal.query(Student).filter_by(name='Mahdi').first()
courses = SessionLocal.query(Course).all()

courses_info_printer(courses)

if Mahdi is not None:
    SessionLocal.delete(Mahdi)
    SessionLocal.commit()
    print('Mahdi deleted successfully in the database.')


courses = SessionLocal.query(Course).all()
courses_info_printer(courses)
