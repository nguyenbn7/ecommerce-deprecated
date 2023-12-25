<script>
	import { ECOMMERCE_NAME } from '$lib/share/constant';
	import { onMount } from 'svelte';
	import { icon } from '@fortawesome/fontawesome-svg-core';
	import { faCheck, faPhoneVolume, faSync, faTruckFast } from '@fortawesome/free-solid-svg-icons';
	import { tns } from 'tiny-slider';
	import '$lib/layout/(nobars)/about/style.scss';

	const heroSectionId = 'heroSection';

	onMount(async () => {
		new (await import('bootstrap')).Carousel(document.getElementById(heroSectionId), {
			interval: 2000,
			ride: 'carousel',
			pause: false
		});

		tns({
			items: 1,
			slideBy: 'page',
			autoplay: true,
			speed: 400,
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

	const features = [
		{ icon: faCheck, name: 'Quality Product' },
		{ icon: faTruckFast, name: 'Free Shipping' },
		{ icon: faSync, name: '7-Day Return' },
		{ icon: faPhoneVolume, name: '24/7 Support' }
	];

	const heroImages = ['hero1.jpg', 'hero2.jpg', 'hero3.jpg'];

	const logoImages = ['angular.png', 'netcore.png', 'react.png', 'redis.png', 'typescript.png'];
</script>

<svelte:head>
	<title>{ECOMMERCE_NAME} - Home</title>
</svelte:head>

<div class="carousel slide" id={heroSectionId}>
	<div class="carousel-indicators">
		{#each heroImages as _, idx}
			<button
				type="button"
				data-bs-target="#{heroSectionId}"
				data-bs-slide-to={idx}
				class:active={idx === 0}
				aria-current="true"
				aria-label="Slide {idx + 1}"
			></button>
		{/each}
	</div>
	<div class="carousel-inner">
		{#each heroImages as image, idx}
			<div class="carousel-item" class:active={idx === 0}>
				<img src="/images/{image}" class="m-0 min-vw-100 min-vh-100 hero-img" alt="slide" />
			</div>
		{/each}
	</div>
	<button
		class="carousel-control-prev"
		type="button"
		data-bs-target="#{heroSectionId}"
		data-bs-slide="prev"
	>
		<span class="carousel-control-prev-icon" aria-hidden="true"></span>
		<span class="visually-hidden">Previous</span>
	</button>
	<button
		class="carousel-control-next"
		type="button"
		data-bs-target="#{heroSectionId}"
		data-bs-slide="next"
	>
		<span class="carousel-control-next-icon" aria-hidden="true"></span>
		<span class="visually-hidden">Next</span>
	</button>
</div>

<!-- Featured Start -->
<div class="bg-light">
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
</div>

<!-- Featured End -->

<!-- Logo Start -->
<div class="container py-5 overflow-x-hidden">
	<h2 class="display-5 fw-light text-center">
		Popular Brands
		<div
			class="border-bottom mb-5 mt-2 border-4 border-warning mx-auto"
			style="width: 1.7em;"
		></div>
	</h2>
	<div class="row align-items-center justify-content-center slider">
		{#each logoImages as image}
			<div class="single-logo-item col-xl-3 col-sm-6 text-center position-relative">
				<img src="/images/home/company-logos/{image}" alt="" />
			</div>
		{/each}
	</div>
</div>

<!-- Logo End -->

<style lang="scss">
	.hero-img {
		object-fit: cover;
		height: 600px;
		width: 100%;
	}

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
