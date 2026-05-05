import { useEffect, useState } from 'react'
import { Outlet } from 'react-router-dom'
import './App.css'
import { useNavigate, useLocation ,useLoaderData} from 'react-router-dom'
// import {test_conection} from './utilities'

function App() {
  const [user, setUser] = useState(useLoaderData())
  const navigate = useNavigate()
  const location = useLocation()

  useEffect(()=>{
    if (user && location.pathname === '/'){
      navigate('/home')}
    else if (!user && location.pathname !='/'){
      navigate('/')
      }
  }, [user,location.pathname])

  return (
    <>
     <Outlet context={{ user, setUser }}/>
    </>
  )
}

export default App