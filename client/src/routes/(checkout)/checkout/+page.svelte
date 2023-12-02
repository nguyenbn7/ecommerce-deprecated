<script>
	import { basket, basketTotals } from '$lib/service/basket.service';
	import { ECOMMERCE_NAME } from '$lib/share/constant';
	import { currency } from '$lib/share/functions';
	import { InputField } from '$lib/share/model';
	import InputForm from '$lib/order/input-form.svelte';

	const billingAddress = {
		fullName: new InputField([]),
		email: new InputField([]),
		address: new InputField([]),
		address2: new InputField([])
	};
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
				<h4 class="d-flex justify-content-between align-items-center mb-3">
					<span class="text-primary">Order Summary</span>
					<a href="/basket" class="fs-5">Edit</a>
				</h4>
				<ul class="list-group mb-3">
					{#if $basket}
						{#each $basket.items as item}
							<li class="list-group-item d-flex justify-content-between align-items-center lh-sm">
								<div class="row align-items-center">
									<div class="col-3 p-1 position-relative">
										<img src={item.picture_url} class="img-thumbnail" alt={item.product_name} />
										<span
											class="position-absolute top-0 start-100 translate-middle badge rounded-pill bg-secondary"
										>
											{item.quantity}
										</span>
									</div>
									<div class="col-8 ms-1">
										<h5 class="my-0">{item.product_name}</h5>
									</div>
								</div>
								<span class="text-body-secondary">{currency(item.price * item.quantity)}</span>
							</li>
						{/each}
					{/if}
					<!-- <li class="list-group-item d-flex justify-content-between bg-body-tertiary">
						<div class="text-success">
							<h6 class="my-0">Promo code</h6>
							<small>EXAMPLECODE</small>
						</div>
						<span class="text-success">−$5</span>
					</li> -->
					<li class="list-group-item d-flex justify-content-between">
						<span>Total (USD)</span>
						<strong>{currency($basketTotals?.total ?? 0)}</strong>
					</li>
				</ul>

				<!-- <form class="card p-2">
					<div class="input-group">
						<input type="text" class="form-control" placeholder="Promo code" />
						<button type="submit" class="btn btn-secondary">Redeem</button>
					</div>
				</form> -->
			</div>
			<div class="col-md-7 col-lg-8">
				<h4 class="mb-3">Billing address</h4>
				<form class="needs-validation">
					<div class="row g-3">
						<div class="col-12">
							<InputForm
								class="form-control"
								inputField={billingAddress.fullName}
								id="fullName"
								placeholder="Example: John Doe"
								label="Full Name"
							></InputForm>
							<!-- <label for="firstName" class="form-label"></label>
							<input
								type="text"
								class="form-control"
								id="firstName"
								placeholder=""
								value=""
								required=""
							/>
							<div class="invalid-feedback">Valid first name is required.</div> -->
						</div>

						<div class="col-12">
							<InputForm
								inputField={billingAddress.email}
								placeholder="johndoe@gmail.com"
								type="email"
								label="Email"
								class="form-control"
								id="email"
							></InputForm>
						</div>

						<div class="col-12">
							<InputForm
								inputField={billingAddress.address}
								placeholder="1234 Main St"
								label="Address"
								class="form-control"
								id="address"
							></InputForm>
						</div>

						<div class="col-12">
							<InputForm
								inputField={billingAddress.address2}
								placeholder="Apartment or suite"
								label="Address 2 <span class="text-body-secondary">(Optional)</span>"
								class="form-control"
								id="address2"
							></InputForm>
						</div>

						<div class="col-md-5">
							<label for="country" class="form-label">Country</label>
							<select class="form-select" id="country">
								<option value="">Choose...</option>
								<option>United States</option>
							</select>
							<div class="invalid-feedback">Please select a valid country.</div>
						</div>

						<div class="col-md-4">
							<label for="state" class="form-label">State</label>
							<select class="form-select" id="state" required="">
								<option value="">Choose...</option>
								<option>California</option>
							</select>
							<div class="invalid-feedback">Please provide a valid state.</div>
						</div>

						<div class="col-md-3">
							<label for="zip" class="form-label">Zip</label>
							<input type="text" class="form-control" id="zip" placeholder="" required="" />
							<div class="invalid-feedback">Zip code required.</div>
						</div>
					</div>

					<hr class="my-4" />

					<div class="form-check">
						<input type="checkbox" class="form-check-input" id="same-address" checked />
						<label class="form-check-label" for="same-address">
							Shipping address is the same as my billing address
						</label>
					</div>

					<hr class="my-4" />

					<h4 class="mb-3">Payment</h4>

					<div class="my-3">
						<div class="form-check">
							<input id="credit" name="paymentMethod" type="radio" class="form-check-input" />
							<label class="form-check-label" for="credit">Credit card</label>
						</div>
						<div class="form-check">
							<input
								id="debit"
								name="paymentMethod"
								type="radio"
								class="form-check-input"
								required=""
							/>
							<label class="form-check-label" for="debit">Debit card</label>
						</div>
						<div class="form-check">
							<input id="paypal" name="paymentMethod" type="radio" class="form-check-input" />
							<label class="form-check-label" for="paypal">Cash</label>
						</div>
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

					<hr class="my-4" />

					<button class="w-100 btn btn-primary btn-lg" type="submit">Continue to checkout</button>
				</form>
			</div>
		</div>
	</main>
</div>
