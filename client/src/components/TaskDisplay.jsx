import Stack from 'react-bootstrap/Stack';
import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';
import { useState } from 'react';
import { deleteTask, editTask } from '../utilities/crudUtilities';

const TaskDisplay = ({task, rmTask, updateTask}) => {

    const [edit, setEdit] = useState(false)
    const [editTitle, setEditTitle] = useState(task.title)

    const editTaskHandle = async() => {
        let editedTask = await editTask(task.id,editTitle)
        if (editedTask){
            updateTask(editedTask)
        }
        setEdit(!edit)
    }

    const handleDelete = async()=>{
        let deletedTask = await deleteTask(task.id)
        if (deletedTask){
            rmTask(task)
        }
    }

    return (
        <>
            <Stack direction="horizontal" gap={3} style={{border:"solid black 1vmin"}}>
            {edit ?
            <>
                <Form.Control 
                    className="me-auto" 
                    placeholder={task.title}
                    value={editTitle}
                    onChange={(e)=>setEditTitle(e.target.value)}
                />
                <Button variant="outline-primary" onClick={editTaskHandle}>Submit</Button>
                <div className="vr" />
                <Button variant="outline-secondary" onClick={()=>[setEdit(!edit), setEditTitle(task.title)]}>Cancel</Button>
            </>
            :
            <>
                <div className="p-2">{task.title}</div>
                <div className="p-2 ms-auto">
                    <Button variant='warning' onClick={()=>setEdit(!edit)}>
                        Edit
                    </Button>
                </div>
                <div className="vr" />
                <div className="p-2">
                    <Button variant='danger' onClick={handleDelete}>
                        Delete
                    </Button>
                </div>
            </>
        }
        </Stack>
        </>
    )
}

export default TaskDisplay