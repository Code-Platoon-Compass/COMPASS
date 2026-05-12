import axios from "axios";

export const api = axios.create({
    baseURL: "/api/v1",
    withCredentials: true,
});

export const test_connection = async() =>{
		    let response = await api.get("test/")
		    console.log(response)
		  }

// Google authentication helper function. Takes the token from the Google login response and the invite code (if it's the user's first time logging in) and sends them to the backend for verification.     
export const handleGoogleAuth = async (token, inviteCode) => {
    try {
        const payload = { token };

        if (inviteCode?.trim()) {
            payload.invite_code = inviteCode.trim();
        }

        let response = await api.post("auth/google-auth/", payload);

        return {
            ok: response.status === 200,
            data: response.data,
            error: null,
        };
    } catch (error) {
        return {
            ok: false,
            data: null,
            error: error.response?.data?.error || 'Google sign in failed. Please try again.',
        };
    }
}
// Logout helper function. Called when the user clicks the logout button. It sends a request to the backend to clear the user's session cookie.
export const handleLogout = async () => {
    try {
        let response = await api.post("auth/logout/");

        return {
            ok: response.status === 200,
            error: null,
        };
    } catch (error) {
        return {
            ok: false,
            error: error.response?.data?.error || 'Logout failed. Please try again.',
        };
    }
}
// Session restoration helper function. Called when the app first loads to check if the user has an active session. It attempts to mint a new access token using the refresh token cookie, then grabs user info. 
export const restoreSession = async () => {
    try {
        // Step 1: use refresh cookie to mint a new access token cookie.
        await api.post("auth/refresh/");

        // Step 2: fetch user profile using the new access token cookie.
        const response = await api.get("auth/me/");

        return {
            ok: response.status === 200,
            data: response.data,
        };
    } catch {
        return {
            ok: false,
            data: null,
        };
    }
}




