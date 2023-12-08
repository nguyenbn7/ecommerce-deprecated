<script>
	import BrandBar from '$lib/brand-bar.svelte';
	import Footer from '$lib/components/share/footer.svelte';
	import NavBar from '$lib/nav-bar.svelte';
	import TopBar from '$lib/top-bar.svelte';
</script>

<TopBar />
<BrandBar />
<NavBar />
<div class="container">
	<slot />
</div>

<Footer></Footer>
