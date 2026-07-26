import { useState } from "react";
import Navbar from "../components/Navbar";
import api from "../services/api";

function Home() {

    const [course, setCourse] = useState({
        course_id: "",
        title: "",
        description: "",
        instructor: "",
        credits: "",
        capacity: "",
        enrolled_count: "",
        price: "",
        status: ""
    });

    const handleSubmit = async (e) => {
    e.preventDefault();

    try {
        const response = await api.post("/course/", {
            course_id: Number(course.course_id),
            title: course.title,
            description: course.description,
            instructor: course.instructor,
            credits: Number(course.credits),
            capacity: Number(course.capacity),
            enrolled_count: Number(course.enrolled_count),
            price: Number(course.price),
            status: course.status
        });

        alert(response.data.message);

        console.log(response.data);

    } catch (error) {
        console.error(error);
        alert("Failed to add course");
    }
};

    return (
        <>
            <Navbar />

            <div className="container">

                <div className="card">

                    <h2>Add New Course</h2>

                    <form onSubmit={handleSubmit}>

                        <input
                            type="number"
                            placeholder="Course ID"
                            value={course.course_id}
                            onChange={(e) =>
                                setCourse({
                                    ...course,
                                    course_id: e.target.value
                                })
                            }
                        />

                        <input
                            type="text"
                            placeholder="Title"
                            value={course.title}
                            onChange={(e) =>
                                setCourse({
                                    ...course,
                                    title: e.target.value
                                })
                            }
                        />

                        <input
                            type="text"
                            placeholder="Description"
                            value={course.description}
                            onChange={(e) =>
                                setCourse({
                                    ...course,
                                    description: e.target.value
                                })
                            }
                        />

                        <input
                            type="text"
                            placeholder="Instructor"
                            value={course.instructor}
                            onChange={(e) =>
                                setCourse({
                                    ...course,
                                    instructor: e.target.value
                                })
                            }
                        />

                        <input
                            type="number"
                            placeholder="Credits"
                            value={course.credits}
                            onChange={(e) =>
                                setCourse({
                                    ...course,
                                    credits: e.target.value
                                })
                            }
                        />

                        <input
                            type="number"
                            placeholder="Capacity"
                            value={course.capacity}
                            onChange={(e) =>
                                setCourse({
                                    ...course,
                                    capacity: e.target.value
                                })
                            }
                        />

                        <input
                            type="number"
                            placeholder="Enrolled Count"
                            value={course.enrolled_count}
                            onChange={(e) =>
                                setCourse({
                                    ...course,
                                    enrolled_count: e.target.value
                                })
                            }
                        />

                        <input
                            type="number"
                            placeholder="Price"
                            value={course.price}
                            onChange={(e) =>
                                setCourse({
                                    ...course,
                                    price: e.target.value
                                })
                            }
                        />

                        <input
                            type="text"
                            placeholder="Status"
                            value={course.status}
                            onChange={(e) =>
                                setCourse({
                                    ...course,
                                    status: e.target.value
                                })
                            }
                        />

                        <button type="submit">
                            Add Course
                        </button>

                    </form>

                </div>

            </div>

        </>
    );
}

export default Home;