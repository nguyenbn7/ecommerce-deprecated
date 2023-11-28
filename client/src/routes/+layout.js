import { loadUser } from '$lib/service/account.service';
import { loadBasket } from '$lib/service/basket.service';

export const ssr = false;
/** @type {import('./$types').LayoutLoad} */
export async function load() {
    await loadBasket();
    await loadUser();
}