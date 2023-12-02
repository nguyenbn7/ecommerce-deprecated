<script context="module">
	import { writable } from 'svelte/store';

	export function breadcrumbService() {
		const { subscribe, update } = writable({});
		return {
			subscribe,
			/**
			 * @param {string} path
			 * @param {string} alias
			 * @example
			 * routes: product/[productId]
			 * call: mapPathToAlias("[productId]", "productName")
			 * Breadcrumb: Home > Product > ProductName
			 */
			mapPathToAlias(path, alias) {
				update((curr) => ({ ...curr, [path]: alias }));
			}
		};
	}
	export const breadcrumb = breadcrumbService();
</script>

<script>
	import { page } from '$app/stores';
	import _ from 'lodash';
	export { styleClasses as class };
	let styleClasses = '';

	$: breadcrumbPaths = buildBreadcrumbPaths($page, $breadcrumb);

	/**
	 * @param {import("@sveltejs/kit").Page<Record<string, string>, string | null>} pageStore
	 * @param {{}} breadcrumbStore
	 */
	function buildBreadcrumbPaths(pageStore, breadcrumbStore) {
		const paths = pageStore.route.id?.split('/').filter((path) => path && path[0] !== '(') ?? [];
		const pathParams = pageStore.params;
		const mapper = breadcrumbStore;

		const builtPaths = [{ alias: _.capitalize('home'), href: paths.length ? '/' : null }];

		for (let idx = 0; idx < paths.length; idx++) {
			let alias = null;
			let href = null;

			// @ts-ignore
			if (paths[idx].startsWith('[')) {
				// @ts-ignore
				if (mapper && mapper[paths[idx]]) alias = titleCase(mapper[paths[idx]]);
				else alias = pathParams[paths[idx].slice(1, -1)];
			} else {
				alias = _.capitalize(paths[idx]);
			}

			if (idx < paths.length - 1) {
				const prefPath = builtPaths.slice(-1)[0].href;
				href =
					prefPath === '/'
						? `${builtPaths.slice(-1)[0].href}${paths[idx]}`
						: `${builtPaths.slice(-1)[0].href}/${paths[idx]}`;
			}
			builtPaths.push({ alias, href });
		}

		return builtPaths;
	}
</script>

<ol class="breadcrumb{styleClasses ? ` ${styleClasses}` : ''}">
	{#each breadcrumbPaths as path, idx}
		{#if !path.href && !idx}
			<li class="breadcrumb-item active" aria-current="page">
				<i class="bi bi-house-door-fill"></i>
				<span class="visually-hidden">{path.alias}</span>
			</li>
		{:else if !path.href}
			<li class="breadcrumb-item active" aria-current="page">
				{path.alias}
			</li>
		{:else if !idx}
			<li class="breadcrumb-item">
				<a class="link-body-emphasis fw-semibold text-decoration-none" href={path.href}>
					<i class="bi bi-house-door-fill"></i>
					<span class="visually-hidden">{path.alias}</span>
				</a>
			</li>
		{:else}
			<li class="breadcrumb-item">
				<a class="link-body-emphasis fw-semibold text-decoration-none" href={path.href}>
					{path.alias}
				</a>
			</li>
		{/if}
	{/each}
</ol>
