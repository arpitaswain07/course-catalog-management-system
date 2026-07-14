from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Course, Enrollment
from schema import CourseCreate, EnrollmentCreate
router = APIRouter(
    prefix="/enrollments",
    tags=["Enrollments"]
)


@router.get("/")
def list_enrollments(db: Session = Depends(get_db)):
    return db.query(Enrollment).all()


@router.get("/{enrollment_id}")
def get_enrollment(
    enrollment_id: int,
    db: Session = Depends(get_db)
):
    enrollment = db.query(Enrollment).filter(
        Enrollment.enrollment_id == enrollment_id
    ).first()

    if enrollment is None:
        raise HTTPException(
            status_code=404,
            detail="Enrollment Not Found"
        )

    return enrollment


@router.post("/")
def create_course(course: CourseCreate, db: Session = Depends(get_db)):
    new_course = Course(
        course_id=course.course_id,
        title=course.title,
        description=course.description,
        instructor=course.instructor,
        credits=course.credits,
        capacity=course.capacity,
        enrolled_count=course.enrolled_count,
        price=course.price,
        status=course.status
    )

    db.add(new_course)
    db.commit()
    db.refresh(new_course)

    return {
        "message": "Course Created Successfully",
        "course": new_course
    }


@router.delete("/{enrollment_id}")
def drop_course(
    enrollment_id: int,
    db: Session = Depends(get_db)
):
    enrollment = db.query(Enrollment).filter(
        Enrollment.enrollment_id == enrollment_id
    ).first()

    if enrollment is None:
        raise HTTPException(
            status_code=404,
            detail="Enrollment Not Found"
        )

    db.delete(enrollment)
    db.commit()

    return {
        "message": "Enrollment Dropped Successfully"
    }


@router.get("/student/{student_id}")
def student_courses(
    student_id: int,
    db: Session = Depends(get_db)
):
    enrollments = db.query(Enrollment).filter(
        Enrollment.student_id == student_id
    ).all()

    return enrollments


@router.get("/course/{course_id}")
def course_students(
    course_id: int,
    db: Session = Depends(get_db)
):
    enrollments = db.query(Enrollment).filter(
        Enrollment.course_id == course_id
    ).all()

    return enrollments
