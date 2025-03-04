import React, { useState } from "react";

const DataBinding1 = () => {
  const companyName = "Capgemini";
  const num1 = 788;
  const num2 = 735;
  const greet = () => "Hello, from greet method";

  const courses = [
    "Python",
    "Data Science",
    "Data Engineering",
    "Cloud",
    "Kubernetes",
  ];

  const [message, setMessage] = useState("Click on the button");
  const handleClick = () => {
    setMessage("Button clicked");
  };

  const [isLoggedIn, setIsLoggedIn] = useState(false);

  return (
    <>
      <header>
        <h1>{companyName}</h1>
        <h2>{isLoggedIn ? "Welcome, user..!" : "Please login"}</h2>
        <button onClick={() => setIsLoggedIn(!isLoggedIn)}>
          {isLoggedIn ? "Logout" : "Login"}
        </button>

        <h3>{message}</h3>
        <button onClick={handleClick}>Click Me</button>

        <h4>Sum: {num1 + num2}</h4>
        <h4>{greet()}</h4>

        <h4>Courses:</h4>
        <ul>
          {courses.map((course, index) => (
            <li key={index}>{course}</li>
          ))}
        </ul>
      </header>
    </>
  );
};

export default DataBinding1;
