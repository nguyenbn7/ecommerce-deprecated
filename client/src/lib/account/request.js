import { ToastService } from "$lib/components/share/toast.svelte";
import { delay, httpClient } from "$lib/share/request";
import { AxiosError } from "axios";
import AccountService from "./service";

httpClient.interceptors.response.use(null, error => {
    if (error instanceof AxiosError) {
        const response = error.response;
        let errorMessage = error.message;
        if (response) {
            errorMessage = response.data.message
        }
        ToastService.notifyError(errorMessage);
        console.log(error)
    }
    throw error;
});

/**
 * @param {LoginDTO} loginDTO
 * @returns {Promise<SignInSuccess>}
 */
async function login(loginDTO) {
    const response = await httpClient.post("account/login", loginDTO);
    return response.data;
}

/**
 * @param {RegisterDTO} registerDTO
 * @returns {Promise<SignInSuccess>}
 */
async function register(registerDTO) {
    const response = await httpClient.post("account/register", registerDTO);
    return response.data;
}

/**
 * @returns {Promise<UserInfoResponse>}
 */
async function getDisplayInfo() {
    const response = await httpClient.get("account/display", {
        headers: {
            Authorization: `Bearer ${AccountService.getAccessToken()}`
        }
    });
    return response.data;
}

const AccountHttpClient = {
    login,
    register,
    getDisplayInfo
}

export default AccountHttpClient;