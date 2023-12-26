<script>
	import '$lib/layout/(nonavbar)/about/style.scss';
	import { ECOMMERCE_NAME } from '$lib/share/constant';
	import HeroSection from '$lib/layout/(navbar)/(home)/hero-section.svelte';
	import FeatureSection from '$lib/layout/(navbar)/(home)/feature-section.svelte';
	import TestinomialSection from '$lib/layout/(navbar)/(home)/testinomial-section.svelte';
	import BrandSection from '$lib/layout/(navbar)/(home)/brand-section.svelte';
	import DealSection from '$lib/layout/(navbar)/(home)/deal-section.svelte';
	import DiscountSection from '$lib/layout/(navbar)/(home)/discount-section.svelte';
	import NewArrivalsSection from '$lib/layout/(navbar)/(home)/new-arrivals-section.svelte';
	import AboutSection from '$lib/layout/(navbar)/(home)/about-section.svelte';
</script>

<svelte:head>
	<title>{ECOMMERCE_NAME} - Home</title>
</svelte:head>

<HeroSection />

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
