import { get, readonly, writable } from 'svelte/store';
import { createHttpClient } from '../httpClient';
import { delayFetch, notifyFetchError } from '../httpClient/plugin';

const httpClientBackground = createHttpClient();

const httpClient = createHttpClient();
httpClient.interceptors.response.use(async response => {
    await delayFetch(1500);
    return response;
}, async error => {
    await delayFetch(1500);
    notifyFetchError(error);
});

const ACCESS_TOKEN = 'token';

/**
 * @type {import("svelte/store").Writable<User | null>}
 */
const currentUserStore = writable(null);

function getAccessToken() {
    return localStorage.getItem(ACCESS_TOKEN) ?? ''
}

async function loadUser() {
    const accessToken = getAccessToken();
    if (!accessToken) return;

    const response = await httpClientBackground.get('account/display', {
        headers: {
            Authorization: `Bearer ${AccountService.getAccessToken()}`
        }
    });
    /**
     * @type {UserInfoResponse}
     */
    const data = response.data;
    currentUserStore.update(() => ({ email: data.email, displayName: data.displayName }));
}

function logout() {
    localStorage.removeItem(ACCESS_TOKEN);
    currentUserStore.update(() => null);
}

/**
 * @param {LoginDTO} loginDTO
 */
async function login(loginDTO) {
    /**
     * @type {SignInSuccess}
     */
    const data = (await httpClient.post('account/login', loginDTO)).data;

    localStorage.setItem(ACCESS_TOKEN, data.token);

    currentUserStore.update(() => ({ email: data.email, displayName: data.displayName }));

    return get(currentUserStore);
}

/**
 * @param {RegisterDTO} registerDTO
 */
async function register(registerDTO) {
    /**
     * @type {SignInSuccess}
     */
    const data = (await httpClient.post('account/register', registerDTO)).data;

    localStorage.setItem(ACCESS_TOKEN, data.token);

    currentUserStore.update(() => ({ email: data.email, displayName: data.displayName }));

    return get(currentUserStore);
}

export const currentUser = readonly(currentUserStore);

export const AccountService = {
    getAccessToken,
    loadUser,
    logout,
    login,
    register
};

