<script>
	import Footer from '$lib/shares/footer.svelte';
	import Navbar from '$lib/shares/navbar.svelte';
	import Navheader from '$lib/shares/navheader.svelte';
</script>

<div class="d-flex flex-column h-100">
	<div class="sticky-top">
		<Navbar></Navbar>
		<Navheader></Navheader>
	</div>
	<main class="flex-grow-1">
		<slot />
	</main>
	<Footer></Footer>
</div>
