<script>
	import { page } from '$app/stores';
	import BrandBar from '$lib/layout/(bars)/brand-bar.svelte';
	import Breadcrumb from '$lib/share/component/breadcrumb.svelte';
	import Footer from '$lib/layout/(bars)/footer.svelte';
	import NavBar from '$lib/layout/(bars)/nav-bar.svelte';
	import TopBar from '$lib/layout/(bars)/top-bar.svelte';
	const mapTitle = [
		{ link: '/shop', name: 'Our Shop' },
		{ link: '/about', name: 'About Us' },
		{ link: '/blog', name: 'Blog' }
	];
</script>

<TopBar />
<BrandBar />
<NavBar />

<div class="d-flex flex-column" style="min-height: 100vh;">
	<!-- TODO: merge breadcrumb with header -->
	<div class="container-fluid bg-secondary-subtle mb-5">
		<div
			class="d-flex flex-column align-items-center justify-content-center"
			style="min-height: 300px"
		>
			<h1 class="fw-semibold text-uppercase mb-3">
				{mapTitle.filter((value) => value.link === $page.url.pathname)[0]?.name}
			</h1>
			<div class="d-inline-flex">
				<Breadcrumb class="breadcrumb ps-1 pb-3" />
			</div>
		</div>
	</div>
	<main class="flex-grow-1 mb-4 mt-5">
		<div class="container-fluid px-5">
			<slot />
		</div>
	</main>
	<Footer></Footer>
</div>
