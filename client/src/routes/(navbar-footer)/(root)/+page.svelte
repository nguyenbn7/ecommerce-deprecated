<script>
	import '$lib/style/tinySlider.scss';
	import AboutSection from '$lib/component/(root)/(navbar-footer)/(root)/about-section.svelte';
	import { APP_NAME } from '$lib/constant';
	import HeroSection from '$lib/component/(root)/(navbar-footer)/(root)/hero-section.svelte';
	import FeatureSection from '$lib/component/(root)/(navbar-footer)/(root)/feature-section.svelte';
	import DealSection from '$lib/component/(root)/(navbar-footer)/(root)/deal-section.svelte';
	import DiscountSection from '$lib/component/(root)/(navbar-footer)/(root)/discount-section.svelte';
	import NewArrivalsSection from '$lib/component/(root)/(navbar-footer)/(root)/new-arrivals-section.svelte';
	import TestinomialSection from '$lib/component/(root)/(navbar-footer)/(root)/testinomial-section.svelte';
	import BrandSection from '$lib/component/(root)/(navbar-footer)/(root)/brand-section.svelte';
</script>

<svelte:head>
	<title>{APP_NAME} - Home</title>
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
