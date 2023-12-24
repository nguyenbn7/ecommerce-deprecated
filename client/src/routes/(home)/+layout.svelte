<script>
	import BrandBar from '$lib/layout/(bars)/brand-bar.svelte';
	import Footer from '$lib/layout/(bars)/footer.svelte';
	import NavBar from '$lib/layout/(bars)/nav-bar.svelte';
	import TopBar from '$lib/layout/(bars)/top-bar.svelte';
</script>

<TopBar />
<BrandBar />
<NavBar />
<div class="container">
	<slot />
</div>

<Footer></Footer>
