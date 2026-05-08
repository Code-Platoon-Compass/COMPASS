import { useState } from "react";
import { Outlet } from "react-router-dom";
import "./App.css";

function App() {
  const [user, setUser] = useState(null);

  return (
    <>
      <Outlet context={{ user, setUser }} />
    </>
  );
}

export default App;
