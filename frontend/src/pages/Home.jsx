
import { useEffect, useState } from "react";
import Navbar from "../components/Navbar";
import Hero from "../components/Hero";
import CourseCard from "../components/CourseCard";
import SearchBar from "../components/SearchBar.jsx";
import api from "../services/api";

function Home() {
    const [courses, setCourses] = useState([]);
    const [searchTerm, setSearchTerm] = useState("");
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState("");

    useEffect(() => {
        const fetchCourses = async () => {
            try {
                const response = await api.get("/course/");
                setCourses(response.data);
            } catch (err) {
                console.error("Failed to fetch courses:", err);
                setError("Unable to load courses. Please try again later.");
            } finally {
                setLoading(false);
            }
        };

        fetchCourses();
    }, []);

    const filteredCourses = courses.filter((course) => {
        const query = searchTerm.toLowerCase();

        return [
            course.course_name,
            course.title,
            course.description,
            course.instructor_name,
            course.instructor
        ]
            .filter(Boolean)
            .some((value) =>
                String(value).toLowerCase().includes(query)
            );
    });

    return (
        <>
            <Navbar />
            <Hero />

            <main className="course-catalog">
                <section className="catalog-header">
                    <h2>Explore Our Courses</h2>
                    <p>Find a course that matches your learning goals.</p>
                </section>

                <SearchBar
                    searchTerm={searchTerm}
                    setSearchTerm={setSearchTerm}
                />

                {loading && <p>Loading courses...</p>}

                {error && <p role="alert">{error}</p>}

                {!loading && !error && filteredCourses.length === 0 && (
                    <p>
                        {courses.length === 0
                            ? "No courses are available yet."
                            : "No courses match your search."}
                    </p>
                )}

                {!loading && !error && filteredCourses.length > 0 && (
                    <div className="course-list">
                        {filteredCourses.map((course) => (
                            <CourseCard
                                key={course.course_id}
                                course={course}
                            />
                        ))}
                    </div>
                )}
            </main>
        </>
    );
}

export default Home;
