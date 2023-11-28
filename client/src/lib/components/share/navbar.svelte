<script>
	import { page } from '$app/stores';
	import { currentUser, logout } from '$lib/service/account.service';
	import { basket } from '$lib/service/basket.service';
	import { readMoreString } from '$lib/util/helper.function';
	import { Dropdown } from 'bootstrap';

	const paths = [
		{ link: '/', name: 'Home' },
		{ link: '/shop', name: 'Shop' },
		{ link: '/about', name: 'About' },
		{ link: '/blog', name: 'Blog' }
	];

	/**
	 * @param {BasketItem[]} items
	 */
	function getCount(items) {
		return items.reduce((total, item) => total + item.quantity, 0);
	}
</script>

<header class="nav nav-expand-md sticky-top bg-body">
	<nav
		class="container-xxl d-flex flex-wrap align-items-center justify-content-center justify-content-md-between py-3"
	>
		<div class="col-md-3 mb-2 mb-md-0">
			<a href="/" class="text-decoration-none">
				<img src="/images/logo.png" alt="logo" style="max-height: 45px;" class="logo" />
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
			{#if $currentUser}
				<a
					class="nav-btn text-info"
					data-bs-toggle="dropdown"
					aria-expanded="false"
					href={'#'}
					title="Profile"
				>
					<i class="bi bi-person-circle"></i>
				</a>
				<ul class="dropdown-menu dropdown-menu-end">
					<li>
						<h2 class="dropdown-header" title={$currentUser.display_name}>
							{readMoreString($currentUser.display_name, 25)}
						</h2>
					</li>
					<li>
						<a class="dropdown-item" href={'#'}>
							<i class="bi bi-card-checklist"></i> View Order
						</a>
					</li>
					<li>
						<a class="dropdown-item" href={'#'}>
							<i class="bi bi-person-fill-gear"></i> View Profile
						</a>
					</li>
					<li><hr class="dropdown-divider" /></li>
					<li>
						<a class="dropdown-item" href={'#'} on:click={logout}>
							<i class="bi bi-box-arrow-in-right"></i> Logout
						</a>
					</li>
				</ul>
			{:else}
				<a class="nav-btn text-secondary" href="/login" title="Login">
					<i class="bi bi-person"></i>
				</a>
			{/if}
			<a
				class="nav-btn position-relative"
				class:text-secondary={!$basket || !$basket.items.length}
				class:text-info={$basket && $basket.items.length}
				href="/basket"
				title="Basket"
			>
				{#if $basket && $basket.items.length}
					<i class="bi bi-basket-fill"></i>
					<span
						class="position-absolute translate-middle p-2 bg-transparent badge rounded-pill text-danger fs-5 cart-no"
					>
						{getCount($basket.items)}
					</span>
				{:else}
					<i class="bi bi-basket"></i>
				{/if}
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

	.cart-no {
		top: 20%;
		left: 100%;
	}

	.logo {
		cursor: pointer;
	}
</style>
