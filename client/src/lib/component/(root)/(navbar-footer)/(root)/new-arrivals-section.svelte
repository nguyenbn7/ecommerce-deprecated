<script>
	import { ProductService } from '$lib/service';
	import { onMount } from 'svelte';

	/**
	 * @type {Product[]}
	 */
	let newArrivals = [];

	onMount(async () => {
		newArrivals = [...(await ProductService.getNewArrivalProducts())];
	});
</script>

<div class="pb-5" style="background-color: #f5f5f5;">
	<div class="container">
		<div class="row">
			<div class="col-lg-8 offset-lg-2 text-center">
				<div class="section-title mt-5 mb-3">
					<h3><span class="text-warning fw-semibold">New</span> Products</h3>
					<p class="mt-1">
						Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aliquid, fuga quas itaque
						eveniet beatae optio.
					</p>
				</div>
			</div>
		</div>

		<div class="row mt-3">
			{#each newArrivals as product}
				<div class="col-lg-4 col-md-6 offset-md-3 offset-lg-0 text-center">
					<div class="single-product-item bg-white">
						<div class="product-image">
							<a href="/shop/{product.id}">
								<img
									class="img-thumbnail bg-transparent border-0"
									src={product.pictureUrl}
									alt={product.name}
								/>
							</a>
						</div>
						<h3>{product.name}</h3>
						<p class="product-price">{product.price}</p>
						<a href={'#'} class="btn btn-danger">
							<i class="fa-solid fa-basket-shopping me-1"></i> Add to Basket
						</a>
					</div>
				</div>
			{/each}
		</div>
	</div>
</div>

<style lang="scss">
	.single-product-item {
		margin-bottom: 30px;
	}

	.single-product-item h3 {
		font-size: 20px;
		font-weight: 600;
		margin-bottom: 10px;
	}

	.single-product-item {
		-webkit-transition: 0.3s;
		-o-transition: 0.3s;
		transition: 0.3s;
	}

	.single-product-item:hover {
		-webkit-box-shadow: 0 0 20px #7e6767;
		box-shadow: 0 0 20px #7e6767;
	}

	.single-product-item {
		padding-bottom: 50px;
		border-radius: 5px;
	}

	a.btn {
		font-family: 'Poppins', sans-serif;
	}

	.product-image img {
		-webkit-transition: 0.3s;
		-o-transition: 0.3s;
		transition: 0.3s;
	}

	.product-image img:hover {
		-webkit-box-shadow: none;
		box-shadow: none;
	}
</style>
