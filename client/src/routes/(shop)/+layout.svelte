<script>
	import { page } from '$app/stores';
	import BrandBar from '$lib/brand-bar.svelte';
	import Breadcrumb from '$lib/components/share/breadcrumb.svelte';
	import Footer from '$lib/components/share/footer.svelte';
	import NavBar from '$lib/nav-bar.svelte';
	import TopBar from '$lib/top-bar.svelte';
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
