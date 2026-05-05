import { useState } from "react";
import { useOutletContext, useLoaderData } from "react-router-dom";
import Stack from 'react-bootstrap/Stack';
import TaskDisplay from "../components/TaskDisplay";
import TaskForm from "../components/TaskForm";
import { userLogOut } from "../Utilities";

const HomePage = () => {
    const {user, setUser} = useOutletContext()
    const [tasks, setTasks] = useState(useLoaderData())

    const addTask = (task) => {
        setTasks([...tasks, task])
    }

    const rmTask = (rmTask) => {
        setTasks(tasks.filter((task)=>(
            task.id !== rmTask.id
        )))
    }

    const editTask = (editTask) => {
        setTasks(tasks.map((task)=>(
            task.id === editTask.id ? editTask : task
        )))
    }

    return (
        <>
            <h1>Welcome {user && ` ${user}`}: Here are your Tasks <button onClick={async()=>setUser(await userLogOut())}>Log Out</button></h1>

            <Stack gap={3}>
                <TaskForm addTask={addTask}/>

                {tasks.map((task)=>(
                    <TaskDisplay 
                        key={task.id} 
                        task={task}
                        rmTask={rmTask}
                        editTask={editTask}
                    />
                ))}

            </Stack>
        </>
    )
}

export default HomePage;