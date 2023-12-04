import { httpClient } from "$lib/share/request";
import { get, readonly, writable } from "svelte/store";

const KEY = 'token';

const tokenStore = writable("");
/**
 * @type {import("svelte/store").Writable<UserInfo | null>}
 */
const userInfo = writable(null)

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

function getAccessToken() {
    tokenStore.update(() => localStorage.getItem(KEY) ?? "");
    return get(tokenStore);
}

async function loadUser() {
    const accessToken = getAccessToken();
    if (!accessToken) return;

    // Check if token is correct one
    const data = await getDisplayInfo();
    userInfo.update(() => ({ email: data.email, displayName: data.display_name }));
}

function logout() {
    tokenStore.update(() => {
        localStorage.removeItem(KEY);
        return "";
    });
    userInfo.update(() => null);
}

/**
 * @param {LoginDTO} loginDTO
 */
async function login(loginDTO) {
    const response = await httpClient.post("account/login", loginDTO);
    /**
     * @type {SignInSuccess}
     */
    const data = response.data;
    localStorage.setItem(KEY, data.token);
    tokenStore.update(() => data.token);
    userInfo.update(() => ({ email: data.email, displayName: data.display_name }))
    return get(userInfo)
}

/**
 * @param {RegisterDTO} registerDTO
 */
async function register(registerDTO) {
    const response = await httpClient.post("account/register", registerDTO);
    const data = response.data;
    localStorage.setItem(KEY, data.token);
    tokenStore.update(() => data.token);
    userInfo.update(() => ({ email: data.email, displayName: data.display_name }))
    return get(userInfo);
}

const currentUser = readonly(userInfo);

const AccountService = {
    getAccessToken,
    loadUser,
    logout,
    login,
    register,
    currentUser
}

export default AccountService;