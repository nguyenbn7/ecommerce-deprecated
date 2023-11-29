<script>
	import Spinner from '$lib/components/share/spinner.svelte';
	import '$lib/style/spinner.custom.scss';
</script>

<Spinner></Spinner>
<slot />

<style lang="scss">
	@import '~bootstrap/scss/bootstrap.scss';
	@import '~bootstrap-icons/font/bootstrap-icons.scss';
</style>
