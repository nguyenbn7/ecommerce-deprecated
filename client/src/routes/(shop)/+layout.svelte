<script>
	import Breadcrumb from '$lib/shares/breadcrumb.svelte';
	import Footer from '$lib/shares/footer.svelte';
	import Navbar from '$lib/shares/navbar.svelte';
	import Navheader from '$lib/shares/navheader.svelte';
</script>

<div class="sticky-top">
	<div class="bg-body">
		<div class="container">
			<Navbar></Navbar>
		</div>
	</div>
	<div class="bg-light">
		<div class="container">
			<Navheader></Navheader>
		</div>
	</div>
</div>

<div class="d-flex flex-column">
	<main class="flex-grow-1">
		<div class="container">
			<Breadcrumb class="breadcrumb-chevron ps-1 pb-3"></Breadcrumb>
			<slot />
		</div>
	</main>
	<Footer></Footer>
</div>
