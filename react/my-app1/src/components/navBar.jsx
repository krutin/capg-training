import React from "react";

const NavBar = ({ onSelectCourse }) => {
  return (
    <nav className="navbar">
      <button onClick={() => onSelectCourse("Python")}>Python</button>
      <button onClick={() => onSelectCourse("DataScience")}>Data Science</button>
      <button onClick={() => onSelectCourse("Azure")}>Azure</button>
      <button onClick={() => onSelectCourse("Kubernetes")}>Kubernetes</button>
    </nav>
  );
};

export default NavBar;