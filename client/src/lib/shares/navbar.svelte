<script>
	import { page } from '$app/stores';
	const paths = [
		{ link: '/', name: 'Home' },
		{ link: '/shop', name: 'Shop' },
		{ link: '/about', name: 'About' },
		{ link: '/blog', name: 'Blog' }
	];
</script>

<header class="nav nav-expand-md sticky-top bg-body">
	<nav
		class="container-xxl d-flex flex-wrap align-items-center justify-content-center justify-content-md-between py-3"
	>
		<div class="col-md-3 mb-2 mb-md-0">
			<a href={'#'} class="text-decoration-none">
				<img src="images/logo.png" alt="logo" style="max-height: 45px;" class="logo" />
			</a>
		</div>

		<ul class="nav col-12 col-md-auto mb-2 justify-content-center mb-md-0 nav-pills">
			{#each paths as path}
				<li>
					<a
						href={path.link}
						class="nav-link px-3"
						class:disabled={$page.url.pathname === path.link}
						class:active={$page.url.pathname === path.link}
						data-sveltekit-preload-data="tap"
					>
						{path.name}
					</a>
				</li>
			{/each}
		</ul>

		<div class="col-md-3 text-end">
			<a class="nav-btn text-secondary" href={'#'} title="Search">
				<i class="bi bi-search"></i>
			</a>
			<a class="nav-btn text-secondary" href="/favorites" title="Wish list">
				<i class="bi bi-heart"></i>
			</a>
			<a class="nav-btn text-secondary" href="/login" title="Login">
				<i class="bi bi-person"></i>
			</a>
			<a class="nav-btn text-secondary" href="/cart" title="Cart">
				<i class="bi bi-cart"></i>
			</a>
		</div>
	</nav>
</header>

<style lang="scss">
	.nav-btn {
		--padding-x: 0.5rem;
		--padding-y: 0.375rem;
		display: inline-block;
		padding: var(--padding-y) var(--padding-x);
		& i {
			font-size: 1.25em;
		}
	}
</style>
