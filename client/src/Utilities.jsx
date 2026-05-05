import axios from "axios";

export const api = axios.create({
  baseURL: "/api/v1/", 
});

export const userAuth = async (userDict, create) => {
  let response = await api.post(`users/${create}/`, userDict);
  if (response.status === 201 || response.status === 200) {
    let { email, token } = response.data;
    // Store the token securely (e.g., in localStorage or HttpOnly cookies)
    localStorage.setItem("token", token);
    api.defaults.headers.common["Authorization"] = `Token ${token}`;
    return email;
  }
  alert(response.data);
  return null;
};

export const userConfirmation = async () => {
  let token = localStorage.getItem("token");
  if (token) {
    api.defaults.headers.common["Authorization"] = `Token ${token}`;
    let response = await api.get("users/");
    if (response.status === 200) {
      return response.data.email;
    }
    return null
  }
  return null;
};

export const userLogOut = async () => {
  let response = await api.post("users/logout/");
  if (response.status === 200) {
    localStorage.removeItem("token");
    delete api.defaults.headers.common["Authorization"];
    return null;
  }
  alert("Something went wrong and logout failed");
  return null
};

export const getTasks = async() => {
    let response = await api.get("tasks/")
    if (response.status === 200){
        let tasks = response.data
        return tasks
    }
    alert(response.data)
    return []
}

export const createTask = async(taskObj) => {
    let response = await api.post("tasks/", taskObj)
    if (response.status === 201){
        return response.data
    }
    alert(response.data)
    return null
}

export const updateTask = async(taskObj) => {
    let response = await api.put(`tasks/${taskObj.id}/`, taskObj)
    if (response.status === 200){
        return response.data
    }
    alert(response.data)
    return null
}

export const deleteTask = async(taskId) => {
    let response = await api.delete(`tasks/${taskId}/`)
    return response.status === 200
}