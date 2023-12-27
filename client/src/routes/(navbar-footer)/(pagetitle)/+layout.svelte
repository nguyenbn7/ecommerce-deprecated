<script>
	import { page } from '$app/stores';
	import Breadcrumb, { breadcrumbService } from '$lib/component/share/breadcrumb.svelte';

	$: breadcrumbs = breadcrumbService.buildAliasPaths($page);
</script>

<div class="container-fluid bg-secondary pb-2 mb-5 page-title">
	<div
		class="d-flex flex-column align-items-center justify-content-center"
		style="min-height: 300px"
	>
		<h1 class="fw-semibold text-uppercase mb-3">
			{breadcrumbs[breadcrumbs.length - 1].alias}
		</h1>
		<div class="d-inline-flex">
			<Breadcrumb class="ps-1 pb-3" {breadcrumbs} style="--bs-breadcrumb-divider: '>';" />
		</div>
	</div>
</div>

<slot />

<style lang="scss">
	.page-title {
		padding-top: 5.3rem !important;
	}
</style>
