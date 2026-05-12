import { useState } from 'react';
import { useNavigate } from 'react-router-dom'
import { handleGoogleAuth } from '../utilities/authUtilities';
import { GoogleLogin } from '@react-oauth/google';

const AuthForm = ({setUser}) => {
    const [inviteCode, setInviteCode] = useState("")
    const [errorMessage, setErrorMessage] = useState("")
    const navigate = useNavigate()

    // When the user successfully logs in with Google, this function will be called with the credential response. Token and invite code are retrieved and sent to the backend for final verification.
    const handleGoogleLoginSuccess = async (credentialResponse) => {
        const token = credentialResponse.credential;
        const result = await handleGoogleAuth(token, inviteCode);

        if (result.ok) {
            setErrorMessage('')
            setUser(result.data);
            navigate("/dashboard");
            return;
        }

        setErrorMessage(result.error);
    }

    // In case users need to switch accounts, this will take them to Google's account chooser page in a new tab. Created as backup in case the auto_select={false} prop on the GoogleLogin component doesn't work as expected for some users.
    const openGoogleAccountChooser = () => {
        window.open('https://accounts.google.com/AccountChooser', '_blank', 'noopener,noreferrer');
    }

    return (
        <div className="auth-form">
            {/* invite code block */}
            <div className="form-block">
                <label className="form-label" htmlFor="invite-code">Invite code (first sign in only)</label>
                <input
                    className="form-input"
                    id="invite-code"
                    type="text"
                    value={inviteCode}
                    onChange={(event) => {
                        setInviteCode(event.target.value)
                        if (errorMessage) {
                            setErrorMessage('')
                        }
                    }}
                    placeholder="Enter your cohort invite code if this is your first login"
                />
            </div>

            {errorMessage ? <p className="error-text">{errorMessage}</p> : null}
            {/* Google login button */}
            <div className="google-wrap">
                <GoogleLogin
                    auto_select={false}
                    onSuccess={handleGoogleLoginSuccess}
                    onError={() => {
                        console.log('Login Failed');
                        alert("Google authentication failed. Please try again.");
                    }}
                />
            </div>
            {/* backup account chooser button */}
            <button
                className="btn-secondary"
                type="button"
                onClick={openGoogleAccountChooser}
            >
                Use a different Google account
            </button>
        </div>
    )
}

export default AuthForm