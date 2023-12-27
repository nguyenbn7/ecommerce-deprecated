<script>
	import PageTitle from '$lib/layout/(navbar)/(shop)/page-title.svelte';
</script>

<PageTitle />
<main class="flex-grow-1 mb-4 mt-5">
	<div class="container-fluid px-5">
		<slot />
	</div>
</main>
