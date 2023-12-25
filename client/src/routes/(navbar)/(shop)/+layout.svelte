<script>
	import PageTitle from '$lib/layout/(bars)/(shop)/page-title.svelte';
	const mapTitle = [
		{ link: '/shop', name: 'Our Shop' },
		{ link: '/about', name: 'About Us' },
		{ link: '/blog', name: 'Blog' }
	];
</script>

<PageTitle />
<main class="flex-grow-1 mb-4 mt-5">
	<div class="container-fluid px-5">
		<slot />
	</div>
</main>
