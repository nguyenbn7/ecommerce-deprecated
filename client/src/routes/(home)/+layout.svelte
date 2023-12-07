<script>
	import Footer from '$lib/components/share/footer.svelte';
	import Navbar from '$lib/components/share/navbar.svelte';
</script>

<Navbar></Navbar>
<div class="container">
	<slot />
</div>

<Footer></Footer>
