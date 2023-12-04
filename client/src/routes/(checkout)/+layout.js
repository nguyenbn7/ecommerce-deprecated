import AccountService from '$lib/(account)/service';
import { redirect } from '@sveltejs/kit';
import { get } from 'svelte/store';

/** @type {import('./$types').LayoutLoad} */
export async function load({ url }) {
	if (!get(AccountService.currentUser)) throw redirect(302, `/login?redirect=${url.pathname}`);
}
