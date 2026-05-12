import { RouterProvider } from "react-router-dom";
import { createRoot } from "react-dom/client";
import router from "./router";
import "./index.css";
import {GoogleOAuthProvider} from "@react-oauth/google";

// Make sure google client id is provided in environment variables in the client .env file. 
createRoot(document.getElementById("root")).render(
  <GoogleOAuthProvider clientId= {import.meta.env.VITE_GOOGLE_CLIENT_ID}>
    <RouterProvider router={router} />
  </GoogleOAuthProvider>
);