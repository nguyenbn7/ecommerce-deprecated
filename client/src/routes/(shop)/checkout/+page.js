import { user } from '$lib/service/account.service';
import { redirect } from '@sveltejs/kit';
import { get } from 'svelte/store';

export const ssr = false;

/** @type {import('./$types').PageLoad} */
export async function load() {
    if (!get(user))
        throw redirect(302, "/login");
}