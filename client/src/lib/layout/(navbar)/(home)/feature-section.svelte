<script>
	import { icon } from '@fortawesome/fontawesome-svg-core';
	import { faCheck, faPhoneVolume, faSync, faTruckFast } from '@fortawesome/free-solid-svg-icons';

	const features = [
		{ icon: faCheck, name: 'Quality Product' },
		{ icon: faTruckFast, name: 'Free Shipping' },
		{ icon: faSync, name: '7-Day Return' },
		{ icon: faPhoneVolume, name: '24/7 Support' }
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
						<h5 class="fw-semibold m-0">{feature.name}</h5>
					</div>
				</div>
			{/each}
		</div>
	</div>
</section>
