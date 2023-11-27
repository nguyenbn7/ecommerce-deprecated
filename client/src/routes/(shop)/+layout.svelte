<script>
	import Breadcrumb from '$lib/components/breadcrumb.svelte';
	import Footer from '$lib/components/footer.svelte';
	import Navbar from '$lib/components/navbar.svelte';
</script>

<Navbar></Navbar>

<div class="d-flex flex-column">
	<main class="flex-grow-1 mb-3 mt-5">
		<div class="container">
			<Breadcrumb class="breadcrumb-chevron ps-1 pb-3"></Breadcrumb>
			<slot />
		</div>
	</main>
	<Footer></Footer>
</div>
