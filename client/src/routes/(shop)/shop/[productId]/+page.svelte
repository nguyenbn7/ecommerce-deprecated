<script>
	import { breadcrumb } from '$lib/shares/breadcrumb.svelte';

	breadcrumb.mapPathToAlias('[productId]', 'Men clothes');
	const productName = 'Men clothes';
</script>

<svelte:head>
	<title>Ecommerce - {productName}</title>
</svelte:head>

<h3>{productName}</h3>
