<script>
	import { page } from '$app/stores';
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
				<li>
					<a
						href="/"
						class="nav-link px-3"
						class:disabled={$page.url.pathname === '/'}
						class:active={$page.url.pathname == '/'}>Home</a
					>
				</li>
				<li>
					<a
						href="/shop"
						class="nav-link px-3"
						class:disabled={$page.url.pathname === '/shop'}
						class:active={$page.url.pathname == '/shop'}>Shop</a
					>
				</li>
				<li>
					<a
						href="/favorites"
						class="nav-link px-3"
						class:disabled={$page.url.pathname === '/favorites'}
						class:active={$page.url.pathname == '/favorites'}
					>
						Wishlist
					</a>
				</li>
				<li>
					<a
						href="/about"
						class="nav-link px-3"
						class:disabled={$page.url.pathname === '/about'}
						class:active={$page.url.pathname == '/about'}
					>
						About
					</a>
				</li>
				<li>
					<a
						href="/blog"
						class="nav-link px-3"
						class:disabled={$page.url.pathname === '/blog'}
						class:active={$page.url.pathname === '/blog'}
					>
						Blog
					</a>
				</li>
			</ul>

			<div class="col-md-3 text-end">
				<a
					type="button"
					class="btn me-2"
					class:btn-outline-success={$page.url.pathname !== '/login'}
					class:btn-success={$page.url.pathname === '/login'}
					class:disabled={$page.url.pathname === '/login'}
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
					href="/register"
				>
					Sign-up
				</a>
			</div>
		</div>
	</div>
</nav>
