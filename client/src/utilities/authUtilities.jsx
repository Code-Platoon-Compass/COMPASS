import axios from "axios";

export const api = axios.create({
    baseURL: "/api/v1",
    withCredentials: true,
});

export const test_connection = async() =>{
		    let response = await api.get("test/")
		    console.log(response)
		  }

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
// export const logout = async()=>{
//     let token = localStorage.getItem("token")
//     api.defaults.headers.common['Authorization'] = `Token ${token}`
//     let response = await api.post("users/logout/")
//     localStorage.removeItem("token");

//     if (response.status == 200){
//         console.log('logged out ')
//         return null
//     }
//     else{
//         return console.errors(response.errors)
//     }
// }

// export const userConfirmation = async() => {
//     let token = localStorage.getItem("token") // 'str' | null
//     if (token){
//         api.defaults.headers.common['Authorization'] = `Token ${token}`
//         let response = await api.get('users/')
//         if (response.status === 200){
//             let user = response.data.email
//             console.log("user confirmed")
//             return user
//         }
//         console.error(response.data)
//         return null
//     }
//     return null
// }

// export const handleUserAuth = async (data, create) => {
//   let response = await api.post(create ? "users/create/" : "users/login/",
//     data
//   );
//   if (response.status === 201 || response.status === 200) {
//     let token = response.data.token;
//     // Store the token securely (e.g., in localStorage or HttpOnly cookies)
//     localStorage.setItem("token", token);
//     api.defaults.headers.common["Authorization"] = `Token ${token}`;
//     return response.data.email;
//   }
//   alert(response.data);
//   return null;
// };



