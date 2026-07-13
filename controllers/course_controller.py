from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Course
from schema import CourseCreate
router = APIRouter(
    prefix="/course",
    tags=["Course"]
)


@router.get("/")
def list_courses(db: Session = Depends(get_db)):
    return db.query(Course).all()


@router.get("/available")
def available_courses(db: Session = Depends(get_db)):
    course = db.query(Course).filter(
        Course.status == "active",
        Course.enrolled_count < Course.capacity
    ).all()

    return course


@router.post("/")
def create_course(course: CourseCreate, db: Session = Depends(get_db)):
    try:
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

    except Exception as e:
        db.rollback()
        return {"error": str(e)}


@router.put("/{course_id}")
def update_course(
    course_id: int,
    updated_course: CourseCreate,
    db: Session = Depends(get_db)
):
    course = db.query(Course).filter(Course.course_id == course_id).first()

    if course is None:
        raise HTTPException(status_code=404, detail="Course Not Found")

    course.title = updated_course.title
    course.description = updated_course.description
    course.instructor = updated_course.instructor
    course.credits = updated_course.credits
    course.capacity = updated_course.capacity
    course.enrolled_count = updated_course.enrolled_count
    course.price = updated_course.price
    course.status = updated_course.status

    db.commit()
    db.refresh(course)

    return {
        "message": "Course Updated Successfully",
        "course": course
    }


@router.delete("/{course_id}")
def delete_course(course_id: int, db: Session = Depends(get_db)):
    course = db.query(Course).filter(Course.course_id == course_id).first()

    if course is None:
        raise HTTPException(status_code=404, detail="Course Not Found")

    db.delete(course)
    db.commit()

    return {
        "message": "Course Deleted Successfully"
    }


@router.get("/{course_id}")
def get_course(course_id: int, db: Session = Depends(get_db)):
    course = db.query(Course).filter(Course.course_id == course_id).first()

    if not course:
        raise HTTPException(status_code=404, detail="Course Not Found")

    return course


@router.get("/instructor/{name}")
def filter_by_instructor(name: str, db: Session = Depends(get_db)):
    course = db.query(Course).filter(
        Course.instructor.ilike(name)
    ).all()

    return course

