<script>
	import Intro from '$lib/layout/(nobars)/about/intro.svelte';
	import Team from '$lib/layout/(nobars)/about/team.svelte';
	import Techstack from '$lib/layout/(nobars)/about/techstack.svelte';
	import { ECOMMERCE_NAME } from '$lib/share/constant';
	import Footer from '$lib/layout/(bars)/footer.svelte';
	import PageTitle from '$lib/layout/(bars)/(shop)/page-title.svelte';
</script>

<svelte:head>
	<title>{ECOMMERCE_NAME} - About</title>
</svelte:head>

<PageTitle />

<Intro />

<Techstack />

<Team />

<Footer />
