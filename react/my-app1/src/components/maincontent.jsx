import React from "react";
import CourseCard from "./coursecard";

const courses = {
  Python: {
    title: "Python Programming",
    image:
      "https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg",
    description:
      "Python is a popular programming language used for web development, automation, and data science.",
  },
  DataScience: {
    title: "Data Science",
    image:
      "https://upload.wikimedia.org/wikipedia/commons/e/eb/Data_science.jpg",
    description:
      "Data science is the process of analyzing data to extract insights and make predictions.",
  },
  Azure: {
    title: "Azure",
    image:
      "https://upload.wikimedia.org/wikipedia/commons/a/a8/Microsoft_Azure_Logo.svg",
    description:
      "Microsoft Azure is a cloud computing platform that provides various cloud services.",
  },
  Kubernetes: {
    title: "Kubernetes",
    image:
      "https://upload.wikimedia.org/wikipedia/commons/3/39/Kubernetes_logo_without_workmark.svg",
    description:
      "Kubernetes is an open-source system for automating deployment, scaling, and management of containerized applications.",
  },
};

const MainContent = ({ selectedCourse }) => {
  return (
    <main className="main-content">
      {selectedCourse ? (
        <CourseCard course={courses[selectedCourse]} />
      ) : (
        <h2>Select a course to view the details</h2>
      )}
    </main>
  );
};

export default MainContent;