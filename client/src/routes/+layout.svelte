<script>
	import { loadUser } from '$lib/service/account.service';
	import { loadBasket } from '$lib/service/basket.service';
	import { onMount } from 'svelte';

	onMount(async () => {
		await loadBasket();
		await loadUser();
	});
</script>

<slot />

<style lang="scss">
	@import '~bootstrap/scss/bootstrap.scss';
	@import '~bootstrap-icons/font/bootstrap-icons.scss';
</style>
