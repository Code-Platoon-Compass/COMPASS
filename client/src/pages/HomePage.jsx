import {  useState } from "react";
import { useLoaderData, useOutletContext } from "react-router-dom";
import Stack from 'react-bootstrap/Stack';
import TaskDisplay from "../components/TaskDisplay";
import TaskForm from "../components/TaskForm";
import { logout } from "../utilities/authUtilities";

const HomePage = () => {
    // navigate = useNavigate()
    // location = useLocation()
    const {user} = useOutletContext()
    const [tasks, setTasks] = useState(useLoaderData())

    // useEffect(()=>{
    //     if (user && location.pathname === '/'){
    //     navigate('/home')}
    //     else if (!user && location.pathname !='/'){
    //     navigate('/')
    //     }
    // }, [user,location.pathname])

    const addTask = (task) => {
        setTasks([...tasks, task])
    }

    const rmTask = (rmTask) => {
        setTasks(tasks.filter((task)=>(
            task.id !== rmTask.id
        )))
    }

    const updateTask = (editTask) => {
        setTasks(tasks.map((task)=>(
            task.id === editTask.id ? editTask : task
        )))
    }

     

    return (
        <>
            <h1>Welcome {user && user}: Here are your Tasks <button onClick={async()=>await logout()}>Log Out</button></h1>

            <Stack gap={3}>
                <TaskForm addTask={addTask}/>

                {tasks.map((task)=>(
                    <TaskDisplay 
                        key={task.id} 
                        task={task}
                        rmTask={rmTask}
                        updateTask={updateTask}
                    />
                ))}

            </Stack>
        </>
    )
}

export default HomePage;