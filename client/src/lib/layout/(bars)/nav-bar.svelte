<script>
	import { page } from '$app/stores';
	import { icon } from '@fortawesome/fontawesome-svg-core';
	import { faCircleUser } from '@fortawesome/free-solid-svg-icons';
	import { onMount } from 'svelte';
	import { readMoreString } from '../../share/helper';
	import { AccountService, currentUser } from '$lib/share/service/account';

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
			{#if !$currentUser}
				<a href="/login" class="btn btn-outline-success me-3">Login</a>
				<a href="/register" class="btn btn-success">Register</a>
			{:else}
				<a
					class="nav-btn text-info me-4"
					data-bs-toggle="dropdown"
					aria-expanded="false"
					href={'#'}
					title="Profile"
				>
					{@html icon(faCircleUser, {
						classes: ["fs-2"]
					}).html}
				</a>
				<ul class="dropdown-menu dropdown-menu-end me-5">
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
			{/if}
		</div>
	</div>
</nav>

<style lang="scss">
	.active-link {
		pointer-events: none;
		cursor: default;
	}
</style>
