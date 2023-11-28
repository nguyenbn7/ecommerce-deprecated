import { setToastContainer } from '$lib/components/share/toast.svelte';
import { loadUser } from '$lib/service/account.service';
import { loadBasket } from '$lib/service/basket.service';

export const ssr = false;
/** @type {import('./$types').LayoutLoad} */
export async function load() {
	setToastContainer('toast-container');
	await loadBasket();
	await loadUser();
}
