import { useState } from 'react';
import { useNavigate, useOutletContext } from 'react-router-dom';
import { googleLogout } from '@react-oauth/google';
import { handleLogout } from '../utilities/authUtilities';

export default function LogoutButton() {
    const { user, setUser } = useOutletContext();
    const navigate = useNavigate();
    const [isSigningOut, setIsSigningOut] = useState(false);
    const [errorMessage, setErrorMessage] = useState('');

    const clearGoogleSession = async (email) => {
        // Sign out of Google Identity Services for this app and disable auto account selection.
        googleLogout();
        window.google?.accounts?.id?.disableAutoSelect?.();

        // Revoke the app's Google permission grant when an email is available.
        if (!email || !window.google?.accounts?.id?.revoke) {
            return;
        }

        await new Promise((resolve) => {
            window.google.accounts.id.revoke(email, () => resolve());
        });
    };

    const onLogout = async () => {
        setIsSigningOut(true);
        setErrorMessage('');

        const result = await handleLogout();

        if (!result.ok) {
            setErrorMessage(result.error);
            setIsSigningOut(false);
            return;
        }

        await clearGoogleSession(user?.email);
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
