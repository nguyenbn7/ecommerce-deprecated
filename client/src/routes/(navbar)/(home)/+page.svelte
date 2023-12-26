<script>
	import { ECOMMERCE_NAME } from '$lib/share/constant';
	import '$lib/layout/(nonavbar)/about/style.scss';
	import HeroSection from '$lib/layout/(navbar)/(home)/hero-section.svelte';
	import FeatureSection from '$lib/layout/(navbar)/(home)/feature-section.svelte';
	import TestinomialSection from '$lib/layout/(navbar)/(home)/testinomial-section.svelte';
	import BrandSection from '$lib/layout/(navbar)/(home)/brand-section.svelte';
	import DealSection from '$lib/layout/(navbar)/(home)/deal-section.svelte';
</script>

<svelte:head>
	<title>{ECOMMERCE_NAME} - Home</title>
</svelte:head>

<HeroSection />

<FeatureSection />

<DealSection />

<!-- Discount -->
<section class="shop-banner">
	<div class="container">
		<h3>December sale is on! <br /> with big <span class="orange-text">Discount...</span></h3>
		<div class="sale-percent"><span>Sale! <br /> Upto</span>50% <span>off</span></div>
		<a href="/shop" class="cart-btn btn-lg">Shop Now</a>
	</div>
</section>

<!-- New Arrivals -->
<div class="product-section mt-150 mb-150">
	<div class="container">
		<div class="row">
			<div class="col-lg-8 offset-lg-2 text-center">
				<div class="section-title">
					<h3><span class="orange-text">Our</span> Products</h3>
					<p>
						Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aliquid, fuga quas itaque
						eveniet beatae optio.
					</p>
				</div>
			</div>
		</div>

		<div class="row">
			<div class="col-lg-4 col-md-6 text-center">
				<div class="single-product-item">
					<div class="product-image">
						<a href="single-product.html"
							><img src="assets/img/products/product-img-1.jpg" alt="" /></a
						>
					</div>
					<h3>Strawberry</h3>
					<p class="product-price"><span>Per Kg</span> 85$</p>
					<a href="cart.html" class="cart-btn"><i class="fas fa-shopping-cart"></i> Add to Cart</a>
				</div>
			</div>
			<div class="col-lg-4 col-md-6 text-center">
				<div class="single-product-item">
					<div class="product-image">
						<a href="single-product.html"
							><img src="assets/img/products/product-img-2.jpg" alt="" /></a
						>
					</div>
					<h3>Berry</h3>
					<p class="product-price"><span>Per Kg</span> 70$</p>
					<a href="cart.html" class="cart-btn"><i class="fas fa-shopping-cart"></i> Add to Cart</a>
				</div>
			</div>
			<div class="col-lg-4 col-md-6 offset-md-3 offset-lg-0 text-center">
				<div class="single-product-item">
					<div class="product-image">
						<a href="single-product.html"
							><img src="assets/img/products/product-img-3.jpg" alt="" /></a
						>
					</div>
					<h3>Lemon</h3>
					<p class="product-price"><span>Per Kg</span> 35$</p>
					<a href="cart.html" class="cart-btn"><i class="fas fa-shopping-cart"></i> Add to Cart</a>
				</div>
			</div>
		</div>
	</div>
</div>

<!-- We are -->
<div class="abt-section mb-150">
	<div class="container">
		<div class="row">
			<div class="col-lg-6 col-md-12">
				<div class="abt-bg">
					<a href="https://www.youtube.com/watch?v=DBLlFWYcIGQ" class="video-play-btn popup-youtube"
						><i class="fas fa-play"></i></a
					>
				</div>
			</div>
			<div class="col-lg-6 col-md-12">
				<div class="abt-text">
					<p class="top-sub">Since Year 1999</p>
					<h2>We are <span class="orange-text">Fruitkha</span></h2>
					<p>
						Etiam vulputate ut augue vel sodales. In sollicitudin neque et massa porttitor
						vestibulum ac vel nisi. Vestibulum placerat eget dolor sit amet posuere. In ut dolor
						aliquet, aliquet sapien sed, interdum velit. Nam eu molestie lorem.
					</p>
					<p>
						Lorem ipsum dolor sit amet, consectetur adipisicing elit. Sapiente facilis illo repellat
						veritatis minus, et labore minima mollitia qui ducimus.
					</p>
					<a href="about.html" class="boxed-btn mt-4">know more</a>
				</div>
			</div>
		</div>
	</div>
</div>

<TestinomialSection />

<!-- News -->
<div class="latest-news pt-150 pb-150">
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
</div>

<BrandSection />
