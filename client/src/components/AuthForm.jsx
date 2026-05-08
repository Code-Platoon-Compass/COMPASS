import { useState } from 'react';
import { useNavigate } from 'react-router-dom'
import { handleGoogleAuth } from '../utilities/authUtilities';
import { GoogleLogin } from '@react-oauth/google';

const AuthForm = ({setUser}) => {
    const [inviteCode, setInviteCode] = useState("")
    const [errorMessage, setErrorMessage] = useState("")
    const navigate = useNavigate()

    const handleGoogleLoginSuccess = async (credentialResponse) => {
        if (!inviteCode.trim()) {
            setErrorMessage('Invite code is required before signing in with Google.')
            return;
        }

        const token = credentialResponse.credential;
        const result = await handleGoogleAuth(token, inviteCode.trim());

        if (result.ok) {
            setErrorMessage('')
            setUser(result.data);
            navigate("/dashboard");
            return;
        }

        setErrorMessage(result.error);
    }

    return (
        <>
            <label htmlFor="invite-code">Invite code</label>
            <input
                id="invite-code"
                type="text"
                value={inviteCode}
                onChange={(event) => {
                    setInviteCode(event.target.value)
                    if (errorMessage) {
                        setErrorMessage('')
                    }
                }}
                placeholder="Enter your cohort invite code"
            />
            {errorMessage ? <p>{errorMessage}</p> : null}
            <GoogleLogin
                onSuccess={handleGoogleLoginSuccess}
                onError={() => {
                    console.log('Login Failed');
                    alert("Google authentication failed. Please try again.");
                }}
            />
        </>
    )
}

export default AuthForm