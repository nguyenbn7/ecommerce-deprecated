<script>
	import { APP_NAME } from '$lib/share/constant';
	import AboutSection from '$lib/component/(root)/(navbar-footer)/(root)/about-section.svelte';
	import DealSection from '$lib/component/(root)/(navbar-footer)/(root)/deal-section.svelte';
	import NewArrivalsSection from '$lib/component/(root)/(navbar-footer)/(root)/new-arrivals-section.svelte';
	import TestinomialSection from '$lib/component/(root)/(navbar-footer)/(root)/testinomial-section.svelte';
	import { onMount } from 'svelte';
	import Section from '$lib/component/share/section.svelte';
	import { tns } from 'tiny-slider';

	/**
	 * @type {HTMLElement}
	 */
	let heroCarousel;
	let active = 0;

	const heroSectionId = 'heroSection';
	const heroImages = ['hero1.jpg', 'hero2.jpg', 'hero3.jpg'];
	const captions = [
		{ subtitle: 'Mega Sale Going On!', heading: 'Get December Discount' },
		{ subtitle: 'Top quality board', heading: '10% off your first order' },
		{ subtitle: 'Unique style', heading: 'Fashionable and Reasonable Price' }
	];

	const features = [
		{
			iconClass: 'fa-solid fa-check',
			name: 'Quality Product',
			description: 'Product with long lifespan'
		},
		{
			iconClass: 'fa-solid fa-truck-fast',
			name: 'Free Shipping',
			description: 'When order over $100'
		},
		{
			iconClass: 'fa-solid fa-rotate',
			name: '7-Day Return',
			description: 'Get refund within 3 days!'
		},
		{
			iconClass: 'fa-solid fa-phone-volume',
			name: '24/7 Support',
			description: 'Get support all day'
		}
	];

	const logoImages = ['angular.png', 'netcore.png', 'react.png', 'redis.png', 'typescript.png'];

	onMount(async () => {
		new (await import('bootstrap')).Carousel(heroCarousel, {
			ride: 'carousel',
			pause: false
		});

		heroCarousel.addEventListener('slid.bs.carousel', (event) => {
			// @ts-ignore
			active = event.to;
		});

		tns({
			container: '.logo-slider',
			items: 1,
			autoplay: true,
			animateDelay: 3,
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

<svelte:head>
	<title>{APP_NAME} - Home</title>
</svelte:head>

<section class="carousel slide" id={heroSectionId} bind:this={heroCarousel}>
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
				<div
					class="carousel-caption h-100 d-flex justify-content-center align-items-center hero-text"
				>
					<div>
						<p
							class="subtitle"
							class:animate__animated={idx === active}
							class:animate__fadeInUp={idx === active}
							class:animated={idx === active}
						>
							{captions[idx].subtitle}
						</p>
						<h1
							class:animate__animated={idx === active}
							class:animate__fadeInUp={idx === active}
							class:animated={idx === active}
							class:animation-duration-300ms={idx === active}
						>
							{captions[idx].heading}
						</h1>
						<div
							class="hero-btns"
							class:animate__animated={idx === active}
							class:animate__fadeInUp={idx === active}
							class:animated={idx === active}
							class:animation-duration-500ms={idx === active}
						>
							<a href="/shop" class="btn btn-warning boxed-btn">Visit Shop</a>
							<a href="/contact" class="btn btn-outline-warning bordered-btn">Contact Us</a>
						</div>
					</div>
				</div>
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
</section>

<section class="features-section">
	<div class="container">
		<div class="row py-5">
			{#each features as feature}
				<div class="col-lg-3 col-md-6 col-sm-12">
					<div class="d-flex align-items-center" style="padding: 30px;">
						<h1 class="text-warning fs-1 fw-bolder me-3">
							<i class={feature.iconClass}></i>
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

<DealSection />

<section class="discount-section">
	<div class="container">
		<h3>December sale is on! <br /> with big <span class="text-warning">Discount...</span></h3>
		<div class="sale-percent"><span>Sale! <br /> Upto</span>50% <span>off</span></div>
		<a href="/shop" class="btn btn-danger">Shop Now</a>
	</div>
</section>

<!-- New Arrivals -->
<NewArrivalsSection />

<AboutSection />

<TestinomialSection />

<!-- News -->
<!-- <div class="latest-news pt-150 pb-150">
	<div class="container">
		<div class="row">
			<div class="col-lg-8 offset-lg-2 text-center">
				<div class="section-title">
					<h3><span class="orange-text">Our</span> News</h3>
					<p>
						Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aliquid, fuga quas itaque
						eveniet beatae optio.
					</p>
				</div>
			</div>
		</div>

		<div class="row">
			<div class="col-lg-4 col-md-6">
				<div class="single-latest-news">
					<a href="single-news.html"><div class="latest-news-bg news-bg-1"></div></a>
					<div class="news-text-box">
						<h3><a href="single-news.html">You will vainly look for fruit on it in autumn.</a></h3>
						<p class="blog-meta">
							<span class="author"><i class="fas fa-user"></i> Admin</span>
							<span class="date"><i class="fas fa-calendar"></i> 27 December, 2019</span>
						</p>
						<p class="excerpt">
							Vivamus lacus enim, pulvinar vel nulla sed, scelerisque rhoncus nisi. Praesent vitae
							mattis nunc, egestas viverra eros.
						</p>
						<a href="single-news.html" class="read-more-btn"
							>read more <i class="fas fa-angle-right"></i></a
						>
					</div>
				</div>
			</div>
			<div class="col-lg-4 col-md-6">
				<div class="single-latest-news">
					<a href="single-news.html"><div class="latest-news-bg news-bg-2"></div></a>
					<div class="news-text-box">
						<h3><a href="single-news.html">A man's worth has its season, like tomato.</a></h3>
						<p class="blog-meta">
							<span class="author"><i class="fas fa-user"></i> Admin</span>
							<span class="date"><i class="fas fa-calendar"></i> 27 December, 2019</span>
						</p>
						<p class="excerpt">
							Vivamus lacus enim, pulvinar vel nulla sed, scelerisque rhoncus nisi. Praesent vitae
							mattis nunc, egestas viverra eros.
						</p>
						<a href="single-news.html" class="read-more-btn"
							>read more <i class="fas fa-angle-right"></i></a
						>
					</div>
				</div>
			</div>
			<div class="col-lg-4 col-md-6 offset-md-3 offset-lg-0">
				<div class="single-latest-news">
					<a href="single-news.html"><div class="latest-news-bg news-bg-3"></div></a>
					<div class="news-text-box">
						<h3><a href="single-news.html">Good thoughts bear good fresh juicy fruit.</a></h3>
						<p class="blog-meta">
							<span class="author"><i class="fas fa-user"></i> Admin</span>
							<span class="date"><i class="fas fa-calendar"></i> 27 December, 2019</span>
						</p>
						<p class="excerpt">
							Vivamus lacus enim, pulvinar vel nulla sed, scelerisque rhoncus nisi. Praesent vitae
							mattis nunc, egestas viverra eros.
						</p>
						<a href="single-news.html" class="read-more-btn"
							>read more <i class="fas fa-angle-right"></i></a
						>
					</div>
				</div>
			</div>
		</div>
		<div class="row">
			<div class="col-lg-12 text-center">
				<a href="news.html" class="boxed-btn">More News</a>
			</div>
		</div>
	</div>
</div> -->

<section class="brand-section">
	<Section containerClass="overflow-x-hidden">
		<div class="row align-items-center justify-content-center logo-slider mt-5">
			{#each logoImages as image}
				<div class="single-logo-item col-xl-3 col-sm-6 text-center position-relative">
					<img src="/images/home/company-logo/{image}" alt={image} />
				</div>
			{/each}
		</div>
	</Section>
</section>

<style lang="scss">
	// Hero section
	.hero-img {
		object-fit: cover;
		height: 600px;
		width: 100%;
		filter: brightness(55%);
	}

	.hero-text p.subtitle {
		color: #f28123;
		font-weight: 700;
		text-transform: uppercase;
		letter-spacing: 0.5rem;
		font-size: 1.25rem;
	}

	.hero-text h1 {
		font-size: 64px;
		font-weight: 700;
		line-height: 1.3;
		color: #fff;
	}

	.hero-btns {
		margin-top: 35px;
	}

	.hero-btns a.bordered-btn {
		margin-left: 15px;
	}

	a.boxed-btn {
		font-family: 'Poppins', sans-serif;
		display: inline-block;
		padding: 10px 20px;
		text-decoration: none;
	}

	a.bordered-btn {
		font-family: 'Poppins', sans-serif;
		display: inline-block;
		padding: 10px 20px;
		text-decoration: none;
	}

	a.boxed-btn,
	a.bordered-btn {
		border-radius: 50px;
	}

	.animation-duration-300ms {
		animation-delay: 0.3s !important;
	}

	.animation-duration-500ms {
		animation-delay: 0.3s !important;
	}

	.animated {
		-webkit-animation-duration: 1s !important;
		animation-duration: 1s !important;
	}

	.features-section {
		background-color: #f5f5f5;
	}

	.discount-section {
		position: relative;
		background-size: cover;
		padding: 110px 0px 115px;
		background-image: url(/images/home/discount/1.jpg);

		& h3 {
			position: relative;
			font-size: 50px;
			line-height: 1.2em;
			margin-bottom: 0px;
		}

		& .sale-percent {
			position: relative;
			font-size: 60px;
			font-weight: 700;
			color: #f28123;

			& span {
				position: relative;
				font-size: 24px;
				line-height: 1.1em;
				color: #051922;
				font-weight: 400;
				text-align: center;
				margin-right: 10px;
				display: inline-block;
			}
		}
	}

	.brand-section {
		.single-logo-item {
			-webkit-transition: 0.3s;
			-o-transition: 0.3s;
			transition: 0.3s;

			& img {
				max-width: 180px;
				max-height: 180px;
				margin: 0 auto;
			}

			&:hover {
				opacity: 0.7;
			}
		}
	}
</style>
