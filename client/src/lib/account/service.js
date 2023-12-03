import { get, writable } from "svelte/store";
import AccountHttpClient from "./request";

const KEY = 'token';

const tokenStore = writable(localStorage.getItem(KEY) ?? "");
/**
 * @type {import("svelte/store").Writable<UserInfo | null>}
 */
const userInfo = writable(null)


function getAccessToken() {
    tokenStore.update(() => localStorage.getItem(KEY) ?? "");
    return get(tokenStore);
}

async function loadUser() {
    const accessToken = getAccessToken();
    if (!accessToken) return;

    // Check if token is correct one
    const data = await AccountHttpClient.getDisplayInfo();
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
    const data = await AccountHttpClient.login(loginDTO);
    localStorage.setItem(KEY, data.token);
    tokenStore.update(() => data.token);
    userInfo.update(() => ({ email: data.email, displayName: data.display_name }))
    return get(userInfo)
}

/**
 * @param {RegisterDTO} registerDTO
 */
async function register(registerDTO) {
    const data = await AccountHttpClient.register(registerDTO);
    localStorage.setItem(KEY, data.token);
    tokenStore.update(() => data.token);
    userInfo.update(() => ({ email: data.email, displayName: data.display_name }))
    return get(userInfo);
}

const AccountService = {
    getAccessToken,
    loadUser,
    logout,
    login,
    register
}

export default AccountService;