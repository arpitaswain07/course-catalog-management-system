from fastapi import FastAPI
from database import engine
import models

from controllers.course_controller import router as course_router
from controllers.enrollment_controller import router as enrollment_router
models.Base.metadata.create_all(bind=engine)
app = FastAPI(
    title="Course Catalog Management System",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to Course Catalog Management System"
    }


app.include_router(course_router)
app.include_router(enrollment_router)
