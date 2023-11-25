<script>
	import { ECOMMERCE_NAME } from '$lib/constants';
</script>

<svelte:head>
	<title>{ECOMMERCE_NAME} - Cart</title>
</svelte:head>

<!-- <div>
        <p>There are no items in your basket</p>
    </div> -->

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
					<tr>
						<th>
							<div class="p-2 d-inline-block">
								<img src="" alt="..." class="img-fluid" style="max-height: 50px;" />
							</div>
							<div class="ms-3 d-inline-block align-middle">
								<h5 class="mb-0">
									<a href="/shop/1" class="text-dark text-decoration-none"> Product Name </a>
								</h5>
								<span class="text-muted fst-italic"> Type: Type </span>
							</div>
						</th>
						<td class="align-middle">
							<strong>$200.00</strong>
						</td>
						<td class="align-middle">
							<div class="d-flex align-items-center">
								<i
									class="bi bi-dash-circle text-warning me-2"
									style="cursor: pointer; font-size: 2em;"
								></i>
								<strong style="font-size: 1.5em;">1</strong>
								<i
									class="bi bi-plus-circle text-warning ms-2"
									style="cursor: pointer; font-size: 2em;"
								></i>
							</div>
						</td>
						<td class="align-middle">
							<strong>$500</strong>
						</td>
						<td class="align-middle">
							<a class="text-danger" href={'#'}>
								<i class="bi bi-trash" style="font-size: 2em; cursor: pointer;"></i>
							</a>
						</td>
					</tr>
				</tbody>
			</table>
		</div>
	</div>
</div>

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
