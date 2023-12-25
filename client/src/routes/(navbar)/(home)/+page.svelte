<script>
	import { ECOMMERCE_NAME } from '$lib/share/constant';
	import { onMount } from 'svelte';
	import { icon } from '@fortawesome/fontawesome-svg-core';
	import {
		faCheck,
		faPhoneVolume,
		faQuoteLeft,
		faQuoteRight,
		faSync,
		faTruckFast
	} from '@fortawesome/free-solid-svg-icons';
	import { tns } from 'tiny-slider';
	import '$lib/layout/(nobars)/about/style.scss';

	const heroSectionId = 'heroSection';

	const features = [
		{ icon: faCheck, name: 'Quality Product' },
		{ icon: faTruckFast, name: 'Free Shipping' },
		{ icon: faSync, name: '7-Day Return' },
		{ icon: faPhoneVolume, name: '24/7 Support' }
	];

	const heroImages = ['hero1.jpg', 'hero2.jpg', 'hero3.jpg'];

	const logoImages = ['angular.png', 'netcore.png', 'react.png', 'redis.png', 'typescript.png'];

	const clients = [
		{
			name: 'Saira Hakim',
			profileImage: 'avatar1.png',
			companyName: 'Local shop owner',
			quote:
				'Sed ut perspiciatis unde omnis iste natus error veritatis et quasi architecto beatae vitae dict eaque ipsa quae ab illo inventore Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium'
		},
		{
			name: 'David Niph',
			profileImage: 'avatar2.png',
			companyName: 'Local shop owner',
			quote:
				'Sed ut perspiciatis unde omnis iste natus error veritatis et quasi architecto beatae vitae dict eaque ipsa quae ab illo inventore Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium'
		},
		{
			name: 'Jacob Sikim',
			profileImage: 'avatar3.png',
			companyName: 'Local shop owner',
			quote:
				'Sed ut perspiciatis unde omnis iste natus error veritatis et quasi architecto beatae vitae dict eaque ipsa quae ab illo inventore Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium'
		}
	];

	onMount(async () => {
		new (await import('bootstrap')).Carousel(document.getElementById(heroSectionId), {
			interval: 2000,
			ride: 'carousel',
			pause: false
		});

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

		tns({
			container: '.testimonial-slider',
			items: 1,
			autoplay: true,
			speed: 1500,
			autoplayButtonOutput: false,
			controls: false
		});
	});
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
				<img
					src="/images/home/hero/{image}"
					class="m-0 min-vw-100 min-vh-100 hero-img"
					alt="slide"
				/>
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

<!-- Deals -->

<!-- Discount -->

<!-- New Arrivals -->
<!-- <div class="container">New Arrivals</div> -->

<!-- We are -->

<!-- Testimonials -->
<div class="py-5 my-5">
	<div class="container overflow-x-hidden">
		<h2 class="display-5 fw-light text-center">
			What Customers Said
			<div
				class="border-bottom mb-5 mt-2 border-4 border-warning mx-auto"
				style="width: 1.7em;"
			></div>
		</h2>
		<div class="row align-items-center justify-content-center testimonial-slider mt-5">
			{#each clients as client}
				<div class="col-xl-3 col-sm-6 text-center">
					<div class="client-avatar">
						<img src="/images/home/testimonial/{client.profileImage}" alt={client.name} />
					</div>
					<div class="client-meta">
						<h3>{client.name} <span>{client.companyName}</span></h3>
						<p class="testimonial-body">
							"{client.quote}"
						</p>
						<span class="quote-icon">
							{@html icon(faQuoteRight).html}
						</span>
					</div>
				</div>
			{/each}
		</div>
	</div>
</div>
<!-- News -->

<!-- Logo Start -->
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
					<img src="/images/home/company-logo/{image}" alt="" />
				</div>
			{/each}
		</div>
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

	/**
	* Clients
	*/
	.client-avatar {
		margin-bottom: 20px;
	}

	.client-meta h3 {
		font-size: 20px;
		font-weight: 600;
	}

	.client-meta h3 span {
		display: block;
		font-size: 70%;
		margin-top: 10px;
		color: #051922;
		font-weight: 600;
		opacity: 0.5;
	}

	p.testimonial-body {
		font-size: 17px;
		font-style: italic;
		width: 700px;
		margin: 0 auto;
		line-height: 1.8;
		color: #999999;
		margin-top: 20px;
	}

	.quote-icon {
		margin-top: 20px;
		font-size: 25px;
		opacity: 0.3;
	}

	.client-avatar img {
		max-width: 100px;
		border-radius: 50%;
		margin: 0 auto;
	}
</style>
