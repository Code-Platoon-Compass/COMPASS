import { useEffect, useState } from 'react'
import { Outlet, useLoaderData, useNavigate, useLocation } from 'react-router-dom'
import { api } from './Utilities.jsx'
import './App.css'

function App() {
  const [user, setUser] = useState(useLoaderData())
  const navigate = useNavigate()
  const location = useLocation()

  useEffect(() => {
    let nullUserUrls = ["/"];
    let isAllowed = nullUserUrls.includes(location.pathname);
    if (user && isAllowed) {
      navigate("/home");
    } else if (!user && !isAllowed) {
      navigate("/");
    } 
  }, [location.pathname, user]);

  const test_connection = async() =>{
    let response = await api.get("test/")
    console.log(response)
  }

  useEffect(()=>{
      test_connection()
  },[])

  useEffect(()=>{
    console.log(user)
  }, [user])

  return (
    <>
     <Outlet context={{ user, setUser }}/>
    </>
  )
}

export default App