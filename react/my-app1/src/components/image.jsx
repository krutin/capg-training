import React, { useState } from "react";

const EventBinding1 = () => {
  const [likes, setLikes] = useState(0);
  const [formData, setFormData] = useState({ name: "", email: "" });
  const [isZoomed, setIsZoomed] = useState(false);

  // Handling the button click to increase likes
  const handleClick = () => {
    setLikes(likes + 1);
  };

  // Handling form input changes
  const handleChange = (event) => {
    setFormData({ ...formData, [event.target.name]: event.target.value });
  };

  // Handling image zoom toggle
  const toggleZoom = () => {
    setIsZoomed(!isZoomed);
  };

  return (
    <div>
      {/* Like Button */}
      <button onClick={handleClick}>Like {likes}</button>

      {/* Form Handling */}
      <h2>Form Input</h2>
      <input
        type="text"
        name="name"
        value={formData.name}
        onChange={handleChange}
        placeholder="Enter name"
      />
      <input
        type="email"
        name="email"
        value={formData.email}
        onChange={handleChange}
        placeholder="Enter email"
      />
      <p>Name: {formData.name}</p>
      <p>Email: {formData.email}</p>

      {/* Image Zoom */}
      <h2>Image Zoom Feature</h2>
      <img
        src="https://i.pinimg.com/736x/8a/70/c5/8a70c566084f92f2e1d645b943243240.jpg"
        alt="Zoomable"
        style={{ width: isZoomed ? "300px" : "150px", cursor: "pointer" }}
        onClick={toggleZoom}
      />
    </div>
  );
};

export default EventBinding1;