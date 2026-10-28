function CourseCard({ course }) {
    return (
        <div className="course-card">

            <h2>{course.title}</h2>

            <p>
                <strong>👨 Instructor:</strong> {course.instructor}
            </p>

            <p>
                <strong>⭐ Credits:</strong> {course.credits}
            </p>

            <p>
                <strong>💺 Capacity:</strong> {course.capacity}
            </p>

            <p>
                <strong>💰 Price:</strong> ₹{course.price}
            </p>

            <button className="view-btn">
                View Details
            </button>

        </div>
    );
}

export default CourseCard;