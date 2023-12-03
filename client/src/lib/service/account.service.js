import { PUBLIC_BASE_API_URL } from '$env/static/public';
import { ToastService } from '$lib/components/share/toast.svelte';
import { get, readonly, writable } from 'svelte/store';

/**
 * @type {import("svelte/store").Writable<UserInfo | undefined>}
 */
const _user = writable(undefined);

const TOKEN_KEY_NAME = 'token';

export const currentUser = readonly(_user);

function getAccessToken() {
	return localStorage.getItem(TOKEN_KEY_NAME);
}

export async function loadUser() {
	const accessToken = getAccessToken();
	if (!accessToken) return;
	const response = await fetch(`${PUBLIC_BASE_API_URL}/account/display`, {
		headers: {
			'Content-Type': 'application/json',
			Authorization: `Bearer ${accessToken}`
		}
	});

	if (!response.ok) {
		_user.update(() => undefined);
		return;
	}

	/**
	 * @type {UserInfo}
	 */
	const data = await response.json();
	_user.update(() => data);
}

export function logout() {
	localStorage.removeItem(TOKEN_KEY_NAME);
	const display_name = get(_user)?.display_name;
	_user.update(() => undefined);
	ToastService.notifyError(`Goodbye ${display_name}`);
}

/**
 * @param {Login} loginForm
 */
export async function loginAs(loginForm) {
	const response = await fetch(`${PUBLIC_BASE_API_URL}/account/login`, {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify(loginForm)
	});
	if (!response.ok) return response;

	/**
	 * @type {SuccessResponse}
	 */
	const data = await response.json();
	localStorage.setItem(TOKEN_KEY_NAME, data.token);
	_user.update(() => ({ email: data.email, display_name: data.display_name }));

	return data;
}

/**
 * @param {Register} registerForm
 */
export async function registerAs(registerForm) {
	const response = await fetch(`${PUBLIC_BASE_API_URL}/account/register`, {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify(registerForm)
	});
	if (!response.ok) return response;

	/**
	 * @type {SuccessResponse}
	 */
	const data = await response.json();
	localStorage.setItem(TOKEN_KEY_NAME, data.token);
	_user.update(() => ({ email: data.email, display_name: data.display_name }));

	return data;
}
