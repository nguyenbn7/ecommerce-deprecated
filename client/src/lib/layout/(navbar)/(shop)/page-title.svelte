<script>
	import { page } from '$app/stores';

	import Breadcrumb, {
		buildBreadcrumbPaths,
		breadcrumb
	} from '$lib/share/component/breadcrumb.svelte';
	$: paths = buildBreadcrumbPaths($page, $breadcrumb);
    // TODO: build paths alias from here.
</script>

<div class="container-fluid bg-secondary pb-2 mb-5" style="padding-top: 5.3rem!important;">
	<div
		class="d-flex flex-column align-items-center justify-content-center"
		style="min-height: 300px"
	>
		<h1 class="fw-semibold text-uppercase mb-3">
			{paths[paths.length - 1].alias}
		</h1>
		<div class="d-inline-flex">
			<Breadcrumb class="breadcrumb ps-1 pb-3" />
		</div>
	</div>
</div>
