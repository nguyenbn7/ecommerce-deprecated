<script>
	import { getBasket } from '$lib/request/cart';
	import { onMount } from 'svelte';

	async function loadBasket() {
		const basketId = localStorage.getItem('basket_id');
		if (basketId) await getBasket(basketId);
	}

	onMount(async () => await loadBasket());
</script>

<slot />

<style lang="scss">
	@import '~bootstrap/scss/bootstrap.scss';
	@import '~bootstrap-icons/font/bootstrap-icons.scss';
</style>
