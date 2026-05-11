import { RouterProvider } from "react-router-dom";
import { createRoot } from "react-dom/client";
import router from "./router";
import "./index.css";
import {GoogleOAuthProvider} from "@react-oauth/google";


createRoot(document.getElementById("root")).render(
  <GoogleOAuthProvider clientId= {import.meta.env.VITE_GOOGLE_CLIENT_ID}>
    <RouterProvider router={router} />
  </GoogleOAuthProvider>
);