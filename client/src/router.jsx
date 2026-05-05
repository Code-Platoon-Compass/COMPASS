import { createBrowserRouter } from 'react-router-dom'
import AuthPage from "./pages/AuthPage"
import HomePage from "./pages/HomePage"
import App from "./App"
import { userConfirmation } from './utilities/authUtilities'
import { getAllTasks } from './utilities/crudUtilities'

const router = createBrowserRouter([
    {
        path:"/",
        loader: userConfirmation,
        element: <App/>,
        children:[
            {
                index:true,
                element:<AuthPage/>
            },
            {
                path:"home",
                loader: getAllTasks,
                element: <HomePage />
            }
        ]
    }
])

export default router