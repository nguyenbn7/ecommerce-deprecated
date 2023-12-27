<script>
	import { icon } from '@fortawesome/fontawesome-svg-core';
	import { faCheck, faPhoneVolume, faSync, faTruckFast } from '@fortawesome/free-solid-svg-icons';

	const features = [
		{ icon: faCheck, name: 'Quality Product', description: 'Product with long lifespan' },
		{ icon: faTruckFast, name: 'Free Shipping', description: 'When order over $100' },
		{ icon: faSync, name: '7-Day Return', description: 'Get refund within 3 days!' },
		{ icon: faPhoneVolume, name: '24/7 Support', description: 'Get support all day' }
	];
</script>

<section class="bg-light">
	<div class="container">
		<div class="row py-5">
			{#each features as feature}
				<div class="col-lg-3 col-md-6 col-sm-12">
					<div class="d-flex align-items-center" style="padding: 30px;">
						<h1 class="text-warning fs-1 fw-bolder me-3">
							{@html icon(feature.icon).html}
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
