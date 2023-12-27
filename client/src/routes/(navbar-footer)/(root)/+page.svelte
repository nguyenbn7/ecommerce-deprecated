<script>
	import { APP_NAME } from '$lib/constant';
	import AboutSection from '$lib/component/(root)/(navbar-footer)/(root)/about-section.svelte';
	import FeatureSection from '$lib/component/(root)/(navbar-footer)/(root)/feature-section.svelte';
	import DealSection from '$lib/component/(root)/(navbar-footer)/(root)/deal-section.svelte';
	import DiscountSection from '$lib/component/(root)/(navbar-footer)/(root)/discount-section.svelte';
	import NewArrivalsSection from '$lib/component/(root)/(navbar-footer)/(root)/new-arrivals-section.svelte';
	import TestinomialSection from '$lib/component/(root)/(navbar-footer)/(root)/testinomial-section.svelte';
	import BrandSection from '$lib/component/(root)/(navbar-footer)/(root)/brand-section.svelte';
	import { onMount } from 'svelte';

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

	onMount(async () => {
		new (await import('bootstrap')).Carousel(heroCarousel, {
			ride: 'carousel',
			pause: false
		});

		heroCarousel.addEventListener('slid.bs.carousel', (event) => {
			// @ts-ignore
			active = event.to;
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

<FeatureSection />

<DealSection />

<DiscountSection />

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

<BrandSection />

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
</style>
