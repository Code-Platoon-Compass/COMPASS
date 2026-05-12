import { useEffect, useState } from "react";
import { Outlet } from "react-router-dom";
import "./App.css";
import { restoreSession } from "./utilities/authUtilities";

function App() {
  const [user, setUser] = useState(null);
  const [authLoading, setAuthLoading] = useState(true);

  useEffect(() => {
    const bootstrapAuth = async () => {
      const result = await restoreSession();
      if (result.ok) {
        setUser(result.data);
      }
      setAuthLoading(false);
    };

    bootstrapAuth();
  }, []);

  return (
    <>
      <Outlet context={{ user, setUser, authLoading }} />
    </>
  );
}

export default App;
