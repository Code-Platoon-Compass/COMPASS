import { useOutletContext } from 'react-router-dom';
import AuthForm from '../components/AuthForm';
import LogoutButton from '../components/LogoutButton';

export default function AuthPage() {
    const { user, setUser, authLoading } = useOutletContext();

    if (authLoading) {
        return <p>Checking session...</p>;
    }

    return (
        <>
            {user ? (
                <>
                    <p>Signed in as {user.email}</p>
                    <LogoutButton />
                </>
            ) : null}
            <AuthForm setUser={setUser} />
        </>
    )
}