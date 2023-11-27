<script>
	import { loadBasket } from '$lib/service/basket.service';
	import { onMount } from 'svelte';

	onMount(async () => await loadBasket());
</script>

<slot />

<style lang="scss">
	@import '~bootstrap/scss/bootstrap.scss';
	@import '~bootstrap-icons/font/bootstrap-icons.scss';
</style>
