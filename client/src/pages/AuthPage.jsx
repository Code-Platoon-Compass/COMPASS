import { useOutletContext } from 'react-router-dom';
import AuthForm from '../components/AuthForm';
import LogoutButton from '../components/LogoutButton';

export default function AuthPage() {
    const { user, setUser, authLoading } = useOutletContext();

    if (authLoading) {
        return (
            <section className="auth-page">
                <div className="auth-panel">
                    <p className="body-text">Checking session...</p>
                </div>
            </section>
        );
    }

    return (
        <section className="auth-page">
            <div className="auth-panel">
                <div className="mb-6 space-y-2 text-left">
                    <h1 className="heading-2">Welcome to Compass</h1>
                    <p className="body-text">Sign in with your approved Google account and cohort invite code.</p>
                </div>

                {user ? (
                    <div className="auth-meta">
                        <p className="body-text">Signed in as {user.email}</p>
                        <LogoutButton />
                    </div>
                ) : null}

                {!user ? <AuthForm setUser={setUser} /> : null}
            </div>
        </section>
    )
}