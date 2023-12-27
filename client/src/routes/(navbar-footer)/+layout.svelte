<script>
	import Footer from '$lib/component/(root)/(navbar-footer)/footer.svelte';
	import Navbar from '$lib/component/(root)/(navbar-footer)/navbar.svelte';
</script>

<div class="fixed-top">
	<Navbar />
</div>
<slot />

<Footer />
