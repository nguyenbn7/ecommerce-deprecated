<script>
	import BrandBar from '$lib/share/layout/brand-bar.svelte';
	import Footer from '$lib/share/layout/footer.svelte';
	import NavBar from '$lib/share/layout/nav-bar.svelte';
	import TopBar from '$lib/share/layout/top-bar.svelte';
</script>

<TopBar />
<BrandBar />
<NavBar />
<div class="container">
	<slot />
</div>

<Footer></Footer>
