<script>
	const features = [
		{
			icon: '<i class="fa-solid fa-check"></i>',
			name: 'Quality Product',
			description: 'Product with long lifespan'
		},
		{
			icon: '<i class="fa-solid fa-truck-fast"></i>',
			name: 'Free Shipping',
			description: 'When order over $100'
		},
		{
			icon: '<i class="fa-solid fa-rotate"></i>',
			name: '7-Day Return',
			description: 'Get refund within 3 days!'
		},
		{
			icon: '<i class="fa-solid fa-phone-volume"></i>',
			name: '24/7 Support',
			description: 'Get support all day'
		}
	];
</script>

<section class="bg-light">
	<div class="container">
		<div class="row py-5">
			{#each features as feature}
				<div class="col-lg-3 col-md-6 col-sm-12">
					<div class="d-flex align-items-center" style="padding: 30px;">
						<h1 class="text-warning fs-1 fw-bolder me-3">
							{@html feature.icon}
						</h1>
						<span>
							<h5 class="fw-semibold m-0 mb-1">{feature.name}</h5>
							<p class="text-muted fw-light">{feature.description}</p>
						</span>
					</div>
				</div>
			{/each}
		</div>
	</div>
</section>
