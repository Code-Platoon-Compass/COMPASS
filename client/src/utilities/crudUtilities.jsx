import axios from "axios";

export const api = axios.create({
    baseURL: "/api/v1",
});

export const deleteTask = async(id)=>{
    let response = await api.delete(`tasks/${id}/`)
        alert( response.data)
        return response.data
}

export const editTask = async(id, title) =>{
    let response = await api.put(`/tasks/${id}/`,{
        'title': title
    })
    if(response.status === 200){
        return response.data
    }else{
        return response.errors
    }
}

export const createTask = async(title)=>{
    // let token = localStorage.getItem("token")
    // api.defaults.headers.common['Authorization'] = `Token ${token}`
    let response = await api.post('/tasks/',
        {"title": title}
    )
    if(response.status == 201){
        return response.data
    }else{
        console.error(response.data)
            return null
    }

}
// url ="tasks/", data= [{task}{task}], repsonse = 200 | 500

export const getAllTasks = async() => {
    let token = localStorage.getItem("token")
    api.defaults.headers.common['Authorization'] = `Token ${token}`
    let response = await api.get("/tasks")
    if (response.status == 200){
        return response.data
    }else{
        console.error(response.data)
        return []
    }
}

