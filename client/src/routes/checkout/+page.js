import { redirect } from '@sveltejs/kit';
import { get } from 'svelte/store';

/** @type {import('./$types').PageLoad} */
export async function load({ parent, url }) {
	await parent();
	const currentUser = get((await import('$lib/(account)/service')).currentUser);
	if (!currentUser) throw redirect(302, `/login?redirect=${url.pathname}`);
}
