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