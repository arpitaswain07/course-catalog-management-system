from sqlalchemy import Column, Integer, String
from database import Base

class Course(Base):
    __tablename__ = "course"

    course_id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    description = Column(String(255))
    instructor = Column(String(100))
    credits = Column(Integer)
    capacity = Column(Integer)
    enrolled_count = Column(Integer)
    price = Column(Integer)
    status = Column(String(20))


class Enrollment(Base):
    __tablename__ = "enrollment"

    enrollment_id = Column(Integer, primary_key=True, index=True)
    course_id = Column(Integer)
    student_id = Column(Integer)
    enrollment_date = Column(String(20))
    status = Column(String(20))