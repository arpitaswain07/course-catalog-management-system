import { useEffect, useState } from "react";
import Navbar from "../components/Navbar";
import Hero from "../components/Hero";
import CourseCard from "../components/CourseCard";
import SearchBar from "../components/SearchBar.jsx";
import api from "../services/api";

function Home() {
    const [courses, setCourses] = useState([]);

    const fetchCourses = async () => {
        try {
            const response = await api.get("/course/");
            setCourses(response.data);
        } catch (error) {
            console.log(error);
        }
    };

    useEffect(() => {
        fetchCourses();
    }, []);

    return (
        <>
            <Navbar />
            <Hero />
            <h1 style={{ color: "red", fontSize: "40px" }}>
  THIS IS HOME
</h1>
            <div style={{ background: "red", color: "white", padding: "20px" }}>
  Search goes here
</div>

            <div className="course-list">
                {courses.map((course) => (
                    <CourseCard
                        key={course.course_id}
                        course={course}
                    />
                ))}
            </div>
        </>
    );
}

export default Home;