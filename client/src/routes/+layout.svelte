<script>
	import { registerSpinnerId } from '$lib/components/share/spinner.svelte';
	import '$lib/style/spinner.custom.scss';
	registerSpinnerId('appSpinner');
</script>

<slot />

<style lang="scss">
	@import '~bootstrap/scss/bootstrap.scss';
	@import '~bootstrap-icons/font/bootstrap-icons.scss';
</style>
