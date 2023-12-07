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

		const builtPaths = [{ alias: _.startCase('home'), href: paths.length ? '/' : null }];

		for (let idx = 0; idx < paths.length; idx++) {
			let alias = null;
			let href = null;

			// @ts-ignore
			if (paths[idx].startsWith('[')) {
				// @ts-ignore
				if (mapper && mapper[paths[idx]]) alias = _.startCase(mapper[paths[idx]]);
				else alias = pathParams[paths[idx].slice(1, -1)];
			} else {
				alias = _.startCase(paths[idx]);
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

<ol
	class={styleClasses ? styleClasses : ''}
	style="--bs-breadcrumb-divider: '>';"
	aria-label="breadcrumb"
>
	{#each breadcrumbPaths as path, idx}
		{#if !path.href && !idx}
			<li class="breadcrumb-item active" aria-current="page">
				{path.alias}
			</li>
		{:else if !path.href}
			<li class="breadcrumb-item active" aria-current="page">
				{path.alias}
			</li>
		{:else if !idx}
			<li class="breadcrumb-item">
				<a class="link-primary fw-semibold text-decoration-none" href={path.href}>
					{path.alias}
				</a>
			</li>
		{:else}
			<li class="breadcrumb-item">
				<a class="link-primary fw-semibold text-decoration-none" href={path.href}>
					{path.alias}
				</a>
			</li>
		{/if}
	{/each}
</ol>
