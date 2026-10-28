from pydantic import BaseModel


class CourseCreate(BaseModel):
    course_id: int
    title: str
    description: str
    instructor: str
    credits: int
    capacity: int
    enrolled_count: int
    price: int
    status: str


class EnrollmentCreate(BaseModel):
    enrollment_id: int
    course_id: int
    student_id: int
    enrollment_date: str
    status: str
