<script>
	import { ECOMMERCE_NAME } from '$lib/share/constant';
	import Address, { AddressForm } from '$lib/order/address.svelte';
	import OrderSummary from '$lib/order/order-summary.svelte';
	import OrderHttpClient from '$lib/order/request';
	import { onMount } from 'svelte';
	import { startCase, toLower } from 'lodash';

	let hasSameAddress = true;

	/**
	 * @type {string[]}
	 */
	let paymentTypes = [];

	onMount(async () => {
		paymentTypes = [...(await OrderHttpClient.getPaymentTypes())];
	});

	const billingAddress = new AddressForm();

	const shippingAddress = new AddressForm();

	function onSubmitForm() {}
</script>

<svelte:head>
	<title>{ECOMMERCE_NAME} - Checkout</title>
</svelte:head>

<div class="container" style="margin-bottom: 7%;">
	<main>
		<div class="py-5 text-center">
			<a href="/">
				<img class="d-block mx-auto mb-4" src="/images/logo.png" alt="" width="250" height="100" />
			</a>
			<h2>Checkout</h2>
		</div>

		<div class="row g-5">
			<div class="col-md-5 col-lg-4 order-md-last">
				<OrderSummary></OrderSummary>
			</div>
			<div class="col-md-7 col-lg-8">
				<form on:submit={onSubmitForm}>
					<div class="card">
						<div class="card-header">
							<h4 class="mb-0">Billing address</h4>
						</div>
						<div class="card-body px-4 pb-4">
							<div class="row g-3">
								<Address addressForm={billingAddress}></Address>

								<div class="form-check mt-4 ms-2">
									<input
										type="checkbox"
										class="form-check-input"
										id="same-address"
										bind:checked={hasSameAddress}
									/>
									<label class="form-check-label" for="same-address">
										Shipping address is the same as my billing address
									</label>
								</div>
							</div>
						</div>
					</div>

					{#if !hasSameAddress}
						<div class="card my-5">
							<div class="card-header">
								<h4 class="mb-0">Shipping address</h4>
							</div>
							<div class="card-body px-4 pb-4">
								<div class="row g-3">
									<Address addressForm={shippingAddress}></Address>
								</div>
							</div>
						</div>
					{/if}

					<div class="card my-5">
						<div class="card-header">
							<h4 class="mb-0">Payment</h4>
						</div>
						<div class="card-body px-4 pb-4">
							<div class="my-3">
								{#each paymentTypes as type}
									<div class="form-check">
										<input type="radio" class="form-check-input" id={type} />
										<label class="form-check-label" for={type}>
											{startCase(toLower(type.split('_').join(' ')))}
										</label>
									</div>
								{/each}
							</div>

							<div class="row gy-3">
								<div class="col-md-6">
									<label for="cc-name" class="form-label">Name on card</label>
									<input type="text" class="form-control" id="cc-name" placeholder="" />
									<small class="text-body-secondary">Full name as displayed on card</small>
									<div class="invalid-feedback">Name on card is required</div>
								</div>

								<div class="col-md-6">
									<label for="cc-number" class="form-label">Credit card number</label>
									<input type="text" class="form-control" id="cc-number" placeholder="" />
									<div class="invalid-feedback">Credit card number is required</div>
								</div>

								<div class="col-md-3">
									<label for="cc-expiration" class="form-label">Expiration</label>
									<input type="text" class="form-control" id="cc-expiration" placeholder="" />
									<div class="invalid-feedback">Expiration date required</div>
								</div>

								<div class="col-md-3">
									<label for="cc-cvv" class="form-label">CVV</label>
									<input type="text" class="form-control" id="cc-cvv" placeholder="" />
									<div class="invalid-feedback">Security code required</div>
								</div>
							</div>
						</div>
					</div>

					<button class="w-100 btn btn-primary btn-lg" type="submit">Continue to checkout</button>
				</form>
			</div>
		</div>
	</main>
</div>
