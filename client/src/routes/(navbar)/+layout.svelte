<script>
	import Footer from '$lib/layout/(navbar)/footer.svelte';
	import Navbar from '$lib/layout/navbar.svelte';
</script>

<div class="fixed-top">
	<Navbar />
</div>
<slot />

<Footer></Footer>
