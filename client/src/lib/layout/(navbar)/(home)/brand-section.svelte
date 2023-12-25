<script>
	import { onMount } from 'svelte';
	import { tns } from 'tiny-slider';

	const logoImages = ['angular.png', 'netcore.png', 'react.png', 'redis.png', 'typescript.png'];

	onMount(async () => {
		tns({
			container: '.logo-slider',
			items: 1,
			autoplay: true,
			speed: 1000,
			autoplayButtonOutput: false,
			controls: false,
			responsive: {
				768: {
					items: 3
				},
				576: {
					items: 2
				},
				992: {
					items: 4
				}
			}
		});
	});
</script>

<div class="py-5 my-5">
	<div class="container overflow-x-hidden">
		<h2 class="display-5 fw-light text-center">
			Top Brands
			<div
				class="border-bottom mb-5 mt-2 border-4 border-warning mx-auto"
				style="width: 1.7em;"
			></div>
		</h2>
		<div class="row align-items-center justify-content-center logo-slider mt-5">
			{#each logoImages as image}
				<div class="single-logo-item col-xl-3 col-sm-6 text-center position-relative">
					<img src="/images/home/company-logo/{image}" alt={image} />
				</div>
			{/each}
		</div>
	</div>
</div>

<style lang="scss">
	.single-logo-item img {
		max-width: 180px;
		max-height: 180px;
		margin: 0 auto;
	}

	.single-logo-item {
		-webkit-transition: 0.3s;
		-o-transition: 0.3s;
		transition: 0.3s;
	}

	.single-logo-item:hover {
		opacity: 0.7;
	}
</style>
