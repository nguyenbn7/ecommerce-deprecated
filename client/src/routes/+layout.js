import AccountService from '$lib/(account)/service';
import BasketService from '$lib/basket/service';

export const ssr = false;

/** @type {import('./$types').LayoutLoad} */
export async function load( ) {
    Promise.all([BasketService.loadBasketBackground(), AccountService.loadUser()])
}