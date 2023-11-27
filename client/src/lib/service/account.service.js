import { PUBLIC_BASE_API_URL } from '$env/static/public';

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
