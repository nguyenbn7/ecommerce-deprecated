import { currentUser } from '$lib/service/account.service';
import { redirect } from '@sveltejs/kit';
import { get } from 'svelte/store';

export const ssr = false;

/** @type {import('./$types').PageLoad} */
export async function load({ parent, url }) {
	await parent();
	if (!get(currentUser)) throw redirect(302, `/login?returnUrl=${url.pathname}`);
}
