<script>
	import { page } from '$app/stores';
	import { AccountService, currentUser } from '$lib/(account)/service';
	import { basket } from '$lib/basket/service';
	import { readMoreString } from '$lib/share/functions';
	import { icon } from '@fortawesome/fontawesome-svg-core';
	import {
		faBasketShopping,
		faCircleUser,
		faHeart,
		faSearch,
		faUser
	} from '@fortawesome/free-solid-svg-icons';
	import { onMount } from 'svelte';

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

	onMount(async () => {
		(await import('bootstrap')).Dropdown;
	});
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
				{@html icon(faSearch).html}
			</a>
			<a class="nav-btn text-secondary" href="/favorites" title="Wish list">
				{@html icon(faHeart).html}
			</a>
			{#if $currentUser}
				<a
					class="nav-btn text-info"
					data-bs-toggle="dropdown"
					aria-expanded="false"
					href={'#'}
					title="Profile"
				>
					{@html icon(faCircleUser).html}
				</a>
				<ul class="dropdown-menu dropdown-menu-end">
					<li>
						<h2 class="dropdown-header" title={$currentUser.displayName}>
							{readMoreString($currentUser.displayName, 25)}
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
						<a class="dropdown-item" href={'#'} on:click={AccountService.logout}>
							<i class="bi bi-box-arrow-in-right"></i> Logout
						</a>
					</li>
				</ul>
			{:else}
				<a class="nav-btn text-secondary" href="/login" title="Login">
					{@html icon(faUser).html}
				</a>
			{/if}
			<a
				class="nav-btn position-relative"
				class:text-secondary={!$basket || !$basket.items.length}
				class:text-info={$basket && $basket.items.length}
				href="/basket"
				title="Basket"
			>
				{@html icon(faBasketShopping).html}
				{#if $basket && $basket.items.length}
					<span
						class="position-absolute translate-middle p-2 bg-transparent badge rounded-pill text-danger fs-5 cart-no"
					>
						{getCount($basket.items)}
					</span>
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
