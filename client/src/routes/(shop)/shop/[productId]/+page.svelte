<script context="module">
	/**
	 * @param {string} productId
	 * @returns {Promise<Product>}
	 */
	async function getProduct(productId) {
		const response = await fetch(`${PUBLIC_BASE_API_URL}/products/${productId}`);
		return await response.json();
	}
</script>

<script>
	import { page } from '$app/stores';
	import { PUBLIC_BASE_API_URL } from '$env/static/public';
	import { formatAsUSD } from '$lib/helpers';
	import { breadcrumb } from '$lib/shares/breadcrumb.svelte';
	import { onMount } from 'svelte';

	/**
	 * @type {Product}
	 */
	export let product;
	let productName = '';
	let buttonText = 'Add to cart';
	let quantity = 1;
	let quantityInBasket = 0;

	breadcrumb.mapPathToAlias('[productId]', '');

	onMount(async () => {
		const productId = $page.params.productId;
		product = await getProduct(productId);
		breadcrumb.mapPathToAlias('[productId]', product.name);
		productName = product.name;
	});
</script>

<svelte:head>
	<title>Ecommerce - {productName}</title>
</svelte:head>

{#if product}
	<div class="container">
		<div class="row">
			<div class="col-6">
				<img src={product.picture_url} alt={product.name} class="w-100" />
			</div>
			<div class="col-6 mt-5">
				<h2>{product.name}</h2>
				<p>{formatAsUSD(product.price)}</p>

				<h5 class="text-primary mb-3">
					You have {quantityInBasket} of this item in your basket
				</h5>

				<div class="d-flex justify-content-start align-items-center">
					<i class="bi bi-dash-circle text-warning me-2" style="cursor: pointer; font-size: 2em;">
					</i>
					<span class="font-weight-bold" style="font-size: 1.5em;">{1}</span>
					<i class="bi bi-plus-circle text-warning ms-2" style="cursor: pointer; font-size: 2em;"
					></i>
					<button class="btn btn-danger ms-4">{'Add to cart'}</button>
				</div>
				<div class="row mt-4">
					<h4>Description</h4>
					<p>{product.description}</p>
				</div>
			</div>
		</div>
	</div>
{/if}
