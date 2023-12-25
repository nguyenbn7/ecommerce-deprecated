<script>
	import Intro from '$lib/layout/(nonavbar)/about/intro.svelte';
	import Team from '$lib/layout/(nonavbar)/about/team.svelte';
	import Techstack from '$lib/layout/(nonavbar)/about/techstack.svelte';
	import { ECOMMERCE_NAME } from '$lib/share/constant';
	import PageTitle from '$lib/layout/(navbar)/(shop)/page-title.svelte';
</script>

<svelte:head>
	<title>{ECOMMERCE_NAME} - About</title>
</svelte:head>

<PageTitle />

<Intro />

<Techstack />

<Team />
