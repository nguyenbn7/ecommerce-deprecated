import { apiClientBackground, httpClient } from '$lib/share/request';
import { get, readonly, writable } from 'svelte/store';

const ACCESS_TOKEN = 'token';

/**
 * @type {import("svelte/store").Writable<string>}
 */
const tokenSource = writable('');
/**
 * @type {import("svelte/store").Writable<User | null>}
 */
const currentUserStore = writable(null);

/**
 * @returns {Promise<UserInfoResponse>}
 */
async function getDisplayInfo() {
	const response = await apiClientBackground.get('account/display', {
		headers: {
			Authorization: `Bearer ${AccountService.getAccessToken()}`
		}
	});
	return response.data;
}

function getAccessToken() {
	tokenSource.update(() => localStorage.getItem(ACCESS_TOKEN) ?? '');
	return get(tokenSource);
}

async function loadUserBackground() {
	const accessToken = getAccessToken();
	if (!accessToken) return;

	// Check if token is correct one
	const data = await getDisplayInfo();
	currentUserStore.update(() => ({ email: data.email, displayName: data.display_name }));
}

function logout() {
	tokenSource.update(() => {
		localStorage.removeItem(ACCESS_TOKEN);
		return '';
	});
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

	tokenSource.update(() => data.token);
	currentUserStore.update(() => ({ email: data.email, displayName: data.display_name }));

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

	tokenSource.update(() => data.token);
	currentUserStore.update(() => ({ email: data.email, displayName: data.display_name }));

	return get(currentUserStore);
}

const currentUser = readonly(currentUserStore);

const AccountService = {
	getAccessToken,
	loadUserBackground,
	logout,
	login,
	register
};

export { AccountService, currentUser };
