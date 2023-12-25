<script>
	import { ECOMMERCE_NAME } from '$lib/share/constant';
	import { onMount } from 'svelte';
	import { icon } from '@fortawesome/fontawesome-svg-core';
	import {
		faCheck,
		faPhoneVolume,
		faRightLeft,
		faTruckFast
	} from '@fortawesome/free-solid-svg-icons';

	/**
	 * @type {HTMLDivElement}
	 */
	let carouselInstance;

	onMount(async () => {
		const carousel = new (await import('bootstrap')).Carousel(carouselInstance, {
			interval: 2000,
			ride: 'carousel',
			pause: false
		});
	});
</script>

<svelte:head>
	<title>{ECOMMERCE_NAME} - Home</title>
</svelte:head>

<div bind:this={carouselInstance} class="carousel slide" id="carouselExample">
	<div class="carousel-indicators">
		<button
			type="button"
			data-bs-target="#carouselExample"
			data-bs-slide-to="0"
			class="active"
			aria-current="true"
			aria-label="Slide 1"
		></button>
		<button
			type="button"
			data-bs-target="#carouselExample"
			data-bs-slide-to="1"
			aria-label="Slide 2"
		></button>
		<button
			type="button"
			data-bs-target="#carouselExample"
			data-bs-slide-to="2"
			aria-label="Slide 3"
		></button>
	</div>
	<div class="carousel-inner">
		<div class="carousel-item active">
			<img src="/images/hero1.jpg" class="m-0 min-vw-100 min-vh-100" alt="slide" />
		</div>
		<div class="carousel-item">
			<img src="/images/hero2.jpg" class="m-0 min-vw-100 min-vh-100" alt="slide" />
		</div>
		<div class="carousel-item">
			<img src="/images/hero3.jpg" class="min-vw-100 min-vh-100" alt="slide" />
		</div>
	</div>
</div>

<!-- Featured Start -->
<!-- <div class="row pb-3 mt-5">
	<div class="col-lg-3 col-md-6 col-sm-12 pb-1">
		<div class="d-flex align-items-center border mb-4" style="padding: 30px;">
			<h1 class="text-primary m-0 me-3 fs-1 fw-bolder">
				{@html icon(faCheck).html}
			</h1>
			<h5 class="fw-semibold m-0">Quality Product</h5>
		</div>
	</div>
	<div class="col-lg-3 col-md-6 col-sm-12 pb-1">
		<div class="d-flex align-items-center border mb-4" style="padding: 30px;">
			<h1 class="text-primary m-0 me-3">
				{@html icon(faTruckFast).html}
			</h1>
			<h5 class="fw-semibold m-0">Free Shipping</h5>
		</div>
	</div>
	<div class="col-lg-3 col-md-6 col-sm-12 pb-1">
		<div class="d-flex align-items-center border mb-4" style="padding: 30px;">
			<h1 class="text-primary m-0 me-3 fw-bolder">
				{@html icon(faRightLeft).html}
			</h1>
			<h5 class="fw-semibold m-0">14-Day Return</h5>
		</div>
	</div>
	<div class="col-lg-3 col-md-6 col-sm-12 pb-1">
		<div class="d-flex align-items-center border mb-4" style="padding: 30px;">
			<h1 class="text-primary m-0 me-3">
				{@html icon(faPhoneVolume).html}
			</h1>
			<h5 class="fw-semibold m-0">24/7 Support</h5>
		</div>
	</div>
</div> -->

<!-- Featured End -->

<!-- <div class="row offer pt-5">
	<div class="col-md-6 pb-4">
		<div
			class="position-relative bg-secondary-subtle text-center text-md-end text-white mb-2 py-5 px-5"
		>
			<img class="feature-img" src="/images/offer-1.png" alt="" />
			<div class="position-relative" style="z-index: 1;">
				<h5 class="text-uppercase text-primary mb-3">20% off the all order</h5>
				<h1 class="mb-4 fw-semibold">Spring Collection</h1>
				<a href="/" class="btn btn-outline-primary py-md-2 px-md-3">Shop Now</a>
			</div>
		</div>
	</div>
	<div class="col-md-6 pb-4">
		<div
			class="position-relative bg-secondary-subtle text-center text-md-start text-white mb-2 py-5 px-5"
		>
			<img class="feature-img" src="/images/offer-2.png" alt="" />
			<div class="position-relative" style="z-index: 1;">
				<h5 class="text-uppercase text-primary mb-3">20% off the all order</h5>
				<h1 class="mb-4 fw-semibold">Winter Collection</h1>
				<a href="/shop" class="btn btn-outline-primary py-md-2 px-md-3">Shop Now</a>
			</div>
		</div>
	</div>
</div> -->

<style lang="scss">
	img {
		object-fit: cover;
		height: 600px;
		width: 100%;
	}

	.offer .feature-img {
		position: absolute;
		max-width: 50%;
		max-height: 90%;
		bottom: 0;
	}

	.offer .text-md-end .feature-img {
		left: 0;
	}

	.offer .text-md-start .feature-img {
		right: 0;
	}

	.feature-img {
		object-fit: contain;
		width: 30%;
	}
</style>
