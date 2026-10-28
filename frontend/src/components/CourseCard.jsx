
import { useState } from "react";

function CourseCard({ course }) {
    const [showDetails, setShowDetails] = useState(false);

    return (
        <article className="course-card">
            <h2>{course.title ?? course.course_name}</h2>

            <p>
                <strong>👨 Instructor:</strong>{" "}
                {course.instructor ?? course.instructor_name ?? "Not specified"}
            </p>

            <p>
                <strong>⭐ Credits:</strong> {course.credits ?? "N/A"}
            </p>

            <p>
                <strong>💺 Capacity:</strong> {course.capacity ?? "N/A"}
            </p>

            <p>
                <strong>💰 Price:</strong> ₹{course.price ?? "N/A"}
            </p>

            <button
                type="button"
                className="view-btn"
                onClick={() => setShowDetails((current) => !current)}
                aria-expanded={showDetails}
            >
                {showDetails ? "Hide Details" : "View Details"}
            </button>

            {showDetails && (
                <section className="course-details">
                    <h3>Course Details</h3>
                    <p><strong>Course ID:</strong> {course.course_id}</p>
                    <p>
                        <strong>Description:</strong>{" "}
                        {course.description ?? "No description available."}
                    </p>
                    <p>
                        <strong>Course name:</strong>{" "}
                        {course.title ?? course.course_name ?? "N/A"}
                    </p>
                </section>
            )}
        </article>
    );
}

export default CourseCard;
