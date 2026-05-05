import { createBrowserRouter } from 'react-router-dom'
import AuthPage from "./pages/AuthPage"
import HomePage from "./pages/HomePage"
import App from "./App"
import { getTasks, userConfirmation } from './Utilities'

const router = createBrowserRouter([
    {
        path:"/",
        element: <App/>,
        loader: userConfirmation,
        children:[
            {
                index:true,
                element:<AuthPage/>
            },
            {
                path:"home",
                element: <HomePage />,
                loader: getTasks
            }
        ]
    }
])

export default router