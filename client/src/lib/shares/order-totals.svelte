<script>
	import { basketTotalsSource } from '$lib/basket';
	import { formatAsUSD } from '$lib/helpers';

	$: totals = $basketTotalsSource;
</script>

<div class="bg-light px-4 py-3 text-uppercase fw-bold">Order Summary</div>

<div class="p-4">
	<p class="fst-italic mb-4">
		Shipping costs will be calculated based on choices made during checkout
	</p>
	{#if totals}
		<ul class="list-unstyled mb-4">
			<li class="d-flex justify-content-between py-3 border-bottom">
				<strong class="text-muted">Order Subtotal</strong>
				<strong>{formatAsUSD(totals.subtotal)}</strong>
			</li>
			<li class="d-flex justify-content-between py-3 border-bottom">
				<strong class="text-muted">Shipping and Handling</strong>
				<strong>{formatAsUSD(totals.shipping)}</strong>
			</li>
			<li class="d-flex justify-content-between py-3 border-bottom">
				<strong class="text-muted">Total</strong>
				<strong>{formatAsUSD(totals.total)}</strong>
			</li>
		</ul>
	{/if}
</div>
