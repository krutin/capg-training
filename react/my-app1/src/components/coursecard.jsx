import React from "react";

const CourseCard = ({ course }) => {
  if (!course) return null; // Avoids errors if no course is selected

  return (
    <div className="course-card">
      <h2>{course.title}</h2>
      <img src={course.image} alt={course.title} style={{ width: "200px", height: "200px" }} />
      <p>{course.description}</p>
    </div>
  );
};

export default CourseCard;