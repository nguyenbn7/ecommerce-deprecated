<script>
	import Breadcrumb from '$lib/shares/breadcrumb.svelte';
	import Footer from '$lib/shares/footer.svelte';
	import Navbar from '$lib/shares/navbar.svelte';
	import Navheader from '$lib/shares/navheader.svelte';
</script>

<div class="d-flex flex-column h-100">
	<div class="sticky-top">
		<Navbar></Navbar>
		<Navheader></Navheader>
	</div>
	<main class="flex-grow-1 container">
		<Breadcrumb class="breadcrumb-chevron p-3 rounded-3"></Breadcrumb>
		<slot />
	</main>
	<Footer></Footer>
</div>
