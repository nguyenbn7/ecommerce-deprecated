<script>
	import Navbar from '$lib/shares/navbar.svelte';
	import '$lib/account.style.scss';
</script>

<div class="sticky-top">
	<div class="bg-body">
		<div class="container">
			<Navbar></Navbar>
		</div>
	</div>
</div>
<div class="d-flex flex-column bg-body-secondary" style="height: 90%;">
	<main class="flex-grow-1 mt-5">
		<div
			class="card m-auto col-8 col-sm-6 col-md-6 col-xl-3 col-xxl-3 shadow border-0 bg-body-tertiary px-4 pt-2 pb-5"
		>
			<slot />
		</div>
		<div class="align-items-center"></div>
	</main>
</div>
