from fastapi import APIRouter, HTTPException
router = APIRouter(
    prefix="/enrollments",
    tags=["Enrollments"]
)
# ------------------------------------------------------
# Hardcoded Enrollment Data
# ------------------------------------------------------
enrollments = [
    {
        "enrollment_id": 1,
        "course_id": 101,
        "student_id": 501,
        "enrollment_date": "2026-07-01",
        "status": "enrolled"
    },
    {
        "enrollment_id": 2,
        "course_id": 103,
        "student_id": 502,
        "enrollment_date": "2026-07-02",
        "status": "completed"
    }
]


@router.get("/")
def list_enrollments():
    return enrollments


@router.get("/{enrollment_id}")
def get_enrollment(enrollment_id: int):
    for enrollment in enrollments:
        if enrollment["enrollment_id"] == enrollment_id:
            return enrollment
    raise HTTPException(status_code=404, detail="Enrollment Not Found")


@router.post("/")
def enroll_student(enrollment: dict):
    enrollments.append(enrollment)
    return {
        "message": "Enrollment Successful",
        "enrollment": enrollment
    }


@router.delete("/{enrollment_id}")
def drop_course(enrollment_id: int):
    for enrollment in enrollments:
        if enrollment["enrollment_id"] == enrollment_id:
            enrollments.remove(enrollment)
            return {
                "message": "Enrollment Dropped Successfully"
            }
    raise HTTPException(status_code=404, detail="Enrollment Not Found")


@router.get("/student/{student_id}")
def student_courses(student_id: int):
    result = []
    for enrollment in enrollments:
        if enrollment["student_id"] == student_id:
            result.append(enrollment)
    return result


@router.get("/course/{course_id}")
def course_students(course_id: int):
    result = []
    for enrollment in enrollments:
        if enrollment["course_id"] == course_id:
            result.append(enrollment)
    return result
