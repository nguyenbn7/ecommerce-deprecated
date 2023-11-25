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
	import { ECOMMERCE_NAME } from '$lib/constants';
	import { formatAsUSD } from '$lib/helpers';
	import { breadcrumb } from '$lib/shares/breadcrumb.svelte';
	import { onMount } from 'svelte';

	/**
	 * @type {Product}
	 */
	let product;
	let productName = '';
	let buttonText = 'Add to cart';
	let quantity = 1;
	let quantityInBasket = 0;

	onMount(async () => {
		const productId = $page.params.productId;
		product = await getProduct(productId);
		productName = product.name;
		breadcrumb.mapPathToAlias('[productId]', productName);
	});

	function incrementQuantity() {
		quantity++;
	}

	function decrementQuantity() {
		if (quantity < 1) return;
		quantity--;
	}
</script>

<svelte:head>
	{#if productName}
		<title>{ECOMMERCE_NAME} - {productName}</title>
	{:else}
		<title>{ECOMMERCE_NAME}</title>
	{/if}
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
					<button
						class="p-0 m-0 me-2 border-0 quantity-btn"
						on:click={decrementQuantity}
						disabled={quantity < 1}
					>
						<i class="bi bi-dash-circle" style="font-size: 2em;"></i>
					</button>
					<span class="font-weight-bold" style="font-size: 1.5em;">{quantity}</span>
					<button class="p-0 m-0 ms-2 border-0 quantity-btn" on:click={incrementQuantity}>
						<i class="bi bi-plus-circle" style="font-size: 2em;"></i>
					</button>
					<button class="btn btn-danger ms-4">{buttonText}</button>
				</div>
				<div class="row mt-4">
					<h4>Description</h4>
					<p>{product.description}</p>
				</div>
			</div>
		</div>
	</div>
{/if}

<style lang="scss">
	.quantity-btn {
		--bs-text-opacity: 1;
		color: rgba(var(--bs-warning-rgb), var(--bs-text-opacity));
		background-color: transparent;
	}

	.quantity-btn:hover i {
		color: rgba(245, 197, 53, 0.8);
	}

	.quantity-btn:active i {
		color: rgb(185, 143, 18);
	}

	.quantity-btn:disabled i {
		color: rgb(207, 183, 109, 0.65);
		pointer-events: none;
	}
</style>
