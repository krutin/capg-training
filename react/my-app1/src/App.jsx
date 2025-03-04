import React, { createContext, useContext } from "react";

// Step 1: Create Context
const UserContext = createContext();

const App = () => {
  const user = "John Doe";

  return (
    // Step 2: Provide Context
    <UserContext.Provider value={user}>
      <Parent />
    </UserContext.Provider>
  );
};

const Parent = () => {
  return <Child />;
};

const Child = () => {
  return <ProfileDetails />;
};

const ProfileDetails = () => {
  // Step 3: Consume Context
  const user = useContext(UserContext);
  return <h2>User: {user}</h2>;
};

export default App;