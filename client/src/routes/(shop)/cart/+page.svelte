<script>
	import { ECOMMERCE_NAME } from '$lib/constants';
	import { formatAsUSD } from '$lib/helpers';
	import { getBasket } from '$lib/request/cart';
	import { onMount } from 'svelte';

	/**
	 * @type {Basket | null}
	 */
	let basket;
	onMount(async () => {
		const basketSource = await getBasket('basket1');
		basketSource.subscribe((b) => (basket = b));
	});
</script>

<svelte:head>
	<title>{ECOMMERCE_NAME} - Cart</title>
</svelte:head>

{#if !basket?.items.length}
	<div>
		<p>There are no items in your basket</p>
	</div>
{:else}
	<div class="container px-0 my-5">
		<div class="row">
			<div class="table-responsive">
				<table class="table">
					<thead class="table-light text-uppercase">
						<tr>
							<th>
								<div class="py-2">Product</div>
							</th>
							<th>
								<div class="py-2">Price</div>
							</th>
							<th>
								<div class="py-2">Quantity</div>
							</th>
							<th>
								<div class="py-2">Total</div>
							</th>
							<th>
								<div class="py-2">Remove</div>
							</th>
						</tr>
					</thead>
					<tbody>
						{#each basket.items as item}
							<tr>
								<th>
									<div class="p-2 d-inline-block">
										<img
											src={item.picture_url}
											alt={item.product_name}
											class="img-fluid"
											style="max-height: 50px;"
										/>
									</div>
									<div class="ms-3 d-inline-block align-middle">
										<h5 class="mb-0">
											<a href="/shop/{basket.id}" class="text-dark text-decoration-none">
												{item.product_name}
											</a>
										</h5>
										<span class="text-muted fst-italic"> Type: {item.type} </span>
									</div>
								</th>
								<td class="align-middle">
									<strong>{formatAsUSD(item.price)}</strong>
								</td>
								<td class="align-middle">
									<div class="d-flex align-items-center">
										<i
											class="bi bi-dash-circle text-warning me-2"
											style="cursor: pointer; font-size: 2em;"
										></i>
										<strong style="font-size: 1.5em;">{item.quantity}</strong>
										<i
											class="bi bi-plus-circle text-warning ms-2"
											style="cursor: pointer; font-size: 2em;"
										></i>
									</div>
								</td>
								<td class="align-middle">
									<strong>{formatAsUSD(item.price * item.quantity)}</strong>
								</td>
								<td class="align-middle">
									<a class="text-danger" href={'#'}>
										<i class="bi bi-trash" style="font-size: 2em; cursor: pointer;"></i>
									</a>
								</td>
							</tr>
						{/each}
					</tbody>
				</table>
			</div>
		</div>
	</div>
{/if}

<!-- <div class="row">
		<div class="col-6 offset-6">
			<app-order-totals></app-order-totals>
			<div class="d-grid">
				<a href="/checkout" class="btn btn-outline-primary py-2">
					Proceed to checkout
				</a>
			</div>
		</div>
	</div> -->
