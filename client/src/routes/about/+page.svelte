<script>
	import Intro from '$lib/about/intro.svelte';
	import Team from '$lib/about/team.svelte';
	import Techstack from '$lib/about/techstack.svelte';
	import Breadcrumb from '$lib/share/component/breadcrumb.svelte';
	import { ECOMMERCE_NAME } from '$lib/share/constant';
	import BrandBar from '$lib/share/layout/brand-bar.svelte';
	import Footer from '$lib/share/layout/footer.svelte';
	import NavBar from '$lib/share/layout/nav-bar.svelte';
	import TopBar from '$lib/share/layout/top-bar.svelte';
</script>

<svelte:head>
	<title>{ECOMMERCE_NAME} - About</title>
</svelte:head>

<TopBar />
<BrandBar />
<NavBar />

<div class="container-fluid bg-secondary-subtle mb-5">
	<div
		class="d-flex flex-column align-items-center justify-content-center"
		style="min-height: 300px"
	>
		<h1 class="fw-semibold text-uppercase mb-3">About Us</h1>
		<div class="d-inline-flex">
			<Breadcrumb class="breadcrumb ps-1 pb-3" />
		</div>
	</div>
</div>

<Intro />

<Techstack />

<Team />

<Footer />
