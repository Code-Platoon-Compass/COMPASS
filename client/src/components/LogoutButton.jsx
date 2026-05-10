import { useState } from 'react';
import { useNavigate, useOutletContext } from 'react-router-dom';
import { handleLogout } from '../utilities/authUtilities';

export default function LogoutButton() {
    const { setUser } = useOutletContext();
    const navigate = useNavigate();
    const [isSigningOut, setIsSigningOut] = useState(false);
    const [errorMessage, setErrorMessage] = useState('');

    const onLogout = async () => {
        setIsSigningOut(true);
        setErrorMessage('');

        const result = await handleLogout();

        if (!result.ok) {
            setErrorMessage(result.error);
            setIsSigningOut(false);
            return;
        }

        setUser(null);
        navigate('/auth');
    };

    return (
        <div className="flex flex-col gap-2">
            <button className="btn-primary" type="button" onClick={onLogout} disabled={isSigningOut}>
                {isSigningOut ? 'Signing out...' : 'Sign out'}
            </button>
            {errorMessage ? <p className="error-text">{errorMessage}</p> : null}
        </div>
    );
}
