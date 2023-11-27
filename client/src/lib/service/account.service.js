import { PUBLIC_BASE_API_URL } from '$env/static/public';
import { readonly, writable } from 'svelte/store';

const _user = writable(undefined);

export const user = readonly(_user);

export async function loadUser() {
	const accessToken = localStorage.getItem("token");
	if (!accessToken) return;
	const response = await fetch(`${PUBLIC_BASE_API_URL}/account/profile`);

	if (!response.ok) {
		_user.update(() => undefined);
		return
	}

	const data = await response.json();
	_user.update(() => data);
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
	return await response.json();
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
	return await response.json();
}
