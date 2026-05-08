import { createBrowserRouter } from 'react-router-dom'
import HomePage from "./pages/HomePage"
import Dashboard from "./pages/Dashboard"
import App from "./App"

const router = createBrowserRouter([
    {
        path:"/",
        element: <App/>,
        children:[
            {
                index: true,
                element: <HomePage />
            },
            {
                path: "dashboard",
                element: <Dashboard />
            }
        ]
    }
])

export default router