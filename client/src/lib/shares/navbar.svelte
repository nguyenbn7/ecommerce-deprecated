<script>
	import { page } from '$app/stores';
	const paths = [
		{ link: '/', name: 'Home' },
		{ link: '/shop', name: 'Shop' },
		{ link: '/favorites', name: 'Wishlist' },
		{ link: '/about', name: 'About' },
		{ link: '/blog', name: 'Blog' }
	];
</script>

<nav class="nav nav-expand-md">
	<div class="container-fluid">
		<div
			class="d-flex flex-wrap align-items-center justify-content-center justify-content-md-between py-3"
		>
			<div class="col-md-3 mb-2 mb-md-0">
				<a href={'#'}>USA EN</a>
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
				<a
					type="button"
					class="btn me-2"
					class:btn-outline-success={$page.url.pathname !== '/login'}
					class:btn-success={$page.url.pathname === '/login'}
					class:disabled={$page.url.pathname === '/login'}
					data-sveltekit-reload
					href="/login"
				>
					Login
				</a>
				<a
					type="button"
					class="btn btn-outline-danger"
					class:btn-outline-danger={$page.url.pathname !== '/register'}
					class:btn-danger={$page.url.pathname === '/register'}
					class:disabled={$page.url.pathname === '/register'}
					data-sveltekit-reload
					href="/register"
				>
					Sign-up
				</a>
			</div>
		</div>
	</div>
</nav>
