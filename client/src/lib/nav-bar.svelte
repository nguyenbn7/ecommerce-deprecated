<script>
	import { page } from '$app/stores';
	import { onMount } from 'svelte';

	const paths = [
		{ link: '/', name: 'Home' },
		{ link: '/shop', name: 'Shop' },
		{ link: '/about', name: 'About' },
		{ link: '/blog', name: 'Blog' }
	];

	onMount(async () => {
		(await import('bootstrap')).Dropdown;
	});
</script>

<nav class="navbar navbar-expand-md border-top border-bottom py-3 px-5">
	<div class="collapse navbar-collapse justify-content-between">
		<div class="navbar-nav me-auto py-0">
			{#each paths as path}
				<li>
					<a
						href={path.link}
						class="nav-link px-3"
						class:border-bottom={$page.url.pathname === path.link}
						class:border-warning={$page.url.pathname === path.link}
						class:border-3={$page.url.pathname === path.link}
						class:active-link={$page.url.pathname === path.link}
					>
						{path.name}
					</a>
				</li>
			{/each}
		</div>
		<div class="navbar-nav ms-auto py-0">
			<a href="/login" class="btn btn-outline-success me-3">Login</a>
			<a href="/register" class="btn btn-success">Register</a>
		</div>
	</div>
</nav>

<style lang="scss">
    .active-link {
        pointer-events: none;
        cursor: default;
    }
</style>
