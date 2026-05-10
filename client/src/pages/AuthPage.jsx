import { useOutletContext } from 'react-router-dom';
import AuthForm from '../components/AuthForm';

export default function AuthPage() {
    const { user, setUser } = useOutletContext();

    return (
        <>
            {user ? <p>Signed in as {user.email}</p> : null}
            <AuthForm setUser={setUser} />
        </>
    )
}